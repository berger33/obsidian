---
id: software.seguranca.tranche10.000917
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

# CloudQuery com **DuckDB e Parquet (`cloudquery/duckdb`, `cloudquery/file`)**: Auditoria Multi-Cloud Portátil e Serverless em Segundos

## Em uma frase
Você não precisa subir um servidor PostgreSQL nem pagar um cluster Snowflake para rodar o CloudQuery em uma auditoria de segurança ou dentro de um runner efêmero de CI/CD: os plugins oficiais de destino **`cloudquery/duckdb`**, **`cloudquery/sqlite`** e **`cloudquery/file` (Parquet / CSV / JSON)** permitem sincronizar toda a postura da nuvem diretamente para um arquivo local ultrarrápido!

## Por que importa
O **DuckDB** é um motor SQL OLAP colunar *in-process* (sem servidor, armazenado em um único arquivo `.db`) que fala a mesma família de tipos colunares do **Apache Arrow** usado internamente pelo CloudQuery.

## Como funciona
Isso significa que você pode rodar `cloudquery sync aws-to-duckdb.yml` em um runner do GitHub Actions, gerar um arquivo `cloud_inventory.duckdb` (ou arquivos `.parquet` comprimidos com Zstandard em um bucket S3) e executar queries analíticas complexas sobre milhões de recursos em milissegundos usando o binário `duckdb`!

## Exemplo
```yaml
# aws-to-duckdb.yml — Sincronizar inventario de seguranca AWS diretamente para um banco colunar portatil DuckDB
kind: destination
spec:
  name: duckdb
  path: cloudquery/duckdb
  registry: cloudquery
  version: "v5.0.0"
  write_mode: overwrite-delete-stale
  spec:
    connection_string: "/cases/cspm/aws_inventory_2026_10.duckdb"
```

## Limites e trade-offs
Outra vantagem forense de usar DuckDB ou arquivos `.parquet`: ao finalizar um pentest cloud ou auditoria trimestral, o arquivo `.duckdb` ou `.parquet` comprimido (frequentemente com apenas alguns megabytes) pode ser arquivado criptografado com **`age`** ou **`gpg`** como **evidência imutável e consultável** do estado exato da infraestrutura naquela data!

## Como verificar
Consulte o arquivo gerado diretamente na CLI: `duckdb /cases/cspm/aws_inventory_2026_10.duckdb "SELECT count(*) FROM aws_s3_buckets;"`.

## Conexões
- [[cloudquery-sincronizacao-incremental-state-backend-cursor-otimizacao]] — Veja também: CloudQuery: **Sincronização Incremental (`backend_options`)** com Cursor de Estado para Tabelas de Grande Volume.
- [[cloudquery-deteccao-drift-historico-temporal-snapshots-sql]] — Veja também: CloudQuery Forense: **Histórico Temporal (`write_mode: append`)** para Investigação de Incidentes ("O Que Mudou na Conta Antes do Ataque?").
- [[cloudquery-arquitetura-elt-apache-arrow-inventario-ativos-cspm]] — Referência cruzada direta com cloudquery-arquitetura-elt-apache-arrow-inventario-ativos-cspm.
- [[steampipe-powerpipe-benchmarks-conformidade-cis-nist-pci-soc2]] — Referência cruzada direta com steampipe-powerpipe-benchmarks-conformidade-cis-nist-pci-soc2.

## Fontes
- [CloudQuery Official GitHub — High-Performance Open-Source Cloud Asset Inventory Powered by Apache Arrow](https://raw.githubusercontent.com/cloudquery/cloudquery/main/README.md) — repositório oficial do CloudQuery cobrindo arquitetura ELT em Go e Apache Arrow, casos de uso de inventário multi-cloud e CSPM; consultado em 2026-10-03.
- [CloudQuery Official CLI Documentation — Getting Started, Sync Modes & Integration Architecture](https://www.cloudquery.io/docs/cli/getting-started) — documentação oficial da CLI do CloudQuery cobrindo configuração de fontes/destinos, modos de sincronização e arquitetura de plugins; consultado em 2026-10-03.
