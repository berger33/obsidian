---
id: software.seguranca.tranche10.000911
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

# **CloudQuery (`cloudquery/cloudquery`)**: Arquitetura **ELT (*Extract-Load-Transform*)** de Alta Performance baseada em **Apache Arrow** e Plugins gRPC

## Em uma frase
**CloudQuery** (`cloudquery/cloudquery`, escrito em Go) é um framework open-source de **Extração, Carga e Transformação (ELT)** projetado para construir **Inventários Unificados de Ativos em Nuvem (*Cloud Asset Inventory*)** e plataformas de **CSPM (*Cloud Security Posture Management*)** sobre o seu próprio banco de dados ou Data Warehouse.

## Por que importa
Diferente de ferramentas que acoplam a coleta de dados a um banco proprietário fechado, a arquitetura do CloudQuery separa completamente **Plugins de Origem (*Sources*: AWS, GCP, Azure, Kubernetes, GitHub, Cloudflare, Okta, CrowdStrike)** de **Plugins de Destino (*Destinations*: PostgreSQL, DuckDB, BigQuery, Snowflake, ClickHouse, S3/Parquet, Neo4j)** usando o formato colunar em memória **Apache Arrow** sobre streams gRPC!

## Como funciona
Durante um comando **`cloudquery sync`**, o binário CLI orquestra um escalonador concorrente em Go que extrai dezenas de milhares de recursos da nuvem com tratamento automático de *rate-limiting* e paginação, transmite os registros tipados em lotes Apache Arrow e os grava diretamente no seu destino com **100% de privacidade (seus dados nunca saem da sua infraestrutura)**!

## Exemplo
```yaml
# config.yml — Pipeline CloudQuery basico sincronizando recursos AWS para um banco PostgreSQL de Seguranca
kind: source
spec:
  name: aws
  path: cloudquery/aws
  registry: cloudquery
  version: "v27.0.0"
  tables: ["aws_s3_buckets", "aws_iam_users", "aws_ec2_instances", "aws_ec2_security_groups"]
  destinations: ["postgresql"]
---
kind:destination
spec:
  name: postgresql
  path: cloudquery/postgresql
  registry: cloudquery
  version: "v8.0.0"
  spec:
    connection_string: "${CQ_PG_DSN}"
```

## Limites e trade-offs
Por usar o sistema de tipos estritos do **Apache Arrow**, o CloudQuery garante que um esquema extraído da AWS (`JSON`, `Timestamp`, `INET`, `CIDR`, `UUID`) seja mapeado com precisão nativa tanto para tabelas relacionais no **PostgreSQL** quanto para arquivos colunares **Parquet** em um Data Lake S3/GCS!

## Como verificar
Execute `cloudquery sync config.yml` para validar o carregamento dos plugins e a sincronização inicial.

## Conexões
- [[cloudquery-configuracao-fontes-aws-gcp-azure-k8s-selecao-tabelas]] — Veja também: CloudQuery: Configuração Fina de **Fontes (`tables`, `skip_tables`, `concurrency`)** e Escalonamento Inteligente (`dfs`, `round-robin`, `shuffle`).
- [[cloudquery-modos-sincronizacao-write-mode-overwrite-delete-stale-append]] — Referência cruzada direta com cloudquery-modos-sincronizacao-write-mode-overwrite-delete-stale-append.
- [[steampipe-comparacao-zero-etl-vs-cloudquery-elt-decisao-cspm]] — Referência cruzada direta com steampipe-comparacao-zero-etl-vs-cloudquery-elt-decisao-cspm.

## Fontes
- [CloudQuery Official GitHub — High-Performance Open-Source Cloud Asset Inventory Powered by Apache Arrow](https://raw.githubusercontent.com/cloudquery/cloudquery/main/README.md) — repositório oficial do CloudQuery cobrindo arquitetura ELT em Go e Apache Arrow, casos de uso de inventário multi-cloud e CSPM; consultado em 2026-10-03.
- [CloudQuery Official CLI Documentation — Getting Started, Sync Modes & Integration Architecture](https://www.cloudquery.io/docs/cli/getting-started) — documentação oficial da CLI do CloudQuery cobrindo configuração de fontes/destinos, modos de sincronização e arquitetura de plugins; consultado em 2026-10-03.
