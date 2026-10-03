---
id: software.devops.tranche14.001305
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

# Pixie: Profiling de Consultas de Banco de Dados (SQL, PostgreSQL, MySQL, Redis) e Métricas LET

## Em uma frase
O Pixie rastreia automaticamente protocolos de bancos de dados (como PostgreSQL, MySQL, Cassandra, MongoDB e Redis) diretamente na rede via eBPF, calculando **Latency, Error e Throughput (LET)** tanto por Pod quanto por consulta normalizada.

## Por que importa
Ativar logs de todas as queries lentas diretamente no servidor de banco de dados de produção pode causar contenção de disco no banco ou exigir permissões administrativas no RDS/Cloud SQL às quais a equipe da aplicação não tem acesso.

## Como funciona
O Pixie decodifica o protocolo wire das conexões que saem dos Pods da aplicação no cluster Kubernetes, normaliza parâmetros literais das queries SQL (agrupando `SELECT * FROM users WHERE id = 1` e `id = 2` no mesmo padrão) e exibe latência p50/p90/p99 e exemplos full-body das consultas mais lentas.

## Exemplo
```bash
px run px/sql_queries
px run px/mysql_data
px run px/postgres_data
```

## Limites e trade-offs
Se a conexão entre o Pod da aplicação e o banco externo utilizar uma biblioteca TLS não suportada pelas `uprobes` do PEM (ou criptografia de camada de aplicação customizada), o Pixie verá o fluxo TCP mas não decodificará o texto da query SQL.

## Como verificar
Valide a captura das queries com `px run px/sql_queries` e verifique o suporte à versão da biblioteca TLS (OpenSSL / Go crypto/tls) dos containers.

## Conexões
- [[pixie-monitoramento-rede-dns-tcp-drops-retransmits-service-map]] — Veja também: Pixie: Monitoramento de Rede, Fluxos DNS, TCP Drops e Retransmits no Cluster.
- [[pixie-continuous-profiling-flamegraphs-cpu-pod-node]] — Veja também: Pixie: Continuous Application Profiling e Flame Graphs de CPU por Pod e Nó.

## Fontes
- [Pixie Official Documentation — Pixie Overview & Architecture (PEM, Vizier, Pixie Cloud, CLI & eBPF Auto-Telemetry)](https://raw.githubusercontent.com/pixie-io/pixie/main/README.md) — Visão geral e arquitetura oficial do Pixie detalhando o Pixie Edge Module (PEM), Vizier, Pixie Cloud, coleta eBPF sem instrumentação manual e linguagem PxL; consultado em 2026-10-03.
- [Pixie GitHub — README.md (Network Monitoring, Service Performance, Database Query Profiling, Continuous Profiling, bpftrace & Dynamic Go Logging)](https://docs.px.dev/about-pixie/what-is-pixie/) — README oficial do pixie-io/pixie (CNCF Sandbox) documentando casos de uso de monitoramento de rede/DNS/TCP drops, profiling de queries SQL, Flame Graphs, bpftrace distribuído e Dynamic Go Logging; consultado em 2026-10-03.
- [Pixie — Official GitHub Repository](https://github.com/pixie-io/pixie) — Repositório oficial do Pixie na CNCF; consultado em 2026-10-03.
