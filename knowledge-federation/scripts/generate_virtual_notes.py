#!/usr/bin/env python3
from kf_common import *
import argparse, itertools, sqlite3

TEMPLATES = {
    "software": ["{sub} - conceito operacional", "{sub} - padrão de projeto", "{sub} - checklist de implementação", "{sub} - risco técnico", "{sub} - prompt para agente"],
    "ia": ["{sub} - conceito de IA", "{sub} - avaliação prática", "{sub} - arquitetura aplicada", "{sub} - risco e mitigação", "{sub} - prompt de verificação"],
    "vibe-coding": ["{sub} - workflow", "{sub} - prompt operacional", "{sub} - critério de aceite", "{sub} - revisão adversarial", "{sub} - erro comum"],
    "jogos": ["{sub} - sistema de jogo", "{sub} - decisão de engine", "{sub} - validação jogável", "{sub} - risco de escopo", "{sub} - pipeline com IA"],
    "cannabis-medicinal": ["{sub} - estudo legal e terapêutico", "{sub} - rastreabilidade", "{sub} - pergunta clínica", "{sub} - evidência científica", "{sub} - segurança do paciente"],
    "micologia": ["{sub} - taxonomia e segurança", "{sub} - pesquisa científica", "{sub} - legislação", "{sub} - cogumelos legais", "{sub} - redução de danos educacional"],
    "negocio-carreira-produto": ["{sub} - hipótese de produto", "{sub} - validação com IA", "{sub} - métrica", "{sub} - distribuição", "{sub} - carreira e portfólio"]
}

SOURCE_HINTS = {
    "software": "docs oficiais, especificações, repositórios e testes executáveis",
    "ia": "documentação de fornecedores, papers, evals e benchmarks com cautela",
    "vibe-coding": "documentação de agentes, estudos de produtividade e auditoria por diff",
    "jogos": "documentação de engines, GDC, postmortems e playtests",
    "cannabis-medicinal": "fontes médicas, regulatórias e jurídicas; sem instrução operacional",
    "micologia": "literatura científica, taxonomia, legislação e segurança; sem cultivo de espécies controladas",
    "negocio-carreira-produto": "experimentos de produto, métricas, entrevistas e evidência de mercado"
}


def ensure_virtual_schema(con):
    con.executescript("""
    CREATE TABLE IF NOT EXISTS virtual_notes (
      id TEXT PRIMARY KEY,
      slug TEXT NOT NULL,
      title TEXT NOT NULL,
      domain TEXT NOT NULL,
      subdomain TEXT NOT NULL,
      type TEXT NOT NULL,
      level TEXT NOT NULL,
      confidence TEXT NOT NULL,
      validity TEXT NOT NULL,
      risk_legal TEXT DEFAULT 'baixo',
      risk_medical TEXT DEFAULT 'baixo',
      operational_content INTEGER DEFAULT 0,
      summary TEXT NOT NULL,
      body_seed TEXT NOT NULL,
      source_hint TEXT,
      prefix TEXT NOT NULL,
      created_at TEXT NOT NULL,
      materialized_path TEXT,
      materialized_at TEXT,
      quality_status TEXT NOT NULL DEFAULT 'catalog_only'
    );
    CREATE INDEX IF NOT EXISTS idx_virtual_domain ON virtual_notes(domain, subdomain);
    CREATE INDEX IF NOT EXISTS idx_virtual_prefix ON virtual_notes(prefix);
    CREATE UNIQUE INDEX IF NOT EXISTS idx_virtual_slug_prefix ON virtual_notes(prefix, slug);
    """)
    columns = {row[1] for row in con.execute("PRAGMA table_info(virtual_notes)")}
    if "quality_status" not in columns:
        con.execute("ALTER TABLE virtual_notes ADD COLUMN quality_status TEXT NOT NULL DEFAULT 'catalog_only'")
    con.execute("CREATE INDEX IF NOT EXISTS idx_virtual_quality_status ON virtual_notes(quality_status)")
    con.commit()


def domain_pairs(cfg):
    pairs=[]
    for domain, spec in cfg["domains"].items():
        for sub in spec.get("subdomains", ["geral"]):
            pairs.append((domain, sub))
    return pairs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--count", type=int, default=100000)
    ap.add_argument("--prefix", default="vscale1")
    ap.add_argument("--commit-every", type=int, default=5000)
    args = ap.parse_args()
    cfg = load_config()
    con = connect(); ensure_virtual_schema(con)
    existing = con.execute("SELECT COUNT(*) FROM virtual_notes WHERE prefix=?", (args.prefix,)).fetchone()[0]
    if existing >= args.count:
        print(f"Prefixo {args.prefix} já tem {existing} notas virtuais; nada a fazer.")
        return
    pairs = domain_pairs(cfg)
    cycle = itertools.cycle(pairs)
    start = existing + 1
    batch=[]; t=now(); inserted=0
    # avança o ciclo para o ponto existente
    for _ in range(existing):
        next(cycle)
    for i in range(start, args.count + 1):
        domain, sub = next(cycle)
        tmpl = TEMPLATES.get(domain, TEMPLATES["software"])[i % 5]
        title = f"{tmpl.format(sub=sub.replace('-', ' ')).title()} — {args.prefix} #{i:06d}"
        slug = slugify(title)
        note_id = f"virtual.{args.prefix}.{slugify(domain)}.{slugify(sub)}.{i:09d}"
        regulated = domain in ["cannabis-medicinal", "micologia"]
        summary = f"Registro de catálogo para {title} em {domain}/{sub}; conteúdo substantivo ainda não produzido."
        body_seed = (
            f"Entrada de inventário ledger-first para {domain}/{sub}. "
            f"Este registro é apenas uma referência planejada e não deve ser materializado ou contado como nota válida. "
            f"Antes da publicação, redigir conteúdo original, registrar fontes verificáveis e passar pelo gate editorial. "
            f"Pista de pesquisa: {SOURCE_HINTS.get(domain, 'fontes confiáveis e verificação crítica')}."
        )
        batch.append((note_id, slug, title, domain, sub, "conceito", "iniciante" if i % 3 else "intermediario", "media", "volatil", "alto" if regulated else "baixo", "alto" if regulated else "baixo", 0, summary, body_seed, SOURCE_HINTS.get(domain, "fontes confiáveis"), args.prefix, t))
        if len(batch) >= args.commit_every:
            con.executemany("""INSERT OR IGNORE INTO virtual_notes(id,slug,title,domain,subdomain,type,level,confidence,validity,risk_legal,risk_medical,operational_content,summary,body_seed,source_hint,prefix,created_at)
                           VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", batch)
            con.commit(); inserted += len(batch); print(f"Inseridos/ignorados {inserted}..."); batch=[]
    if batch:
        con.executemany("""INSERT OR IGNORE INTO virtual_notes(id,slug,title,domain,subdomain,type,level,confidence,validity,risk_legal,risk_medical,operational_content,summary,body_seed,source_hint,prefix,created_at)
                       VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", batch)
        con.commit(); inserted += len(batch)
    total = con.execute("SELECT COUNT(*) FROM virtual_notes WHERE prefix=?", (args.prefix,)).fetchone()[0]
    print(f"Notas virtuais no prefixo {args.prefix}: {total}")

if __name__ == "__main__":
    main()
