#!/usr/bin/env python3
"""Print inventory statistics for a compressed or extracted ledger."""
import sqlite3
import argparse
from checkpoint_common import cached_sqlite_from_archive


def main():
    ap = argparse.ArgumentParser(description="Estatísticas de inventário do checkpoint ledger (não valida conteúdo).")
    ap.add_argument("--archive", default=None)
    args = ap.parse_args()
    con = sqlite3.connect(cached_sqlite_from_archive(args.archive))
    columns = {row[1] for row in con.execute("PRAGMA table_info(virtual_notes)")}
    virtual_total = con.execute("SELECT COUNT(*) FROM virtual_notes").fetchone()[0]
    materialized = con.execute("SELECT COUNT(*) FROM virtual_notes WHERE materialized_path IS NOT NULL").fetchone()[0]
    placeholder_predicates = [
        "lower(coalesce(summary,'')) LIKE '%nota virtual sobre%'",
        "lower(coalesce(body_seed,'')) LIKE '%registro virtual ledger-first%'",
        "lower(coalesce(title,'')) LIKE '%vscale%'",
    ]
    if "quality_status" in columns:
        placeholder_predicates.append("lower(coalesce(quality_status,'')) = 'catalog_only'")
    placeholders = con.execute(
        "SELECT COUNT(*) FROM virtual_notes WHERE " + " OR ".join(placeholder_predicates)
    ).fetchone()[0]
    regulated = con.execute(
        "SELECT COUNT(*) FROM virtual_notes WHERE domain IN ('cannabis-medicinal','micologia') AND operational_content != 0"
    ).fetchone()[0]
    quality_reviewed = 0
    if "quality_status" in columns:
        quality_reviewed = con.execute(
            "SELECT COUNT(*) FROM virtual_notes WHERE lower(quality_status) IN ('reviewed','valid')"
        ).fetchone()[0]

    print("virtual_catalog_records", virtual_total)
    print("records_with_template_markers", placeholders)
    print("materialization_paths_not_editorial_validation", materialized)
    print("quality_reviewed_records_type_not_distinguished", quality_reviewed)
    print("regulated_operational_markers", regulated)
    print("\nby_domain")
    for domain, count in con.execute("SELECT domain, COUNT(*) FROM virtual_notes GROUP BY domain ORDER BY COUNT(*) DESC"):
        print(domain, count)
    con.close()


if __name__ == "__main__":
    main()
