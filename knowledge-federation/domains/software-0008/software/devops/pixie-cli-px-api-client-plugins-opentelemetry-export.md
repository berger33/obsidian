---
id: software.devops.tranche14.001310
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-14.md"
fontes: ["https://docs.px.dev/about-pixie/what-is-pixie/", "https://raw.githubusercontent.com/pixie-io/pixie/main/README.md", "https://github.com/pixie-io/pixie"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Pixie: Automação com Pixie CLI (px), Client API e Exportação para OpenTelemetry

## Em uma frase
Além da interface web interativa (**Live UI**), o Pixie pode ser operado via **Pixie CLI (`px`)**, **Client API** (Go/Python para Slackbots e automações de SRE) e **Plugins de retenção** que exportam dados processados por scripts PxL no formato **OpenTelemetry (OTLP)**.

## Por que importa
Como os PEMs armazenam a telemetria bruta apenas em memória local por algumas horas, métricas agregadas de longo prazo precisam ser exportadas periodicamente para um backend durável.

## Como funciona
Com o sistema de plugins do Pixie e scripts PxL de exportação (`px.export(df, px.otel.Data(...))`), o Vizier executa consultas agendadas na borda e envia apenas as métricas e spans filtrados/agregados via OTLP para coletores OpenTelemetry, Prometheus, Grafana ou New Relic.

## Exemplo
```bash
px api-key create -s
px run px/namespaces -o json
```

## Limites e trade-offs
Exportar 100% dos eventos HTTP brutos sem agregação prévia no script PxL do plugin OpenTelemetry anula a vantagem de computação na borda do Pixie e encarece a ingestão externa.

## Como verificar
Agregue as métricas (como LET por serviço a cada minuto) ou filtre apenas anomalias dentro do script PxL antes de chamar `px.export` para o coletor OTLP.

## Conexões
- [[pixie-service-performance-mapas-latencia-slowest-requests]] — Veja também: Pixie: Monitoramento de Performance de Serviços (Service Maps, Latência por Endpoint e Slowest Requests).

## Fontes
- [Pixie Official Documentation — Pixie Overview & Architecture (PEM, Vizier, Pixie Cloud, CLI & eBPF Auto-Telemetry)](https://docs.px.dev/about-pixie/what-is-pixie/) — Visão geral e arquitetura oficial do Pixie detalhando o Pixie Edge Module (PEM), Vizier, Pixie Cloud, coleta eBPF sem instrumentação manual e linguagem PxL; consultado em 2026-10-03.
- [Pixie GitHub — README.md (Network Monitoring, Service Performance, Database Query Profiling, Continuous Profiling, bpftrace & Dynamic Go Logging)](https://raw.githubusercontent.com/pixie-io/pixie/main/README.md) — README oficial do pixie-io/pixie (CNCF Sandbox) documentando casos de uso de monitoramento de rede/DNS/TCP drops, profiling de queries SQL, Flame Graphs, bpftrace distribuído e Dynamic Go Logging; consultado em 2026-10-03.
- [Pixie — Official GitHub Repository](https://github.com/pixie-io/pixie) — Repositório oficial do Pixie na CNCF; consultado em 2026-10-03.
