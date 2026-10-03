---
id: software.devops.tranche05.000413
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
fontes: ["https://raw.githubusercontent.com/VictoriaMetrics/VictoriaMetrics/master/README.md", "https://docs.victoriametrics.com/victoriametrics/keyconcepts/", "https://github.com/VictoriaMetrics/VictoriaMetrics"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Compatibilidade com PromQL e extensões de performance e usabilidade do MetricsQL

## Em uma frase
O VictoriaMetrics suporta tanto a linguagem padrão **PromQL** quanto o **MetricsQL**, uma linguagem de consulta retrocompatível com PromQL projetada para oferecer maior performance e funções simplificadas para análise de séries temporais. Por manter compatibilidade com a API de consulta do Prometheus, dashboards existentes do Grafana e regras de alerta escritas em PromQL continuam funcionando sem alterações ao apontar para o VictoriaMetrics.

## Por que importa
Em consultas analíticas sobre grandes intervalos históricos ou métricas com contadores que sofrem resets, certas expressões PromQL tradicionais exigem combinações verbosas de funções; o MetricsQL otimiza a execução interna e adiciona funções ergonômicas sem quebrar painéis PromQL legados.

## Como funciona
Mantenha regras e dashboards compartilhados em PromQL padrão quando precisar de portabilidade estrita com o Prometheus puro, e aproveite as funções e otimizações do MetricsQL nos painéis analíticos avançados servidos pelo VictoriaMetrics.

## Exemplo
Ao migrar centenas de dashboards do Kubernetes do Prometheus para o VictoriaMetrics no Grafana, a equipe apenas troca a URL do data source e obtém tempos de resposta mais rápidos nas mesmas consultas PromQL, passando a usar funções do MetricsQL nos novos painéis de capacidade.

## Limites e trade-offs
Se você escrever regras de alerta utilizando funções exclusivas do MetricsQL, lembre-se de que essas regras devem ser avaliadas pelo componente `vmalert` conectado ao VictoriaMetrics, pois um servidor Prometheus puro não reconhecerá extensões específicas do MetricsQL.

## Como verificar
Execute consultas PromQL e MetricsQL contra o endpoint `/api/v1/query` e `/api/v1/query_range` do VictoriaMetrics e confirme a precisão das séries retornadas.

## Conexões
- [[victoria-prometheus-long-term-storage-and-global-query-view]] — Veja também: Armazenamento de longo prazo para Prometheus e visão global de consulta no VictoriaMetrics.
- [[victoria-multi-protocol-ingestion-prometheus-influx-graphite-otel]] — Veja também: Ingestão multi-protocolo: Prometheus, InfluxDB, Graphite, OpenTSDB, DataDog, NewRelic e OpenTelemetry.

## Fontes
- [VictoriaMetrics GitHub — README.md (Single-Node & Cluster, MetricsQL, Protocols, Snapshots & Benchmarks)](https://raw.githubusercontent.com/VictoriaMetrics/VictoriaMetrics/master/README.md) — README oficial do VictoriaMetrics detalhando versões Single-node e Cluster sob licença Apache-2.0, armazenamento de longo prazo para Prometheus, linguagens PromQL e MetricsQL, snapshots instantâneos, 11 protocolos de ingestão, suporte a NFS (EFS/Filestore), recursos Enterprise/LTS e benchmarks de RAM e compressão.; consultado em 2026-10-03.
- [VictoriaMetrics Documentation — Key Concepts & Quick Start](https://docs.victoriametrics.com/victoriametrics/keyconcepts/) — Documentação oficial de conceitos fundamentais e início rápido do VictoriaMetrics.; consultado em 2026-10-03.
- [VictoriaMetrics — Official GitHub Repository](https://github.com/VictoriaMetrics/VictoriaMetrics) — Repositório principal Apache-2.0 do VictoriaMetrics com binários para single-node, cluster e vmutils.; consultado em 2026-10-03.
