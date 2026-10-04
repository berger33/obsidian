---
id: software.devops.tranche16.001583
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

# Volcano: `PodGroup` e plugin `gang` para agendamento all-or-nothing sem deadlocks de recursos

## Em uma frase
O recurso `PodGroup` (`scheduling.volcano.sh/v1beta1`) e o plugin `gang` do Volcano Scheduler garantem a semântica de agendamento *all-or-nothing*: um job distribuído só tem seus Pods vinculados aos nós se pelo menos `minMember` Pods (e recursos `minResources`) puderem ser alocados simultaneamente.

## Por que importa
Quando dois jobs de treinamento que pedem 8 GPUs cada competem em um cluster com apenas 12 GPUs livres, o agendamento individual Pod a Pod aloca 6 GPUs para o Job A e 6 GPUs para o Job B: nenhum dos dois consegue iniciar o treinamento (`all-reduce` trava aguardando os demais pares) e ambos retêm as GPUs indefinidamente em *deadlock*.

## Como funciona
Durante cada ciclo de sessão do Volcano Scheduler, as ações `enqueue` e `allocate` consultam o plugin `gang`. Se o cluster não tiver capacidade livre para satisfazer `minResources` e `minMember` do `PodGroup` inteiro, nenhum Pod daquele grupo é comitado aos nós naquela rodada, deixando as GPUs livres para um job que caiba integralmente.

## Exemplo
```yaml
apiVersion: scheduling.volcano.sh/v1beta1
kind: PodGroup
metadata:
  name: ray-cluster-pg
  namespace: default
spec:
  minMember: 4
  minResources:
    cpu: "16"
    memory: "64Gi"
    nvidia.com/gpu: "4"
  queue: default
```

## Limites e trade-offs
Frameworks externos como Spark Operator, Kubeflow Training Operator, KubeRay e Flink Operator criam objetos `PodGroup` automaticamente quando configurados para usar o Volcano como scheduler.

## Como verificar
Execute `kubectl get pg` (atalho para `podgroups.scheduling.volcano.sh`) e observe a transição de fase de `Pending` para `Inqueue` e `Running` apenas quando todos os `minMember` recursos estão disponíveis.

## Conexões
- [[volcano-scheduler-vcjob-multi-task-lifecycle-policies-eventos]] — Veja também: Volcano Job (`vcjob`): especificação multi-task (`ps`/`worker`) e políticas de reação a eventos de falha.
- [[volcano-scheduler-pipeline-sessao-actions-enqueue-allocate-preempt-backfill]] — Veja também: Volcano Scheduler: arquitetura de pipeline de sessão (`enqueue`, `allocate`, `preempt`, `reclaim`, `backfill`).

## Fontes
- [Volcano GitHub — README.md (Kubernetes-Native Batch Scheduling System for AI/ML, Big Data & HPC, Ecosystem Integrations & CNCF Incubating Status)](https://raw.githubusercontent.com/volcano-sh/volcano/master/README.md) — README oficial do volcano-sh/volcano (CNCF Incubating) apresentando o agendador batch e suas integrações nativas com PyTorch, Ray, Spark, Kubeflow, Flink e MPI; consultado em 2026-10-03.
- [Volcano Official Documentation — Architecture (Volcano Scheduler, ControllerManager, Admission & vcctl CLI)](https://volcano.sh/docs/home/architecture/) — Documentação oficial de arquitetura do Volcano descrevendo o Scheduler baseado em ações/plugins, Queue/PodGroup/VCJob ControllerManager, Admission e vcctl; consultado em 2026-10-03.
- [Volcano — Official GitHub Repository](https://github.com/volcano-sh/volcano) — Repositório oficial Apache-2.0 do Volcano na CNCF; consultado em 2026-10-03.
