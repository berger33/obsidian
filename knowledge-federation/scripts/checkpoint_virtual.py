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
    notes = con.execute("SELECT COUNT(*) FROM notes").fetchone()[0]
    try:
        virtual = con.execute("SELECT COUNT(*) FROM virtual_notes").fetchone()[0]
    except sqlite3.OperationalError:
        virtual = 0
    label = args.label or f"ledger-n{notes}-v{virtual}"
    outdir = ROOT / "archives"; outdir.mkdir(parents=True, exist_ok=True)
    out = outdir / f"ledger-{label}.zip"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        z.write(DB, "knowledge.sqlite")
    (outdir / "LATEST-LEDGER.txt").write_text(f"label={label}\nnotes={notes}\nvirtual_notes={virtual}\narchive={out.name}\ncreated_at={now()}\n", encoding="utf-8")
    if args.prune_materialized:
        shutil.rmtree(ROOT / "materialized", ignore_errors=True)
    print(out)

if __name__ == "__main__":
    main()
