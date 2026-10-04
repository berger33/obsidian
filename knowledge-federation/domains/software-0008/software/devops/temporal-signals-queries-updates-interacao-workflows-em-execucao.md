---
id: software.devops.tranche19.001836
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

# Temporal `Signals`, `Queries` e `Updates`: interação assíncrona e síncrona com Workflows em execução

## Em uma frase
Um Workflow Execution em andamento no Temporal pode interagir em tempo real com clientes externos por meio de três primitivas: **`Signal`** (mensagem assíncrona gravada no histórico que muda o estado/fluxo do Workflow), **`Query`** (leitura síncrona somente-leitura do estado atual) e **`Update`** (operação síncrona validada que muta o estado e retorna um valor ao chamador).

## Por que importa
Em um processo de aprovação de crédito ou carrinho de compras que aguarda confirmação humana ou webhook de pagamento, o Workflow precisa receber eventos externos de forma durável sem fazer polling constante em um banco externo.

## Como funciona
Quando um cliente envia um `Signal` (`temporal workflow signal`), o History Service grava imediatamente o evento `WorkflowExecutionSignaled` no histórico e agenda uma Workflow Task para acordar o Workflow. Quando envia um `Update` (`temporal workflow update`), o Worker valida a entrada (podendo rejeitá-la sem poluir o histórico), executa a mutação durável e retorna o resultado na mesma chamada RPC.

## Exemplo
```bash
temporal workflow signal \
  --workflow-id order-1042 \
  --name approve_order \
  --input '{"approver": "alice"}'

temporal workflow query \
  --workflow-id order-1042 \
  --type get_order_status
```

## Limites e trade-offs
Um handler de `Query` nunca deve modificar variáveis de estado do Workflow nem agendar Activities ou Timers, pois uma `Query Task` não gera eventos persistidos no histórico.

## Como verificar
Envie um `signal` e execute uma `query` via `temporal workflow` CLI contra um Workflow ativo e verifique o evento registrado em `temporal workflow show`.

## Conexões
- [[temporal-persistencia-datastore-postgresql-mysql-cassandra-visibility]] — Veja também: Temporal Persistence e Visibility: bancos de dados suportados (`PostgreSQL`, `MySQL`, `Cassandra`) e Advanced Visibility (`Elasticsearch` / SQL).
- [[temporal-continue-as-new-limites-event-history-workflows-longos]] — Veja também: Temporal `Continue-As-New`: prevenção de explosão de histórico em Workflows de longa duração ou loops contínuos.

## Fontes
- [Temporal GitHub — README.md (Durable Execution Platform, Local Dev Server, Temporal CLI & Web UI)](https://raw.githubusercontent.com/temporalio/temporal/main/docs/architecture/README.md) — README oficial do temporalio/temporal apresentando o servidor de execução durável, CLI temporal e inicialização start-dev; consultado em 2026-10-03.
- [Temporal Server Architecture Documentation — High-Level Architecture (Frontend, History, Matching, Internal Workers, Event Sourcing & Tasks)](https://raw.githubusercontent.com/temporalio/temporal/main/README.md) — Documentação oficial de arquitetura interna do Temporal detalhando processos do usuário vs cluster Temporal, shards do History Service, Task Queues e tipos de Tasks; consultado em 2026-10-03.
- [Temporal — Official GitHub Repository](https://github.com/temporalio/temporal) — Repositório oficial MIT do Temporal Server; consultado em 2026-10-03.
