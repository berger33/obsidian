#!/usr/bin/env python3
from pathlib import Path
import re, json
from kf_common import ROOT, now

VAULT = ROOT / "study-vault-1m-packs"
REPORT = VAULT / "_meta" / "auditoria-study-vault.md"
LINK_RE = re.compile(r"!??\[\[([^\]|#]+)(?:[#|][^\]]*)?\]\]")

def main():
    if not VAULT.exists():
        raise SystemExit("study-vault-1m-packs não existe")
    md = sorted(VAULT.rglob("*.md"))
    stems = {p.stem for p in md}
    paths = {p.relative_to(VAULT).as_posix() for p in md}
    broken=[]; total_links=0
    for p in md:
        txt=p.read_text(encoding="utf-8", errors="ignore")
        for m in LINK_RE.finditer(txt):
            target=m.group(1).strip()
            total_links += 1
            if target.endswith(".md"):
                ok = target in paths or target.replace(" ", "%20") in paths
            else:
                ok = target in stems
            if not ok:
                broken.append((p.relative_to(VAULT).as_posix(), target))
    canvas = sorted(VAULT.rglob("*.canvas"))
    report = [
        "# Auditoria — Study Vault 1M Packs",
        "",
        f"Gerado em: {now()}",
        "",
        f"Arquivos Markdown: {len(md)}",
        f"Canvas: {len(canvas)}",
        f"Links wiki analisados: {total_links}",
        f"Links quebrados: {len(broken)}",
        "",
    ]
    if broken:
        report += ["## Links quebrados", ""]
        for src,tgt in broken[:200]:
            report.append(f"- `{src}` → `[[{tgt}]]`")
        if len(broken)>200:
            report.append(f"- ... mais {len(broken)-200}")
    else:
        report.append("Nenhum link quebrado encontrado pela auditoria simples de wiki links.")
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(report)+"\n", encoding="utf-8")
    print(REPORT)
    print(f"markdown={len(md)} canvas={len(canvas)} links={total_links} broken={len(broken)}")
    raise SystemExit(1 if broken else 0)

if __name__ == "__main__":
    main()
