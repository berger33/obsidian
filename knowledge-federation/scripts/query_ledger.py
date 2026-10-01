#!/usr/bin/env python3
import argparse, sqlite3
from kf_common import DB


def main():
    ap = argparse.ArgumentParser(description="Consulta rápida no ledger de notas virtuais/físicas.")
    ap.add_argument("query", nargs="?", default="", help="Texto a buscar no título/slug/resumo")
    ap.add_argument("--domain", default=None)
    ap.add_argument("--subdomain", default=None)
    ap.add_argument("--virtual", action="store_true", help="Busca em virtual_notes em vez de notes")
    ap.add_argument("--limit", type=int, default=25)
    args = ap.parse_args()

    if not DB.exists():
        raise SystemExit("registry/knowledge.sqlite não existe. Restaure com: python knowledge-federation/scripts/restore_ledger_checkpoint.py")

    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    table = "virtual_notes" if args.virtual else "notes"
    cols = {r[1] for r in con.execute(f"PRAGMA table_info({table})")}
    if not cols:
        raise SystemExit(f"Tabela ausente: {table}")

    where = []
    params = []
    if args.domain:
        where.append("domain=?"); params.append(args.domain)
    if args.subdomain:
        where.append("subdomain=?"); params.append(args.subdomain)
    if args.query:
        q = f"%{args.query}%"
        if table == "virtual_notes":
            where.append("(title LIKE ? OR slug LIKE ? OR summary LIKE ?)")
            params.extend([q, q, q])
        else:
            where.append("(title LIKE ? OR slug LIKE ?)")
            params.extend([q, q])
    sql = f"SELECT id, slug, title, domain, subdomain FROM {table}"
    if where:
        sql += " WHERE " + " AND ".join(where)
    sql += " ORDER BY domain, subdomain, title LIMIT ?"
    params.append(args.limit)
    for r in con.execute(sql, params):
        print(f"[{r['domain']}/{r['subdomain']}] {r['title']} :: {r['slug']}")

if __name__ == "__main__":
    main()
