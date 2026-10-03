---
id: software.devops.tranche19.001826
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-19.md"
fontes: ["https://raw.githubusercontent.com/nuclio/nuclio/development/docs/concepts/architecture.md", "https://raw.githubusercontent.com/nuclio/nuclio/development/README.md", "https://github.com/nuclio/nuclio"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Nuclio Triggers de Tempo Real: ingestão paralela de streams (`Kafka`, `Kinesis`, `RabbitMQ`, `MQTT`, `NATS`, `Cron` e `HTTP`)

## Em uma frase
Diferentemente de plataformas que convertem cada mensagem de fila em uma requisição HTTP externa, os **Event-source listeners** do Nuclio conectam-se nativamente por dentro do próprio Function Processor a **Apache Kafka**, **AWS Kinesis**, **RabbitMQ**, **MQTT**, **NATS**, **V3IO**, **Cron** e **HTTP**.

## Por que importa
Manter conexões TCP nativas com partições de um consumer group Kafka diretamente nos workers do Function Processor elimina saltos de rede intermediários, preserva ordenação por partição e gerencia commits de offsets/checkpoints com baixa latência.

## Como funciona
Na seção `spec.triggers` do `function.yaml`, basta declarar o tipo de trigger (ex.: `kind: kafka-cluster`), a lista de `brokers`, os `topics` e o `consumerGroup`. O Nuclio distribui automaticamente as partições entre as réplicas dos Pods da função e os workers internos de cada processor.

## Exemplo
```yaml
spec:
  runtime: golang
  handler: main:HandleEvent
  triggers:
    kafkaStream:
      kind: kafka-cluster
      numWorkers: 4
      attributes:
        brokers:
          - kafka-0.kafka.svc.cluster.local:9092
        topics:
          - telemetry-events
        consumerGroup: nuclio-telemetry-cg
```

## Limites e trade-offs
Em triggers de stream como Kafka, se o handler retornar erro (ou ocorrer falha antes da confirmação), o listener aplica as políticas de retentativa/backoff configuradas antes de avançar o checkpoint da partição.

## Como verificar
Aplique uma função com trigger `kafka-cluster` (ou `cron`) e monitore nos logs estruturados do processor o balanceamento de partições e o processamento dos eventos.

## Conexões
- [[nuclio-nuctl-cli-build-deploy-invoke-function-yaml-kaniko]] — Veja também: Nuclio `nuctl` CLI e Builder Kaniko: construção segura de imagens de função in-cluster e deploy declarativo.
- [[nuclio-data-bindings-conexoes-persistentes-context-zero-copy]] — Veja também: Nuclio Data Bindings: conexões persistentes pré-inicializadas em `context.data_binding` com prefetching e caching.

## Fontes
- [Nuclio GitHub — README.md (High-Performance Serverless for Real-Time Events, Data Processing, GPUs, Kaniko & Kubernetes)](https://raw.githubusercontent.com/nuclio/nuclio/development/docs/concepts/architecture.md) — README oficial do nuclio/nuclio apresentando integração com Jupyter/Kubeflow/MLRun, suporte a GPUs, builder Kaniko e fluxo de deploy; consultado em 2026-10-03.
- [Nuclio Official Documentation — Architecture (Function Processors, Event-Source Listeners, Native/SHMEM/Shell Runtimes, Allocators & Auth-Proxy)](https://raw.githubusercontent.com/nuclio/nuclio/development/README.md) — Documentação oficial de arquitetura do Nuclio detalhando o Function Processor, Blocking vs Non-blocking Allocator, Data Bindings e sidecar auth-proxy; consultado em 2026-10-03.
- [Nuclio — Official GitHub Repository](https://github.com/nuclio/nuclio) — Repositório oficial Apache-2.0 do projeto Nuclio; consultado em 2026-10-03.
