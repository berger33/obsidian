---
id: software.devops.tranche14.001301
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

# Pixie: Arquitetura de Observabilidade eBPF (PEM, Vizier e Pixie Cloud) na CNCF

## Em uma frase
O **Pixie** (`pixie-io/pixie`, projeto **CNCF Sandbox** originalmente doado pela New Relic) é uma plataforma de observabilidade para aplicações Kubernetes que utiliza **eBPF** para capturar automaticamente telemetria de protocolos, métricas de recursos, fluxos de rede e perfis contínuos de CPU sem instrumentação manual de código.

## Por que importa
Adicionar SDKs de tracing, agentes de linguagem e sidecars em dezenas de microsserviços poliglotas exige recompilar imagens e aumenta a latência e o consumo de memória dos Pods.

## Como funciona
A arquitetura do Pixie divide-se em três camadas principais: o **Pixie Edge Module (PEM)** (agente DaemonSet instalado por nó que coleta dados via eBPF e os armazena localmente em memória no próprio nó), o **Vizier** (coletor instalado por cluster que gerencia os PEMs e executa consultas distribuídas) e o **Pixie Cloud** (hospedado ou self-hosted, responsável por autenticação, gerenciamento de usuários e proxy de consultas para a Live UI, CLI `px` e Client API), mantendo o consumo de CPU tipicamente abaixo de 2% a 5% do cluster.

## Exemplo
```bash
px deploy
px get viziers
px get pems
```

## Limites e trade-offs
Tentar enviar todo o volume bruto de eventos eBPF dos PEMs para um banco de dados centralizado externo satura a banda de saída do cluster, razão pela qual o Pixie processa e armazena os dados em tabelas in-memory na borda (nos próprios nós).

## Como verificar
Verifique a saúde do Vizier e dos PEMs após o deploy com `px get viziers` e `px get pems` no cluster.

## Conexões
- [[pixie-auto-telemetria-full-body-requests-http-grpc-dns]] — Veja também: Pixie: Auto-Telemetria eBPF de Requisições Full-Body (HTTP, gRPC e DNS) sem Sidecars.

## Fontes
- [Pixie Official Documentation — Pixie Overview & Architecture (PEM, Vizier, Pixie Cloud, CLI & eBPF Auto-Telemetry)](https://docs.px.dev/about-pixie/what-is-pixie/) — Visão geral e arquitetura oficial do Pixie detalhando o Pixie Edge Module (PEM), Vizier, Pixie Cloud, coleta eBPF sem instrumentação manual e linguagem PxL; consultado em 2026-10-03.
- [Pixie GitHub — README.md (Network Monitoring, Service Performance, Database Query Profiling, Continuous Profiling, bpftrace & Dynamic Go Logging)](https://raw.githubusercontent.com/pixie-io/pixie/main/README.md) — README oficial do pixie-io/pixie (CNCF Sandbox) documentando casos de uso de monitoramento de rede/DNS/TCP drops, profiling de queries SQL, Flame Graphs, bpftrace distribuído e Dynamic Go Logging; consultado em 2026-10-03.
- [Pixie — Official GitHub Repository](https://github.com/pixie-io/pixie) — Repositório oficial do Pixie na CNCF; consultado em 2026-10-03.
