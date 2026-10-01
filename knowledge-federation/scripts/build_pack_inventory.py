#!/usr/bin/env python3
from pathlib import Path
from kf_common import ROOT, now

ARCH = ROOT / "archives"
OUT = ROOT / "PACK-INVENTORY.md"


def main():
    packs = sorted(ARCH.glob("study-pack-*.zip"))
    lines = [
        "# Inventário de study packs",
        "",
        f"Gerado em: {now()}",
        "",
        "## Vault consolidado",
        "",
        "```text",
        "archives/study-vault-1m-packs.zip",
        "```",
        "",
        "## Packs individuais",
        "",
        "| # | Arquivo | Tamanho |",
        "|---:|---|---:|",
    ]
    for i,p in enumerate(packs,1):
        kb = p.stat().st_size / 1024
        size = f"{kb:.0f}K" if kb < 1024 else f"{kb/1024:.1f}M"
        lines.append(f"| {i} | `{p.relative_to(ROOT).as_posix()}` | {size} |")
    lines += ["", f"Total de packs individuais: **{len(packs)}**.", ""]
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(OUT)

if __name__ == "__main__":
    main()
