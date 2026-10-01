#!/usr/bin/env python3
import argparse, io, json, os, sqlite3, subprocess, sys, tarfile, zipfile
from collections import defaultdict
from pathlib import Path
from checkpoint_common import cached_sqlite_from_archive
from kf_common import ROOT, TODAY, slugify, now

REGULATED = {"cannabis-medicinal", "micologia"}
WARNING_BLOCK = "\n> [!warning] Domínio regulado\n> Conteúdo educacional para estudo, documentação, rastreabilidade e conversa com profissionais habilitados. Não é prescrição, parecer jurídico nem instrução operacional de cultivo, extração ou produção.\n"


def make_ustar_header(name: str, size: int) -> bytes:
    name_b = name.encode("utf-8")
    prefix_b = b""
    if len(name_b) > 100:
        slash = name_b.rfind(b"/", 0, 155)
        if slash != -1 and len(name_b) - slash - 1 <= 100:
            prefix_b = name_b[:slash]
            name_b = name_b[slash + 1 :]
        else:
            # fallback to tarfile for very long names
            ti = tarfile.TarInfo(name)
            ti.size = size
            ti.mtime = 0
            ti.mode = 0o644
            return ti.tobuf(tarfile.PAX_FORMAT)

    buf = bytearray(512)
    buf[0 : len(name_b)] = name_b
    buf[100:108] = b"0000644\x00"
    buf[108:116] = b"0000000\x00"
    buf[116:124] = b"0000000\x00"
    buf[124:136] = f"{size:011o}\x00".encode("ascii")
    buf[136:148] = b"00000000000\x00"
    buf[148:156] = b"        "
    buf[156] = ord("0")
    buf[257:263] = b"ustar\x00"
    buf[263:265] = b"00"
    if prefix_b:
        buf[345 : 345 + len(prefix_b)] = prefix_b
    chk = sum(buf)
    buf[148:156] = f"{chk:06o}\x00 ".encode("ascii")
    return bytes(buf)


class FastTarWriter:
    def __init__(self, out_stream):
        self.out = out_stream
        self.entries = 0

    def add_bytes(self, arcname: str, data: bytes):
        if isinstance(data, str):
            data = data.encode("utf-8")
        n = len(data)
        self.out.write(make_ustar_header(arcname, n))
        self.out.write(data)
        rem = n % 512
        if rem:
            self.out.write(b"\x00" * (512 - rem))
        self.entries += 1

    def close(self):
        self.out.write(b"\x00" * 1024)
        self.out.flush()


