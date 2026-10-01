#!/usr/bin/env python3
from pathlib import Path
import argparse, zipfile
from kf_common import ROOT, DB


def read_latest():
    p = ROOT / "archives" / "LATEST-LEDGER.txt"
    data = {}
    if p.exists():
        for line in p.read_text(encoding="utf-8").splitlines():
            if "=" in line:
                k, v = line.split("=", 1)
                data[k.strip()] = v.strip()
    return data


def main():
    ap = argparse.ArgumentParser(description="Restaura o SQLite ledger a partir de um checkpoint compactado.")
    ap.add_argument("--archive", default=None, help="Caminho do zip do ledger. Se omitido, usa archives/LATEST-LEDGER.txt")
    ap.add_argument("--force", action="store_true", help="Sobrescreve registry/knowledge.sqlite se já existir")
    args = ap.parse_args()

    if args.archive:
        archive = Path(args.archive)
    else:
        latest = read_latest()
        name = latest.get("archive")
        if not name:
            raise SystemExit("Não encontrei archive em archives/LATEST-LEDGER.txt")
        archive = ROOT / "archives" / name

    if not archive.exists():
        raise SystemExit(f"Archive não encontrado: {archive}")
    if DB.exists() and not args.force:
        raise SystemExit(f"{DB} já existe. Use --force para sobrescrever.")

    DB.parent.mkdir(parents=True, exist_ok=True)
    if DB.exists():
        DB.unlink()
    with zipfile.ZipFile(archive) as z:
        z.extract("knowledge.sqlite", DB.parent)
    print(f"Ledger restaurado: {DB}")
    print(f"Origem: {archive}")

if __name__ == "__main__":
    main()
