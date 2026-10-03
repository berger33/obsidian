---
id: software.devops.tranche19.001839
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

# Temporal Activity Timeouts e Heartbeats: configuração de `StartToCloseTimeout`, `ScheduleToCloseTimeout`, `HeartbeatTimeout` e `RetryPolicy`

## Em uma frase
Toda execução de `Activity` no Temporal é protegida por quatro timeouts configuráveis (`ScheduleToStartTimeout`, `StartToCloseTimeout`, `ScheduleToCloseTimeout` e `HeartbeatTimeout`) combinados com uma **`RetryPolicy`** automática (`InitialInterval`, `BackoffCoefficient`, `MaximumInterval`, `MaximumAttempts`, `NonRetryableErrorTypes`).

## Por que importa
Se um Pod de Worker sofrer `OOMKilled` ou desligamento abrupto da VM enquanto executava uma Activity de codificação de vídeo de 2 horas, sem um `HeartbeatTimeout` curto o Temporal precisaria esperar as 2 horas inteiras do `StartToCloseTimeout` antes de perceber que o Worker morreu e reagendar a Activity em outro Pod.

## Como funciona
Para Activities curtas (segundos), basta definir `StartToCloseTimeout` (ex.: `30s`). Para Activities longas (minutos ou horas), a Activity chama `activity.RecordHeartbeat(ctx, progress)` periodicamente e configura `HeartbeatTimeout: 30s`: se o Worker cair, em 30 segundos outro Worker assume a Activity e lê os detalhes do último heartbeat (`activity.GetHeartbeatDetails`) para continuar de onde parou.

## Exemplo
```go
ao := workflow.ActivityOptions{
    StartToCloseTimeout: 2 * time.Hour,
    HeartbeatTimeout:    30 * time.Second,
    RetryPolicy: &temporal.RetryPolicy{
        InitialInterval:        time.Second,
        BackoffCoefficient:     2.0,
        MaximumInterval:        time.Minute,
        NonRetryableErrorTypes: []string{"InvalidAccountError"},
    },
}
```

## Limites e trade-offs
Por padrão no Temporal, uma `Activity` tem retentativas ilimitadas (`MaximumAttempts: 0`) até que o `ScheduleToCloseTimeout` expire ou que o erro retornado seja marcado como não retentável (`temporal.NewNonRetryableApplicationError`).

## Como verificar
Inspecione as tentativas e o último erro de uma Activity pendente em tempo real com `temporal workflow describe --workflow-id <id>`.

## Conexões
- [[temporal-namespaces-retencao-archival-s3-gcs-isolamento-multi-tenant]] — Veja também: Temporal `Namespaces`: isolamento multi-tenant, período de retenção de histórico e `Archival` para S3/GCS.
- [[temporal-cli-operacoes-reset-terminate-cancel-batch-schedules]] — Veja também: Temporal CLI em Produção: operações de `workflow reset`, `cancel`, `terminate`, `batch` e `schedule`.

## Fontes
- [Temporal GitHub — README.md (Durable Execution Platform, Local Dev Server, Temporal CLI & Web UI)](https://raw.githubusercontent.com/temporalio/temporal/main/docs/architecture/README.md) — README oficial do temporalio/temporal apresentando o servidor de execução durável, CLI temporal e inicialização start-dev; consultado em 2026-10-03.
- [Temporal Server Architecture Documentation — High-Level Architecture (Frontend, History, Matching, Internal Workers, Event Sourcing & Tasks)](https://raw.githubusercontent.com/temporalio/temporal/main/README.md) — Documentação oficial de arquitetura interna do Temporal detalhando processos do usuário vs cluster Temporal, shards do History Service, Task Queues e tipos de Tasks; consultado em 2026-10-03.
- [Temporal — Official GitHub Repository](https://github.com/temporalio/temporal) — Repositório oficial MIT do Temporal Server; consultado em 2026-10-03.
