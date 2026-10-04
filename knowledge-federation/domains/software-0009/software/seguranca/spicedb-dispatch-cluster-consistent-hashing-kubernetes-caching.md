---
id: software.seguranca.tranche01.000079
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

# SpiceDB Dispatching Distribuído em Cluster Kubernetes: roteamento por *Consistent Hashing* entre réplicas para maximizar Cache Hit

## Em uma frase
Quando múltiplas réplicas do SpiceDB rodam em um cluster Kubernetes com o **Dispatch Server** interno habilitado (`--dispatch-cluster-enabled=true` e `--dispatch-upstream-addr=kubernetes:///spicedb.authz.svc.cluster.local:50053`), os nós usam **Consistent Hashing** para encaminhar subproblemas de avaliação do grafo sempre para a mesma réplica que já possui aquele subgrafo em cache de memória!

## Por que importa
Se um cluster de 10 Pods do SpiceDB mantivesse caches locais independentes sem *consistent hashing dispatch*, cada Pod teria apenas 10% de taxa de acerto de cache e 90% das subconsultas precisariam bater no banco de dados.

## Como funciona
Com o dispatch de cluster ativado na porta `50053`, se o Pod A recebe um `CheckPermission` sobre `document:1 -> folder:2 -> org:3`, ele despacha a subconsulta de `org:3` para o Pod responsável por aquele hash no anel, alcançando taxas de cache hit próximas de 100% e latências P95 de poucos milissegundos.

## Exemplo
```bash
# Iniciando o SpiceDB em cluster Kubernetes com dispatch entre pares habilitado:
spicedb serve \
  --grpc-preshared-key "${SPICEDB_PRESHARED_KEY}" \
  --dispatch-cluster-enabled=true \
  --dispatch-upstream-addr="kubernetes:///spicedb.authz.svc.cluster.local:50053" \
  --datastore-engine=postgres \
  --datastore-conn-uri="${POSTGRES_URI}"
```

## Limites e trade-offs
Para que a resolução `kubernetes:///` funcione, configure um Service *headless* (`clusterIP: None`) expondo a porta `50053` dos Pods do SpiceDB.

## Como verificar
Monitore as métricas Prometheus do SpiceDB na porta `9090` (`/metrics`) verificando `spicedb_dispatch_...` e a taxa de acerto do cache de dispatch.

## Conexões
- [[spicedb-datastores-postgres-cockroachdb-spanner-mysql-migrate]] — Veja também: SpiceDB Datastores de Produção e `spicedb migrate`: escolha entre `postgres`, `cockroachdb`, `spanner` e `mysql`.
- [[spicedb-watch-api-bulk-import-export-backup-auditoria-eventos]] — Veja também: SpiceDB `Watch` API e Operações em Massa (`zed backup` / `zed restore` / `zed import`): streaming de mudanças e migração de dados.

## Fontes
- [AuthZed SpiceDB GitHub — README.md (Distributed Permissions Database, Zanzibar Architecture, Consistency Modes, Datastores & zed CLI)](https://raw.githubusercontent.com/authzed/spicedb/main/README.md) — README oficial do authzed/spicedb detalhando a arquitetura do banco de permissões, garantias de consistência por requisição, motores de armazenamento e execução em Kubernetes; consultado em 2026-10-03.
- [AuthZed SpiceDB Official Documentation — Schema Language Reference (Definitions, Relations vs Permissions, +, &, -, -> Operators, Precedence & Caveats)](https://authzed.com/docs/spicedb/concepts/schema) — Referência oficial da linguagem de schema do SpiceDB cobrindo definitions, subject relations, wildcards, operadores de conjunto, alerta de precedência do operador + e caveats CEL; consultado em 2026-10-03.
- [AuthZed SpiceDB — Official GitHub Repository](https://github.com/authzed/spicedb) — Repositório oficial Apache-2.0 do AuthZed SpiceDB; consultado em 2026-10-03.
