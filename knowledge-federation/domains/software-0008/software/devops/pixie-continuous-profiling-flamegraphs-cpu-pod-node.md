---
id: software.devops.tranche14.001306
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

# Pixie: Continuous Application Profiling e Flame Graphs de CPU por Pod e Nó

## Em uma frase
Os agentes PEM do Pixie incluem um **profiler contínuo de CPU** baseado em amostragem eBPF que gera **Flame Graphs (gráficos de chama)** detalhados por nó, namespace, Pod e container para linguagens compiladas e interpretadas.

## Por que importa
Tentar anexar um profiler manual (`pprof`, `perf` ou `gdb`) apenas depois que um pico curto de CPU já ocorreu perde a janela do incidente.

## Como funciona
O profiler do Pixie amostra periodicamente as pilhas de execução (stack traces de kernel e espaço de usuário) com sobrecarga mínima em todos os nós do cluster, resolvendo símbolos das funções para exibir visualmente no Flame Graph quais funções exatas estão consumindo tempo de CPU.

## Exemplo
```bash
px run px/node
px run px/pod -- -p default/api-server-7d8f9c-x2k9p
```

## Limites e trade-offs
Imagens de container compiladas em C/C++/Rust/Go que tiveram todas as tabelas de símbolos totalmente removidas (`strip --strip-all`) exibirão endereços hexadecimais no Flame Graph em vez dos nomes legíveis das funções.

## Como verificar
Mantenha a tabela básica de símbolos (ou informações de frame pointer) nos binários de produção para obter Flame Graphs legíveis no Pixie.

## Conexões
- [[pixie-database-query-profiling-sql-postgres-mysql-redis-let]] — Veja também: Pixie: Profiling de Consultas de Banco de Dados (SQL, PostgreSQL, MySQL, Redis) e Métricas LET.
- [[pixie-distributed-bpftrace-deployment-tabelas-customizadas]] — Veja também: Pixie: Implantação Distribuída de Programas bpftrace no Cluster com Tabelas PxL.

## Fontes
- [Pixie Official Documentation — Pixie Overview & Architecture (PEM, Vizier, Pixie Cloud, CLI & eBPF Auto-Telemetry)](https://raw.githubusercontent.com/pixie-io/pixie/main/README.md) — Visão geral e arquitetura oficial do Pixie detalhando o Pixie Edge Module (PEM), Vizier, Pixie Cloud, coleta eBPF sem instrumentação manual e linguagem PxL; consultado em 2026-10-03.
- [Pixie GitHub — README.md (Network Monitoring, Service Performance, Database Query Profiling, Continuous Profiling, bpftrace & Dynamic Go Logging)](https://docs.px.dev/about-pixie/what-is-pixie/) — README oficial do pixie-io/pixie (CNCF Sandbox) documentando casos de uso de monitoramento de rede/DNS/TCP drops, profiling de queries SQL, Flame Graphs, bpftrace distribuído e Dynamic Go Logging; consultado em 2026-10-03.
- [Pixie — Official GitHub Repository](https://github.com/pixie-io/pixie) — Repositório oficial do Pixie na CNCF; consultado em 2026-10-03.
