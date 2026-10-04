---
id: software.devops.tranche16.001582
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

# Volcano Job (`vcjob`): especificação multi-task (`ps`/`worker`) e políticas de reação a eventos de falha

## Em uma frase
O CRD `Job` do Volcano (`batch.volcano.sh/v1alpha1`, abreviado como `vcjob`) permite declarar em um único recurso múltiplos templates de tarefas heterogêneas (`tasks`, como `ps` parameter server, `master` e `worker`) e políticas granulares de ciclo de vida (`policies`) acionadas por eventos como `PodFailed`, `PodEvicted` ou `TaskCompleted`.

## Por que importa
O `batch/v1 Job` nativo do Kubernetes suporta apenas um único template homogêneo de Pod. Já treinamentos distribuídos (TensorFlow PS/Worker, MPI Master/Worker, Ray Head/Worker) exigem papéis distintos com diferentes quantidades de GPU/CPU e regras coordenadas de reinício (por exemplo, reiniciar o job inteiro se um worker falhar, ou encerrar o job com sucesso assim que a tarefa `master` terminar).

## Como funciona
No `vcjob`, cada entrada em `spec.tasks` define seu próprio `replicas`, `template` e `policies` locais, enquanto `spec.policies` define reações globais mapeando eventos (`Event`) para ações como `RestartJob`, `AbortJob`, `CompleteJob` ou `TerminateJob`. O ControllerManager cria automaticamente o `PodGroup` associado e gerencia as transições de fase do job.

## Exemplo
```yaml
apiVersion: batch.volcano.sh/v1alpha1
kind: Job
metadata:
  name: distributed-pytorch
spec:
  minAvailable: 3
  schedulerName: volcano
  queue: default
  policies:
    - event: PodEvicted
      action: RestartJob
  tasks:
    - replicas: 1
      name: master
      policies:
        - event: TaskCompleted
          action: CompleteJob
      template:
        spec:
          restartPolicy: Never
          containers:
            - name: trainer
              image: pytorch/pytorch:2.4.0-cuda12.1-cudnn9-runtime
    - replicas: 2
      name: worker
      template:
        spec:
          restartPolicy: Never
          containers:
            - name: trainer
              image: pytorch/pytorch:2.4.0-cuda12.1-cudnn9-runtime
```

## Limites e trade-offs
Se `minAvailable` no nível do `vcjob` não for informado explicitamente, o Volcano calcula o valor somando as réplicas de todas as `tasks` (ou os `minAvailable` individuais de cada task).

## Como verificar
Submeta o manifesto acima e execute `kubectl get vcjob distributed-pytorch` para inspecionar o status (`Running` -> `Completed`) e a criação automática dos Pods `distributed-pytorch-master-0` e `worker-0/1`.

## Conexões
- [[volcano-scheduler-arquitetura-batch-hpc-ai-cncf-vcctl]] — Veja também: Volcano: arquitetura CNCF Incubating de agendamento batch, HPC e IA/ML no Kubernetes (`scheduler`, `controllermanager`, `admission`, `vcctl`).
- [[volcano-scheduler-podgroup-gang-scheduling-all-or-nothing-deadlock]] — Veja também: Volcano: `PodGroup` e plugin `gang` para agendamento all-or-nothing sem deadlocks de recursos.

## Fontes
- [Volcano GitHub — README.md (Kubernetes-Native Batch Scheduling System for AI/ML, Big Data & HPC, Ecosystem Integrations & CNCF Incubating Status)](https://raw.githubusercontent.com/volcano-sh/volcano/master/README.md) — README oficial do volcano-sh/volcano (CNCF Incubating) apresentando o agendador batch e suas integrações nativas com PyTorch, Ray, Spark, Kubeflow, Flink e MPI; consultado em 2026-10-03.
- [Volcano Official Documentation — Architecture (Volcano Scheduler, ControllerManager, Admission & vcctl CLI)](https://volcano.sh/docs/home/architecture/) — Documentação oficial de arquitetura do Volcano descrevendo o Scheduler baseado em ações/plugins, Queue/PodGroup/VCJob ControllerManager, Admission e vcctl; consultado em 2026-10-03.
- [Volcano — Official GitHub Repository](https://github.com/volcano-sh/volcano) — Repositório oficial Apache-2.0 do Volcano na CNCF; consultado em 2026-10-03.
