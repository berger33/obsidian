---
id: software.devops.tranche05.000406
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

# Arquitetura nativa em OpenTelemetry e ingestão multi-protocolo (OTLP, Jaeger, Zipkin e Kafka)

## Em uma frase
O README oficial enfatiza que a camada receptora (`receiver layer`), o formato de tráfego em rede (`wire format`) e o formato de armazenamento do Tempo são todos baseados diretamente nos padrões (`open-telemetry/opentelemetry-proto`) e no código (`open-telemetry/opentelemetry-collector`) estabelecidos pelo **OpenTelemetry** (`opentelemetry.io`). Além do protocolo nativo OTLP (gRPC e HTTP), o Tempo é totalmente compatível com **Jaeger, Zipkin e Kafka**, ingerindo lotes em qualquer um desses formatos, fazendo buffer e gravando-os em Azure, GCS, S3 ou disco local.

## Por que importa
Basear o receptor e o modelo interno diretamente no `opentelemetry-collector` e no `opentelemetry-proto` evita traduções com perda de semântica ao receber dados OTLP modernos, enquanto o suporte simultâneo a Jaeger, Zipkin e Kafka permite migrar aplicações legadas gradualmente sem trocar todos os SDKs de uma só vez.

## Como funciona
Aponte os exportadores OTLP das aplicações ou do OpenTelemetry Collector central para o distribuidor do Tempo, e utilize a ingestão via **Apache Kafka** quando desejar desacoplar picos extremos de tráfego entre os coletores de borda e os ingesters do Tempo.

## Exemplo
Em uma empresa em transição de Jaeger para OpenTelemetry, serviços legados enviam spans em formato Jaeger, filas críticas publicam traces em um tópico Kafka e novos serviços exportam OTLP gRPC; o mesmo cluster Tempo ingere os três fluxos perfeitamente.

## Limites e trade-offs
Ao receber traces diretamente das aplicações sem um OpenTelemetry Collector intermediário, garanta balanceamento de carga adequado para distribuir as conexões gRPC de longa duração uniformemente entre os distribuidores do Tempo.

## Como verificar
Envie um trace de teste via OTLP (ou Jaeger/Zipkin) para o receptor do Tempo e confirme nas métricas de ingestão (`tempo_distributor_spans_received_total`) o recebimento e persistência do lote.

## Conexões
- [[tempo-apache-parquet-default-storage-format]] — Veja também: Apache Parquet como formato colunar padrão de armazenamento a partir do Grafana Tempo 2.0.
- [[tempo-deployment-topologies-compose-helm-and-jsonnet]] — Veja também: Exemplos e modelos de implantação do Tempo com Docker Compose, Helm e Jsonnet (Tanka).

## Fontes
- [Grafana Tempo GitHub — README.md (Object Storage Tracing, Traces Drilldown, TraceQL & Apache Parquet)](https://raw.githubusercontent.com/grafana/tempo/main/README.md) — README oficial do Grafana Tempo detalhando operação exclusiva sobre armazenamento de objetos (S3, GCS, Azure ou disco local), integração com Grafana/Prometheus/Loki, app Traces Drilldown, linguagem TraceQL e TraceQL metrics, formato padrão Apache Parquet (Tempo 2.0), compatibilidade OpenTelemetry/Jaeger/Zipkin/Kafka e utilitários tempo-vulture e tempo-cli.; consultado em 2026-10-03.
- [Grafana Tempo Documentation — Getting Started](https://grafana.com/docs/tempo/latest/getting-started/) — Guia oficial de início rápido e operação do Grafana Tempo.; consultado em 2026-10-03.
- [Grafana Tempo — Official GitHub Repository](https://github.com/grafana/tempo) — Repositório oficial do Grafana Tempo distribuído sob AGPL-3.0-only (com exceções Apache-2.0 em LICENSING.md).; consultado em 2026-10-03.
