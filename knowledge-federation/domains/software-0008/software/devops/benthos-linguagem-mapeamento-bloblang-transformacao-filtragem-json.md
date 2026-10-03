---
id: software.devops.tranche20.001992
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

# Redpanda Connect `Bloblang`: linguagem declarativa de mapeamento, transformação, enriquecimento e filtragem de streams

## Em uma frase
O **Bloblang** (`processor: mapping` ou `mutation`) é a linguagem de mapeamento nativa do Redpanda Connect / Benthos projetada especificamente para transformar documentos estruturados (JSON, Avro, Protobuf, Parquet) e metadados de mensagens em tempo real com segurança de tipos e alta performance.

## Por que importa
Usar scripts Python externos, expressões regulares frágeis ou templates de texto para reestruturar payloads JSON aninhados, mascarar PII e descartar eventos inválidos em pipelines de alto throughput cria gargalos de CPU e falhas de parsing.

## Como funciona
Em um mapeamento Bloblang: 1) `this` (ou `.`) referencia o documento de entrada imutável; 2) `root` é o novo documento de saída sendo construído; 3) `meta("chave")` lê metadados da mensagem (como tópico Kafka, partição ou headers HTTP); e 4) atribuir **`root = deleted()`** descarta a mensagem limpa e imediatamente do stream (confirmando o ACK na origem sem enviá-la ao `output`)!

## Exemplo
```yaml
pipeline:
  processors:
    - mapping: |
        # Descarta eventos de heartbeat ou de teste:
        if this.event_type == "heartbeat" {
          root = deleted()
        } else {
          root.order_id = this.id.uppercase()
          root.total_cents = (this.amount * 100).round()
          root.customer_email_hash = this.customer.email.lowercase().hash("sha256").encode("hex")
          root.source_topic = meta("kafka_topic")
        }
```

## Limites e trade-offs
A diferença entre `mapping` e `mutation` no Bloblang é que `mapping` cria um documento `root` novo do zero (ideal para filtrar campos e garantir schema limpo), enquanto `mutation` modifica o documento existente *in-place*.

## Como verificar
Teste suas expressões Bloblang interativamente ou via CLI executando `rpk connect blobl 'root.upper = this.msg.uppercase()'` com JSON no `stdin`.

## Conexões
- [[benthos-arquitetura-redpanda-connect-stream-processor-at-least-once]] — Veja também: Redpanda Connect (Benthos): arquitetura de processamento declarativo de streams com entrega *at-least-once* sem estado em disco.
- [[benthos-change-data-capture-cdc-postgres-mysql-mongodb-iceberg]] — Veja também: Redpanda Connect Change Data Capture (`CDC`) e Lakehouse: streaming de `postgres_cdc` para tabelas Apache Iceberg no S3.

## Fontes
- [Redpanda Connect GitHub — README.md (Declarative Stream Processor, At-Least-Once Transaction Model, CDC to Iceberg, /ping & /ready Probes)](https://raw.githubusercontent.com/redpanda-data/connect/main/README.md) — README oficial do redpanda-data/connect detalhando instalação, execução via Docker/CLI, exemplo de Postgres CDC para Iceberg, probes HTTP e SDK de extensibilidade em Go; consultado em 2026-10-03.
- [Redpanda Connect Official Documentation — About Redpanda Connect (Bloblang Mapping, Stateless In-Process Transactions, Batching, Branching & Observability)](https://docs.redpanda.com/redpanda-connect/about) — Documentação oficial de arquitetura do Redpanda Connect / Benthos cobrindo garantias de entrega, Bloblang, conectores e operação cloud-native; consultado em 2026-10-03.
- [Redpanda Connect (Benthos) — Official GitHub Repository](https://github.com/redpanda-data/connect) — Repositório oficial do Redpanda Connect / Benthos; consultado em 2026-10-03.
