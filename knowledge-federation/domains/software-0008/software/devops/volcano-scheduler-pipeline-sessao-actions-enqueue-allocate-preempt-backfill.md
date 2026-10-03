---
id: software.devops.tranche16.001584
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

# Volcano Scheduler: arquitetura de pipeline de sessão (`enqueue`, `allocate`, `preempt`, `reclaim`, `backfill`)

## Em uma frase
O Volcano Scheduler processa o agendamento em ciclos de sessão (*Session*), executando uma sequência configurável de **Actions** (`enqueue`, `allocate`, `preempt`, `reclaim`, `backfill`, `reserve`) orquestradas por **Plugins** (`gang`, `proportion`, `drf`, `priority`, `nodeorder`, `binpack`, `predicates`).

## Por que importa
Diferentes clusters têm objetivos distintos: um cluster de treinamento de LLMs prioriza empacotamento denso (`binpack`) e gang scheduling com reclamação de cotas entre filas (`reclaim`), enquanto um cluster de CI prioriza preenchimento rápido de lacunas com jobs pequenos (`backfill`).

## Como funciona
Configurado via `ConfigMap` `volcano-scheduler-configmap`, o scheduler abre um snapshot do cluster a cada ciclo, executa `enqueue` (admitindo `PodGroups` de `Pending` para `Inqueue`), `allocate` (alocando recursos livres segundo os scores dos plugins), `preempt` (preemptando tarefas de menor prioridade dentro da mesma fila), `reclaim` (recuperando recursos emprestados para outras filas quando a fila dona precisa) e `backfill` (alocando Pods pequenos `BestEffort` ou unitários nas sobras).

## Exemplo
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: volcano-scheduler-configmap
  namespace: volcano-system
data:
  volcano-scheduler.conf: |
    actions: "enqueue, allocate, backfill, reclaim, preempt"
    tiers:
    - plugins:
      - name: priority
      - name: gang
      - name: conformance
    - plugins:
      - name: drf
      - name: predicates
      - name: proportion
      - name: nodeorder
      - name: binpack
```

## Limites e trade-offs
A ordem declarada tanto na string `actions` quanto na lista `tiers` de `plugins` altera diretamente as decisões de agendamento; por exemplo, omitir `reclaim` em `actions` impede que uma `Queue` recupere recursos que foram emprestados por outra `Queue`.

## Como verificar
Inspecione `kubectl get configmap volcano-scheduler-configmap -n volcano-system -o yaml` para verificar o pipeline de ações e plugins ativo no cluster.

## Conexões
- [[volcano-scheduler-podgroup-gang-scheduling-all-or-nothing-deadlock]] — Veja também: Volcano: `PodGroup` e plugin `gang` para agendamento all-or-nothing sem deadlocks de recursos.
- [[volcano-scheduler-crd-queue-proportion-reclaimable-fair-share]] — Veja também: Volcano: governança multi-tenant de recursos com CRD `Queue`, plugin `proportion` e `reclaimable`.

## Fontes
- [Volcano GitHub — README.md (Kubernetes-Native Batch Scheduling System for AI/ML, Big Data & HPC, Ecosystem Integrations & CNCF Incubating Status)](https://volcano.sh/docs/home/architecture/) — README oficial do volcano-sh/volcano (CNCF Incubating) apresentando o agendador batch e suas integrações nativas com PyTorch, Ray, Spark, Kubeflow, Flink e MPI; consultado em 2026-10-03.
- [Volcano Official Documentation — Architecture (Volcano Scheduler, ControllerManager, Admission & vcctl CLI)](https://raw.githubusercontent.com/volcano-sh/volcano/master/README.md) — Documentação oficial de arquitetura do Volcano descrevendo o Scheduler baseado em ações/plugins, Queue/PodGroup/VCJob ControllerManager, Admission e vcctl; consultado em 2026-10-03.
- [Volcano — Official GitHub Repository](https://github.com/volcano-sh/volcano) — Repositório oficial Apache-2.0 do Volcano na CNCF; consultado em 2026-10-03.
