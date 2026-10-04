---
id: software.devops.tranche19.001833
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

# Temporal: segregação entre `Workflows` determinísticos (Replay de Histórico) e `Activities` idempotentes

## Em uma frase
O contrato fundamental de programação do Temporal exige segregar o código da aplicação em definições de **`Workflow`** (que devem ser 100% **determinísticas** e livres de efeitos colaterais diretos) e definições de **`Activity`** (que encapsulam todas as chamadas externas de I/O, rede, relógio ou banco de dados e devem ser **idempotentes**).

## Por que importa
Para reconstruir o estado exato de uma função que estava dormindo há 15 dias ou cujo Worker sofreu crash no meio da execução, o Worker do SDK faz *replay* do histórico de eventos gravado no History Service; se o código do Workflow usasse `time.Now()`, `rand.Int()` ou chamasse uma API HTTP fora de uma Activity, o replay tomaria um caminho diferente do original (`NonDeterministicError`).

## Como funciona
Quando o Workflow chama uma `Activity`, o Worker envia o comando `ScheduleActivityTask` ao History Service; quando a Activity termina, seu resultado é gravado no evento `ActivityTaskCompleted` do histórico. Durante um replay futuro, o Worker não reexecuta a Activity — ele simplesmente lê o resultado já registrado no evento do histórico e avança até o ponto atual.

## Exemplo
```go
func OrderWorkflow(ctx workflow.Context, orderID string) error {
    ao := workflow.ActivityOptions{
        StartToCloseTimeout: 30 * time.Second,
    }
    ctx = workflow.WithActivityOptions(ctx, ao)
    var paymentReceipt string
    if err := workflow.ExecuteActivity(ctx, ChargePaymentActivity, orderID).Get(ctx, &paymentReceipt); err != nil {
        return err
    }
    return workflow.ExecuteActivity(ctx, ShipOrderActivity, orderID, paymentReceipt).Get(ctx, nil)
}
```

## Limites e trade-offs
Nunca realize chamadas de rede, leitura de disco, acesso a variáveis globais mutáveis, goroutines nativas (`go func()`) ou `time.Sleep` diretamente dentro de uma função de Workflow: use sempre `workflow.ExecuteActivity`, `workflow.Go` e `workflow.Sleep`.

## Como verificar
Execute o linter/replayer do SDK (`WorkflowReplayer`) contra históricos JSON exportados por `temporal workflow show` em seu pipeline de CI para detectar quebras de determinismo antes do deploy.

## Conexões
- [[temporal-quatro-servicos-internos-frontend-history-matching-worker]] — Veja também: Temporal Server Internals: papel dos 4 serviços (`Frontend`, `History`, `Matching` e `Worker`).
- [[temporal-task-queues-workflow-tasks-activity-tasks-query-tasks]] — Veja também: Temporal `Task Queues` e Tipos de Tarefas: ciclo de polling de `Workflow Tasks`, `Activity Tasks` e `Query Tasks`.

## Fontes
- [Temporal GitHub — README.md (Durable Execution Platform, Local Dev Server, Temporal CLI & Web UI)](https://raw.githubusercontent.com/temporalio/temporal/main/docs/architecture/README.md) — README oficial do temporalio/temporal apresentando o servidor de execução durável, CLI temporal e inicialização start-dev; consultado em 2026-10-03.
- [Temporal Server Architecture Documentation — High-Level Architecture (Frontend, History, Matching, Internal Workers, Event Sourcing & Tasks)](https://raw.githubusercontent.com/temporalio/temporal/main/README.md) — Documentação oficial de arquitetura interna do Temporal detalhando processos do usuário vs cluster Temporal, shards do History Service, Task Queues e tipos de Tasks; consultado em 2026-10-03.
- [Temporal — Official GitHub Repository](https://github.com/temporalio/temporal) — Repositório oficial MIT do Temporal Server; consultado em 2026-10-03.
