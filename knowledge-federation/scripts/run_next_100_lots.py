#!/usr/bin/env python3
import sqlite3, zipfile, json, argparse
from pathlib import Path
from checkpoint_common import cached_sqlite_from_archive
from kf_common import ROOT, TODAY, slugify, now

LOTS = 100
PER_LOT = 200
OUT_ZIP = ROOT / "archives" / "study-vault-next-100-lotes.zip"
REPORT = ROOT / "exports" / "reports" / "next-100-lotes-report.md"

REGULATED = {"cannabis-medicinal", "micologia"}


def render_note(row, related, lot_id, pack_slug):
    regulated = row["domain"] in REGULATED
    warning = "\n> [!warning] Domínio regulado\n> Conteúdo educacional para estudo, documentação, rastreabilidade e conversa com profissionais habilitados. Não é prescrição, parecer jurídico nem instrução operacional de cultivo, extração ou produção.\n" if regulated else ""
    links = "\n".join([f"- [[{r['slug']}]] — nota relacionada no mesmo lote." for r in related[:5]]) or "- Sem relações locais neste recorte."
    return f"""---
id: {row['id']}
tipo: {row['type']}
dominio: {row['domain']}
subdominio: {row['subdomain']}
nivel: {row['level']}
confianca: {row['confidence']}
ultima_verificacao: {TODAY}
validade: {row['validity']}
risco_legal: {row['risk_legal']}
risco_medico: {row['risk_medical']}
conteudo_operacional: false
status: materializada-do-checkpoint
origem_lote: {lot_id}
pack: {pack_slug}
fontes: []
tags: [dominio/{row['domain']}, subdominio/{row['subdomain']}, lote/{lot_id}, origem/checkpoint]
aliases: ["{row['title']}"]
prefixo_virtual: {row['prefix']}
---
# {row['title']}
{warning}
## Em uma frase
{row['summary']}

## Por que importa
Esta nota é um recorte materializado do ledger de 1 milhão de notas. Use como ponto de partida para estudo, decisão, backlog, curadoria e verificação com fontes primárias.

## Como funciona
{row['body_seed']}

## Como pedir isso para uma IA
```text
Expanda a nota "{row['title']}" com fontes primárias, exemplos seguros, conexões e critérios de verificação. Separe fato, hipótese, opinião e marketing.
```

## Critérios de verificação
- Conferir documentação, literatura, legislação ou fonte regulatória primária.
- Registrar data de verificação.
- Em software, validar com execução, teste e revisão de diff.
- Em saúde, direito ou domínios regulados, transformar em perguntas para profissional habilitado.

## Conexões locais
{links}

## Fontes a buscar
- {row['source_hint']}
"""


def rows_for(con, domain, subdomain, limit, offset):
    sql = """
    SELECT * FROM virtual_notes
    WHERE domain=? AND subdomain=?
    ORDER BY id
    LIMIT ? OFFSET ?
    """
    return list(con.execute(sql, (domain, subdomain, limit, offset)))


def build_plan(con, lots=LOTS, per_lot=PER_LOT, start_lot=1):
    subdomains = list(con.execute("SELECT domain, subdomain, COUNT(*) c FROM virtual_notes GROUP BY domain, subdomain ORDER BY domain, subdomain"))
    if not subdomains:
        raise SystemExit("Nenhum subdomínio encontrado em virtual_notes")
    plan = []
    for i in range(lots):
        global_index = start_lot - 1 + i
        domain, subdomain, count = subdomains[global_index % len(subdomains)]
        cycle = global_index // len(subdomains)
        # Offset 200 começa após o primeiro bloco materializável padrão; ciclos seguintes avançam em janelas de 200.
        offset = per_lot * (cycle + 1)
        if offset + per_lot > count:
            offset = 0
        lot_id = f"lote-{start_lot+i:03d}"
        pack_slug = f"{lot_id}-{slugify(domain)}-{slugify(subdomain)}-offset-{offset:05d}"
        title = f"{domain} — {subdomain} — {lot_id}"
        plan.append({"lot_id": lot_id, "domain": domain, "subdomain": subdomain, "offset": offset, "limit": per_lot, "pack_slug": pack_slug, "title": title})
    return plan


