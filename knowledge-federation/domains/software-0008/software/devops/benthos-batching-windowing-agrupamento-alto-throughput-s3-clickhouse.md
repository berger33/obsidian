---
id: software.devops.tranche20.001995
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-20.md"
fontes: ["https://raw.githubusercontent.com/redpanda-data/connect/main/README.md", "https://docs.redpanda.com/redpanda-connect/about", "https://github.com/redpanda-data/connect"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Redpanda Connect Batching e Micro-Batching: configuração de `batching` (`count`, `byte_size`, `period`) e `archive` para S3 e ClickHouse

## Em uma frase
Para atingir alto throughput ao escrever em destinos que penalizam escritas unitárias pequenas (como **Amazon S3**, **Google Cloud Storage**, **Apache Iceberg**, **ClickHouse**, **Elasticsearch** ou **BigQuery**), o Redpanda Connect oferece políticas declarativas de **`batching`** (`count`, `byte_size`, `period`, `check`) combinadas com processadores de lote (`archive`, `compress`, `parquet_encode`).

## Por que importa
Fazer um `PutObject` no S3 ou um `INSERT` no ClickHouse para cada evento individual de 500 bytes geraria milhares de requisições por segundo, estourando limites de taxa e criando milhões de arquivos minúsculos (*small files problem*).

## Como funciona
Configurado no `input` ou diretamente dentro do `output`, o bloco `batching` acumula mensagens em memória até que **qualquer uma** das condições seja atingida (ex.: `count: 1000` mensagens, `byte_size: 10485760` [10 MiB] ou `period: 10s`). Dentro de `batching.processors`, você pode compactar o lote inteiro em um único arquivo `.ndjson.gz` ou Parquet antes de o `output` realizar uma única escrita transacional.

## Exemplo
```yaml
output:
  aws_s3:
    bucket: "corp-telemetry-archive"
    path: 'events/${! timestamp_unix() }-${! uuid_v4() }.ndjson.gz'
    batching:
      count: 5000
      byte_size: 10485760
      period: 30s
      processors:
        - archive:
            format: lines
        - compress:
            algorithm: gzip
```

## Limites e trade-offs
Graças ao modelo de transação em processo, os offsets de todas as 5.000 mensagens do lote no Kafka/SQS só são confirmados (*committed*) depois que o arquivo `.ndjson.gz` inteiro foi gravado com sucesso no bucket S3.

## Como verificar
Verifique nas métricas Prometheus (`output_batch_sent`) que os eventos estão sendo enviados em lotes agrupados.

## Conexões
- [[benthos-tratamento-erros-dead-letter-queue-switch-fallback-retry]] — Veja também: Redpanda Connect Tratamento de Erros e Dead-Letter Queues (`DLQ`): uso de `try`, `catch`, `fallback` e `switch` sem perder mensagens.
- [[benthos-enriquecimento-sincrono-branch-http-cache-rate-limit-resources]] — Veja também: Redpanda Connect `branch`, `cache` e `rate_limit`: enriquecimento de eventos com APIs externas e caches compartilhados (`redis`/`s3`).

## Fontes
- [Redpanda Connect GitHub — README.md (Declarative Stream Processor, At-Least-Once Transaction Model, CDC to Iceberg, /ping & /ready Probes)](https://raw.githubusercontent.com/redpanda-data/connect/main/README.md) — README oficial do redpanda-data/connect detalhando instalação, execução via Docker/CLI, exemplo de Postgres CDC para Iceberg, probes HTTP e SDK de extensibilidade em Go; consultado em 2026-10-03.
- [Redpanda Connect Official Documentation — About Redpanda Connect (Bloblang Mapping, Stateless In-Process Transactions, Batching, Branching & Observability)](https://docs.redpanda.com/redpanda-connect/about) — Documentação oficial de arquitetura do Redpanda Connect / Benthos cobrindo garantias de entrega, Bloblang, conectores e operação cloud-native; consultado em 2026-10-03.
- [Redpanda Connect (Benthos) — Official GitHub Repository](https://github.com/redpanda-data/connect) — Repositório oficial do Redpanda Connect / Benthos; consultado em 2026-10-03.
