#!/usr/bin/env python3
from kf_common import *
import argparse, zipfile

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vault", required=True)
    args = ap.parse_args()
    src = ROOT / "domains" / args.vault
    if not src.exists(): raise SystemExit(f"Vault não encontrado: {src}")
    out = ROOT / "exports" / "zips" / f"{args.vault}.zip"
    out.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for f in src.rglob("*"):
            if f.is_file(): z.write(f, f.relative_to(ROOT / "domains"))
    print(out)

if __name__ == "__main__":
    main()
