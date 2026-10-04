---
id: software.devops.tranche05.000401
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

# Grafana Tempo como backend de tracing distribuído de alta escala baseado apenas em object storage

## Em uma frase
O Grafana Tempo é um backend de rastreamento distribuído (distributed tracing) de código aberto, fácil de operar e projetado para alta escala. Conforme destaca o README oficial, o Tempo é altamente eficiente em custo porque **exige apenas armazenamento de objetos (object storage) para operar** — gravando lotes de traces diretamente em Amazon S3, Google Cloud Storage (GCS), Azure Blob Storage ou disco local — sem depender de clusters caros de indexação full-text como Elasticsearch ou Cassandra, integrando-se profundamente ao Grafana, Prometheus e Loki.

## Por que importa
Em sistemas de microsserviços de alto tráfego, o custo de indexar cada atributo de cada span em bancos de busca tradicionais força equipes a adotar taxas mínimas de amostragem (sampling de 0,1% ou 1%), perdendo justamente os traces de erros raros. Ao armazenar traces em object storage com formato colunar, o Tempo permite reter 100% ou altas frações dos traces por uma fração do custo.

## Como funciona
Configure o Tempo apontando seu backend de armazenamento para um bucket S3, GCS ou Azure dedicado (ou disco local em ambientes de desenvolvimento) e conecte-o como fonte de dados no Grafana ao lado do Prometheus (exemplars) e do Loki (correlação por `traceID`).

## Exemplo
Uma plataforma de pagamentos ingere milhões de spans por minuto no Grafana Tempo usando um bucket S3 como único armazenamento persistente; quando um alerta do Prometheus dispara, o exemplar no gráfico leva diretamente ao `traceID` armazenado no Tempo.

## Limites e trade-offs
Dimensione adequadamente os buffers locais (WAL/memória dos ingesters) antes do flush para o bucket de object storage para absorver picos de escrita e evitar perda de lotes caso uma instância de ingestão reinicie abruptamente.

## Como verificar
Consulte o endpoint de prontidão do Tempo e execute uma busca por `traceID` no Grafana confirmando a leitura direta dos blocos gravados no bucket de armazenamento de objetos.

## Conexões
- [[tempo-traces-drilldown-ui-and-red-metrics]] — Veja também: Exploração sem queries e métricas RED com o aplicativo Grafana Traces Drilldown.

## Fontes
- [Grafana Tempo GitHub — README.md (Object Storage Tracing, Traces Drilldown, TraceQL & Apache Parquet)](https://raw.githubusercontent.com/grafana/tempo/main/README.md) — README oficial do Grafana Tempo detalhando operação exclusiva sobre armazenamento de objetos (S3, GCS, Azure ou disco local), integração com Grafana/Prometheus/Loki, app Traces Drilldown, linguagem TraceQL e TraceQL metrics, formato padrão Apache Parquet (Tempo 2.0), compatibilidade OpenTelemetry/Jaeger/Zipkin/Kafka e utilitários tempo-vulture e tempo-cli.; consultado em 2026-10-03.
- [Grafana Tempo Documentation — Getting Started](https://grafana.com/docs/tempo/latest/getting-started/) — Guia oficial de início rápido e operação do Grafana Tempo.; consultado em 2026-10-03.
- [Grafana Tempo — Official GitHub Repository](https://github.com/grafana/tempo) — Repositório oficial do Grafana Tempo distribuído sob AGPL-3.0-only (com exceções Apache-2.0 em LICENSING.md).; consultado em 2026-10-03.
