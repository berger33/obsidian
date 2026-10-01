#!/usr/bin/env python3
from pathlib import Path
import argparse
from kf_common import DB
from checkpoint_common import latest_ledger_archive, extract_sqlite_archive


def main():
    ap = argparse.ArgumentParser(description="Restaura o SQLite ledger a partir de um checkpoint compactado (.sqlite.xz ou .zip).")
    ap.add_argument("--archive", default=None, help="Caminho do checkpoint do ledger. Se omitido, usa archives/LATEST-LEDGER.txt")
    ap.add_argument("--force", action="store_true", help="Sobrescreve registry/knowledge.sqlite se já existir")
    args = ap.parse_args()

    archive = Path(args.archive) if args.archive else latest_ledger_archive()
    if not archive.exists():
        raise SystemExit(f"Archive não encontrado: {archive}")
    if DB.exists() and not args.force:
        raise SystemExit(f"{DB} já existe. Use --force para sobrescrever.")

    DB.parent.mkdir(parents=True, exist_ok=True)
    if DB.exists():
        DB.unlink()
    extract_sqlite_archive(archive, DB)
    print(f"Ledger restaurado: {DB}")
    print(f"Origem: {archive}")


if __name__ == "__main__":
    main()
