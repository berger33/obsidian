---
id: software.devops.tranche16.001581
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
fontes: ["https://raw.githubusercontent.com/volcano-sh/volcano/master/README.md", "https://volcano.sh/docs/home/architecture/", "https://github.com/volcano-sh/volcano"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Volcano: arquitetura CNCF Incubating de agendamento batch, HPC e IA/ML no Kubernetes (`scheduler`, `controllermanager`, `admission`, `vcctl`)

## Em uma frase
O Volcano (projeto CNCF Incubating, evoluído a partir do `kube-batch`) é um sistema nativo de agendamento em lote (*batch scheduling*) para Kubernetes projetado para cargas de alto desempenho de IA/ML/DL, Big Data e HPC (PyTorch, TensorFlow, Spark, Flink, Ray, MPI, Horovod).

## Por que importa
O `kube-scheduler` padrão do Kubernetes agenda Pod por Pod individualmente (*pod-by-pod*), sem visibilidade nativa do conceito de um job distribuído composto por dezenas de tarefas interdependentes nem de filas compartilhadas com justiça (*fair-share*) entre departamentos.

## Como funciona
O Volcano é composto por quatro módulos principais: **Volcano Scheduler** (motor de agendamento orientado a sessões, `Actions` e `Plugins` que opera sobre `PodGroup`), **ControllerManager** (que gerencia o ciclo de vida dos CRDs `Queue`, `PodGroup` e `VolcanoJob`/`vcjob`), **Admission** (webhook de validação e mutação de CRDs) e **vcctl** (cliente de linha de comando para operar jobs e filas).

## Exemplo
```bash
kubectl apply -f https://raw.githubusercontent.com/volcano-sh/volcano/master/installer/volcano-development.yaml
kubectl get pods -n volcano-system
```

## Limites e trade-offs
Para que um workload comum ou CRD externo seja agendado pelo Volcano, o campo `spec.schedulerName` dos Pods deve ser configurado como `volcano` (nos objetos `batch.volcano.sh/v1alpha1` `Job`, o controlador já define isso automaticamente).

## Como verificar
Verifique no namespace `volcano-system` que os Pods `volcano-admission`, `volcano-controllers` e `volcano-scheduler` estão `Running` e prontos.

## Conexões
- [[volcano-scheduler-vcjob-multi-task-lifecycle-policies-eventos]] — Veja também: Volcano Job (`vcjob`): especificação multi-task (`ps`/`worker`) e políticas de reação a eventos de falha.

## Fontes
- [Volcano GitHub — README.md (Kubernetes-Native Batch Scheduling System for AI/ML, Big Data & HPC, Ecosystem Integrations & CNCF Incubating Status)](https://raw.githubusercontent.com/volcano-sh/volcano/master/README.md) — README oficial do volcano-sh/volcano (CNCF Incubating) apresentando o agendador batch e suas integrações nativas com PyTorch, Ray, Spark, Kubeflow, Flink e MPI; consultado em 2026-10-03.
- [Volcano Official Documentation — Architecture (Volcano Scheduler, ControllerManager, Admission & vcctl CLI)](https://volcano.sh/docs/home/architecture/) — Documentação oficial de arquitetura do Volcano descrevendo o Scheduler baseado em ações/plugins, Queue/PodGroup/VCJob ControllerManager, Admission e vcctl; consultado em 2026-10-03.
- [Volcano — Official GitHub Repository](https://github.com/volcano-sh/volcano) — Repositório oficial Apache-2.0 do Volcano na CNCF; consultado em 2026-10-03.
