---
id: software.devops.tranche05.000414
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

# Ingestão multi-protocolo: Prometheus, InfluxDB, Graphite, OpenTSDB, DataDog, NewRelic e OpenTelemetry

## Em uma frase
O README oficial documenta suporte nativo a scraping, ingestão e backfilling de métricas em uma ampla variedade de protocolos abertos e comerciais: **exporters Prometheus**, **Prometheus remote write API** e **Prometheus exposition format**; **InfluxDB line protocol** sobre HTTP, TCP e UDP; **Graphite plaintext protocol** com suporte a tags; **OpenTSDB** via telnet `put` e HTTP `/api/put`; formato **JSON line**; dados **CSV arbitrários**; formato binário nativo; agente **DataDog** ou **DogStatsD**; agente de infraestrutura **NewRelic**; e formato de métricas **OpenTelemetry (OTLP)**, além de agregação de stream capaz de substituir o StatsD.

## Por que importa
Em grandes organizações, diferentes equipes e sistemas legados emitem telemetria em protocolos distintos (sensores IoT em InfluxDB line protocol, servidores antigos em Graphite/StatsD, agentes corporativos em DogStatsD e microsserviços modernos em OpenTelemetry e Prometheus). Receber todos em um único TSDB elimina silos de monitoramento.

## Como funciona
Centralize a ingestão de métricas heterogêneas habilitando os endpoints correspondentes no VictoriaMetrics (ou `vmagent`) e consulte todas as séries resultantes de forma padronizada via PromQL/MetricsQL no Grafana.

## Exemplo
Uma indústria conecta sensores de telemetria que falam InfluxDB line protocol, serviços legados Graphite e clusters Kubernetes com OpenTelemetry ao mesmo VictoriaMetrics, correlacionando todas as métricas no mesmo dashboard.

## Limites e trade-offs
Padronize convenções de nomenclatura de métricas e rótulos (ou aplique regras de `relabeling` na entrada) ao ingerir protocolos diversos para evitar proliferação desorganizada de nomes de séries.

## Como verificar
Envie uma métrica de teste via formato Prometheus ou InfluxDB line protocol para o VictoriaMetrics e consulte-a imediatamente via API PromQL para confirmar a ingestão.

## Conexões
- [[victoria-promql-and-metricsql-query-languages]] — Veja também: Compatibilidade com PromQL e extensões de performance e usabilidade do MetricsQL.
- [[victoria-instant-snapshots-and-nfs-storage-support]] — Veja também: Backups com snapshots instantâneos (hard links) e suporte a armazenamento NFS (EFS e Filestore).

## Fontes
- [VictoriaMetrics GitHub — README.md (Single-Node & Cluster, MetricsQL, Protocols, Snapshots & Benchmarks)](https://raw.githubusercontent.com/VictoriaMetrics/VictoriaMetrics/master/README.md) — README oficial do VictoriaMetrics detalhando versões Single-node e Cluster sob licença Apache-2.0, armazenamento de longo prazo para Prometheus, linguagens PromQL e MetricsQL, snapshots instantâneos, 11 protocolos de ingestão, suporte a NFS (EFS/Filestore), recursos Enterprise/LTS e benchmarks de RAM e compressão.; consultado em 2026-10-03.
- [VictoriaMetrics Documentation — Key Concepts & Quick Start](https://docs.victoriametrics.com/victoriametrics/keyconcepts/) — Documentação oficial de conceitos fundamentais e início rápido do VictoriaMetrics.; consultado em 2026-10-03.
- [VictoriaMetrics — Official GitHub Repository](https://github.com/VictoriaMetrics/VictoriaMetrics) — Repositório principal Apache-2.0 do VictoriaMetrics com binários para single-node, cluster e vmutils.; consultado em 2026-10-03.
