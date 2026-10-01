#!/usr/bin/env python3
from kf_common import *
import argparse, sqlite3


def ensure_virtual_schema(con):
    # no-op schema guard for fresh DBs
    con.execute("""CREATE TABLE IF NOT EXISTS virtual_notes (
      id TEXT PRIMARY KEY, slug TEXT, title TEXT, domain TEXT, subdomain TEXT, type TEXT, level TEXT,
      confidence TEXT, validity TEXT, risk_legal TEXT, risk_medical TEXT, operational_content INTEGER,
      summary TEXT, body_seed TEXT, source_hint TEXT, prefix TEXT, created_at TEXT,
      materialized_path TEXT, materialized_at TEXT
    )""")
    con.commit()


def render(row, related):
    regulated = row["domain"] in ["cannabis-medicinal", "micologia"]
    warning = "\n> [!warning] Domínio regulado\n> Conteúdo educacional e de organização de estudo. Não é instrução operacional, prescrição, parecer jurídico ou substituto de profissional habilitado.\n" if regulated else ""
    links = "\n".join([f"- [[{r['slug']}]] — nota virtual materializada relacionada." for r in related[:5]])
    return f"""---
id: {row['id']}
tipo: {row['type']}
dominio: {row['domain']}
subdominio: {row['subdomain']}
nivel: {row['level']}
confianca: {row['confidence']}
ultima_verificacao: {TODAY}
validade: {row['validity']}
risco_legal: {row['risk_legal']}
risco_medico: {row['risk_medical']}
conteudo_operacional: false
status: materializada
fontes: []
tags: [dominio/{row['domain']}, subdominio/{row['subdomain']}, origem/virtual]
aliases: ["{row['title']}"]
prefixo_virtual: {row['prefix']}
---
# {row['title']}
{warning}
## Em uma frase
{row['summary']}

## Por que importa
Esta nota faz parte do ledger de conhecimento em escala. Ela existe para ser estudada, expandida e conectada quando o tema se tornar relevante para uma decisão prática.

## Como funciona
{row['body_seed']}

## Como pedir isso para uma IA
```text
Expanda a nota "{row['title']}" usando fontes primárias, separando fato, hipótese e opinião. Gere conexões com notas relacionadas, riscos, critérios de verificação e perguntas para especialistas quando necessário.
```

## Como verificar
- Conferir fontes oficiais ou acadêmicas.
- Marcar dados voláteis com data.
- Em software, validar com teste, diff e execução.
- Em domínios regulados, transformar em perguntas para profissional habilitado.

## Conexões
{links}

## Fontes a buscar
- {row['source_hint']}
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--domain", default=None)
    ap.add_argument("--subdomain", default=None)
    ap.add_argument("--prefix", default=None)
    ap.add_argument("--limit", type=int, default=1000)
    ap.add_argument("--out", default="materialized")
    args = ap.parse_args()
    con = connect(); ensure_virtual_schema(con)
    where=[]; params=[]
    if args.domain:
        where.append("domain=?"); params.append(args.domain)
    if args.subdomain:
        where.append("subdomain=?"); params.append(args.subdomain)
    if args.prefix:
        where.append("prefix=?"); params.append(args.prefix)
    where.append("materialized_path IS NULL")
    sql = "SELECT * FROM virtual_notes WHERE " + " AND ".join(where) + " ORDER BY id LIMIT ?"
    params.append(args.limit)
    rows = con.execute(sql, params).fetchall()
    if not rows:
        print("Nenhuma nota virtual pendente para materializar.")
        return
    base = ROOT / args.out
    base.mkdir(parents=True, exist_ok=True)
    # related dentro do lote materializado
    for idx,row in enumerate(rows):
        related = rows[idx+1:idx+6] + rows[:5]
        outdir = base / row["domain"] / row["subdomain"]
        outdir.mkdir(parents=True, exist_ok=True)
        path = outdir / f"{row['slug']}.md"
        content = render(row, related)
        path.write_text(content, encoding="utf-8")
        con.execute("UPDATE virtual_notes SET materialized_path=?, materialized_at=? WHERE id=?", (str(path.relative_to(ROOT)), now(), row["id"]))
    con.commit()
    print(f"Materializadas {len(rows)} notas em {base}")

if __name__ == "__main__":
    main()
