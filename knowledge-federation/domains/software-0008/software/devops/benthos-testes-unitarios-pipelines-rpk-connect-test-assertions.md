---
id: software.devops.tranche20.001997
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

# Redpanda Connect Unit Testing (`rpk connect test`): testes unitários determinísticos de pipelines e mapeamentos YAML em CI/CD

## Em uma frase
O Redpanda Connect possui um framework nativo de **testes unitários declarativos** executado por **`rpk connect test`** (ou `redpanda-connect test`), onde blocos `tests:` (no próprio arquivo YAML do pipeline ou em arquivos `*_benthos_test.yaml` separados) injetam lotes de mensagens de entrada, simulam mocks de processadores externos e validam predicados de saída.

## Por que importa
Pipelines de transformação de dados em YAML frequentemente contêm regras complexas de negócio em Bloblang; implantar alterações sem testes unitários automatizados em CI/CD arrisca quebrar contratos de schema dos consumidores.

## Como funciona
Cada caso em `tests:` define `name`, `target_processors` (ex.: `"/pipeline/processors"`), `environment` (variáveis simuladas), `input_batch` (conteúdo e metadados de entrada) e `output_batches` (contendo asserções como `json_equals`, `content_equals`, `metadata_equals` ou `bloblang` para verificar a saída exata).

## Exemplo
```yaml
tests:
  - name: "Filtra heartbeats e transforma pedidos válidos"
    target_processors: "/pipeline/processors"
    input_batch:
      - content: '{"event_type": "heartbeat"}'
      - content: '{"event_type": "order", "id": "ord-1", "amount": 10.5}'
    output_batches:
      - - json_equals:
            order_id: "ORD-1"
            total_cents: 1050
```

## Limites e trade-offs
Nos testes unitários do Redpanda Connect, o `input` e o `output` reais de rede (como Kafka ou S3) nunca são conectados — apenas os `target_processors` são exercitados em memória em milissegundos, tornando-os ideais para rodar em cada commit no Git.

## Como verificar
Execute `rpk connect test ./pipelines/...` em sua pipeline de CI para garantir que 100% dos testes de transformação passem.

## Conexões
- [[benthos-enriquecimento-sincrono-branch-http-cache-rate-limit-resources]] — Veja também: Redpanda Connect `branch`, `cache` e `rate_limit`: enriquecimento de eventos com APIs externas e caches compartilhados (`redis`/`s3`).
- [[benthos-observabilidade-probes-ping-ready-prometheus-opentelemetry-tracing]] — Veja também: Redpanda Connect Observabilidade no Kubernetes: probes `/ping` e `/ready` (`:4195`), métricas Prometheus e traces OpenTelemetry.

## Fontes
- [Redpanda Connect GitHub — README.md (Declarative Stream Processor, At-Least-Once Transaction Model, CDC to Iceberg, /ping & /ready Probes)](https://raw.githubusercontent.com/redpanda-data/connect/main/README.md) — README oficial do redpanda-data/connect detalhando instalação, execução via Docker/CLI, exemplo de Postgres CDC para Iceberg, probes HTTP e SDK de extensibilidade em Go; consultado em 2026-10-03.
- [Redpanda Connect Official Documentation — About Redpanda Connect (Bloblang Mapping, Stateless In-Process Transactions, Batching, Branching & Observability)](https://docs.redpanda.com/redpanda-connect/about) — Documentação oficial de arquitetura do Redpanda Connect / Benthos cobrindo garantias de entrega, Bloblang, conectores e operação cloud-native; consultado em 2026-10-03.
- [Redpanda Connect (Benthos) — Official GitHub Repository](https://github.com/redpanda-data/connect) — Repositório oficial do Redpanda Connect / Benthos; consultado em 2026-10-03.
