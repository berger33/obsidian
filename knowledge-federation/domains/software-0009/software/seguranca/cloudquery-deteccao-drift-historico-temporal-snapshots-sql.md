---
id: software.seguranca.tranche10.000918
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

# CloudQuery Forense: **Histórico Temporal (`write_mode: append`)** para Investigação de Incidentes ("O Que Mudou na Conta Antes do Ataque?")

## Em uma frase
Durante uma investigação de incidente em nuvem (DFIR), a pergunta mais difícil que o SOC precisa responder é: **"Esse Security Group ou essa IAM Policy maliciosa estava aberta há 6 meses ou foi alterada ontem às 03:00 da manhã? E como era a configuração exata desse recurso na terça-feira passada?"**

## Por que importa
Se o seu inventário sobrescreve os dados a cada leitura, o passado é destruído; porém, quando você configura o destino do CloudQuery com **`write_mode: append`** (em PostgreSQL particionado, ClickHouse, BigQuery ou S3 Parquet), cada execução agendada grava um novo snapshot datado pela coluna **`_cq_sync_time`**!

## Como funciona
Com isso, usando funções de janela SQL (`LAG()` / `LEAD()` sobre `PARTITION BY arn ORDER BY _cq_sync_time`), você reconstrói a **Linha do Tempo Completa de Mudanças de Configuração (*Configuration Drift Timeline*)** de qualquer ativo da organização!

## Exemplo
```sql
-- Detectar recursos S3 cuja configuracao de bloqueio de acesso publico MUDOU entre duas sincronizacoes consecutivas!
WITH historico AS (
  SELECT
    arn,
    _cq_sync_time,
    block_public_acls,
    LAG(block_public_acls) OVER (PARTITION BY arn ORDER BY _cq_sync_time) AS prev_block_public_acls
  FROM
    aws_s3_buckets_history
)
SELECT
  arn,
  _cq_sync_time AS change_detected_at,
  prev_block_public_acls AS before_value,
  block_public_acls AS after_value
FROM
  historico
WHERE
  prev_block_public_acls IS DISTINCT FROM block_public_acls;
```

## Limites e trade-offs
Em bancos PostgreSQL que usam `write_mode: append`, lembre-se de que a chave primária padrão (`pk_mode`) não pode ser apenas o `arn` (pois haverá múltiplas linhas para o mesmo `arn` em datas diferentes); o CloudQuery ajusta as constraints ou permite incluir `_cq_sync_time` na chave composta para preservar o histórico sem conflito.

## Como verificar
Cruze o timestamp `change_detected_at` encontrado na query acima com os eventos do AWS CloudTrail no Timesketch/OpenSearch para identificar o autor exato da mudança.

## Conexões
- [[cloudquery-exportacao-datalake-duckdb-parquet-s3-clickhouse-analise]] — Veja também: CloudQuery com **DuckDB e Parquet (`cloudquery/duckdb`, `cloudquery/file`)**: Auditoria Multi-Cloud Portátil e Serverless em Segundos.
- [[cloudquery-grafo-ativos-seguranca-neo4j-caminhos-ataque-iam-rede]] — Veja também: CloudQuery + **Neo4j (`cloudquery/neo4j`)**: Construção de **Grafos de Superfície de Ataque Cloud** (Rede -> Computação -> Identidade -> Dados).
- [[cloudquery-arquitetura-elt-apache-arrow-inventario-ativos-cspm]] — Referência cruzada direta com cloudquery-arquitetura-elt-apache-arrow-inventario-ativos-cspm.
- [[cloudquery-modos-sincronizacao-write-mode-overwrite-delete-stale-append]] — Referência cruzada direta com cloudquery-modos-sincronizacao-write-mode-overwrite-delete-stale-append.
- [[timesketch-arquitetura-analise-colaborativa-timelines-forenses-opensearch]] — Referência cruzada direta com timesketch-arquitetura-analise-colaborativa-timelines-forenses-opensearch.

## Fontes
- [CloudQuery Official GitHub — High-Performance Open-Source Cloud Asset Inventory Powered by Apache Arrow](https://raw.githubusercontent.com/cloudquery/cloudquery/main/README.md) — repositório oficial do CloudQuery cobrindo arquitetura ELT em Go e Apache Arrow, casos de uso de inventário multi-cloud e CSPM; consultado em 2026-10-03.
- [CloudQuery Official CLI Documentation — Getting Started, Sync Modes & Integration Architecture](https://www.cloudquery.io/docs/cli/getting-started) — documentação oficial da CLI do CloudQuery cobrindo configuração de fontes/destinos, modos de sincronização e arquitetura de plugins; consultado em 2026-10-03.