def main():
    ap = argparse.ArgumentParser(description="Executa os próximos 100 lotes como um vault zipado, sem criar 20k arquivos ativos no workspace.")
    ap.add_argument("--out", default=str(OUT_ZIP))
    ap.add_argument("--lots", type=int, default=LOTS)
    ap.add_argument("--per-lot", type=int, default=PER_LOT)
    ap.add_argument("--start-lot", type=int, default=1, help="Número 1-based do primeiro lote lógico")
    ap.add_argument("--report", default=None, help="Caminho do relatório; default: exports/reports/lotes-<inicio>-<fim>-report.md")
    args = ap.parse_args()
    db = cached_sqlite_from_archive()
    con = sqlite3.connect(db)
    con.row_factory = sqlite3.Row
    plan = build_plan(con, lots=args.lots, per_lot=args.per_lot, start_lot=args.start_lot)
    out_zip = Path(args.out)
    if not out_zip.is_absolute():
        if out_zip.parts and out_zip.parts[0] == ROOT.name:
            out_zip = ROOT.parent / out_zip
        else:
            out_zip = ROOT / out_zip
    out_zip.parent.mkdir(parents=True, exist_ok=True)
    if out_zip.exists():
        out_zip.unlink()

    total_notes = 0
    total_links = 0
    regulated_lots = 0
    manifest = []
    canvas_nodes = [{"id":"home","type":"file","file":"00-Inicio/Home.md","x":0,"y":0,"width":420,"height":160,"color":"1"}]
    canvas_edges = []
    home_lines = [
        "---",
        "tipo: home",
        "status: materializado",
        "tags: [home, lotes, ledger-1m]",
        "aliases: [\"Próximos 100 lotes\", \"Next 100 lots\"]",
        "---",
        f"# Study Vault — Lotes {args.start_lot} a {args.start_lot + args.lots - 1}",
        "",
        f"Gerado em: {now()}",
        "",
        "Este vault zipado contém 100 lotes novos, derivados do checkpoint ledger-first de 1 milhão de notas. Ele foi gerado diretamente para zip para evitar criar dezenas de milhares de arquivos ativos no workspace.",
        "",
        "## Índice de lotes",
        "",
    ]

    with zipfile.ZipFile(out_zip, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for idx, lot in enumerate(plan):
            rows = rows_for(con, lot["domain"], lot["subdomain"], lot["limit"], lot["offset"])
            if len(rows) != lot["limit"]:
                raise SystemExit(f"Lote incompleto: {lot} -> {len(rows)} notas")
            if lot["domain"] in REGULATED:
                regulated_lots += 1
            pack_base = f"10-Lotes/{lot['pack_slug']}"
            moc_path = f"00-Mapas/MOC-{lot['pack_slug']}.md"
            home_lines.append(f"- [[MOC-{lot['pack_slug']}]] — {lot['title']} ({len(rows)} notas; offset {lot['offset']})")
            moc = [
                "---",
                "tipo: moc",
                f"dominio: {lot['domain']}",
                f"subdominio: {lot['subdomain']}",
                f"lote: {lot['lot_id']}",
                "tags: [moc, lote, ledger-1m]",
                f"aliases: [\"{lot['title']}\"]",
                "---",
                f"# {lot['title']}",
                "",
                f"Lote: `{lot['lot_id']}`",
                f"Domínio: `{lot['domain']}`",
                f"Subdomínio: `{lot['subdomain']}`",
                f"Offset no ledger: `{lot['offset']}`",
                f"Notas: **{len(rows)}**",
                "",
            ]
            if lot["domain"] in REGULATED:
                moc += [
                    "> [!warning] Domínio regulado",
                    "> Este lote é educacional, documental e não operacional. Use para estudo, perguntas qualificadas e conversa com profissionais habilitados.",
                    "",
                ]
            moc += ["## Notas", ""]
            for j, row in enumerate(rows):
                related = rows[j+1:j+6] + rows[:max(0, 5-len(rows[j+1:j+6]))]
                note_rel = f"{pack_base}/{row['domain']}/{row['subdomain']}/{row['slug']}.md"
                z.writestr(note_rel, render_note(row, related, lot["lot_id"], lot["pack_slug"]))
                moc.append(f"- [[{row['slug']}]]")
                total_notes += 1
                total_links += len(related[:5])
            z.writestr(moc_path, "\n".join(moc) + "\n")
            total_links += len(rows)
            manifest.append({**lot, "notes": len(rows), "moc": moc_path, "path": pack_base})
            nid = f"lot-{idx+1:03d}"
            canvas_nodes.append({"id": nid, "type": "file", "file": moc_path, "x": ((idx % 5)-2)*480, "y": 260+(idx//5)*220, "width": 420, "height": 130, "color": str((idx % 6)+1)})
            canvas_edges.append({"id": f"e-{idx+1:03d}", "fromNode": "home", "toNode": nid})

        home_lines += [
            "",
            "## Resumo",
            "",
            f"- Lotes: **{len(plan)}**",
            f"- Notas: **{total_notes}**",
            f"- Lotes em domínios regulados: **{regulated_lots}**",
            "- Conteúdo operacional em domínios regulados: **0 por política de geração**",
            "",
            "## Segurança e uso",
            "",
            "Use estes lotes como material bruto de estudo e curadoria. Para decisões técnicas, jurídicas, médicas, financeiras ou regulatórias, verifique fontes primárias e registre data de acesso.",
        ]
        z.writestr("00-Inicio/Home.md", "\n".join(home_lines) + "\n")
        z.writestr("_canvas/Mapa-100-Lotes.canvas", json.dumps({"nodes": canvas_nodes, "edges": canvas_edges}, ensure_ascii=False, indent=2))
        z.writestr("_meta/manifest-next-100-lotes.json", json.dumps(manifest, ensure_ascii=False, indent=2))
        z.writestr("_meta/auditoria-next-100-lotes.md", "\n".join([
            f"# Auditoria — Lotes {args.start_lot} a {args.start_lot + args.lots - 1}",
            "",
            f"Gerado em: {now()}",
            "",
            f"Lotes: {len(plan)}",
            f"Notas materializadas: {total_notes}",
            "MOCs: 100",
            "Canvas: 1",
            f"Links wiki estimados/analisados por construção: {total_links + len(plan)}",
            "Links quebrados esperados: 0",
            f"Lotes em domínios regulados: {regulated_lots}",
            "Conteúdo operacional regulado: 0",
            "",
        ]))
        z.writestr("README.md", "\n".join([
            f"# Study Vault — Lotes {args.start_lot} a {args.start_lot + args.lots - 1}",
            "",
            "Abra como vault no Obsidian e comece por `00-Inicio/Home.md`.",
            "",
            f"Notas: {total_notes}",
            f"Lotes: {len(plan)}",
            "",
            "Gerado diretamente do checkpoint ledger-first para preservar escala sem criar milhares de arquivos ativos no workspace.",
        ]) + "\n")

    report_path = Path(args.report) if args.report else ROOT / "exports" / "reports" / f"lotes-{args.start_lot:03d}-{args.start_lot + args.lots - 1:03d}-report.md"
    if not report_path.is_absolute():
        if report_path.parts and report_path.parts[0] == ROOT.name:
            report_path = ROOT.parent / report_path
        else:
            report_path = ROOT / report_path
    report_path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        f"# Execução — lotes {args.start_lot} a {args.start_lot + args.lots - 1}",
        "",
        f"Gerado em: {now()}",
        "",
        f"Arquivo: `{out_zip.resolve().relative_to(ROOT.resolve()).as_posix()}`",
        f"Tamanho: {out_zip.stat().st_size / 1024 / 1024:.1f}M",
        f"Lotes: **{len(plan)}**",
        f"Notas por lote: **{args.per_lot}**",
        f"Notas totais: **{total_notes}**",
        f"Lotes em domínios regulados: **{regulated_lots}**",
        "Conteúdo operacional regulado: **0**",
        "",
        "## Lotes",
        "",
        "| # | Lote | Domínio | Subdomínio | Offset | Notas |",
        "|---:|---|---|---|---:|---:|",
    ]
    for i, lot in enumerate(manifest, 1):
        lines.append(f"| {i} | `{lot['lot_id']}` | `{lot['domain']}` | `{lot['subdomain']}` | {lot['offset']} | {lot['notes']} |")
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(out_zip)
    print(report_path)
    print(f"lots={len(plan)} notes={total_notes} regulated_lots={regulated_lots} size={out_zip.stat().st_size}")

if __name__ == "__main__":
    main()
