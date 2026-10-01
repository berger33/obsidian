#!/usr/bin/env python3
import sqlite3, argparse
from checkpoint_common import cached_sqlite_from_archive


def main():
    ap = argparse.ArgumentParser(description="Estatísticas rápidas do checkpoint ledger.")
    ap.add_argument("--archive", default=None)
    args = ap.parse_args()
    con = sqlite3.connect(cached_sqlite_from_archive(args.archive))
    print("virtual_notes", con.execute("SELECT COUNT(*) FROM virtual_notes").fetchone()[0])
    print("materialized", con.execute("SELECT COUNT(*) FROM virtual_notes WHERE materialized_path IS NOT NULL").fetchone()[0])
    print("regulated_operational", con.execute("SELECT COUNT(*) FROM virtual_notes WHERE domain IN ('cannabis-medicinal','micologia') AND operational_content != 0").fetchone()[0])
    print("\nby_domain")
    for d,c in con.execute("SELECT domain, COUNT(*) FROM virtual_notes GROUP BY domain ORDER BY COUNT(*) DESC"):
        print(d, c)

if __name__ == "__main__":
    main()
