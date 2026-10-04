---
id: software.seguranca.tranche10.000913
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

# CloudQuery: Modos de Escrita no Destino (**`overwrite-delete-stale`**, **`overwrite`** e **`append`**) e Migração Automática de Schema (`migrate_mode`)

## Em uma frase
Como o CloudQuery lida no banco de dados de destino quando um recurso da nuvem (como um Pod Kubernetes efêmero ou uma instância EC2 encerrada) **deixa de existir** entre a sincronização de ontem e a sincronização de hoje?

## Por que importa
Isso é controlado pela propriedade **`write_mode`** no manifesto `kind: destination`: **(1) `overwrite-delete-stale` (padrão recomendado para estado atual)** — faz `UPSERT` dos recursos encontrados usando a chave primária (`_cq_id` / ARN) e, ao final do sync bem-sucedido, **remove automaticamente (`DELETE`) os registros daquela fonte cujo `_cq_sync_time` é anterior ao sync atual** (mantendo o banco um espelho exato do que está vivo agora!); **(2) `overwrite`** — faz `UPSERT` sem deletar registros antigos; e **(3) `append`** — nunca sobrescreve nem deleta linhas anteriores, inserindo uma nova versão de cada recurso a cada sync para criar um **Histórico de Auditoria Temporal (*Time-Travel Inventory*)**!

## Como funciona
Além disso, `migrate_mode: safe` (padrão) aplica automaticamente adições de novas colunas quando você atualiza a versão de um plugin, abortando apenas se uma mudança exigir recriação destrutiva de tabela (que exigiria `migrate_mode: forced`).

## Exemplo
```yaml
# pg-destination.yml — Configuracao de destino PostgreSQL com remocao automatica de ativos obsoletos e lotes otimizados
kind: destination
spec:
  name: postgresql
  path: cloudquery/postgresql
  registry: cloudquery
  version: "v8.0.0"
  write_mode: overwrite-delete-stale
  migrate_mode: safe
  spec:
    connection_string: "${CQ_PG_DSN}"
    batch_size: 10000
    batch_size_bytes: 4194304
```

## Limites e trade-offs
Dica arquitetural poderosa: você pode declarar **dois destinos na mesma execução de `cloudquery sync`** (`destinations: ["postgresql_current", "s3_parquet_history"]`) — enviando um único fluxo de extração da nuvem simultaneamente para o **PostgreSQL em modo `overwrite-delete-stale`** (para consultas rápidas do estado atual) e para um bucket **S3 em formato Parquet em modo `append`** (para retenção forense de longo prazo a custo quase zero)!

## Como verificar
Verifique as colunas de metadados `_cq_id`, `_cq_parent_id`, `_cq_source_name` e `_cq_sync_time` criadas automaticamente em todas as tabelas pelo CloudQuery.

## Conexões
- [[cloudquery-configuracao-fontes-aws-gcp-azure-k8s-selecao-tabelas]] — Veja também: CloudQuery: Configuração Fina de **Fontes (`tables`, `skip_tables`, `concurrency`)** e Escalonamento Inteligente (`dfs`, `round-robin`, `shuffle`).
- [[cloudquery-descoberta-multi-conta-aws-organizations-gcp-folders-azure]] — Veja também: CloudQuery em Escala Enterprise: Descoberta Automática de Contas via **AWS Organizations (`org`)**, **GCP Folders** e **Azure Subscriptions**.
- [[cloudquery-arquitetura-elt-apache-arrow-inventario-ativos-cspm]] — Referência cruzada direta com cloudquery-arquitetura-elt-apache-arrow-inventario-ativos-cspm.
- [[cloudquery-deteccao-drift-historico-temporal-snapshots-sql]] — Referência cruzada direta com cloudquery-deteccao-drift-historico-temporal-snapshots-sql.
- [[cloudquery-exportacao-datalake-duckdb-parquet-s3-clickhouse-analise]] — Referência cruzada direta com cloudquery-exportacao-datalake-duckdb-parquet-s3-clickhouse-analise.

## Fontes
- [CloudQuery Official GitHub — High-Performance Open-Source Cloud Asset Inventory Powered by Apache Arrow](https://raw.githubusercontent.com/cloudquery/cloudquery/main/README.md) — repositório oficial do CloudQuery cobrindo arquitetura ELT em Go e Apache Arrow, casos de uso de inventário multi-cloud e CSPM; consultado em 2026-10-03.
- [CloudQuery Official CLI Documentation — Getting Started, Sync Modes & Integration Architecture](https://www.cloudquery.io/docs/cli/getting-started) — documentação oficial da CLI do CloudQuery cobrindo configuração de fontes/destinos, modos de sincronização e arquitetura de plugins; consultado em 2026-10-03.
