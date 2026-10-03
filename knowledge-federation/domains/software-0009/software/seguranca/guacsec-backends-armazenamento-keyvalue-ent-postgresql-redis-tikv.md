---
id: software.seguranca.tranche04.000376
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-04.md"
fontes: ["https://raw.githubusercontent.com/guacsec/guac/main/README.md", "https://docs.guac.sh/guac/", "https://github.com/guacsec/guac/blob/main/use-cases.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# OpenSSF GUAC: Backends de Persistência (`keyvalue` In-Memory vs `ent` com PostgreSQL)

## Em uma frase
O Assembler do GUAC suporta múltiplos backends de armazenamento por trás da mesma interface GraphQL, sendo os dois backends oficiais suportados, completos e otimizados: **`keyvalue`** (em memória) e **`ent` com PostgreSQL** (persistente).

## Por que importa
Permite iniciar testes rápidos de conformidade ou jobs efêmeros de CI com o backend `keyvalue` sem infraestrutura externa, e operar um grafo corporativo persistente de longo prazo usando `ent` sobre PostgreSQL gerenciado.

## Como funciona
O backend `keyvalue` mantém todas as entidades e arestas em memória RAM (com variantes experimentais sobre Redis e TiKV), servindo como implementação de referência da API GraphQL. Já o backend `ent` utiliza o framework *entgo* otimizado especificamente para PostgreSQL, persistindo milhões de nós de pacotes, SBOMs e atestações com integridade relacional.

## Exemplo
```bash
# Iniciar o servidor GraphQL do GUAC usando o backend persistente Ent com PostgreSQL
guacgql \
  --gql-backend ent \
  --db-driver postgres \
  --db-address "postgres://guac_user:${DB_PASS}@postgres.internal.corp:5432/guac_db?sslmode=verify-full" \
  --db-migrate
```

## Limites e trade-offs
Os backends `arangodb` e `neo4j` presentes no repositório são classificados oficialmente como *unsupported/incomplete*; em produção, utilize exclusivamente o backend `ent` com PostgreSQL (ou `keyvalue` para instâncias efêmeras).

## Como verificar
Execute `guacgql` com `--gql-backend ent --db-migrate` e confirme a criação das tabelas no PostgreSQL e a resposta HTTP 200 na introspecção GraphQL.

## Conexões
- [[guacsec-consultas-vulnerabilidades-transitivas-guacone-query-vuln-vex]] — Veja também: OpenSSF GUAC: Rastreamento de Vulnerabilidades Transitivas (`guacone query vuln`) e Filtragem por VEX (`OpenVEX` / `CSAF`).
- [[guacsec-arquitetura-eventos-nats-jetstream-collectsub-escala]] — Veja também: OpenSSF GUAC: Pipeline Assíncrono em Escala com NATS JetStream, `collectsub` e `guacingest`.
- [[guacsec-arquitetura-openssf-supply-chain-graph-sbom-slsa-vex]] — Referência cruzada direta com guacsec-arquitetura-openssf-supply-chain-graph-sbom-slsa-vex.
- [[guacsec-api-graphql-rest-guac-visualizer-integracao]] — Referência cruzada direta com guacsec-api-graphql-rest-guac-visualizer-integracao.

## Fontes
- [OpenSSF GUAC GitHub — README.md (Graph for Understanding Artifact Composition Architecture, Supported Input Documents & GraphQL Backends)](https://raw.githubusercontent.com/guacsec/guac/main/README.md) — README oficial do guacsec/guac apresentando o modelo lógico de agregação e síntese da cadeia de suprimentos, formatos suportados e backends Ent/PostgreSQL e Keyvalue; consultado em 2026-10-03.
- [OpenSSF GUAC Official Documentation — GUAC Docs (Visualizer, Querying Vulnerabilities via CLI guacone, Known Package Queries & SBOM Mapping)](https://docs.guac.sh/guac/) — Documentação oficial do GUAC demonstrando consultas transitivas de vulnerabilidades, inspeção de pacotes PURL e enriquecimento com OSV.dev, deps.dev e Scorecard; consultado em 2026-10-03.
- [OpenSSF GUAC — Official Supply Chain Use Cases (use-cases.md)](https://github.com/guacsec/guac/blob/main/use-cases.md) — Documento oficial de casos de uso de auditoria, resposta a incidentes e políticas no OpenSSF GUAC; consultado em 2026-10-03.
