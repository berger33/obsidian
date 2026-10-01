#!/usr/bin/env python3
from pathlib import Path
import argparse, zipfile, sqlite3, os, shutil
from kf_common import ROOT, DB, now


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--label", default=None)
    ap.add_argument("--prune-materialized", action="store_true")
    args = ap.parse_args()
    if not DB.exists():
        raise SystemExit(f"DB ausente: {DB}")
    con = sqlite3.connect(DB)
    physical_records = con.execute("SELECT COUNT(*) FROM notes").fetchone()[0]
    try:
        virtual_records = con.execute("SELECT COUNT(*) FROM virtual_notes").fetchone()[0]
        columns = {row[1] for row in con.execute("PRAGMA table_info(virtual_notes)")}
        materialized_paths = (
            con.execute("SELECT COUNT(*) FROM virtual_notes WHERE materialized_path IS NOT NULL").fetchone()[0]
            if "materialized_path" in columns else 0
        )
    except sqlite3.OperationalError:
        virtual_records = 0
        materialized_paths = 0
    label = args.label or f"ledger-n{physical_records}-v{virtual_records}"
    outdir = ROOT / "archives"; outdir.mkdir(parents=True, exist_ok=True)
    out = outdir / f"ledger-{label}.zip"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        z.write(DB, "knowledge.sqlite")
    (outdir / "LATEST-LEDGER.txt").write_text(
        f"label={label}\nphysical_records={physical_records}\nvirtual_catalog_records={virtual_records}\n"
        f"materialized_paths={materialized_paths}\narchive={out.name}\ncreated_at={now()}\n",
        encoding="utf-8",
    )
    if args.prune_materialized:
        shutil.rmtree(ROOT / "materialized", ignore_errors=True)
    print(out)

if __name__ == "__main__":
    main()
