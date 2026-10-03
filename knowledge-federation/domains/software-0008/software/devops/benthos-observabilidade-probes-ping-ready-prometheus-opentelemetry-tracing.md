---
id: software.devops.tranche20.001998
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

# Redpanda Connect Observabilidade no Kubernetes: probes `/ping` e `/ready` (`:4195`), métricas Prometheus e traces OpenTelemetry

## Em uma frase
Conforme documentado no README oficial do Redpanda Connect, todo processo expõe um servidor HTTP embutido (porta padrão `4195`) com dois endpoints de probe prontos para o Kubernetes — **`/ping`** (liveness probe) e **`/ready`** (readiness probe) — além de exportar métricas **Prometheus** e traces **OpenTelemetry** ponta-a-ponto.

## Por que importa
Em um Deployment Kubernetes, se a `readinessProbe` verificar apenas se a porta TCP está aberta, o Pod será considerado pronto mesmo quando a conexão com o broker Kafka de entrada ou com o banco de destino caiu.

## Como funciona
No Redpanda Connect: 1) **`/ping`** retorna sempre HTTP `200 OK` enquanto o processo estiver vivo (ideal para `livenessProbe`); 2) **`/ready`** retorna HTTP `200 OK` **somente quando tanto o `input` quanto o `output` estão ativamente conectados**, retornando `503 Service Unavailable` caso qualquer ponta perca conexão; 3) `metrics.prometheus` expõe contadores e histogramas em `/metrics`; e 4) `tracer.open_telemetry_collector` emite spans para cada processador do pipeline.

## Exemplo
```yaml
http:
  address: 0.0.0.0:4195
  enabled: true

metrics:
  prometheus: {}

tracer:
  open_telemetry_collector:
    grpc:
      - address: otel-collector.monitoring.svc:4317
```

## Limites e trade-offs
Nunca aponte a `livenessProbe` do Kubernetes para `/ready` no Redpanda Connect: se um banco de dados externo ficar indisponível por 2 minutos, `/ready` retornará `503` (o que deve apenas marcar o Pod como não-pronto na `readinessProbe`, e não matar o container em loop na `livenessProbe`).

## Como verificar
Consulte `curl -i http://localhost:4195/ping`, `curl -i http://localhost:4195/ready` e `curl -s http://localhost:4195/metrics` no container em execução.

## Conexões
- [[benthos-testes-unitarios-pipelines-rpk-connect-test-assertions]] — Veja também: Redpanda Connect Unit Testing (`rpk connect test`): testes unitários determinísticos de pipelines e mapeamentos YAML em CI/CD.
- [[benthos-streams-mode-multiplexacao-pipelines-rest-api-resources]] — Veja também: Redpanda Connect `Streams Mode` e `Resources`: execução de múltiplos pipelines independentes em um único processo e API HTTP.

## Fontes
- [Redpanda Connect GitHub — README.md (Declarative Stream Processor, At-Least-Once Transaction Model, CDC to Iceberg, /ping & /ready Probes)](https://raw.githubusercontent.com/redpanda-data/connect/main/README.md) — README oficial do redpanda-data/connect detalhando instalação, execução via Docker/CLI, exemplo de Postgres CDC para Iceberg, probes HTTP e SDK de extensibilidade em Go; consultado em 2026-10-03.
- [Redpanda Connect Official Documentation — About Redpanda Connect (Bloblang Mapping, Stateless In-Process Transactions, Batching, Branching & Observability)](https://docs.redpanda.com/redpanda-connect/about) — Documentação oficial de arquitetura do Redpanda Connect / Benthos cobrindo garantias de entrega, Bloblang, conectores e operação cloud-native; consultado em 2026-10-03.
- [Redpanda Connect (Benthos) — Official GitHub Repository](https://github.com/redpanda-data/connect) — Repositório oficial do Redpanda Connect / Benthos; consultado em 2026-10-03.
