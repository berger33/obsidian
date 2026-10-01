#!/usr/bin/env python3
from kf_common import *
import argparse

BLOCKED_TERMS = [
    "passo a passo de cultivo", "parametros de cultivo", "substrato para psilocybe", "inoculacao de psilocybe",
    "frutificacao de psilocybe", "extracao operacional", "otimizacao de potencia", "ocultacao", "burlar fiscalizacao"
]

def render_note(item, manifest, related):
    domain = item["domain"]
    regulated = domain in ["cannabis-medicinal", "micologia"]
    safety = "\n> [!warning] Domínio regulado\n> Esta nota é educacional e não substitui médico, advogado, farmacêutico, agrônomo ou autoridade competente. Não contém instruções operacionais de produção, extração ou evasão legal.\n" if regulated else ""
    sources = []
    if domain == "software": sources = ["https://developer.mozilla.org/", "https://docs.github.com/"]
    elif domain == "ia": sources = ["https://modelcontextprotocol.io/", "https://docs.github.com/en/copilot"]
    elif domain == "vibe-coding": sources = ["https://code.claude.com/docs/en/overview", "https://docs.github.com/en/copilot"]
    elif domain == "jogos": sources = ["https://docs.godotengine.org/", "https://unity.com/products/pricing-updates"]
    elif domain == "cannabis-medicinal": sources = ["https://www.gov.br/anvisa/", "https://www.gov.br/anpd/pt-br"]
    elif domain == "micologia": sources = ["https://www.ncbi.nlm.nih.gov/", "https://www.gov.br/anvisa/"]
    else: sources = ["https://docs.github.com/"]
    links = "\n".join([f"- [[{r['slug']}]] — nota relacionada do mesmo lote." for r in related[:4]])
    body = f"""---
id: {item['id']}
tipo: {item['type']}
dominio: {item['domain']}
subdominio: {item['subdomain']}
nivel: {item['level']}
confianca: media
ultima_verificacao: {TODAY}
validade: volatil
risco_legal: {item['risk_legal']}
risco_medico: {item['risk_medical']}
conteudo_operacional: false
status: semente
fontes: {sources}
tags: [dominio/{item['domain']}, subdominio/{item['subdomain']}]
aliases: [{item['title']!r}]
lote: {manifest['batch_id']}
---
# {item['title']}
{safety}
## Em uma frase
Nota semente sobre **{item['title']}**, criada para compor o mapa federado de conhecimento em {item['domain']} / {item['subdomain']}.

## Por que importa
Este tópico ajuda a transformar conhecimento disperso em decisões práticas. Para um orquestrador de IA, a utilidade está em saber formular perguntas melhores, verificar respostas, registrar fontes e conectar o assunto a projetos reais.

## Como funciona
Use esta nota como ponto de entrada. Em lotes futuros ela pode ser expandida com pesquisa profunda, fontes específicas, exemplos seguros, comparativos e árvores de decisão. A versão atual prioriza estrutura, rastreabilidade e conexão no grafo.

## Quando usar / quando não usar
Use quando precisar mapear o assunto, criar perguntas para especialistas ou orientar um agente de pesquisa. Não use como prescrição médica, parecer jurídico, instrução operacional regulada ou substituto de validação profissional.

## Como pedir isso para uma IA
```text
Pesquise {item['title']} com fontes primárias, separe fato de opinião, registre data de verificação, aponte riscos e produza uma versão segura para estudo no Obsidian.
```

## Conexões
{links}

## Fontes
""" + "\n".join([f"- {s} — fonte inicial a verificar, acesso: {TODAY}." for s in sources]) + "\n"
    low = body.lower()
    if any(t in low for t in BLOCKED_TERMS):
        raise ValueError(f"Filtro de segurança acionado para {item['id']}")
    return body

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch", required=True)
    ap.add_argument("--limit", type=int, default=None)
    args = ap.parse_args()
    con = connect()
    mp = manifest_path(args.batch)
    if not mp.exists():
        raise SystemExit(f"Manifesto não encontrado. Rode generate_seed_manifest.py --batch {args.batch}")
    manifest = read_json(mp)
    items = manifest["items"][:args.limit] if args.limit else manifest["items"]
    statep = batch_state_path(args.batch)
    state = read_json(statep) if statep.exists() else {"batch_id": args.batch, "last_completed_index": 0, "total": len(items), "status": "drafting"}
    start = int(state.get("last_completed_index", 0))
    outdir = note_dir(manifest["vault"], manifest["domain"], manifest["subdomain"])
    outdir.mkdir(parents=True, exist_ok=True)
    generated = 0
    for idx in range(start, len(items)):
        item = items[idx]
        related = [x for x in items if x["id"] != item["id"]]
        related = related[idx+1:idx+5] + related[:4]
        content = render_note(item, manifest, related)
        path = outdir / f"{item['slug']}.md"
        path.write_text(content, encoding="utf-8")
        h = sha(content)
        t = now()
        con.execute("""INSERT OR REPLACE INTO notes(id,slug,title,domain,subdomain,type,level,status,batch_id,vault,path,content_hash,risk_legal,risk_medical,operational_content,created_at,updated_at)
                       VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", (item["id"], item["slug"], item["title"], item["domain"], item["subdomain"], item["type"], item["level"], "drafted", args.batch, manifest["vault"], str(path.relative_to(ROOT)), h, item["risk_legal"], item["risk_medical"], 0, t, t))
        for r in related[:4]:
            con.execute("INSERT OR IGNORE INTO links(from_id,to_id,batch_id) VALUES(?,?,?)", (item["id"], r["id"], args.batch))
        generated += 1
        if (idx + 1) % 50 == 0 or idx == len(items) - 1:
            write_json(statep, {"batch_id": args.batch, "status": "drafting", "last_completed_index": idx + 1, "total": len(items), "updated_at": now()})
            con.execute("UPDATE batches SET generated_count=?, status=?, updated_at=? WHERE batch_id=?", (idx + 1, "drafting", now(), args.batch))
            con.commit()
    con.execute("UPDATE batches SET generated_count=?, status=?, updated_at=? WHERE batch_id=?", (len(items), "auditing", now(), args.batch))
    con.commit()
    print(f"Geradas {generated} notas em {outdir}")

if __name__ == "__main__":
    main()
