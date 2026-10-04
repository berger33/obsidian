---
id: software.devops.tranche20.001993
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

# Redpanda Connect Change Data Capture (`CDC`) e Lakehouse: streaming de `postgres_cdc` para tabelas Apache Iceberg no S3

## Em uma frase
Conforme destacado no README oficial, o Redpanda Connect oferece conectores **Change Data Capture (CDC)** de primeira classe (para **PostgreSQL**, **MySQL**, **MongoDB**, **Oracle**, **MSSQL** e **DynamoDB CDC**) combinados com saídas nativas de Lakehouse como **Apache Iceberg** (`output.iceberg` com evolução automática de schema).

## Por que importa
Manter um cluster Kafka Connect separado com Debezium, Schema Registry e consumidores Spark apenas para replicar tabelas transacionais do PostgreSQL em tabelas analíticas Apache Iceberg no S3 exige gerenciar três sistemas distribuídos distintos.

## Como funciona
Em um único manifesto YAML do Redpanda Connect, o input `postgres_cdc` faz o snapshot inicial (`stream_snapshot: true`) e lê o log de replicação lógica (WAL) das tabelas especificadas, enquanto o output `iceberg` grava diretamente nas tabelas Iceberg no S3 (autenticado no catálogo Glue/REST via SigV4) roteando dinamicamente por `table: ${! meta("table") }` e aplicando `schema_evolution.enabled: true`.

## Exemplo
```yaml
input:
  postgres_cdc:
    dsn: postgres://user:pass@db.example.com:5432/app?sslmode=require
    schema: public
    tables: [ orders, customers ]
    stream_snapshot: true

output:
  iceberg:
    catalog:
      url: https://glue.us-east-1.amazonaws.com/iceberg
      warehouse: "123456789012"
    namespace: cdc
    table: ${! meta("table") }
    storage:
      aws_s3:
        bucket: my-iceberg-warehouse
        region: us-east-1
    schema_evolution:
      enabled: true
      table_location: s3://my-iceberg-warehouse/cdc/
```

## Limites e trade-offs
Certifique-se de que o banco PostgreSQL de origem esteja configurado com `wal_level = logical` e que o slot de replicação seja monitorado para evitar retenção excessiva de WAL caso o pipeline fique parado por longo período.

## Como verificar
Valide a configuração do conector CDC e Iceberg com `rpk connect lint cdc-iceberg.yaml`.

## Conexões
- [[benthos-linguagem-mapeamento-bloblang-transformacao-filtragem-json]] — Veja também: Redpanda Connect `Bloblang`: linguagem declarativa de mapeamento, transformação, enriquecimento e filtragem de streams.
- [[benthos-tratamento-erros-dead-letter-queue-switch-fallback-retry]] — Veja também: Redpanda Connect Tratamento de Erros e Dead-Letter Queues (`DLQ`): uso de `try`, `catch`, `fallback` e `switch` sem perder mensagens.

## Fontes
- [Redpanda Connect GitHub — README.md (Declarative Stream Processor, At-Least-Once Transaction Model, CDC to Iceberg, /ping & /ready Probes)](https://raw.githubusercontent.com/redpanda-data/connect/main/README.md) — README oficial do redpanda-data/connect detalhando instalação, execução via Docker/CLI, exemplo de Postgres CDC para Iceberg, probes HTTP e SDK de extensibilidade em Go; consultado em 2026-10-03.
- [Redpanda Connect Official Documentation — About Redpanda Connect (Bloblang Mapping, Stateless In-Process Transactions, Batching, Branching & Observability)](https://docs.redpanda.com/redpanda-connect/about) — Documentação oficial de arquitetura do Redpanda Connect / Benthos cobrindo garantias de entrega, Bloblang, conectores e operação cloud-native; consultado em 2026-10-03.
- [Redpanda Connect (Benthos) — Official GitHub Repository](https://github.com/redpanda-data/connect) — Repositório oficial do Redpanda Connect / Benthos; consultado em 2026-10-03.
