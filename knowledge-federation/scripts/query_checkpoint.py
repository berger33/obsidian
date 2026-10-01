#!/usr/bin/env python3
import argparse, sqlite3
from checkpoint_common import cached_sqlite_from_archive, latest_ledger_archive


def main():
    ap = argparse.ArgumentParser(description="Consulta o checkpoint ledger sem restaurar o SQLite gigante no workspace.")
    ap.add_argument("query", nargs="?", default="")
    ap.add_argument("--archive", default=None)
    ap.add_argument("--domain", default=None)
    ap.add_argument("--subdomain", default=None)
    ap.add_argument("--limit", type=int, default=25)
    ap.add_argument("--force-extract", action="store_true")
    ap.add_argument("--count-only", action="store_true")
    args = ap.parse_args()
    db = cached_sqlite_from_archive(args.archive, force=args.force_extract)
    con = sqlite3.connect(db)
    con.row_factory = sqlite3.Row
    where=[]; params=[]
    if args.domain:
        where.append("domain=?"); params.append(args.domain)
    if args.subdomain:
        where.append("subdomain=?"); params.append(args.subdomain)
    if args.query:
        q=f"%{args.query}%"
        where.append("(title LIKE ? OR slug LIKE ? OR summary LIKE ?)")
        params += [q,q,q]
    sql_where = (" WHERE " + " AND ".join(where)) if where else ""
    if args.count_only:
        print(con.execute("SELECT COUNT(*) FROM virtual_notes" + sql_where, params).fetchone()[0])
        return
    sql = "SELECT id, slug, title, domain, subdomain, prefix FROM virtual_notes" + sql_where + " ORDER BY domain, subdomain, title LIMIT ?"
    params.append(args.limit)
    for r in con.execute(sql, params):
        print(f"[{r['domain']}/{r['subdomain']}] {r['title']} :: {r['slug']} :: {r['prefix']}")

if __name__ == "__main__":
    main()
