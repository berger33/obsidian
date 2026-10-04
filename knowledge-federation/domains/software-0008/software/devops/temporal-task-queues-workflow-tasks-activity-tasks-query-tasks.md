---
id: software.devops.tranche19.001834
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-19.md"
fontes: ["https://raw.githubusercontent.com/temporalio/temporal/main/docs/architecture/README.md", "https://raw.githubusercontent.com/temporalio/temporal/main/README.md", "https://github.com/temporalio/temporal"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Temporal `Task Queues` e Tipos de Tarefas: ciclo de polling de `Workflow Tasks`, `Activity Tasks` e `Query Tasks`

## Em uma frase
No Temporal, o **Matching Service** mantém **`Task Queues`** nomeadas (criadas dinamicamente sob demanda quando um cliente inicia um Workflow ou um Worker começa a fazer polling), despachando três tipos de tarefas para os Workers: **Workflow Tasks**, **Activity Tasks** e **Query Tasks**.

## Por que importa
Diferentemente de brokers de mensageria tradicionais onde é necessário provisionar tópicos e partições administrativamente, as Task Queues do Temporal são leves, roteiam tarefas apenas para os Workers que registraram os tipos correspondentes e suportam *Worker Versioning* e *Sticky Execution* (cache de estado no Worker).

## Como funciona
O ciclo opera assim: 1) uma **Workflow Task** retoma a execução do código do Workflow no Worker até ele bloquear (em um timer ou chamada de Activity) e devolve ao servidor a lista de comandos seguintes; 2) uma **Activity Task** executa o código de I/O da Activity e devolve o resultado ou erro; e 3) uma **Query Task** inspeciona o estado atual de um Workflow no Worker e devolve apenas o resultado da consulta sem avançar nem gravar eventos no histórico.

## Exemplo
```bash
# Inspecionando os Workers conectados (Pollers) em uma Task Queue específica:
temporal task-queue describe --task-queue order-processing-tq
```

## Limites e trade-offs
Se `temporal task-queue describe` mostrar zero `Pollers` para a Task Queue onde seus Workflows foram iniciados, os Workflows ficarão aguardando em estado `Running` até que os Pods dos Workers subam e comecem a fazer polling.

## Como verificar
Execute `temporal task-queue describe --task-queue <nome>` para auditar todos os Workers ativos, seus builds e taxas de despacho.

## Conexões
- [[temporal-workflows-determinismo-replay-history-vs-activities-idempotentes]] — Veja também: Temporal: segregação entre `Workflows` determinísticos (Replay de Histórico) e `Activities` idempotentes.
- [[temporal-persistencia-datastore-postgresql-mysql-cassandra-visibility]] — Veja também: Temporal Persistence e Visibility: bancos de dados suportados (`PostgreSQL`, `MySQL`, `Cassandra`) e Advanced Visibility (`Elasticsearch` / SQL).

## Fontes
- [Temporal GitHub — README.md (Durable Execution Platform, Local Dev Server, Temporal CLI & Web UI)](https://raw.githubusercontent.com/temporalio/temporal/main/docs/architecture/README.md) — README oficial do temporalio/temporal apresentando o servidor de execução durável, CLI temporal e inicialização start-dev; consultado em 2026-10-03.
- [Temporal Server Architecture Documentation — High-Level Architecture (Frontend, History, Matching, Internal Workers, Event Sourcing & Tasks)](https://raw.githubusercontent.com/temporalio/temporal/main/README.md) — Documentação oficial de arquitetura interna do Temporal detalhando processos do usuário vs cluster Temporal, shards do History Service, Task Queues e tipos de Tasks; consultado em 2026-10-03.
- [Temporal — Official GitHub Repository](https://github.com/temporalio/temporal) — Repositório oficial MIT do Temporal Server; consultado em 2026-10-03.
