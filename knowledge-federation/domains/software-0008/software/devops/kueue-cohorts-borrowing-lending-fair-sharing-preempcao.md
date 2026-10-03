---
id: software.devops.tranche16.001593
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
fontes: ["https://kueue.sigs.k8s.io/docs/concepts/", "https://raw.githubusercontent.com/kubernetes-sigs/kueue/main/README.md", "https://github.com/kubernetes-sigs/kueue"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Kubernetes Kueue: empréstimo de cotas via `Cohort`, `Fair Sharing` e políticas de preempção

## Em uma frase
Múltiplas `ClusterQueues` podem pertencer a um mesmo `cohort`, permitindo que uma fila tome emprestada cota ociosa (`borrowingLimit`) de outras filas do grupo (`lendingLimit`) sob regras de *Fair Sharing* e preempção automática.

## Por que importa
Quando a equipe de Pesquisa não está usando suas 16 GPUs nominais no fim de semana, a equipe de Engenharia de Dados pode usar essa capacidade ociosa via `cohort`, com a garantia contratual de que, assim que a Pesquisa submeter um job na segunda-feira, a cota emprestada será retomada imediatamente.

## Como funciona
Quando uma `ClusterQueue` submete um `Workload` que cabe dentro de sua própria `nominalQuota`, mas essa capacidade está atualmente emprestada a outra `ClusterQueue` do mesmo `cohort`, a política `preemption.reclaimWithinCohort: Any` (ou `LowerPriority`) instrui o Kueue a preemptar o workload que está tomando recursos emprestados, liberando a cota para o dono legítimo.

## Exemplo
```yaml
apiVersion: kueue.x-k8s.io/v1beta2
kind: ClusterQueue
metadata:
  name: research-cq
spec:
  cohortName: ai-shared-cohort
  queueingStrategy: BestEffortFIFO
  preemption:
    reclaimWithinCohort: Any
    withinClusterQueue: LowerPriority
  resourceGroups:
    - coveredResources: ["nvidia.com/gpu"]
      flavors:
        - name: on-demand-flavor
          resources:
            - name: "nvidia.com/gpu"
              nominalQuota: 16
              borrowingLimit: 8
              lendingLimit: 12
```

## Limites e trade-offs
A diferença entre `StrictFIFO` e `BestEffortFIFO` em `queueingStrategy` é crítica: no `StrictFIFO`, se o primeiro job da fila for grande demais para caber na cota livre atual, ele bloqueia todos os jobs menores atrás dele; no `BestEffortFIFO` (padrão), jobs menores podem ultrapassar o job bloqueado e aproveitar a cota disponível.

## Como verificar
Submeta jobs nas duas `ClusterQueues` do mesmo `cohort` e inspecione `kubectl describe clusterqueue research-cq` para verificar o uso nominal versus o uso emprestado (`Borrowed`).

## Conexões
- [[kueue-resourceflavor-clusterqueue-localqueue-modelo-tres-camadas]] — Veja também: Kubernetes Kueue: modelo de três camadas com `ResourceFlavor`, `ClusterQueue` e `LocalQueue`.
- [[kueue-flavor-fungibility-fallback-spot-ondemand]] — Veja também: Kubernetes Kueue: fungibilidade de flavors (`flavorFungibility`) para fallback automático entre Spot e On-Demand.

## Fontes
- [Kubernetes Kueue GitHub — README.md (Job Queueing, Resource Flavor Fungibility, Fair Sharing, AdmissionChecks, TAS, MultiKueue & v1beta2 Readiness)](https://kueue.sigs.k8s.io/docs/concepts/) — README oficial do kubernetes-sigs/kueue detalhando recursos de fila, admissão parcial, ProvisioningRequest, MultiKueue e integrações com JobSet/Ray/Kubeflow; consultado em 2026-10-03.
- [Kubernetes Kueue Official Documentation — Core Concepts (ResourceFlavor, ClusterQueue, LocalQueue, Workload, Cohort, Preemption & DRA)](https://raw.githubusercontent.com/kubernetes-sigs/kueue/main/README.md) — Documentação oficial de conceitos do Kueue explicando Quota Reservation, Admission, WorkloadPriorityClass, Topology-Aware Scheduling e Dynamic Resource Allocation; consultado em 2026-10-03.
- [Kubernetes Kueue — Official GitHub Repository](https://github.com/kubernetes-sigs/kueue) — Repositório oficial Apache-2.0 do Kubernetes SIG-Scheduling Kueue; consultado em 2026-10-03.
