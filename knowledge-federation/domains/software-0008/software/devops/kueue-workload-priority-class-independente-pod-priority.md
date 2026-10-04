---
id: software.devops.tranche16.001595
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

# Kubernetes Kueue: `WorkloadPriorityClass` para priorização de fila independente de `PriorityClass` de Pod

## Em uma frase
O CRD `WorkloadPriorityClass` (`kueue.x-k8s.io/v1beta2`) permite atribuir prioridades exclusivas para ordenação de enfileiramento e preempção de `Workloads` no Kueue, separadamente da `scheduling.k8s.io/v1 PriorityClass` usada pelo `kube-scheduler` nos Pods.

## Por que importa
Se uma equipe aumentar a `PriorityClass` padrão do Kubernetes em um Job batch para furar a fila de batch, os Pods desse Job também ganhariam o poder de preemptar Pods de microsserviços online de produção no nível do `kube-scheduler`.

## Como funciona
Ao referenciar uma `WorkloadPriorityClass` através do label `kueue.x-k8s.io/priority-class` no Job, o valor numérico daquela classe governa exclusivamente a ordem de admissão e a preempção entre `Workloads` gerenciados pelo Kueue, mantendo a `PriorityClass` de Pod intacta para proteger cargas online no nível de nó.

## Exemplo
```yaml
apiVersion: kueue.x-k8s.io/v1beta2
kind: WorkloadPriorityClass
metadata:
  name: urgent-batch-priority
value: 5000
description: "Prioridade alta apenas dentro das filas batch do Kueue"
---
apiVersion: batch/v1
kind: Job
metadata:
  name: hotfix-model-eval
  labels:
    kueue.x-k8s.io/queue-name: user-queue
    kueue.x-k8s.io/priority-class: urgent-batch-priority
spec:
  parallelism: 2
  template:
    spec:
      restartPolicy: Never
      containers:
        - name: eval
          image: ghcr.io/org/eval:v1.0
```

## Limites e trade-offs
Uma `WorkloadPriorityClass` nunca é copiada para `spec.priorityClassName` do Pod; as duas hierarquias de prioridade são completamente ortogonais por design.

## Como verificar
Execute `kubectl get workloads` e confirme que o `Workload` correspondente ao Job exibe `urgent-batch-priority` e é admitido à frente de jobs de menor prioridade na mesma `ClusterQueue`.

## Conexões
- [[kueue-flavor-fungibility-fallback-spot-ondemand]] — Veja também: Kubernetes Kueue: fungibilidade de flavors (`flavorFungibility`) para fallback automático entre Spot e On-Demand.
- [[kueue-admission-checks-provisioning-request-cluster-autoscaler]] — Veja também: Kubernetes Kueue: `AdmissionChecks` e integração com `ProvisioningRequest` do Cluster Autoscaler.

## Fontes
- [Kubernetes Kueue GitHub — README.md (Job Queueing, Resource Flavor Fungibility, Fair Sharing, AdmissionChecks, TAS, MultiKueue & v1beta2 Readiness)](https://kueue.sigs.k8s.io/docs/concepts/) — README oficial do kubernetes-sigs/kueue detalhando recursos de fila, admissão parcial, ProvisioningRequest, MultiKueue e integrações com JobSet/Ray/Kubeflow; consultado em 2026-10-03.
- [Kubernetes Kueue Official Documentation — Core Concepts (ResourceFlavor, ClusterQueue, LocalQueue, Workload, Cohort, Preemption & DRA)](https://raw.githubusercontent.com/kubernetes-sigs/kueue/main/README.md) — Documentação oficial de conceitos do Kueue explicando Quota Reservation, Admission, WorkloadPriorityClass, Topology-Aware Scheduling e Dynamic Resource Allocation; consultado em 2026-10-03.
- [Kubernetes Kueue — Official GitHub Repository](https://github.com/kubernetes-sigs/kueue) — Repositório oficial Apache-2.0 do Kubernetes SIG-Scheduling Kueue; consultado em 2026-10-03.
