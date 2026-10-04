---
id: software.devops.tranche14.001303
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

# Pixie: Linguagem de Consulta PxL (Pixie Language) Baseada em DataFrames Pythonicos

## Em uma frase
O **PxL (Pixie Language)** é a linguagem de consulta declarativa e Pythonica (inspirada na sintaxe do Pandas `df = px.DataFrame(...)`) utilizada de forma unificada na Live UI, na CLI `px` e nas APIs clientes do Pixie para filtrar, agregar e juntar tabelas de telemetria no cluster.

## Por que importa
Linguagens de consulta proprietárias e rígidas dificultam cruzar na mesma consulta métricas de rede TCP, latência de banco de dados SQL e metadados de Pods Kubernetes.

## Como funciona
Um script PxL importa o módulo `px`, carrega uma tabela distribuída dos PEMs (como `px.DataFrame(table='http_events', start_time='-5m')`), enriquece os registros com contexto Kubernetes (`df.ctx['service']`, `df.ctx['pod']`), aplica filtros e agregações (`groupby`, `agg`) e exibe o resultado com `px.display(df)`.

## Exemplo
```python
import px

df = px.DataFrame(table='http_events', start_time='-5m')
df.service = df.ctx['service']
df = df[df['resp_status'] >= 500]
cols = ['time_', 'service', 'req_path', 'resp_status', 'latency']
px.display(df[cols])
```

## Limites e trade-offs
Carregar tabelas de altíssimo volume com janelas `start_time` muito longas sem filtrar ou agregar antes de chamar `px.display()` transfere um volume excessivo de linhas dos PEMs para a interface.

## Como verificar
Aplique filtros e agregações (`groupby`) diretamente no DataFrame PxL antes de chamar `px.display()` para executar a redução de dados distribuída nos próprios nós.

## Conexões
- [[pixie-auto-telemetria-full-body-requests-http-grpc-dns]] — Veja também: Pixie: Auto-Telemetria eBPF de Requisições Full-Body (HTTP, gRPC e DNS) sem Sidecars.
- [[pixie-monitoramento-rede-dns-tcp-drops-retransmits-service-map]] — Veja também: Pixie: Monitoramento de Rede, Fluxos DNS, TCP Drops e Retransmits no Cluster.

## Fontes
- [Pixie Official Documentation — Pixie Overview & Architecture (PEM, Vizier, Pixie Cloud, CLI & eBPF Auto-Telemetry)](https://raw.githubusercontent.com/pixie-io/pixie/main/README.md) — Visão geral e arquitetura oficial do Pixie detalhando o Pixie Edge Module (PEM), Vizier, Pixie Cloud, coleta eBPF sem instrumentação manual e linguagem PxL; consultado em 2026-10-03.
- [Pixie GitHub — README.md (Network Monitoring, Service Performance, Database Query Profiling, Continuous Profiling, bpftrace & Dynamic Go Logging)](https://docs.px.dev/about-pixie/what-is-pixie/) — README oficial do pixie-io/pixie (CNCF Sandbox) documentando casos de uso de monitoramento de rede/DNS/TCP drops, profiling de queries SQL, Flame Graphs, bpftrace distribuído e Dynamic Go Logging; consultado em 2026-10-03.
- [Pixie — Official GitHub Repository](https://github.com/pixie-io/pixie) — Repositório oficial do Pixie na CNCF; consultado em 2026-10-03.
