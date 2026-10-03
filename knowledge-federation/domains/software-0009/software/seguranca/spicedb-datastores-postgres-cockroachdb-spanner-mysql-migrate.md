---
id: software.seguranca.tranche01.000078
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-01.md"
fontes: ["https://raw.githubusercontent.com/authzed/spicedb/main/README.md", "https://authzed.com/docs/spicedb/concepts/schema", "https://github.com/authzed/spicedb"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# SpiceDB Datastores de Produção e `spicedb migrate`: escolha entre `postgres`, `cockroachdb`, `spanner` e `mysql`

## Em uma frase
O SpiceDB desacopla o motor de avaliação de grafo da camada de persistência, suportando quatro *datastore engines* de produção além do modo `memory`: **`postgres`** (PostgreSQL), **`cockroachdb`** (CockroachDB multi-região), **`spanner`** (Google Cloud Spanner) e **`mysql`** (MySQL), gerenciados pelo comando **`spicedb migrate`** e pelo **SpiceDB Operator** no Kubernetes.

## Por que importa
A escolha do datastore define a topologia geográfica e as garantias de janela de quantização do `ZedToken`: para implantações em uma única região, o **PostgreSQL** entrega excelente custo-benefício e baixa latência; para implantações ativas-ativas distribuídas globalmente em múltiplas regiões, **CockroachDB** ou **Cloud Spanner** fornecem transações distribuídas nativas.

## Como funciona
Antes de iniciar o `spicedb serve` contra um banco persistente, execute `spicedb migrate head --datastore-engine postgres --datastore-conn-uri ...` para criar/atualizar as tabelas de tuplas e transações.

## Exemplo
```bash
# Executando migrações até a versão head no PostgreSQL e iniciando o servidor SpiceDB:
spicedb migrate head \
  --datastore-engine postgres \
  --datastore-conn-uri "postgres://spicedb:secret@pg.internal:5432/spicedb?sslmode=require"

spicedb serve \
  --grpc-preshared-key "${SPICEDB_PRESHARED_KEY}" \
  --datastore-engine postgres \
  --datastore-conn-uri "postgres://spicedb:secret@pg.internal:5432/spicedb?sslmode=require"
```

## Limites e trade-offs
No PostgreSQL, o SpiceDB também suporta roteamento para réplicas somente-leitura para escalar horizontalmente a vazão de consultas.

## Como verificar
Verifique a revisão atual de migração do datastore com `spicedb datastore repair` / logs de inicialização do `spicedb serve`.

## Conexões
- [[spicedb-validacao-testes-schema-zed-validate-assertions-ci]] — Veja também: SpiceDB Validação e Testes em CI/CD (`zed validate`): arquivos YAML de schema, relacionamentos de teste, `assertions` e `expected_relations`.
- [[spicedb-dispatch-cluster-consistent-hashing-kubernetes-caching]] — Veja também: SpiceDB Dispatching Distribuído em Cluster Kubernetes: roteamento por *Consistent Hashing* entre réplicas para maximizar Cache Hit.

## Fontes
- [AuthZed SpiceDB GitHub — README.md (Distributed Permissions Database, Zanzibar Architecture, Consistency Modes, Datastores & zed CLI)](https://raw.githubusercontent.com/authzed/spicedb/main/README.md) — README oficial do authzed/spicedb detalhando a arquitetura do banco de permissões, garantias de consistência por requisição, motores de armazenamento e execução em Kubernetes; consultado em 2026-10-03.
- [AuthZed SpiceDB Official Documentation — Schema Language Reference (Definitions, Relations vs Permissions, +, &, -, -> Operators, Precedence & Caveats)](https://authzed.com/docs/spicedb/concepts/schema) — Referência oficial da linguagem de schema do SpiceDB cobrindo definitions, subject relations, wildcards, operadores de conjunto, alerta de precedência do operador + e caveats CEL; consultado em 2026-10-03.
- [AuthZed SpiceDB — Official GitHub Repository](https://github.com/authzed/spicedb) — Repositório oficial Apache-2.0 do AuthZed SpiceDB; consultado em 2026-10-03.
