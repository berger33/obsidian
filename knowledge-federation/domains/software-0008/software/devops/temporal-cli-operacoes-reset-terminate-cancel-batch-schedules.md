---
id: software.devops.tranche19.001840
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

# Temporal CLI em Produção: operações de `workflow reset`, `cancel`, `terminate`, `batch` e `schedule`

## Em uma frase
A CLI oficial **`temporal`** unifica a operação do cluster e o diagnóstico/recuperação de incidentes em produção por meio dos subcomandos `temporal workflow` (`show`, `describe`, `stack`, `cancel`, `terminate`, `reset`), `temporal batch` e `temporal schedule`.

## Por que importa
Se um bug em uma API externa ou em uma Activity corromper o estado no passo 5 de 500 Workflows em produção, em vez de perder as execuções ou escrever scripts de banco de dados manuais, o operador corrige o Worker e usa **`temporal workflow reset`** para rebobinar os Workflows exatamente para o evento anterior ao passo 5.

## Como funciona
Além disso, `temporal schedule create` substitui cronjobs tradicionais com controle de sobreposição (`Skip`, `BufferOne`, `CancelOther`), backfill de janelas perdidas e pausa/retomada imediata.

## Exemplo
```bash
# Rebobinando um Workflow para o primeiro WorkflowTaskCompleted após corrigir um bug no Worker:
temporal workflow reset \
  --workflow-id order-1042 \
  --type FirstWorkflowTask \
  --reason "Reprocessando após correção do serviço de estoque"
```

## Limites e trade-offs
Entenda a diferença crítica entre `cancel` e `terminate`: `temporal workflow cancel` envia um pedido gracioso ao Workflow (permitindo executar blocos `defer`/compensação de Saga), enquanto `temporal workflow terminate` encerra a execução imediatamente no servidor sem rodar código adicional no Worker.

## Como verificar
Use `temporal workflow show --workflow-id <id>` para listar todos os eventos numerados do histórico e `temporal workflow stack --workflow-id <id>` para ver a stack trace exata onde um Workflow ativo está bloqueado.

## Conexões
- [[temporal-timeouts-activities-retry-policy-heartbeat-long-running]] — Veja também: Temporal Activity Timeouts e Heartbeats: configuração de `StartToCloseTimeout`, `ScheduleToCloseTimeout`, `HeartbeatTimeout` e `RetryPolicy`.

## Fontes
- [Temporal GitHub — README.md (Durable Execution Platform, Local Dev Server, Temporal CLI & Web UI)](https://raw.githubusercontent.com/temporalio/temporal/main/README.md) — README oficial do temporalio/temporal apresentando o servidor de execução durável, CLI temporal e inicialização start-dev; consultado em 2026-10-03.
- [Temporal Server Architecture Documentation — High-Level Architecture (Frontend, History, Matching, Internal Workers, Event Sourcing & Tasks)](https://raw.githubusercontent.com/temporalio/temporal/main/docs/architecture/README.md) — Documentação oficial de arquitetura interna do Temporal detalhando processos do usuário vs cluster Temporal, shards do History Service, Task Queues e tipos de Tasks; consultado em 2026-10-03.
- [Temporal — Official GitHub Repository](https://github.com/temporalio/temporal) — Repositório oficial MIT do Temporal Server; consultado em 2026-10-03.
