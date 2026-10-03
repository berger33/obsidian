---
id: software.devops.tranche16.001594
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
fontes: ["https://raw.githubusercontent.com/kubernetes-sigs/kueue/main/README.md", "https://kueue.sigs.k8s.io/docs/concepts/", "https://github.com/kubernetes-sigs/kueue"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Kubernetes Kueue: fungibilidade de flavors (`flavorFungibility`) para fallback automático entre Spot e On-Demand

## Em uma frase
O mecanismo de *Flavor Fungibility* do Kueue permite que um `Workload` tente alocar recursos na ordem de preferência dos `ResourceFlavors` listados na `ClusterQueue` (por exemplo, tentando primeiro nós `spot` mais baratos e fazendo fallback automático para `on-demand`, ou vice-versa).

## Por que importa
Sem fungibilidade automática no controlador de fila, o desenvolvedor precisaria escolher manualmente no manifesto do Job se quer usar nós Spot ou On-Demand, e reenviar o Job manualmente caso a cota ou capacidade Spot se esgote.

## Como funciona
Em `spec.resourceGroups[*].flavors`, a ordem da lista define a preferência da `ClusterQueue`. Com `spec.flavorFungibility` (`whenCanBorrow: Borrow | TryNextFlavor` e `whenCanPreempt: Preempt | TryNextFlavor`), o administrador controla se o Kueue deve primeiro tentar emprestar cota do `cohort` no primeiro flavor antes de passar para o segundo flavor, ou se deve tentar primeiro a cota própria no próximo flavor.

## Exemplo
```yaml
apiVersion: kueue.x-k8s.io/v1beta2
kind: ClusterQueue
metadata:
  name: hybrid-spot-cq
spec:
  flavorFungibility:
    whenCanBorrow: TryNextFlavor
    whenCanPreempt: TryNextFlavor
  resourceGroups:
    - coveredResources: ["cpu", "memory"]
      flavors:
        - name: spot-flavor
          resources:
            - name: "cpu"
              nominalQuota: 32
            - name: "memory"
              nominalQuota: 128Gi
        - name: on-demand-flavor
          resources:
            - name: "cpu"
              nominalQuota: 32
            - name: "memory"
              nominalQuota: 128Gi
```

## Limites e trade-offs
Quando o Kueue escolhe um `ResourceFlavor` específico para admitir o `Workload`, ele injeta automaticamente os `nodeLabels` e `tolerations` daquele flavor nos templates de Pod do Job antes de mudar `suspend: false`.

## Como verificar
Inspecione o objeto `Workload` (`kubectl get workload -o yaml`) após a admissão e verifique em `status.admission.podSetAssignments` qual `ResourceFlavor` foi atribuído a cada conjunto de Pods.

## Conexões
- [[kueue-cohorts-borrowing-lending-fair-sharing-preempcao]] — Veja também: Kubernetes Kueue: empréstimo de cotas via `Cohort`, `Fair Sharing` e políticas de preempção.
- [[kueue-workload-priority-class-independente-pod-priority]] — Veja também: Kubernetes Kueue: `WorkloadPriorityClass` para priorização de fila independente de `PriorityClass` de Pod.

## Fontes
- [Kubernetes Kueue GitHub — README.md (Job Queueing, Resource Flavor Fungibility, Fair Sharing, AdmissionChecks, TAS, MultiKueue & v1beta2 Readiness)](https://raw.githubusercontent.com/kubernetes-sigs/kueue/main/README.md) — README oficial do kubernetes-sigs/kueue detalhando recursos de fila, admissão parcial, ProvisioningRequest, MultiKueue e integrações com JobSet/Ray/Kubeflow; consultado em 2026-10-03.
- [Kubernetes Kueue Official Documentation — Core Concepts (ResourceFlavor, ClusterQueue, LocalQueue, Workload, Cohort, Preemption & DRA)](https://kueue.sigs.k8s.io/docs/concepts/) — Documentação oficial de conceitos do Kueue explicando Quota Reservation, Admission, WorkloadPriorityClass, Topology-Aware Scheduling e Dynamic Resource Allocation; consultado em 2026-10-03.
- [Kubernetes Kueue — Official GitHub Repository](https://github.com/kubernetes-sigs/kueue) — Repositório oficial Apache-2.0 do Kubernetes SIG-Scheduling Kueue; consultado em 2026-10-03.
