---
id: software.devops.tranche16.001586
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

# Volcano: algoritmo `drf` (*Dominant Resource Fairness*) e filas hierárquicas para justiça multi-recurso

## Em uma frase
O plugin `drf` (*Dominant Resource Fairness*) do Volcano Scheduler garante compartilhamento justo dentro de uma fila e em árvores de filas hierárquicas quando jobs demandam proporções muito diferentes de múltiplos tipos de recursos (CPU, RAM, GPU, NPU).

## Por que importa
Um algoritmo de agendamento que olha apenas para CPU trataria como iguais um job de pré-processamento que usa 32 CPUs e 0 GPUs e um job de treinamento que usa 4 CPUs e 8 GPUs (100% das GPUs do nó), permitindo que um único job monopolize o recurso escasso.

## Como funciona
O plugin `drf` calcula para cada job (e usuário/subfila) o seu *recurso dominante* — a maior fração de qualquer recurso total do cluster que aquele job consome (por exemplo, `8/16 = 50%` de GPUs é maior que `4/128 = 3,1%` de CPUs, logo o share dominante é `0.50`). O Volcano prioriza o agendamento dos jobs cujo share dominante acumulado seja o menor, equilibrando cargas intensivas em CPU, memória e aceleradores.

## Exemplo
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: volcano-drf-hierarchy
  namespace: volcano-system
data:
  volcano-scheduler.conf: |
    actions: "enqueue, allocate, reclaim"
    tiers:
    - plugins:
      - name: gang
      - name: drf
        enableHierarchy: true
      - name: proportion
```

## Limites e trade-offs
Quando `enableHierarchy: true` é habilitado no plugin `drf` / `capacity`, as filas podem ser organizadas em árvore pai-filho usando anotações de hierarquia para refletir departamentos e subequipes.

## Como verificar
Verifique nos logs do `volcano-scheduler` (com verbosidade `-v=4`) o cálculo do *dominant resource* e do valor de *share* atribuído a cada `PodGroup` durante a fase `allocate`.

## Conexões
- [[volcano-scheduler-crd-queue-proportion-reclaimable-fair-share]] — Veja também: Volcano: governança multi-tenant de recursos com CRD `Queue`, plugin `proportion` e `reclaimable`.
- [[volcano-scheduler-plugins-ssh-env-svc-mpi-pytorch-horovod]] — Veja também: Volcano: plugins de ciclo de vida de VCJob (`ssh`, `env` e `svc`) para MPI, PyTorch e Horovod.

## Fontes
- [Volcano GitHub — README.md (Kubernetes-Native Batch Scheduling System for AI/ML, Big Data & HPC, Ecosystem Integrations & CNCF Incubating Status)](https://volcano.sh/docs/home/architecture/) — README oficial do volcano-sh/volcano (CNCF Incubating) apresentando o agendador batch e suas integrações nativas com PyTorch, Ray, Spark, Kubeflow, Flink e MPI; consultado em 2026-10-03.
- [Volcano Official Documentation — Architecture (Volcano Scheduler, ControllerManager, Admission & vcctl CLI)](https://raw.githubusercontent.com/volcano-sh/volcano/master/README.md) — Documentação oficial de arquitetura do Volcano descrevendo o Scheduler baseado em ações/plugins, Queue/PodGroup/VCJob ControllerManager, Admission e vcctl; consultado em 2026-10-03.
- [Volcano — Official GitHub Repository](https://github.com/volcano-sh/volcano) — Repositório oficial Apache-2.0 do Volcano na CNCF; consultado em 2026-10-03.
