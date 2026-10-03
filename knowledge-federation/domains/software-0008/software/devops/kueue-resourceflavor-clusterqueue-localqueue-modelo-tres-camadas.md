---
id: software.devops.tranche16.001592
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

# Kubernetes Kueue: modelo de três camadas com `ResourceFlavor`, `ClusterQueue` e `LocalQueue`

## Em uma frase
A governança de recursos no Kueue estrutura-se em três objetos complementares: `ResourceFlavor` (cluster-scoped, descreve variantes físicas/comerciais de nós), `ClusterQueue` (cluster-scoped, define pools de cotas e políticas de fila) e `LocalQueue` (namespaced, ponto de entrada para os jobs de uma equipe).

## Por que importa
Em nuvens públicas e data centers híbridos, "1 GPU" ou "1 CPU" não é um recurso uniforme: existem nós spot, on-demand, GPUs A100 vs H100 e arquiteturas x86 vs ARM. Ao mesmo tempo, equipes trabalham isoladas em seus namespaces sem permissão para editar objetos globais de cota.

## Como funciona
O administrador declara `ResourceFlavors` (por exemplo `spot-gpu` e `ondemand-gpu` associados a `nodeLabels` e `nodeTaints`), agrupa as cotas `nominalQuota` por flavor dentro de uma `ClusterQueue` e cria em cada namespace de equipe uma `LocalQueue` que aponta para aquela `ClusterQueue`. Os usuários apenas adicionam o label `kueue.x-k8s.io/queue-name: <local-queue>` em seus Jobs.

## Exemplo
```yaml
apiVersion: kueue.x-k8s.io/v1beta2
kind: ResourceFlavor
metadata:
  name: on-demand- flavor
spec:
  nodeLabels:
    cloud.google.com/gke-spot: "false"
---
apiVersion: kueue.x-k8s.io/v1beta2
kind: ClusterQueue
metadata:
  name: team-a-cq
spec:
  namespaceSelector: {}
  resourceGroups:
    - coveredResources: ["cpu", "memory", "nvidia.com/gpu"]
      flavors:
        - name: on-demand-flavor
          resources:
            - name: "cpu"
              nominalQuota: 64
            - name: "memory"
              nominalQuota: 256Gi
            - name: "nvidia.com/gpu"
              nominalQuota: 8
---
apiVersion: kueue.x-k8s.io/v1beta2
kind: LocalQueue
metadata:
  namespace: team-a
  name: user-queue
spec:
  clusterQueue: team-a-cq
```

## Limites e trade-offs
Se o campo `spec.namespaceSelector` da `ClusterQueue` for omitido completamente, a `ClusterQueue` não admitirá workloads de nenhum namespace; use `namespaceSelector: {}` para permitir qualquer namespace ou um seletor de labels explícito.

## Como verificar
Execute `kubectl get clusterqueue team-a-cq` e `kubectl get localqueue -n team-a` e confirme que ambas reportam condição `Active: True`.

## Conexões
- [[kueue-arquitetura-job-level-manager-quota-reservation-admission]] — Veja também: Kubernetes Kueue: arquitetura SIG-Scheduling de enfileiramento no nível de Job, reserva de cota e admissão.
- [[kueue-cohorts-borrowing-lending-fair-sharing-preempcao]] — Veja também: Kubernetes Kueue: empréstimo de cotas via `Cohort`, `Fair Sharing` e políticas de preempção.

## Fontes
- [Kubernetes Kueue GitHub — README.md (Job Queueing, Resource Flavor Fungibility, Fair Sharing, AdmissionChecks, TAS, MultiKueue & v1beta2 Readiness)](https://kueue.sigs.k8s.io/docs/concepts/) — README oficial do kubernetes-sigs/kueue detalhando recursos de fila, admissão parcial, ProvisioningRequest, MultiKueue e integrações com JobSet/Ray/Kubeflow; consultado em 2026-10-03.
- [Kubernetes Kueue Official Documentation — Core Concepts (ResourceFlavor, ClusterQueue, LocalQueue, Workload, Cohort, Preemption & DRA)](https://raw.githubusercontent.com/kubernetes-sigs/kueue/main/README.md) — Documentação oficial de conceitos do Kueue explicando Quota Reservation, Admission, WorkloadPriorityClass, Topology-Aware Scheduling e Dynamic Resource Allocation; consultado em 2026-10-03.
- [Kubernetes Kueue — Official GitHub Repository](https://github.com/kubernetes-sigs/kueue) — Repositório oficial Apache-2.0 do Kubernetes SIG-Scheduling Kueue; consultado em 2026-10-03.
