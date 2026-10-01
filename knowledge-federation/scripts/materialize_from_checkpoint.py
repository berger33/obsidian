#!/usr/bin/env python3
import argparse, sqlite3, zipfile, shutil
from pathlib import Path
from checkpoint_common import cached_sqlite_from_archive
from kf_common import ROOT, TODAY


def render(row, related):
    regulated = row["domain"] in ["cannabis-medicinal", "micologia"]
    warning = "\n> [!warning] Domínio regulado\n> Conteúdo educacional para organização de estudo e conversa com profissionais habilitados. Não é prescrição, parecer jurídico nem instrução operacional.\n" if regulated else ""
    links = "\n".join([f"- [[{r['slug']}]] — relacionada no mesmo recorte materializado." for r in related[:5]])
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
status: catalog-placeholder
quality_status: catalog_only
fontes: []
tags: [dominio/{row['domain']}, subdominio/{row['subdomain']}, origem/checkpoint]
aliases: ["{row['title']}"]
prefixo_virtual: {row['prefix']}
---
# {row['title']}
{warning}
## Em uma frase
{row['summary']}

## Por que importa
Este arquivo apenas materializa um registro de catálogo. O corpo substantivo não foi redigido nem validado; não conte esta página como nota pronta para estudo ou decisão.

## Como funciona
{row['body_seed']}

## Como pedir isso para uma IA
```text
Expanda a nota "{row['title']}" com fontes primárias, exemplos seguros, conexões e critérios de verificação. Separe fato, hipótese, opinião e marketing.
```

## Como verificar
- Conferir documentação, literatura ou fonte regulatória primária.
- Registrar data de verificação.
- Em software, validar com execução, teste e revisão de diff.
- Em saúde, direito ou domínios regulados, transformar em perguntas para profissional habilitado.

## Conexões
{links}

## Fontes a buscar
- {row['source_hint']}
"""


def main():
    ap = argparse.ArgumentParser(description="Materializa registros de catálogo como placeholders Markdown; não produz notas válidas.")
    ap.add_argument("--archive", default=None)
    ap.add_argument("--domain", default=None)
    ap.add_argument("--subdomain", default=None)
    ap.add_argument("--prefix", default=None)
    ap.add_argument("--query", default=None)
    ap.add_argument("--limit", type=int, default=500)
    ap.add_argument("--out", default="checkpoint-materialized")
    ap.add_argument("--zip", dest="zip_path", default=None)
    ap.add_argument("--clean", action="store_true")
    ap.add_argument(
        "--allow-catalog-stubs", action="store_true",
        help="Permite materializar registros de catálogo como placeholders explicitamente marcados; não são notas válidas.",
    )
    args = ap.parse_args()
    if args.limit < 1:
        ap.error("--limit deve ser positivo")
    if not args.allow_catalog_stubs:
        raise SystemExit(
            "Materialização de registros-template bloqueada por padrão. "
            "Use --allow-catalog-stubs apenas para inspeção/recuperação; isso não cria notas válidas."
        )

    db = cached_sqlite_from_archive(args.archive)
    con = sqlite3.connect(db)
    con.row_factory = sqlite3.Row
    where=[]; params=[]
    if args.domain:
        where.append("domain=?"); params.append(args.domain)
    if args.subdomain:
        where.append("subdomain=?"); params.append(args.subdomain)
    if args.prefix:
        where.append("prefix=?"); params.append(args.prefix)
    if args.query:
        q=f"%{args.query}%"; where.append("(title LIKE ? OR slug LIKE ? OR summary LIKE ?)"); params += [q,q,q]
    sql = "SELECT * FROM virtual_notes"
    if where:
        sql += " WHERE " + " AND ".join(where)
    sql += " ORDER BY domain, subdomain, title LIMIT ?"
    params.append(args.limit)
    rows = list(con.execute(sql, params))
    outbase = ROOT / args.out
    if args.clean and outbase.exists():
        shutil.rmtree(outbase)
    outbase.mkdir(parents=True, exist_ok=True)
    for idx,row in enumerate(rows):
        related = rows[idx+1:idx+6] + rows[:5]
        outdir = outbase / row["domain"] / row["subdomain"]
        outdir.mkdir(parents=True, exist_ok=True)
        (outdir / f"{row['slug']}.md").write_text(render(row, related), encoding="utf-8")
    readme = outbase / "README.md"
    readme.write_text(
        f"# Recorte de catálogo materializado\n\nArquivos-placeholder: {len(rows)}\n"
        f"Notas válidas aprovadas: 0\n"
        f"Filtro: domain={args.domain}, subdomain={args.subdomain}, prefix={args.prefix}, query={args.query}\n",
        encoding="utf-8",
    )
    if args.zip_path:
        zpath = ROOT / args.zip_path
        zpath.parent.mkdir(parents=True, exist_ok=True)
        if zpath.exists(): zpath.unlink()
        with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
            for f in outbase.rglob("*"):
                if f.is_file(): z.write(f, f.relative_to(ROOT))
        print(zpath)
    print(f"Materializados {len(rows)} registros como catalog-placeholder em {outbase}; não são notas válidas.")

if __name__ == "__main__":
    main()
