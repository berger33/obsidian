---
id: software.devops.tranche20.001991
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

# Redpanda Connect (Benthos): arquitetura de processamento declarativo de streams com entrega *at-least-once* sem estado em disco

## Em uma frase
O **Redpanda Connect** (evolução do projeto **Benthos**, distribuído como um único binário estático em Go ou imagem OCI mínima baseada em `scratch`) é um processador de streams cloud-native declarativo que move, enriquece, filtra e transforma dados entre centenas de fontes (`input`) e destinos (`output`) usando um único arquivo YAML.

## Por que importa
Frameworks pesados de processamento de streams (como clusters JVM distribuídos com estado em disco local RocksDB) exigem infraestrutura complexa de checkpoints e recuperação de estado mesmo para pipelines de integração, CDC, roteamento de eventos e ETL em tempo real.

## Como funciona
O diferencial arquitetural do Redpanda Connect / Benthos é seu **modelo de transação em processo (*in-process transaction model*) sem estado persistido em disco**: uma mensagem lida do `input` só recebe confirmação (*ACK* / commit de offset no Kafka, SQS, NATS ou RabbitMQ) **depois** que atravessou todos os `processors` em memória e foi confirmada com sucesso pelo `output`. Isso garante entrega **at-least-once por padrão**, mesmo diante de crashes abruptos do Pod ou perda de disco, mantendo os Pods 100% stateless e horizontalmente escaláveis.

## Exemplo
```yaml
input:
  kafka_franz:
    seed_brokers: [ "kafka.prod.svc:9092" ]
    topics: [ "orders.raw" ]
    consumer_group: "connect-orders-cg"

pipeline:
  processors:
    - mapping: |
        root = this
        root.processed_at = now()

output:
  aws_s3:
    bucket: "corp-orders-lake"
    path: 'orders/${! timestamp_unix_nano() }.json'
```

## Limites e trade-offs
Como não há estado intermediário gravado em disco local (`buffer: none` por padrão), escalar um Deployment do Redpanda Connect no Kubernetes basta alterar `replicas` ou anexar um HPA/KEDA sem preocupar-se com perda de mensagens em volumes locais.

## Como verificar
Execute `rpk connect lint config.yaml` (ou `redpanda-connect lint config.yaml`) para validar estaticamente a sintaxe do pipeline.

## Conexões
- [[benthos-linguagem-mapeamento-bloblang-transformacao-filtragem-json]] — Veja também: Redpanda Connect `Bloblang`: linguagem declarativa de mapeamento, transformação, enriquecimento e filtragem de streams.

## Fontes
- [Redpanda Connect GitHub — README.md (Declarative Stream Processor, At-Least-Once Transaction Model, CDC to Iceberg, /ping & /ready Probes)](https://raw.githubusercontent.com/redpanda-data/connect/main/README.md) — README oficial do redpanda-data/connect detalhando instalação, execução via Docker/CLI, exemplo de Postgres CDC para Iceberg, probes HTTP e SDK de extensibilidade em Go; consultado em 2026-10-03.
- [Redpanda Connect Official Documentation — About Redpanda Connect (Bloblang Mapping, Stateless In-Process Transactions, Batching, Branching & Observability)](https://docs.redpanda.com/redpanda-connect/about) — Documentação oficial de arquitetura do Redpanda Connect / Benthos cobrindo garantias de entrega, Bloblang, conectores e operação cloud-native; consultado em 2026-10-03.
- [Redpanda Connect (Benthos) — Official GitHub Repository](https://github.com/redpanda-data/connect) — Repositório oficial do Redpanda Connect / Benthos; consultado em 2026-10-03.
