#!/usr/bin/env python3
from kf_common import *
import argparse, re

BLOCK_PATTERNS = [
  r"passo\s+a\s+passo\s+de\s+cultivo", r"substrato\s+para\s+psilocybe", r"inocula", r"frutifica",
  r"otimiza.{0,30}(potencia|rendimento)", r"burlar\s+fiscalizacao", r"ocultacao"
]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch", required=True)
    args = ap.parse_args()
    con = connect()
    b = con.execute("SELECT * FROM batches WHERE batch_id=?", (args.batch,)).fetchone()
    if not b: raise SystemExit("batch não encontrado")
    rows = con.execute("SELECT * FROM notes WHERE batch_id=?", (args.batch,)).fetchall()
    broken=[]; nofm=[]; blocked=[]; orphan=[]
    slugs = {r["slug"] for r in rows}
    incoming = {r["slug"]: 0 for r in rows}
    for r in rows:
        p = ROOT / r["path"]
        if not p.exists():
            broken.append(f"arquivo ausente: {r['path']}")
            continue
        txt = p.read_text(encoding="utf-8")
        if not txt.startswith("---"):
            nofm.append(r["slug"])
        if r["domain"] in ["cannabis-medicinal", "micologia"]:
            for pat in BLOCK_PATTERNS:
                if re.search(pat, txt, re.I):
                    blocked.append(f"{r['slug']} :: {pat}")
        for lk in re.findall(r"\[\[([^\]|#]+)", txt):
            if lk in incoming: incoming[lk]+=1
            elif lk not in slugs:
                broken.append(f"{r['slug']} -> {lk}")
    for s,c in incoming.items():
        if c == 0 and len(rows) > 1:
            # em lotes pequenos pode haver órfãos parciais; mantém relatório apenas
            orphan.append(s)
    status = "complete" if not broken and not nofm and not blocked else "needs_review"
    report = f"""# Auditoria {args.batch}

- lote: {args.batch}
- domínio: {b['domain']}/{b['subdomain']}
- notas no registro: {len(rows)}
- status sugerido: {status}
- links/arquivos quebrados: {len(broken)}
- sem frontmatter: {len(nofm)}
- bloqueios de segurança: {len(blocked)}
- possíveis órfãs dentro do lote: {len(orphan)}

## Links/arquivos quebrados
{chr(10).join('- '+x for x in broken[:200]) or 'Nenhum.'}

## Sem frontmatter
{chr(10).join('- '+x for x in nofm[:200]) or 'Nenhum.'}

## Bloqueios de segurança
{chr(10).join('- '+x for x in blocked[:200]) or 'Nenhum.'}

## Possíveis órfãs
{chr(10).join('- [[{}]]'.format(x) for x in orphan[:200]) or 'Nenhuma.'}
"""
    apath = audit_path(args.batch)
    apath.parent.mkdir(parents=True, exist_ok=True)
    apath.write_text(report, encoding="utf-8")
    con.execute("UPDATE batches SET status=?, audit_path=?, updated_at=? WHERE batch_id=?", (status, str(apath.relative_to(ROOT)), now(), args.batch))
    con.commit()
    print(f"Auditoria: {apath} status={status}")

if __name__ == "__main__":
    main()
