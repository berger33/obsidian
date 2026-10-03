---
id: software.devops.tranche14.001309
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
fontes: ["https://raw.githubusercontent.com/pixie-io/pixie/main/README.md", "https://docs.px.dev/about-pixie/what-is-pixie/", "https://github.com/pixie-io/pixie"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Pixie: Monitoramento de Performance de Serviços (Service Maps, Latência por Endpoint e Slowest Requests)

## Em uma frase
O Pixie constrói automaticamente mapas de topologia de serviços (**Service Performance**) e calcula taxas de requisição, taxas de erro e percentis de latência (p50, p90, p99) por serviço e por endpoint, além de amostrar as requisições mais lentas.

## Por que importa
Em arquiteturas de microsserviços onde nem todos os serviços propagam cabeçalhos de trace distribuído (`traceparent` W3C), ferramentas baseadas apenas em OpenTracing/OpenTelemetry deixam pontos cegos no mapa de dependências.

## Como funciona
Como o Pixie observa todas as conexões de rede diretamente no kernel de cada nó via PEM, o script `px/service` e `px/cluster` reconstrói o grafo completo de comunicação L4/L7 entre todos os Pods do cluster e lista exemplos reais das requisições mais lentas de qualquer serviço.

## Exemplo
```bash
px run px/cluster
px run px/service -- -s default/checkout-service
px run px/slow_http_requests
```

## Limites e trade-offs
Filtrar métricas de serviço apenas pelo nome do Pod individual perde a visão agregada quando um Deployment escala horizontalmente com HPA.

## Como verificar
Consulte pelo identificador `namespace/service` em `px run px/service` para agregar a latência e taxa de erro de todas as réplicas do serviço.

## Conexões
- [[pixie-dynamic-go-logging-uprobes-debug-producao-sem-redeploy]] — Veja também: Pixie: Dynamic Go Logging em Produção sem Recompilação ou Redeploy de Binários.
- [[pixie-cli-px-api-client-plugins-opentelemetry-export]] — Veja também: Pixie: Automação com Pixie CLI (px), Client API e Exportação para OpenTelemetry.

## Fontes
- [Pixie Official Documentation — Pixie Overview & Architecture (PEM, Vizier, Pixie Cloud, CLI & eBPF Auto-Telemetry)](https://raw.githubusercontent.com/pixie-io/pixie/main/README.md) — Visão geral e arquitetura oficial do Pixie detalhando o Pixie Edge Module (PEM), Vizier, Pixie Cloud, coleta eBPF sem instrumentação manual e linguagem PxL; consultado em 2026-10-03.
- [Pixie GitHub — README.md (Network Monitoring, Service Performance, Database Query Profiling, Continuous Profiling, bpftrace & Dynamic Go Logging)](https://docs.px.dev/about-pixie/what-is-pixie/) — README oficial do pixie-io/pixie (CNCF Sandbox) documentando casos de uso de monitoramento de rede/DNS/TCP drops, profiling de queries SQL, Flame Graphs, bpftrace distribuído e Dynamic Go Logging; consultado em 2026-10-03.
- [Pixie — Official GitHub Repository](https://github.com/pixie-io/pixie) — Repositório oficial do Pixie na CNCF; consultado em 2026-10-03.
