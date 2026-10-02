#!/usr/bin/env python3
from kf_common import *
from note_quality import assess_markdown
import argparse, re

BLOCK_PATTERNS = [
  r"passo\s+a\s+passo\s+de\s+cultivo", r"substrato\s+para\s+psilocybe", r"inocula", r"frutifica",
  r"otimiza.{0,30}(potencia|rendimento)", r"burlar\s+fiscalizacao", r"ocultacao"
]


def suggested_batch_status(structural_ok, quality_ok, note_count, factually_reviewed_count):
    """A complete batch needs the gate and an explicit human or AI review per note."""
    if not structural_ok or not quality_ok:
        return "needs_review"
    if note_count > 0 and factually_reviewed_count == note_count:
        return "complete"
    return "ready_for_review"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch", required=True)
    args = ap.parse_args()
    con = connect()
    b = con.execute("SELECT * FROM batches WHERE batch_id=?", (args.batch,)).fetchone()
    if not b: raise SystemExit("batch não encontrado")
    rows = con.execute("SELECT * FROM notes WHERE batch_id=?", (args.batch,)).fetchall()
    broken=[]; nofm=[]; blocked=[]; orphan=[]; quality_issues=[]
    quality_ready=0; human_reviewed=0; ai_reviewed=0; factually_reviewed=0
    slugs = {r["slug"] for r in rows}
    incoming = {r["slug"]: 0 for r in rows}
    for r in rows:
        p = ROOT / r["path"]
        if not p.exists():
            broken.append(f"arquivo ausente: {r['path']}")
            con.execute("UPDATE notes SET quality_status='needs_review' WHERE id=?", (r["id"],))
            continue
        txt = p.read_text(encoding="utf-8")
        if not txt.startswith("---"):
            nofm.append(r["slug"])
        quality = assess_markdown(txt, r["path"])
        if quality["ready_for_review"]:
            quality_ready += 1
            quality_status = "reviewed" if quality["valid_reviewed"] else "ready_for_review"
        else:
            quality_status = "needs_review"
            quality_issues.append(f"{r['slug']} :: {', '.join(quality['errors'])}")
        con.execute("UPDATE notes SET quality_status=? WHERE id=?", (quality_status, r["id"]))
        if quality["human_reviewed"]:
            human_reviewed += 1
        if quality["ai_reviewed"]:
            ai_reviewed += 1
        if quality["valid_reviewed"]:
            factually_reviewed += 1
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
    structural_ok = not broken and not nofm and not blocked
    quality_ok = bool(rows) and len(quality_issues) == 0 and quality_ready == len(rows)
    status = suggested_batch_status(structural_ok, quality_ok, len(rows), factually_reviewed)
    report = f"""# Auditoria {args.batch}

- lote: {args.batch}
- domínio: {b['domain']}/{b['subdomain']}
- notas no registro: {len(rows)}
- candidatas aprovadas no gate automatizado: {quality_ready}/{len(rows)}
- notas com revisão factual humana registrada: {human_reviewed}/{len(rows)}
- notas com revisão factual por IA registrada: {ai_reviewed}/{len(rows)}
- notas com revisão factual humana ou por IA: {factually_reviewed}/{len(rows)}
- status sugerido: {status}
- links/arquivos quebrados: {len(broken)}
- sem frontmatter: {len(nofm)}
- bloqueios de segurança: {len(blocked)}
- pendências no gate de conteúdo: {len(quality_issues)}
- possíveis órfãs dentro do lote: {len(orphan)}

> Passar pelo gate automatizado não comprova veracidade. `complete` exige também revisão factual registrada por pessoa ou IA; o tipo e o responsável permanecem separados no frontmatter e neste relatório.

## Links/arquivos quebrados
{chr(10).join('- '+x for x in broken[:200]) or 'Nenhum.'}

## Sem frontmatter
{chr(10).join('- '+x for x in nofm[:200]) or 'Nenhum.'}

## Bloqueios de segurança
{chr(10).join('- '+x for x in blocked[:200]) or 'Nenhum.'}

## Pendências de conteúdo
{chr(10).join('- '+x for x in quality_issues[:200]) or 'Nenhuma.'}

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
