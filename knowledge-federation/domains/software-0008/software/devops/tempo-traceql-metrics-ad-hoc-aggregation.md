---
id: software.devops.tranche05.000404
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-05.md"
fontes: ["https://raw.githubusercontent.com/grafana/tempo/main/README.md", "https://grafana.com/docs/tempo/latest/getting-started/", "https://github.com/grafana/tempo"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Geração ad-hoc de métricas a partir de traces com TraceQL metrics no Tempo

## Em uma frase
O README oficial documenta o **TraceQL metrics** (`grafana.com/docs/tempo/latest/traceql/metrics-queries/`) como um recurso no Grafana Tempo que cria métricas diretamente a partir dos traces armazenados. Consultas de métricas estendem consultas TraceQL aplicando funções agregadoras sobre os resultados dos traces, permitindo agregação ad-hoc de qualquer consulta TraceQL existente por qualquer dimensão disponível nos spans — exatamente da mesma forma que consultas de métricas em LogQL geram métricas a partir de logs no Loki.

## Por que importa
Métricas pré-agregadas no Prometheus frequentemente não possuem etiquetas de alta cardinalidade (como `customer_id`, `tenant_id` ou versão específica de SDK) por limites de memória de séries temporais. O TraceQL metrics permite calcular taxas, quantis e contagens agrupadas por qualquer atributo presente nos spans sob demanda, sem ter precisado pré-configurar uma métrica específica antes do incidente.

## Como funciona
Use consultas TraceQL metrics para calcular taxas de erro, latências percentis ou volume de chamadas agrupados por atributos arbitrários dos spans durante análises pós-incidente ou explorações de capacidade.

## Exemplo
Quando um cliente corporativo reporta lentidão isolada em sua conta, o engenheiro usa TraceQL metrics para agregar a duração média e p95 dos spans filtrados pelo atributo `span.tenant.id` daquele cliente nas últimas duas horas.

## Limites e trade-offs
Como o TraceQL metrics é classificado no README oficial como um recurso experimental que varre blocos de traces sob demanda, avalie o consumo de recursos dos queriers antes de usá-lo em dezenas de painéis de atualização contínua a cada poucos segundos.

## Como verificar
Execute uma consulta TraceQL metrics agregando spans por `resource.service.name` no Grafana e verifique a série temporal resultante gerada diretamente a partir dos traces.

## Conexões
- [[tempo-traceql-query-language-for-spans-and-traces]] — Veja também: Linguagem de consulta TraceQL inspirada em LogQL e PromQL no Grafana Tempo.
- [[tempo-apache-parquet-default-storage-format]] — Veja também: Apache Parquet como formato colunar padrão de armazenamento a partir do Grafana Tempo 2.0.

## Fontes
- [Grafana Tempo GitHub — README.md (Object Storage Tracing, Traces Drilldown, TraceQL & Apache Parquet)](https://raw.githubusercontent.com/grafana/tempo/main/README.md) — README oficial do Grafana Tempo detalhando operação exclusiva sobre armazenamento de objetos (S3, GCS, Azure ou disco local), integração com Grafana/Prometheus/Loki, app Traces Drilldown, linguagem TraceQL e TraceQL metrics, formato padrão Apache Parquet (Tempo 2.0), compatibilidade OpenTelemetry/Jaeger/Zipkin/Kafka e utilitários tempo-vulture e tempo-cli.; consultado em 2026-10-03.
- [Grafana Tempo Documentation — Getting Started](https://grafana.com/docs/tempo/latest/getting-started/) — Guia oficial de início rápido e operação do Grafana Tempo.; consultado em 2026-10-03.
- [Grafana Tempo — Official GitHub Repository](https://github.com/grafana/tempo) — Repositório oficial do Grafana Tempo distribuído sob AGPL-3.0-only (com exceções Apache-2.0 em LICENSING.md).; consultado em 2026-10-03.
