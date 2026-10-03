---
id: software.devops.tranche05.000402
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

# Exploração sem queries e métricas RED com o aplicativo Grafana Traces Drilldown

## Em uma frase
O README oficial destaca o aplicativo **Traces Drilldown** (`github.com/grafana/traces-drilldown`, anteriormente chamado Explore Traces) na suíte Grafana Explore, que oferece uma experiência intuitiva e sem necessidade de escrever queries (**queryless**) para analisar dados de rastreamento no Tempo. Suas funcionalidades centrais incluem: análise ponto-e-clique para identificar traces lentos ou com erro, visão geral de **métricas RED (Rate, Errors e Duration)** para destacar gargalos de performance, comparação automática de traces para isolar atributos problemáticos e visualizações simplificadas sem precisar construir consultas TraceQL manualmente.

## Por que importa
Durante um incidente de produção, engenheiros de plantão nem sempre dominam a sintaxe avançada de uma linguagem de consulta de traces; o Traces Drilldown acelera o diagnóstico apresentando imediatamente as taxas de requisição, erro e duração (RED) e comparando automaticamente os atributos dos spans anômalos contra a linha de base normal.

## Como funciona
Habilite o aplicativo Traces Drilldown no Grafana conectado ao Tempo para que todas as equipes de produto possam investigar regressões de latência e picos de erro visualmente antes de aprofundar em filtros específicos.

## Exemplo
Ao investigar um aumento de latência p99 no serviço de checkout, o SRE abre o Traces Drilldown, observa o pico de Duration na visão RED e usa a comparação automática (`Automated Comparison`) para descobrir que todos os traces lentos compartilham o atributo de uma mesma região de banco de dados.

## Limites e trade-offs
Para que o Traces Drilldown exiba métricas RED precisas e comparações ricas, garanta que as aplicações instrumentadas com OpenTelemetry emitam códigos de status de span consistentes e atributos semânticos padronizados.

## Como verificar
Abra a interface do Traces Drilldown no Grafana, selecione um serviço instrumentado e confirme a renderização dos gráficos de Rate, Errors e Duration e da comparação automática de atributos.

## Conexões
- [[tempo-object-storage-distributed-tracing-backend]] — Veja também: Grafana Tempo como backend de tracing distribuído de alta escala baseado apenas em object storage.
- [[tempo-traceql-query-language-for-spans-and-traces]] — Veja também: Linguagem de consulta TraceQL inspirada em LogQL e PromQL no Grafana Tempo.

## Fontes
- [Grafana Tempo GitHub — README.md (Object Storage Tracing, Traces Drilldown, TraceQL & Apache Parquet)](https://raw.githubusercontent.com/grafana/tempo/main/README.md) — README oficial do Grafana Tempo detalhando operação exclusiva sobre armazenamento de objetos (S3, GCS, Azure ou disco local), integração com Grafana/Prometheus/Loki, app Traces Drilldown, linguagem TraceQL e TraceQL metrics, formato padrão Apache Parquet (Tempo 2.0), compatibilidade OpenTelemetry/Jaeger/Zipkin/Kafka e utilitários tempo-vulture e tempo-cli.; consultado em 2026-10-03.
- [Grafana Tempo Documentation — Getting Started](https://grafana.com/docs/tempo/latest/getting-started/) — Guia oficial de início rápido e operação do Grafana Tempo.; consultado em 2026-10-03.
- [Grafana Tempo — Official GitHub Repository](https://github.com/grafana/tempo) — Repositório oficial do Grafana Tempo distribuído sob AGPL-3.0-only (com exceções Apache-2.0 em LICENSING.md).; consultado em 2026-10-03.
