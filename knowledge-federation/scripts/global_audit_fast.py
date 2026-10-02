#!/usr/bin/env python3
from kf_common import *
from collections import Counter


def main():
    con = connect()
    total = con.execute("SELECT COUNT(*) FROM notes").fetchone()[0]
    deep = con.execute("SELECT COUNT(*) FROM notes WHERE status='deep'").fetchone()[0]
    note_quality_ready = con.execute("SELECT COUNT(*) FROM notes WHERE quality_status='ready_for_review'").fetchone()[0]
    note_quality_reviewed = con.execute("SELECT COUNT(*) FROM notes WHERE quality_status='reviewed'").fetchone()[0]
    note_quality_needs_review = con.execute("SELECT COUNT(*) FROM notes WHERE quality_status='needs_review'").fetchone()[0]
    try:
        virtual_total = con.execute("SELECT COUNT(*) FROM virtual_notes").fetchone()[0]
        virtual_materialized = con.execute("SELECT COUNT(*) FROM virtual_notes WHERE materialized_path IS NOT NULL").fetchone()[0]
        virtual_by_domain = con.execute("SELECT domain, COUNT(*) c FROM virtual_notes GROUP BY domain ORDER BY c DESC").fetchall()
        virtual_by_sub = con.execute("SELECT domain, subdomain, COUNT(*) c FROM virtual_notes GROUP BY domain, subdomain ORDER BY c DESC LIMIT 100").fetchall()
        virtual_dup_slug = con.execute("SELECT prefix, slug, COUNT(*) c FROM virtual_notes GROUP BY prefix, slug HAVING c > 1 LIMIT 200").fetchall()
        virtual_regulated_operational = con.execute("SELECT COUNT(*) FROM virtual_notes WHERE domain IN ('cannabis-medicinal','micologia') AND operational_content != 0").fetchone()[0]
        virtual_columns = {r[1] for r in con.execute("PRAGMA table_info(virtual_notes)")}
        if "quality_status" in virtual_columns:
            virtual_quality_ready = con.execute("SELECT COUNT(*) FROM virtual_notes WHERE quality_status='ready_for_review'").fetchone()[0]
            virtual_quality_reviewed = con.execute("SELECT COUNT(*) FROM virtual_notes WHERE quality_status='reviewed'").fetchone()[0]
            virtual_quality_catalog = con.execute("SELECT COUNT(*) FROM virtual_notes WHERE quality_status='catalog_only'").fetchone()[0]
            virtual_quality_needs_review = con.execute("SELECT COUNT(*) FROM virtual_notes WHERE quality_status='needs_review'").fetchone()[0]
        else:
            virtual_quality_ready = virtual_quality_reviewed = virtual_quality_catalog = virtual_quality_needs_review = 0
    except Exception:
        virtual_total = 0; virtual_materialized = 0; virtual_by_domain = []; virtual_by_sub = []; virtual_dup_slug = []; virtual_regulated_operational = 0
        virtual_quality_ready = virtual_quality_reviewed = virtual_quality_catalog = virtual_quality_needs_review = 0
    batches = con.execute("SELECT status, COUNT(*) c FROM batches GROUP BY status ORDER BY status").fetchall()
    by_domain = con.execute("SELECT domain, COUNT(*) c FROM notes GROUP BY domain ORDER BY c DESC").fetchall()
    by_vault = con.execute("SELECT vault, COUNT(*) c FROM notes GROUP BY vault ORDER BY vault").fetchall()
    by_sub = con.execute("SELECT domain, subdomain, COUNT(*) c FROM notes GROUP BY domain, subdomain ORDER BY c DESC LIMIT 100").fetchall()
    dup_slug = con.execute("SELECT vault, slug, COUNT(*) c FROM notes GROUP BY vault, slug HAVING c > 1 LIMIT 200").fetchall()
    dup_title = con.execute("SELECT domain, subdomain, lower(title) t, COUNT(*) c FROM notes GROUP BY domain, subdomain, lower(title) HAVING c > 1 LIMIT 200").fetchall()
    regulated_operational = con.execute("SELECT COUNT(*) FROM notes WHERE domain IN ('cannabis-medicinal','micologia') AND operational_content != 0").fetchone()[0]
    active_files = 0
    domains_dir = ROOT / "domains"
    if domains_dir.exists():
        active_files = sum(1 for p in domains_dir.rglob("*.md"))
    archives = sorted((ROOT / "archives").glob("domains-*.tar.xz"))
    registry_scope_note = []
    if total == 0 and virtual_total == 0:
        registry_scope_note = [
            "> **Escopo:** o `registry/knowledge.sqlite` está sem registros físicos ou virtuais nesta execução. Esses zeros descrevem somente o banco local, não a presença de conteúdo nos arquivos; use a [auditoria de qualidade por arquivos](note-quality-audit.md) para a contagem editorial.",
            "",
        ]
    report = [
        "# Auditoria Global Rápida",
        "",
        f"Atualizado em: {now()}",
        "",
        *registry_scope_note,
        f"- Notas físicas registradas no SQLite: {total}",
        f"- Registros virtuais de catálogo no SQLite (não equivalem a notas validadas): {virtual_total}",
        f"- Registros virtuais com caminho de materialização: {virtual_materialized} (materialização não é validação editorial)",
        f"- Total de registros no inventário (físicos + virtuais): {total + virtual_total}",
        f"- Notas profundas físicas: {deep}",
        f"- Notas físicas prontas para revisão / revisadas / pendentes: {note_quality_ready} / {note_quality_reviewed} / {note_quality_needs_review}",
        f"- Registros virtuais catalog_only / prontos para revisão / revisados / pendentes: {virtual_quality_catalog} / {virtual_quality_ready} / {virtual_quality_reviewed} / {virtual_quality_needs_review}",
        "- Lotes por status: " + (", ".join(f"{b['status']}={b['c']}" for b in batches) or "nenhum lote registrado no SQLite"),
        f"- Arquivos Markdown ativos em domains/: {active_files}",
        f"- Archives de domains existentes: {len(archives)}",
        f"- Slugs duplicados por vault: {len(dup_slug)}",
        f"- Títulos duplicados por domínio/subdomínio: {len(dup_title)}",
        f"- Notas físicas reguladas marcadas como operacionais: {regulated_operational}",
        f"- Notas virtuais reguladas marcadas como operacionais: {virtual_regulated_operational}",
        f"- Slugs duplicados em notas virtuais por prefixo: {len(virtual_dup_slug)}",
        "",
        "## Contagem por domínio — notas físicas",
        "",
    ]
    report += [f"- {r['domain']}: {r['c']}" for r in by_domain] or ["Nenhuma."]
    report += ["", "## Contagem por domínio — notas virtuais", ""]
    report += [f"- {r['domain']}: {r['c']}" for r in virtual_by_domain] or ["Nenhuma."]
    report += ["", "## Contagem por vault", ""]
    report += [f"- {r['vault']}: {r['c']}" for r in by_vault]
    report += ["", "## Top subdomínios — notas físicas", ""]
    report += [f"- {r['domain']}/{r['subdomain']}: {r['c']}" for r in by_sub] or ["Nenhum."]
    report += ["", "## Top subdomínios — notas virtuais", ""]
    report += [f"- {r['domain']}/{r['subdomain']}: {r['c']}" for r in virtual_by_sub] or ["Nenhum."]
    report += ["", "## Duplicatas de slug", ""]
    report += [f"- {r['vault']} / {r['slug']} ({r['c']})" for r in dup_slug] or ["Nenhuma."]
    report += ["", "## Duplicatas de título", ""]
    report += [f"- {r['domain']}/{r['subdomain']} / {r['t']} ({r['c']})" for r in dup_title] or ["Nenhuma."]
    out = ROOT / "exports" / "reports" / "global-audit-fast.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(report)+"\n", encoding="utf-8")
    print(out)

if __name__ == "__main__":
    main()
