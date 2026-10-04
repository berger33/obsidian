---
id: software.devops.tranche05.000403
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

# Linguagem de consulta TraceQL inspirada em LogQL e PromQL no Grafana Tempo

## Em uma frase
O Tempo implementa o **TraceQL** (`grafana.com/docs/tempo/latest/traceql/`), uma linguagem de consulta projetada especificamente para traces (traces-first query language) e inspirada no **LogQL** (do Loki) e no **PromQL** (do Prometheus). Com o TraceQL, operadores e desenvolvedores podem formular consultas direcionadas sobre propriedades estruturais de traces, atributos de recurso (`resource.*`), atributos de span (`span.*`), duração, status e relações hierárquicas entre spans pai e filho.

## Por que importa
Buscar traces apenas por um `traceID` conhecido ou por filtros planos de tag única não permite responder perguntas estruturais complexas, como encontrar todas as requisições onde um serviço A chamou um serviço B que retornou erro HTTP 500 e levou mais de 2 segundos. O TraceQL expressa essas condições relacionais diretamente sobre os spans.

## Como funciona
Utilize o editor TraceQL no Grafana para construir consultas que combinem seletores de span (`{ resource.service.name = "api" && span.http.status_code >= 500 }`), operadores de duração (`duration > 500ms`) e encadeamento estrutural entre serviços.

## Exemplo
Para localizar chamadas lentas ao banco de dados originadas apenas por um endpoint específico da API, o engenheiro executa uma consulta TraceQL filtrando o span raiz pelo atributo de rota HTTP e os spans filhos pelo sistema de banco de dados com duração acima do limiar.

## Limites e trade-offs
Evite consultas TraceQL sem nenhum filtro de atributo seletivo sobre janelas de tempo muito longas (vários dias) em clusters de altíssimo volume, restringindo sempre a janela temporal e os atributos de `resource.service.name` para aproveitar o pruning dos blocos Parquet.

## Como verificar
Execute uma consulta TraceQL no Grafana filtrando por `resource.service.name` e `duration`, confirmando o retorno rápido dos traces correspondentes.

## Conexões
- [[tempo-traces-drilldown-ui-and-red-metrics]] — Veja também: Exploração sem queries e métricas RED com o aplicativo Grafana Traces Drilldown.
- [[tempo-traceql-metrics-ad-hoc-aggregation]] — Veja também: Geração ad-hoc de métricas a partir de traces com TraceQL metrics no Tempo.

## Fontes
- [Grafana Tempo GitHub — README.md (Object Storage Tracing, Traces Drilldown, TraceQL & Apache Parquet)](https://raw.githubusercontent.com/grafana/tempo/main/README.md) — README oficial do Grafana Tempo detalhando operação exclusiva sobre armazenamento de objetos (S3, GCS, Azure ou disco local), integração com Grafana/Prometheus/Loki, app Traces Drilldown, linguagem TraceQL e TraceQL metrics, formato padrão Apache Parquet (Tempo 2.0), compatibilidade OpenTelemetry/Jaeger/Zipkin/Kafka e utilitários tempo-vulture e tempo-cli.; consultado em 2026-10-03.
- [Grafana Tempo Documentation — Getting Started](https://grafana.com/docs/tempo/latest/getting-started/) — Guia oficial de início rápido e operação do Grafana Tempo.; consultado em 2026-10-03.
- [Grafana Tempo — Official GitHub Repository](https://github.com/grafana/tempo) — Repositório oficial do Grafana Tempo distribuído sob AGPL-3.0-only (com exceções Apache-2.0 em LICENSING.md).; consultado em 2026-10-03.
