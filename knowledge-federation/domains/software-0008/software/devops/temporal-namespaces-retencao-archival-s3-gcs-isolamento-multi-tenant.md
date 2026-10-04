---
id: software.devops.tranche19.001838
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
fontes: ["https://raw.githubusercontent.com/temporalio/temporal/main/README.md", "https://raw.githubusercontent.com/temporalio/temporal/main/docs/architecture/README.md", "https://github.com/temporalio/temporal"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Temporal `Namespaces`: isolamento multi-tenant, período de retenção de histórico e `Archival` para S3/GCS

## Em uma frase
No Temporal, o **`Namespace`** é a unidade de isolamento multi-tenant para Workflows, Task Queues, limites de taxa, período de retenção de histórico (`--retention`) e configuração de arquivamento de longo prazo (**`Archival`** para Amazon S3, Google Cloud Storage ou disco local).

## Por que importa
Guardar eternamente no banco transacional primário (PostgreSQL/Cassandra) os históricos completos de milhões de Workflows já encerrados encareceria o armazenamento de baixa latência; por isso, todo Namespace apaga os históricos fechados após o período de retenção configurado (ex.: 7 a 30 dias).

## Como funciona
Com o **Archival** habilitado no Namespace (executado pelo *Internal Workers Service* do Temporal), assim que o prazo de retenção de um Workflow encerrado expira no banco primário, seu histórico de eventos e registro de visibilidade são enviados para um bucket S3/GCS antes da deleção local, permanecendo consultáveis para auditoria histórica.

## Exemplo
```bash
temporal operator namespace create \
  --namespace payments-prod \
  --retention 30d \
  --description "Namespace de produção para pagamentos"
temporal operator namespace describe --namespace payments-prod
```

## Limites e trade-offs
Dois Workflows em Namespaces diferentes podem usar exatamente o mesmo `WorkflowID` sem qualquer colisão, e dentro de um mesmo Namespace o Temporal garante que nunca existam duas execuções abertas (`Running`) simultâneas com o mesmo `WorkflowID`.

## Como verificar
Execute `temporal operator namespace list` e `temporal operator namespace describe` para auditar o período de retenção de cada ambiente.

## Conexões
- [[temporal-continue-as-new-limites-event-history-workflows-longos]] — Veja também: Temporal `Continue-As-New`: prevenção de explosão de histórico em Workflows de longa duração ou loops contínuos.
- [[temporal-timeouts-activities-retry-policy-heartbeat-long-running]] — Veja também: Temporal Activity Timeouts e Heartbeats: configuração de `StartToCloseTimeout`, `ScheduleToCloseTimeout`, `HeartbeatTimeout` e `RetryPolicy`.

## Fontes
- [Temporal GitHub — README.md (Durable Execution Platform, Local Dev Server, Temporal CLI & Web UI)](https://raw.githubusercontent.com/temporalio/temporal/main/README.md) — README oficial do temporalio/temporal apresentando o servidor de execução durável, CLI temporal e inicialização start-dev; consultado em 2026-10-03.
- [Temporal Server Architecture Documentation — High-Level Architecture (Frontend, History, Matching, Internal Workers, Event Sourcing & Tasks)](https://raw.githubusercontent.com/temporalio/temporal/main/docs/architecture/README.md) — Documentação oficial de arquitetura interna do Temporal detalhando processos do usuário vs cluster Temporal, shards do History Service, Task Queues e tipos de Tasks; consultado em 2026-10-03.
- [Temporal — Official GitHub Repository](https://github.com/temporalio/temporal) — Repositório oficial MIT do Temporal Server; consultado em 2026-10-03.
