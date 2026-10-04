---
id: software.testes.tranche09.000301
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-09.md"
fontes: ["https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/", "https://kubernetes.io/docs/concepts/workloads/controllers/job/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Kubernetes CronJob: testar execução idempotente, não exactly-once

## Em uma frase
CronJob agenda Jobs, mas interrupções e decisões do controller não formam uma garantia de execução exatamente uma vez.

## Por que importa
Controladores Kubernetes reconciliam estado de forma assíncrona, então uma assertion instantânea sobre Pod isolado não representa necessariamente o resultado desejado. Uma rotina que assume unicidade pode duplicar cobranças ou deixar trabalho perdido quando controladores reconciliam atrasados.

## Como funciona
Teste objetos e condições observáveis em cluster isolado, aguarde convergência com timeout e valide identidades e plugins que participam do comportamento. Projete a tarefa para idempotência e teste concorrência conforme concurrencyPolicy e janela de scheduling usada.

## Exemplo
Duas execuções sobre o mesmo intervalo encontram chave de idempotência e deixam um único efeito de negócio.

## Limites e trade-offs
Comportamento depende da versão, controller, scheduler e plugins instalados; dry-run do API server não prova execução de rede ou workload. Horário observado pode variar conforme atraso, suspensão e política configurada; cron não substitui fila transacional.

## Como verificar
Simule reexecução do mesmo período, atraso e sobreposição no cluster de teste e verifique estado final e logs do Job.

## Conexões
- [[kubernetes-job-completion-backoff]] — Veja também: Kubernetes Job: testar conclusão e retries do controller.
- [[kubernetes-deployment-rollout-observed-state]] — Veja também: Kubernetes Deployment: aguardar rollout e validar aplicação.

## Fontes
- [Kubernetes — CronJobs](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/) — agendamento de Jobs e políticas de concorrência; consultado em 2026-10-02.
- [Kubernetes — Jobs](https://kubernetes.io/docs/concepts/workloads/controllers/job/) — Jobs, completions, paralelismo, retries e limites de execução; consultado em 2026-10-02.