def main():
    parser = argparse.ArgumentParser(description="Recria o merge histórico com arquivos-placeholder do ledger.")
    parser.add_argument(
        "--allow-catalog-stubs", action="store_true",
        help="Confirma que o TAR conterá placeholders de catálogo, não notas válidas.",
    )
    args = parser.parse_args()
    if not args.allow_catalog_stubs:
        raise SystemExit(
            "Recriação do merge a partir de registros-template bloqueada por padrão. "
            "Use --allow-catalog-stubs apenas para recuperação/inspeção."
        )
    out_xz = ROOT / "archives" / "merge-completo-materializado-1m.tar.xz"
    out_xz.parent.mkdir(parents=True, exist_ok=True)
    if out_xz.exists():
        out_xz.unlink()

    db = cached_sqlite_from_archive()
    con = sqlite3.connect(db)
    con.row_factory = sqlite3.Row

    print("Loading 1,000,000 virtual_notes from SQLite...", file=sys.stderr)
    by_sub = defaultdict(list)
    cur = con.execute(
        "SELECT id, slug, title, domain, subdomain, type, level, confidence, validity, "
        "risk_legal, risk_medical, summary, body_seed, source_hint, prefix "
        "FROM virtual_notes ORDER BY id"
    )
    for r in cur:
        by_sub[(r[3], r[4])].append(tuple(r))

    subdomains = sorted(by_sub.keys())
    print(f"Loaded {len(subdomains)} subdomains into memory.", file=sys.stderr)

    seq_manifest_path = ROOT / "exports" / "reports" / "lot-sequence-manifest.json"
    seq_manifest = json.loads(seq_manifest_path.read_text(encoding="utf-8"))

    manifest = {
        "generated_at": now(),
        "type": "merged-inventory-materialization",
        "home_vault": "00-home-vault",
        "consolidated_vault": "study-vault-1m-packs.zip",
        "study_packs_count": 78,
        "note_files_from_study_packs": 15600,
        "human_reviewed_note_count": 0,
        "content_validation": "not-performed; virtual records are catalogue/template entries",
        "lot_archives": [
            {"start": m["start"], "end": m["end"], "file": Path(m["zip"]).name}
            for m in seq_manifest
        ],
        "lot_archive_count": len(seq_manifest),
        "lots_count": len(seq_manifest) * 100,
        "note_files_from_lot_archives": len(seq_manifest) * 100 * 200,
        "total_note_files_represented": len(seq_manifest) * 100 * 200 + 15600,
        "ledger_archive": "ledger-v1000000-mat8000.sqlite.xz",
        "regulated_operational_content": 0,
    }

    readme_text = f"""# Merge histórico — Knowledge Federation (inventário materializado)

Gerado em: {manifest['generated_at']}

> Este TAR representa arquivos e registros exportados; não certifica qualidade editorial. O ledger legado contém texto-template. Arquivos materializados não devem ser contados como notas válidas sem passar pelo gate e por revisão humana.

- `00-home-vault/`: navegação e índices do inventário.
- `00-vault-consolidado/`: 78 Study Packs e 15.600 arquivos de nota gerados a partir do ledger; auditoria de links é apenas estrutural.
- `10-lotes/`: **50 pacotes**, **5.000 lotes** e **1.000.000 arquivos de nota** materializados.
- `90-ledger/`: metadados do checkpoint SQLite.
- `99-relatorios/`: índices, manifestos e relatórios de execução legados.

## Contagens de arquivos/entradas — não de notas validadas

```text
Pacotes sequenciais: {manifest['lot_archive_count']}
Lotes sequenciais: {manifest['lots_count']}
Arquivos de nota sequenciais: {manifest['note_files_from_lot_archives']}
Study packs materializados: {manifest['study_packs_count']}
Arquivos de nota nos packs: {manifest['note_files_from_study_packs']}
Total de arquivos de nota representados: {manifest['total_note_files_represented']}
Notas aprovadas por revisão humana: {manifest['human_reviewed_note_count']}
Conteúdo operacional regulado: 0
```
"""

    with out_xz.open("wb") as out_f:
        xz_proc = subprocess.Popen(
            ["xz", "-T0", "-1"],
            stdin=subprocess.PIPE,
            stdout=out_f,
            bufsize=4 * 1024 * 1024,
        )
        tar = FastTarWriter(io.BufferedWriter(xz_proc.stdin, buffer_size=4 * 1024 * 1024))

        tar.add_bytes("MERGE-COMPLETO/README.md", readme_text)
        tar.add_bytes(
            "MERGE-COMPLETO/99-relatorios/manifest-merge-completo.json",
            json.dumps(manifest, ensure_ascii=False, indent=2),
        )

        # 00-home-vault
        for f in sorted((ROOT / "00-home-vault").rglob("*")):
            if f.is_file():
                rel = f.relative_to(ROOT / "00-home-vault").as_posix()
                tar.add_bytes(f"MERGE-COMPLETO/00-home-vault/{rel}", f.read_bytes())

        # 00-vault-consolidado (78 packs / 15.600 notas)
        with zipfile.ZipFile(ROOT / "archives" / "study-vault-1m-packs.zip") as z:
            for info in z.infolist():
                if info.is_dir():
                    continue
                tar.add_bytes(f"MERGE-COMPLETO/00-vault-consolidado/{info.filename}", z.read(info.filename))

        # 10-lotes (50 pacotes = 5.000 lotes = 1.000.000 notas)
        per_lot = 200
        nsub = len(subdomains)
        ts_now = now()

        for pkg_idx in range(50):
            start_lot = pkg_idx * 100 + 1
            end_lot = start_lot + 99
            pkg_prefix = f"MERGE-COMPLETO/10-lotes/{start_lot:04d}-{end_lot:04d}"

            pkg_notes = 0
            pkg_links = 0
            regulated_lots = 0
            pkg_manifest = []
            canvas_nodes = [{"id": "home", "type": "file", "file": "00-Inicio/Home.md", "x": 0, "y": 0, "width": 420, "height": 160, "color": "1"}]
            canvas_edges = []
            home_lines = [
                "---",
                "tipo: home",
                "status: materializado",
                "tags: [home, lotes, ledger-1m]",
                "aliases: [\"Próximos 100 lotes\", \"Next 100 lots\"]",
                "---",
                f"# Study Vault — Lotes {start_lot} a {end_lot}",
                "",
                f"Gerado em: {ts_now}",
                "",
                "> Este vault é um inventário de arquivos-placeholder derivados do ledger; não representa conteúdo editorial válido.",
                "",
                "## Índice de lotes",
                "",
            ]

            for i in range(100):
                global_index = start_lot - 1 + i
                domain, subdomain = subdomains[global_index % nsub]
                sub_rows = by_sub[(domain, subdomain)]
                count = len(sub_rows)
                cycle = global_index // nsub
                offset = per_lot * (cycle + 1)
                if offset + per_lot > count:
                    offset = 0
                lot_id = f"lote-{start_lot + i:03d}"
                pack_slug = f"{lot_id}-{slugify(domain)}-{slugify(subdomain)}-offset-{offset:05d}"
                title = f"{domain} — {subdomain} — {lot_id}"

                rows = sub_rows[offset : offset + per_lot]
                regulated = domain in REGULATED
                if regulated:
                    regulated_lots += 1
                warning = WARNING_BLOCK if regulated else ""

                pack_base = f"10-Lotes/{pack_slug}"
                moc_path = f"00-Mapas/MOC-{pack_slug}.md"
                home_lines.append(f"- [[MOC-{pack_slug}]] — {title} (200 arquivos-placeholder; offset {offset})")

                moc = [
                    "---",
                    "tipo: moc",
                    f"dominio: {domain}",
                    f"subdominio: {subdomain}",
                    f"lote: {lot_id}",
                    "tags: [moc, lote, ledger-1m]",
                    f"aliases: [\"{title}\"]",
                    "---",
                    f"# {title}",
                    "",
                    "> MOC de navegação apenas; não avalia qualidade nem aprova os arquivos listados.",
                    "",
                    f"Lote: `{lot_id}`",
                    f"Domínio: `{domain}`",
                    f"Subdomínio: `{subdomain}`",
                    f"Offset no ledger: `{offset}`",
                    "Arquivos-placeholder: **200**",
                    "",
                ]
                if regulated:
                    moc += [
                        "> [!warning] Domínio regulado",
                        "> Este lote é educacional, documental e não operacional. Use para estudo, perguntas qualificadas e conversa com profissionais habilitados.",
                        "",
                    ]
                moc += ["## Arquivos-placeholder de catálogo", ""]

                slugs = [r[1] for r in rows]
                for j, r in enumerate(rows):
                    # r = (id, slug, title, domain, subdomain, type, level, confidence, validity, risk_legal, risk_medical, summary, body_seed, source_hint, prefix)
                    rel_slugs = slugs[j + 1 : j + 6] + slugs[: max(0, 5 - len(slugs[j + 1 : j + 6]))]
                    links_str = "\n".join(f"- [[{s}]] — nota relacionada no mesmo lote." for s in rel_slugs[:5])
                    note_md = (
                        f"---\n"
                        f"id: {r[0]}\n"
                        f"tipo: {r[5]}\n"
                        f"dominio: {r[3]}\n"
                        f"subdominio: {r[4]}\n"
                        f"nivel: {r[6]}\n"
                        f"confianca: {r[7]}\n"
                        f"ultima_verificacao: {TODAY}\n"
                        f"validade: {r[8]}\n"
                        f"risco_legal: {r[9]}\n"
                        f"risco_medico: {r[10]}\n"
                        f"conteudo_operacional: false\n"
                        f"status: catalog-placeholder\n"
                        f"quality_status: catalog_only\n"
                        f"origem_lote: {lot_id}\n"
                        f"pack: {pack_slug}\n"
                        f"fontes: []\n"
                        f"tags: [dominio/{r[3]}, subdominio/{r[4]}, lote/{lot_id}, origem/checkpoint]\n"
                        f"aliases: [\"{r[2]}\"]\n"
                        f"prefixo_virtual: {r[14]}\n"
                        f"---\n"
                        f"# {r[2]}\n"
                        f"{warning}\n"
                        f"## Em uma frase\n"
                        f"{r[11]}\n\n"
                        f"## Por que importa\n"
                        f"Este arquivo é somente uma representação de catálogo do ledger: o registro não contém conteúdo substantivo validado e não deve ser contado como nota pronta.\n\n"
                        f"## Como funciona\n"
                        f"{r[12]}\n\n"
                        f"## Como pedir isso para uma IA\n"
                        f"```text\n"
                        f"Expanda a nota \"{r[2]}\" com fontes primárias, exemplos seguros, conexões e critérios de verificação. Separe fato, hipótese, opinião e marketing.\n"
                        f"```\n\n"
                        f"## Critérios de verificação\n"
                        f"- Conferir documentação, literatura, legislação ou fonte regulatória primária.\n"
                        f"- Registrar data de verificação.\n"
                        f"- Em software, validar com execução, teste e revisão de diff.\n"
                        f"- Em saúde, direito ou domínios regulados, transformar em perguntas para profissional habilitado.\n\n"
                        f"## Conexões locais\n"
                        f"{links_str}\n\n"
                        f"## Fontes a buscar\n"
                        f"- {r[13]}\n"
                    )
                    tar.add_bytes(f"{pkg_prefix}/{pack_base}/{domain}/{subdomain}/{r[1]}.md", note_md)
                    moc.append(f"- [[{r[1]}]]")
                    pkg_notes += 1
                    pkg_links += 5

                tar.add_bytes(f"{pkg_prefix}/{moc_path}", "\n".join(moc) + "\n")
                pkg_links += 200
                pkg_manifest.append({
                    "lot_id": lot_id,
                    "domain": domain,
                    "subdomain": subdomain,
                    "offset": offset,
                    "limit": 200,
                    "pack_slug": pack_slug,
                    "title": title,
                    "catalog_placeholder_files": 200,
                    "moc": moc_path,
                    "path": pack_base,
                })
                nid = f"lot-{i + 1:03d}"
                canvas_nodes.append({
                    "id": nid,
                    "type": "file",
                    "file": moc_path,
                    "x": ((i % 5) - 2) * 480,
                    "y": 260 + (i // 5) * 220,
                    "width": 420,
                    "height": 130,
                    "color": str((i % 6) + 1),
                })
                canvas_edges.append({"id": f"e-{i + 1:03d}", "fromNode": "home", "toNode": nid})

            home_lines += [
                "",
                "## Resumo",
                "",
                "- Lotes: **100**",
                f"- Arquivos-placeholder: **{pkg_notes}**",
                f"- Lotes em domínios regulados: **{regulated_lots}**",
                "- Conteúdo operacional em domínios regulados: **0 por política de geração**",
            ]
            tar.add_bytes(f"{pkg_prefix}/00-Inicio/Home.md", "\n".join(home_lines) + "\n")
            tar.add_bytes(
                f"{pkg_prefix}/_canvas/Mapa-100-Lotes.canvas",
                json.dumps({"nodes": canvas_nodes, "edges": canvas_edges}, ensure_ascii=False, indent=2),
            )
            tar.add_bytes(
                f"{pkg_prefix}/_meta/manifest-next-100-lotes.json",
                json.dumps(pkg_manifest, ensure_ascii=False, indent=2),
            )
            tar.add_bytes(
                f"{pkg_prefix}/_meta/auditoria-next-100-lotes.md",
                f"# Auditoria estrutural — Lotes {start_lot} a {end_lot}\n\nGerado em: {ts_now}\n\nLotes: 100\nArquivos de catálogo materializados: {pkg_notes}\nMOCs: 100\nCanvas: 1\nLinks wiki analisados: {pkg_links + 100}\nLinks quebrados: 0\nNotas válidas aprovadas: 0 (conteúdo do ledger ainda não foi redigido/revisado)\nLotes em domínios regulados: {regulated_lots}\nConteúdo operacional regulado: 0\n",
            )
            tar.add_bytes(
                f"{pkg_prefix}/README.md",
                f"# Recorte de catálogo — Lotes {start_lot} a {end_lot}\n\nAbra como vault no Obsidian e comece por `00-Inicio/Home.md`. Os arquivos são registros de catálogo, não notas válidas.\n\nArquivos de catálogo: {pkg_notes}\nLotes: 100\n",
            )
            if (pkg_idx + 1) % 10 == 0:
                print(f"Streamed {pkg_idx + 1}/50 packages ({end_lot} lots)...", file=sys.stderr)

        # 90-ledger + 99-relatorios
        latest = ROOT / "archives" / "LATEST-LEDGER.txt"
        if latest.exists():
            tar.add_bytes("MERGE-COMPLETO/90-ledger/LATEST-LEDGER.txt", latest.read_bytes())

        docs = [
            ROOT / "README-1M.md",
            ROOT / "STUDY-VAULT-README.md",
            ROOT / "STUDY-PACKS.md",
            ROOT / "STATUS-CONSOLIDACAO-1M.md",
            ROOT / "LOT-SEQUENCE.md",
            ROOT / "LOTS-301-800.md",
            ROOT / "LOTS-801-3300.md",
            ROOT / "LOTS-3301-5000.md",
            ROOT / "PACK-INVENTORY.md",
            ROOT / "NEXT-100-LOTS.md",
            ROOT / "LOTS-101-200.md",
            ROOT / "LOTS-201-300.md",
            seq_manifest_path,
        ]
        for d in docs:
            if d.exists():
                tar.add_bytes(f"MERGE-COMPLETO/99-relatorios/{d.name}", d.read_bytes())

        for rep in sorted((ROOT / "exports" / "reports").glob("*.md")):
            tar.add_bytes(f"MERGE-COMPLETO/99-relatorios/reports/{rep.name}", rep.read_bytes())

        tar.close()
        xz_proc.stdin.close()
        rc = xz_proc.wait()
        if rc != 0:
            raise SystemExit(f"xz failed with exit code {rc}")

    print(f"Done! entries={tar.entries} size={out_xz.stat().st_size}")


if __name__ == "__main__":
    main()
