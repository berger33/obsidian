---
id: software.devops.tranche20.001994
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

# Redpanda Connect Tratamento de Erros e Dead-Letter Queues (`DLQ`): uso de `try`, `catch`, `fallback` e `switch` sem perder mensagens

## Em uma frase
No Redpanda Connect / Benthos, falhas de transformação ou rejeição no destino são tratadas explicitamente no pipeline por meio dos processadores **`try`** e **`catch`**, da função Bloblang **`errored()`** e dos outputs compostos **`fallback`**, **`switch`** e **`retry`**.

## Por que importa
Em um pipeline *at-least-once*, se uma única mensagem malformada (*poison pill*) falhar repetidamente no `processor` ou for rejeitada com HTTP `400` pelo `output`, sem uma rota de *Dead-Letter Queue (DLQ)* o pipeline ficaria travado tentando reprocessá-la ou descartaria o dado silenciosamente.

## Como funciona
Quando um processor dentro de um bloco `try` falha (ex.: falha de validação JSON Schema ou enriquecimento HTTP), a mensagem não é perdida — ela é marcada internamente com a flag de erro (testável via `if errored()` e `error()`). Em seguida, um bloco `catch` pode anexar o motivo do erro (`root.dlq_error = error()`) e um output **`switch`** roteia mensagens com `check: errored()` para um tópico Kafka de DLQ ou bucket S3 de quarentena, enquanto envia as mensagens válidas para o destino principal!

## Exemplo
```yaml
pipeline:
  processors:
    - try:
        - schema_registry_decode:
            url: http://schema-registry:8081
        - mapping: 'root = this.parse_json()'
    - catch:
        - mapping: |
            meta dlq_reason = error()

output:
  switch:
    cases:
      - check: errored()
        output:
          kafka_franz:
            seed_brokers: [ "kafka:9092" ]
            topic: "orders.dlq"
      - output:
          kafka_franz:
            seed_brokers: [ "kafka:9092" ]
            topic: "orders.validated"
```

## Limites e trade-offs
Atenção: um bloco `catch` limpa a flag de erro das mensagens ao terminar; se você quiser que o `output.switch` posterior ainda detecte `errored()`, não limpe o erro no `catch` (ou defina um metadado explícito `meta is_dlq = "true"` e avalie `meta("is_dlq") == "true"` no `switch`).

## Como verificar
Teste o caminho feliz e o caminho de DLQ com testes unitários (`rpk connect test`) antes de implantar o pipeline.

## Conexões
- [[benthos-change-data-capture-cdc-postgres-mysql-mongodb-iceberg]] — Veja também: Redpanda Connect Change Data Capture (`CDC`) e Lakehouse: streaming de `postgres_cdc` para tabelas Apache Iceberg no S3.
- [[benthos-batching-windowing-agrupamento-alto-throughput-s3-clickhouse]] — Veja também: Redpanda Connect Batching e Micro-Batching: configuração de `batching` (`count`, `byte_size`, `period`) e `archive` para S3 e ClickHouse.

## Fontes
- [Redpanda Connect GitHub — README.md (Declarative Stream Processor, At-Least-Once Transaction Model, CDC to Iceberg, /ping & /ready Probes)](https://raw.githubusercontent.com/redpanda-data/connect/main/README.md) — README oficial do redpanda-data/connect detalhando instalação, execução via Docker/CLI, exemplo de Postgres CDC para Iceberg, probes HTTP e SDK de extensibilidade em Go; consultado em 2026-10-03.
- [Redpanda Connect Official Documentation — About Redpanda Connect (Bloblang Mapping, Stateless In-Process Transactions, Batching, Branching & Observability)](https://docs.redpanda.com/redpanda-connect/about) — Documentação oficial de arquitetura do Redpanda Connect / Benthos cobrindo garantias de entrega, Bloblang, conectores e operação cloud-native; consultado em 2026-10-03.
- [Redpanda Connect (Benthos) — Official GitHub Repository](https://github.com/redpanda-data/connect) — Repositório oficial do Redpanda Connect / Benthos; consultado em 2026-10-03.
