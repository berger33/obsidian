---
id: software.devops.tranche16.001590
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-16.md"
fontes: ["https://volcano.sh/docs/home/architecture/", "https://raw.githubusercontent.com/volcano-sh/volcano/master/README.md", "https://github.com/volcano-sh/volcano"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Volcano: operação de jobs e filas pela linha de comando com `vcctl`

## Em uma frase
O `vcctl` é o cliente oficial de linha de comando do Volcano para listar, inspecionar, suspender (`job suspend`), retomar (`job resume`), deletar jobs e gerenciar o estado de filas (`queue get`, `queue list`, `queue operate`).

## Por que importa
Durante manutenções emergenciais em nós de GPU ou quando um job prioritário precisa entrar imediatamente, operadores de plataforma precisam pausar jobs batch em andamento ou fechar temporariamente uma `Queue` para novas admissões com um único comando.

## Como funciona
Com o binário `vcctl`, o operador pode executar `vcctl job list -n ai-training`, `vcctl job view --name <job>`, `vcctl job suspend --name <job>` (que libera os Pods ativos mantendo a definição do `vcjob` pronta para retomada posterior via `vcctl job resume`) e `vcctl queue operate --name <queue> --action close` / `open`.

## Exemplo
```bash
vcctl queue list
vcctl job list --namespace default
vcctl job suspend --name distributed-pytorch --namespace default
vcctl job resume --name distributed-pytorch --namespace default
```

## Limites e trade-offs
Suspender um `vcjob` em execução com `vcctl job suspend` encerra os Pods ativos daquele job; para que o treinamento retome sem perder horas de progresso no `vcctl job resume`, o código de treinamento deve salvar checkpoints periódicos em um volume persistente.

## Como verificar
Execute `vcctl job list` antes e depois de `vcctl job suspend` e verifique a mudança de status do job e a liberação imediata dos recursos alocáveis na fila.

## Conexões
- [[volcano-scheduler-integracao-ecossistema-spark-ray-kubeflow-flink]] — Veja também: Volcano: integração nativa com Spark, KubeRay, Kubeflow Trainer e Flink sobre Kubernetes.

## Fontes
- [Volcano GitHub — README.md (Kubernetes-Native Batch Scheduling System for AI/ML, Big Data & HPC, Ecosystem Integrations & CNCF Incubating Status)](https://volcano.sh/docs/home/architecture/) — README oficial do volcano-sh/volcano (CNCF Incubating) apresentando o agendador batch e suas integrações nativas com PyTorch, Ray, Spark, Kubeflow, Flink e MPI; consultado em 2026-10-03.
- [Volcano Official Documentation — Architecture (Volcano Scheduler, ControllerManager, Admission & vcctl CLI)](https://raw.githubusercontent.com/volcano-sh/volcano/master/README.md) — Documentação oficial de arquitetura do Volcano descrevendo o Scheduler baseado em ações/plugins, Queue/PodGroup/VCJob ControllerManager, Admission e vcctl; consultado em 2026-10-03.
- [Volcano — Official GitHub Repository](https://github.com/volcano-sh/volcano) — Repositório oficial Apache-2.0 do Volcano na CNCF; consultado em 2026-10-03.
