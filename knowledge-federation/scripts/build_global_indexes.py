#!/usr/bin/env python3
import json, sqlite3
from pathlib import Path
from checkpoint_common import cached_sqlite_from_archive
from kf_common import ROOT, TODAY, now
from build_all_78_study_packs import ALL_78_PACKS, DOMAIN_TITLES


def main():
    db = cached_sqlite_from_archive()
    con = sqlite3.connect(db)
    con.row_factory = sqlite3.Row

    home_vault = ROOT / "00-home-vault"
    mocs_dir = home_vault / "MOCs"
    canvas_dir = home_vault / "_canvas"
    obs_dir = home_vault / ".obsidian"
    mocs_dir.mkdir(parents=True, exist_ok=True)
    canvas_dir.mkdir(parents=True, exist_ok=True)
    obs_dir.mkdir(parents=True, exist_ok=True)

    phys_count = con.execute("SELECT COUNT(*) FROM notes").fetchone()[0]
    virt_count = con.execute("SELECT COUNT(*) FROM virtual_notes").fetchone()[0]
    dom_rows = list(con.execute("SELECT domain, COUNT(*) c FROM virtual_notes GROUP BY domain ORDER BY c DESC"))
    sub_rows = list(con.execute("SELECT domain, subdomain, COUNT(*) c FROM virtual_notes GROUP BY domain, subdomain ORDER BY domain, subdomain"))

    seq_manifest = json.loads((ROOT / "exports" / "reports" / "lot-sequence-manifest.json").read_text(encoding="utf-8"))

    sub_by_domain = {d: [] for d in DOMAIN_TITLES}
    for r in sub_rows:
        sub_by_domain[r["domain"]].append((r["subdomain"], r["c"]))

    packs_by_domain = {d: [] for d in DOMAIN_TITLES}
    for p in ALL_78_PACKS:
        packs_by_domain[p[1]].append(p)

    # 1. MOCs por domínio
    for domain, title in DOMAIN_TITLES.items():
        total_dom = sum(c for _, c in sub_by_domain[domain])
        lines = [
            "---",
            "tipo: moc-global-dominio",
            f"dominio: {domain}",
            f"ultima_verificacao: {TODAY}",
            "tags: [moc, global, ledger-1m]",
            f"aliases: [\"MOC Global — {title}\"]",
            "---",
            f"# MOC Global — {title}",
            "",
            "> MOC de navegação; seus links e contagens não aprovam notas nem participam do gate editorial.",
            "",
            f"- Domínio: `{domain}`",
            f"- Registros virtuais de catálogo no ledger (não validados): **{total_dom:,}**".replace(",", "."),
            f"- Subdomínios: **{len(sub_by_domain[domain])}**",
            f"- Study Packs materializados (200 arquivos cada; conteúdo não validado): **{len(packs_by_domain[domain])}** (**{len(packs_by_domain[domain]) * 200:,} arquivos**)".replace(",", "."),
            "",
            "## Subdomínios e Volume no Ledger",
            "",
            "| Subdomínio | Registros no catálogo | Pack materializado (200 arquivos) | Arquivo ZIP |",
            "|---|---:|---|---|",
        ]
        pack_map = {p[2]: p for p in packs_by_domain[domain]}
        for sub, cnt in sub_by_domain[domain]:
            p = pack_map[sub]
            lines.append(f"| `{sub}` | {cnt:,} | `{p[0]}` ({p[3]}) | `archives/{p[5]}` |".replace(",", "."))
        lines += [
            "",
            "## Navegação",
            "",
            "- Voltar para [[Home]]",
            "- Ver [[Indice-Global]]",
            "- Ver [[MOC-78-Study-Packs]]",
            "- Ver [[MOC-5000-Lotes-Sequenciais]]",
        ]
        (mocs_dir / f"MOC-{domain}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

        # Canvas do domínio no 00-home-vault
        color = packs_by_domain[domain][0][4]
        cnodes = [{
            "id": "dom",
            "type": "file",
            "file": f"MOCs/MOC-{domain}.md",
            "x": 0,
            "y": 0,
            "width": 440,
            "height": 160,
            "color": color,
        }]
        cedges = []
        for idx, (sub, cnt) in enumerate(sub_by_domain[domain]):
            nid = f"sub-{idx}"
            p = pack_map[sub]
            cnodes.append({
                "id": nid,
                "type": "text",
                "text": f"### {p[3]}\nSubdomínio: `{sub}`\nLedger: **{cnt:,}** registros\nPack: `archives/{p[5]}` (200 arquivos-placeholder)".replace(",", "."),
                "x": ((idx % 4) - 1.5) * 480,
                "y": 260 + (idx // 4) * 220,
                "width": 420,
                "height": 150,
                "color": color,
            })
            cedges.append({"id": f"e-{idx}", "fromNode": "dom", "toNode": nid})
        (canvas_dir / f"Mapa-{domain}.canvas").write_text(
            json.dumps({"nodes": cnodes, "edges": cedges}, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    # 2. MOC dos 78 Study Packs
    pack_moc_lines = [
        "---",
        "tipo: moc-global",
        f"ultima_verificacao: {TODAY}",
        "tags: [moc, study-packs, ledger-1m]",
        "aliases: [\"MOC — 78 Study Packs\"]",
        "---",
        "# MOC Global — 78 Study Packs históricos (15.600 arquivos)",
        "",
        "> MOC de navegação apenas; não participa do gate de qualidade e não aprova os arquivos listados.",
        "",
        "Os **78 subdomínios** da taxonomia possuem um pacote de **200 arquivos-placeholder** (`15.600` arquivos no total), materializados a partir de registros do ledger. Não são conteúdo validado.",
        "",
        "| # | Domínio | Subdomínio | Título | Arquivos-placeholder | Arquivo Individual |",
        "|---:|---|---|---|---:|---|",
    ]
    for idx, (pack_slug, domain, subdomain, title, color, zip_name) in enumerate(ALL_78_PACKS, 1):
        pack_moc_lines.append(f"| {idx} | [[MOC-{domain}|{domain}]] | `{subdomain}` | {title} | 200 | `archives/{zip_name}` |")
    (mocs_dir / "MOC-78-Study-Packs.md").write_text("\n".join(pack_moc_lines) + "\n", encoding="utf-8")

    # 3. MOC dos 5.000 Lotes Sequenciais
    lot_moc_lines = [
        "---",
        "tipo: moc-global",
        f"ultima_verificacao: {TODAY}",
        "tags: [moc, lotes, ledger-1m]",
        "aliases: [\"MOC — 5000 Lotes Sequenciais\"]",
        "---",
        "# MOC Global — 5.000 lotes históricos (1.000.000 de arquivos)",
        "",
        "> MOC de navegação apenas; não participa do gate de qualidade e não aprova os arquivos listados.",
        "",
        "A sequência contém **50 pacotes × 100 lotes × 200 arquivos-placeholder = 1.000.000 de arquivos** a partir do ledger. Os totais não são uma validação do conteúdo.",
        "",
        "| # | Intervalo | Pasta no Merge Completo | Arquivos de nota | Lotes Regulados | Relatório |",
        "|---:|---|---|---:|---:|---|",
    ]
    for idx, m in enumerate(seq_manifest, 1):
        interval = f"{m['start']:04d}-{m['end']:04d}"
        lot_moc_lines.append(
            f"| {idx} | `{interval}` | `MERGE-COMPLETO/10-lotes/{interval}/` | {m['notes']:,} | {m['regulated_lots']} | `{m['report']}` |".replace(",", ".")
        )
    (mocs_dir / "MOC-5000-Lotes-Sequenciais.md").write_text("\n".join(lot_moc_lines) + "\n", encoding="utf-8")

    # 4. Indice-Global.md
    idx_lines = [
        "---",
        "tipo: indice-global",
        f"ultima_verificacao: {TODAY}",
        "tags: [indice, global, ledger-1m]",
        "---",
        "# Índice Global — Knowledge Federation (inventário legado de 1 milhão)",
        "",
        "> As contagens descrevem registros e arquivos históricos. O ledger contém texto-template; nada é promovido a nota válida por aparecer neste índice.",
        "",
        f"Atualizado em: {now()}",
        "",
        "## Resumo Executivo",
        "",
        f"- **Registros virtuais de catálogo (conteúdo não validado):** {virt_count:,}".replace(",", "."),
        f"- **Registros físicos iniciais:** {phys_count}",
        f"- **Total de registros no inventário:** {virt_count + phys_count:,}".replace(",", "."),
        "- **Arquivos sequenciais materializados:** 5.000 lotes / **1.000.000 arquivos**; materialização não é validação editorial",
        "- **Study Packs históricos:** 78 packs × 200 arquivos = **15.600 arquivos de nota**",
        "- **Total de arquivos representados no merge histórico:** **1.015.600**, sem MOCs/relatórios",
        "- **Notas revisadas por pessoa identificada:** 0 no checkpoint legado; consultar a auditoria de qualidade",
        "- **Conteúdo operacional em domínios regulados:** **0**",
        "",
        "## Distribuição por Domínio no Ledger",
        "",
        "| Domínio | Registros virtuais do catálogo | Subdomínios | Packs (200 arquivos) | MOC Global |",
        "|---|---:|---:|---:|---|",
    ]
    for r in dom_rows:
        d = r["domain"]
        c = r["c"]
        nsub = len(sub_by_domain[d])
        idx_lines.append(f"| `{d}` | {c:,} | {nsub} | {nsub} ({nsub * 200:,} arquivos-placeholder) | [[MOC-{d}]] |".replace(",", "."))

    idx_lines += [
        "",
        "## Contagem por Domínio / Subdomínio (78 Subdomínios)",
        "",
        "| # | Domínio | Subdomínio | Registros virtuais no Ledger |",
        "|---:|---|---|---:|",
    ]
    for i, r in enumerate(sub_rows, 1):
        idx_lines.append(f"| {i} | `{r['domain']}` | `{r['subdomain']}` | {r['c']:,} |".replace(",", "."))

    (home_vault / "Indice-Global.md").write_text("\n".join(idx_lines) + "\n", encoding="utf-8")

    # 5. Home.md
    home_lines = [
        "---",
        "tipo: home-global",
        f"ultima_verificacao: {TODAY}",
        "tags: [home, global, ledger-1m]",
        "aliases: [\"Home — Knowledge Federation\"]",
        "---",
        "# Home — Knowledge Federation (inventário legado de 1 milhão)",
        "",
        "Este checkpoint contém 1.000.000 de registros virtuais de catálogo, não notas editoriais validadas. A materialização e a auditoria de links não comprovam qualidade; consulte o gate de conteúdo antes de contar notas.",
        "",
        "- [[MOC-Confiabilidade-e-Contratos]] — lote autoral atual, aguardando revisão humana.",
        "- [[note-quality-audit]] — contagem de candidatas, templates e revisão humana.",
        "",
        "## Mapas de inventário",
        "",
        "- [[Indice-Global]] — Inventário completo dos 7 domínios e 78 subdomínios",
        "- [[MOC-78-Study-Packs]] — 78 pacotes históricos / 15.600 arquivos de nota (conteúdo não validado)",
        "- [[MOC-5000-Lotes-Sequenciais]] — lotes históricos / 1.000.000 de arquivos materializados (não equivalem a notas válidas)",
        "",
        "## MOCs por Domínio",
        "",
    ]
    for d, title in DOMAIN_TITLES.items():
        home_lines.append(f"- [[MOC-{d}|MOC Global — {title}]] (`_canvas/Mapa-{d}.canvas`)")

    home_lines += [
        "",
        "## Canvases Visuais (`_canvas/`)",
        "",
        "- `_canvas/Mapa-Global.canvas`",
        "- `_canvas/Mapa-software.canvas`",
        "- `_canvas/Mapa-ia.canvas`",
        "- `_canvas/Mapa-vibe-coding.canvas`",
        "- `_canvas/Mapa-jogos.canvas`",
        "- `_canvas/Mapa-cannabis-medicinal.canvas`",
        "- `_canvas/Mapa-micologia.canvas`",
        "- `_canvas/Mapa-negocio-carreira-produto.canvas`",
    ]
    (home_vault / "Home.md").write_text("\n".join(home_lines) + "\n", encoding="utf-8")

    # 6. Mapa-Global.canvas
    gnodes = [
        {"id": "home", "type": "file", "file": "Home.md", "x": 0, "y": 0, "width": 420, "height": 160, "color": "1"},
        {"id": "idx", "type": "file", "file": "Indice-Global.md", "x": -520, "y": 0, "width": 420, "height": 160, "color": "2"},
        {"id": "packs", "type": "file", "file": "MOCs/MOC-78-Study-Packs.md", "x": 520, "y": 0, "width": 420, "height": 160, "color": "4"},
        {"id": "lots", "type": "file", "file": "MOCs/MOC-5000-Lotes-Sequenciais.md", "x": 0, "y": -240, "width": 460, "height": 160, "color": "5"},
    ]
    gedges = [
        {"id": "e-idx", "fromNode": "home", "toNode": "idx"},
        {"id": "e-packs", "fromNode": "home", "toNode": "packs"},
        {"id": "e-lots", "fromNode": "home", "toNode": "lots"},
    ]
    for idx, (d, title) in enumerate(DOMAIN_TITLES.items()):
        nid = f"dom-{idx}"
        color = packs_by_domain[d][0][4]
        gnodes.append({
            "id": nid,
            "type": "file",
            "file": f"MOCs/MOC-{d}.md",
            "x": ((idx % 4) - 1.5) * 520,
            "y": 280 + (idx // 4) * 240,
            "width": 440,
            "height": 150,
            "color": color,
        })
        gedges.append({"id": f"ed-{idx}", "fromNode": "home", "toNode": nid})
    (canvas_dir / "Mapa-Global.canvas").write_text(
        json.dumps({"nodes": gnodes, "edges": gedges}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    (obs_dir / "app.json").write_text(json.dumps({"readableLineLength": True}, indent=2), encoding="utf-8")
    print("00-home-vault completo gerado com sucesso.")


if __name__ == "__main__":
    main()
