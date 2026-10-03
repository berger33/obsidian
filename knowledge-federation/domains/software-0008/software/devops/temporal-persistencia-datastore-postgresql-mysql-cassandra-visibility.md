---
id: software.devops.tranche19.001835
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

# Temporal Persistence e Visibility: bancos de dados suportados (`PostgreSQL`, `MySQL`, `Cassandra`) e Advanced Visibility (`Elasticsearch` / SQL)

## Em uma frase
A camada de persistência do Temporal Server divide-se em dois stores lógicos: o **Default Store** (que guarda as tabelas críticas de shards, execuções mutáveis, históricos de eventos e filas de tarefas) e o **Visibility Store** (que indexa metadados e *Search Attributes* customizados para listagem e filtragem de Workflows na Web UI e CLI).

## Por que importa
O padrão de acesso do motor de execução (`History` / `Matching`) exige transações rápidas por chave primária (`ShardID`, `NamespaceID`, `WorkflowID`, `RunID`), enquanto operadores humanos e dashboards precisam fazer buscas complexas (`WorkflowType = 'Order' AND CustomCustomerTier = 'VIP' AND ExecutionStatus = 'Running'`).

## Como funciona
O Temporal suporta **PostgreSQL**, **MySQL** e **Apache Cassandra** para o Default Store (e SQLite para `start-dev`). Nas versões modernas, o **Advanced Visibility** (com *Custom Search Attributes*) funciona tanto sobre **Elasticsearch/OpenSearch** quanto diretamente sobre **PostgreSQL** (12+) e **MySQL** (8.0+) sem exigir cluster Elasticsearch separado.

## Exemplo
```bash
# Criando um Search Attribute customizado no namespace via Temporal CLI:
temporal operator search-attribute create \
  --namespace default \
  --name CustomerId --type Keyword
temporal workflow list --query 'CustomerId = "cust-99" AND ExecutionStatus = "Running"'
```

## Limites e trade-offs
Na implantação e atualização do Temporal Server em produção sobre PostgreSQL ou MySQL, utilize as ferramentas de migração de schema (`temporal-sql-tool` ou `temporal-cassandra-tool`) para atualizar tanto o banco `temporal` quanto o banco `temporal_visibility` antes de subir os novos binários.

## Como verificar
Liste os atributos de busca disponíveis com `temporal operator search-attribute list --namespace default`.

## Conexões
- [[temporal-task-queues-workflow-tasks-activity-tasks-query-tasks]] — Veja também: Temporal `Task Queues` e Tipos de Tarefas: ciclo de polling de `Workflow Tasks`, `Activity Tasks` e `Query Tasks`.
- [[temporal-signals-queries-updates-interacao-workflows-em-execucao]] — Veja também: Temporal `Signals`, `Queries` e `Updates`: interação assíncrona e síncrona com Workflows em execução.

## Fontes
- [Temporal GitHub — README.md (Durable Execution Platform, Local Dev Server, Temporal CLI & Web UI)](https://raw.githubusercontent.com/temporalio/temporal/main/docs/architecture/README.md) — README oficial do temporalio/temporal apresentando o servidor de execução durável, CLI temporal e inicialização start-dev; consultado em 2026-10-03.
- [Temporal Server Architecture Documentation — High-Level Architecture (Frontend, History, Matching, Internal Workers, Event Sourcing & Tasks)](https://raw.githubusercontent.com/temporalio/temporal/main/README.md) — Documentação oficial de arquitetura interna do Temporal detalhando processos do usuário vs cluster Temporal, shards do History Service, Task Queues e tipos de Tasks; consultado em 2026-10-03.
- [Temporal — Official GitHub Repository](https://github.com/temporalio/temporal) — Repositório oficial MIT do Temporal Server; consultado em 2026-10-03.
