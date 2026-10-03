---
id: software.seguranca.tranche10.000916
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-10.md"
fontes: ["https://raw.githubusercontent.com/cloudquery/cloudquery/main/README.md", "https://www.cloudquery.io/docs/cli/getting-started"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# CloudQuery: **Sincronização Incremental (`backend_options`)** com Cursor de Estado para Tabelas de Grande Volume

## Em uma frase
Algumas tabelas de nuvem crescem continuamente ou possuem dezenas de milhares de registros que raramente mudam (como imagens ECR, snapshots EBS antigos, eventos ou repositórios): buscar tudo do zero em cada execução de hora em hora desperdiça tempo e cota de API.

## Por que importa
O CloudQuery resolve isso com o suporte a **Tabelas Incrementais (*Incremental Sync*)** através da configuração **`backend_options`** no manifesto `kind: source`!

## Como funciona
Quando você aponta `backend_options` para um plugin de destino (como o próprio banco PostgreSQL, em uma tabela dedicada de estado como `cq_state_aws`), os resolvedores incrementais do CloudQuery gravam o **cursor/timestamp da última sincronização por conta e região** e, na execução seguinte, buscam nas APIs da nuvem apenas os registros criados ou modificados após aquele cursor!

## Exemplo
```yaml
# aws-incremental.yml — Habilitando persistencia de estado incremental (backend_options) no proprio Postgres
kind: source
spec:
  name: aws
  path: cloudquery/aws
  registry: cloudquery
  version: "v27.0.0"
  tables: ["aws_ecr_repository_images", "aws_cloudtrail_events"]
  destinations: ["postgresql"]
  backend_options:
    table_name: "cq_cursor_state_aws"
    connection: "@@plugins.postgresql.connection"
```

## Limites e trade-offs
Atenção importante ao combinar tabelas incrementais com `write_mode`: se você usar `write_mode: overwrite-delete-stale` em conjunto com uma tabela incremental que só busca registros novos na última hora, o CloudQuery sabe proteger os registros antigos das tabelas marcadas como incrementais, ou você pode usar `write_mode: overwrite` / `append` para tabelas de eventos históricos!

## Como verificar
Inspecione a tabela `cq_cursor_state_aws` no PostgreSQL para verificar os cursores salvos por tabela e conta.

## Conexões
- [[cloudquery-politicas-seguranca-sql-cspm-aws-gcp-azure-k8s]] — Veja também: CloudQuery **CSPM Policies em SQL**: Execução de Views de Conformidade (**CIS, NIST, PCI DSS**) e Detecção de Exposição Pública sobre o Banco Sincronizado.
- [[cloudquery-exportacao-datalake-duckdb-parquet-s3-clickhouse-analise]] — Veja também: CloudQuery com **DuckDB e Parquet (`cloudquery/duckdb`, `cloudquery/file`)**: Auditoria Multi-Cloud Portátil e Serverless em Segundos.
- [[cloudquery-arquitetura-elt-apache-arrow-inventario-ativos-cspm]] — Referência cruzada direta com cloudquery-arquitetura-elt-apache-arrow-inventario-ativos-cspm.
- [[cloudquery-modos-sincronizacao-write-mode-overwrite-delete-stale-append]] — Referência cruzada direta com cloudquery-modos-sincronizacao-write-mode-overwrite-delete-stale-append.
- [[cloudquery-configuracao-fontes-aws-gcp-azure-k8s-selecao-tabelas]] — Referência cruzada direta com cloudquery-configuracao-fontes-aws-gcp-azure-k8s-selecao-tabelas.

## Fontes
- [CloudQuery Official GitHub — High-Performance Open-Source Cloud Asset Inventory Powered by Apache Arrow](https://raw.githubusercontent.com/cloudquery/cloudquery/main/README.md) — repositório oficial do CloudQuery cobrindo arquitetura ELT em Go e Apache Arrow, casos de uso de inventário multi-cloud e CSPM; consultado em 2026-10-03.
- [CloudQuery Official CLI Documentation — Getting Started, Sync Modes & Integration Architecture](https://www.cloudquery.io/docs/cli/getting-started) — documentação oficial da CLI do CloudQuery cobrindo configuração de fontes/destinos, modos de sincronização e arquitetura de plugins; consultado em 2026-10-03.
