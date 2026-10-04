---
id: software.devops.tranche14.001304
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

# Pixie: Monitoramento de Rede, Fluxos DNS, TCP Drops e Retransmits no Cluster

## Em uma frase
O Pixie monitora a camada de rede do cluster Kubernetes sem alterar o CNI, gerando mapas de fluxo de tráfego entre serviços, grafos de requisições e respostas DNS completas e mapas de **TCP drops** e **TCP retransmits** por Pod e nó.

## Por que importa
Falhas intermitentes de resolução DNS (`NXDOMAIN` ou timeouts no CoreDNS) e retransmissões TCP silenciosas causadas por perda de pacotes entre nós degradam o p99 das aplicações sem aparecerem nos logs de aplicação.

## Como funciona
Usando probes eBPF na pilha de rede do kernel, o Pixie rastreia cada pacote descartado ou retransmitido e cada pacote DNS, permitindo executar scripts nativos como `px/net_flow_graph`, `px/dns_flow_graph` e `px/tcp_drops` para identificar imediatamente quais pares de Pods ou nós apresentam degradação.

## Exemplo
```bash
px run px/net_flow_graph
px run px/tcp_drops
```

## Limites e trade-offs
Inspecionar apenas métricas de largura de banda por interface de nó esconde retransmissões TCP localizadas entre dois Pods específicos que se comunicam com baixa vazão mas alta perda.

## Como verificar
Execute `px run px/tcp_drops` e `px run px/dns_data` sempre que investigar aumentos súbitos de latência entre microsserviços.

## Conexões
- [[pixie-pxl-query-language-pythonic-dataframes-scripts]] — Veja também: Pixie: Linguagem de Consulta PxL (Pixie Language) Baseada em DataFrames Pythonicos.
- [[pixie-database-query-profiling-sql-postgres-mysql-redis-let]] — Veja também: Pixie: Profiling de Consultas de Banco de Dados (SQL, PostgreSQL, MySQL, Redis) e Métricas LET.

## Fontes
- [Pixie Official Documentation — Pixie Overview & Architecture (PEM, Vizier, Pixie Cloud, CLI & eBPF Auto-Telemetry)](https://raw.githubusercontent.com/pixie-io/pixie/main/README.md) — Visão geral e arquitetura oficial do Pixie detalhando o Pixie Edge Module (PEM), Vizier, Pixie Cloud, coleta eBPF sem instrumentação manual e linguagem PxL; consultado em 2026-10-03.
- [Pixie GitHub — README.md (Network Monitoring, Service Performance, Database Query Profiling, Continuous Profiling, bpftrace & Dynamic Go Logging)](https://docs.px.dev/about-pixie/what-is-pixie/) — README oficial do pixie-io/pixie (CNCF Sandbox) documentando casos de uso de monitoramento de rede/DNS/TCP drops, profiling de queries SQL, Flame Graphs, bpftrace distribuído e Dynamic Go Logging; consultado em 2026-10-03.
- [Pixie — Official GitHub Repository](https://github.com/pixie-io/pixie) — Repositório oficial do Pixie na CNCF; consultado em 2026-10-03.
