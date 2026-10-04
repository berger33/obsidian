---
id: software.seguranca.tranche01.000080
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

# SpiceDB `Watch` API e Operações em Massa (`zed backup` / `zed restore` / `zed import`): streaming de mudanças e migração de dados

## Em uma frase
O SpiceDB expõe a API gRPC **`Watch`** (que emite em tempo real um stream contínuo de todas as mutações de relacionamentos e alterações de schema à medida que ocorrem no datastore) e comandos de linha de comando na ferramenta `zed` para **backup, restore e importação em lote (`zed backup`, `zed restore`, `zed import`)**.

## Por que importa
Sistemas externos de busca (como Elasticsearch/OpenSearch), caches de borda ou trilhas de auditoria de segurança frequentemente precisam reagir em tempo real sempre que uma permissão é concedida ou revogada no SpiceDB.

## Como funciona
Consumindo o stream da `Watch` API a partir de um `ZedToken` de checkpoint, um worker assíncrono recebe cada tupla adicionada ou removida em ordem transacional. Já `zed backup` e `zed restore` permitem copiar um banco inteiro de produção para um ambiente de staging ou teste local em segundos.

## Exemplo
```bash
# Realizando backup completo do schema e relacionamentos para um arquivo local e restaurando:
zed backup prod-permissions.backup
zed restore prod-permissions.backup
```

## Limites e trade-offs
Ao importar milhões de relacionamentos iniciais durante uma migração para o SpiceDB, utilize a API `BulkImportRelationships` (via `zed restore` / `zed import`) em vez de chamar `WriteRelationships` tupla por tupla.

## Como verificar
Inspecione o arquivo de backup ou valide a contagem de relacionamentos restaurados com `zed relationship read`.

## Conexões
- [[spicedb-dispatch-cluster-consistent-hashing-kubernetes-caching]] — Veja também: SpiceDB Dispatching Distribuído em Cluster Kubernetes: roteamento por *Consistent Hashing* entre réplicas para maximizar Cache Hit.

## Fontes
- [AuthZed SpiceDB GitHub — README.md (Distributed Permissions Database, Zanzibar Architecture, Consistency Modes, Datastores & zed CLI)](https://raw.githubusercontent.com/authzed/spicedb/main/README.md) — README oficial do authzed/spicedb detalhando a arquitetura do banco de permissões, garantias de consistência por requisição, motores de armazenamento e execução em Kubernetes; consultado em 2026-10-03.
- [AuthZed SpiceDB Official Documentation — Schema Language Reference (Definitions, Relations vs Permissions, +, &, -, -> Operators, Precedence & Caveats)](https://authzed.com/docs/spicedb/concepts/schema) — Referência oficial da linguagem de schema do SpiceDB cobrindo definitions, subject relations, wildcards, operadores de conjunto, alerta de precedência do operador + e caveats CEL; consultado em 2026-10-03.
- [AuthZed SpiceDB — Official GitHub Repository](https://github.com/authzed/spicedb) — Repositório oficial Apache-2.0 do AuthZed SpiceDB; consultado em 2026-10-03.
