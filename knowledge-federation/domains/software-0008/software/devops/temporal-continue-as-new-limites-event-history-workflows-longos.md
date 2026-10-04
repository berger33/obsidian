---
id: software.devops.tranche19.001837
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

# Temporal `Continue-As-New`: prevenção de explosão de histórico em Workflows de longa duração ou loops contínuos

## Em uma frase
Para Workflows que rodam em loop contínuo (como um agente que monitora uma conta para sempre ou processa milhões de eventos em série), a primitiva **`Continue-As-New`** encerra atomicamente a execução atual (`RunID` antigo) e inicia uma nova execução (`RunID` novo) com o mesmo `WorkflowID` passando o estado acumulado como argumento.

## Por que importa
Como o Temporal funciona por Event Sourcing (gravando cada Activity, Timer e Signal em um histórico append-only por `RunID`), um loop infinito em um único `RunID` acumularia dezenas de milhares de eventos até atingir o limite rígido de tamanho/contagem de eventos do History Service.

## Como funciona
Os SDKs do Temporal expõem `workflow.GetInfo(ctx).GetContinueAsNewSuggested()` (acionado quando o histórico se aproxima de alguns milhares de eventos ou megabytes). Ao retornar um erro `workflow.NewContinueAsNewError(ctx, MyWorkflow, currentState)`, o servidor cria o novo `RunID` na mesma transação sem perder nenhum Signal pendente.

## Exemplo
```go
func EntityMonitorWorkflow(ctx workflow.Context, state MonitorState) error {
    for {
        // Processa um ciclo de eventos e Activities...
        if workflow.GetInfo(ctx).GetContinueAsNewSuggested() {
            return workflow.NewContinueAsNewError(ctx, EntityMonitorWorkflow, state)
        }
    }
}
```

## Limites e trade-offs
Consulte sempre `GetContinueAsNewSuggested()` em Workflows que possuem loops `for`/`while` ou que recebem número ilimitado de `Signals` ao longo do tempo.

## Como verificar
Inspecione o tamanho do histórico (`HistoryLength` e `HistorySizeBytes`) de uma execução com `temporal workflow describe --workflow-id <id>`.

## Conexões
- [[temporal-signals-queries-updates-interacao-workflows-em-execucao]] — Veja também: Temporal `Signals`, `Queries` e `Updates`: interação assíncrona e síncrona com Workflows em execução.
- [[temporal-namespaces-retencao-archival-s3-gcs-isolamento-multi-tenant]] — Veja também: Temporal `Namespaces`: isolamento multi-tenant, período de retenção de histórico e `Archival` para S3/GCS.

## Fontes
- [Temporal GitHub — README.md (Durable Execution Platform, Local Dev Server, Temporal CLI & Web UI)](https://raw.githubusercontent.com/temporalio/temporal/main/docs/architecture/README.md) — README oficial do temporalio/temporal apresentando o servidor de execução durável, CLI temporal e inicialização start-dev; consultado em 2026-10-03.
- [Temporal Server Architecture Documentation — High-Level Architecture (Frontend, History, Matching, Internal Workers, Event Sourcing & Tasks)](https://raw.githubusercontent.com/temporalio/temporal/main/README.md) — Documentação oficial de arquitetura interna do Temporal detalhando processos do usuário vs cluster Temporal, shards do History Service, Task Queues e tipos de Tasks; consultado em 2026-10-03.
- [Temporal — Official GitHub Repository](https://github.com/temporalio/temporal) — Repositório oficial MIT do Temporal Server; consultado em 2026-10-03.
