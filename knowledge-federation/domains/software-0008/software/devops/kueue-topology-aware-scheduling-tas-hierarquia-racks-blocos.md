---
id: software.devops.tranche16.001598
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

# Kubernetes Kueue: *Topology-Aware Scheduling* (`TAS`) com CRD `Topology` para comunicação Pod-a-Pod

## Em uma frase
O *Topology-Aware Scheduling* (`TAS`) do Kueue utiliza o CRD `Topology` (`kueue.x-k8s.io/v1beta2`) vinculado a um `ResourceFlavor` para alocar todos os Pods de um `Workload` (ou fatias de `PodSet`) dentro do mesmo bloco, rack ou nó do data center.

## Por que importa
Em treinamentos distribuídos multi-nó (como `JobSet` ou `PyTorchJob`), o Kueue não deve apenas verificar se existem 16 GPUs livres espalhadas pelo cluster; ele precisa garantir que existam 16 GPUs livres no mesmo bloco/rack de rede de baixa latência antes de admitir o workload.

## Como funciona
O administrador declara um objeto `Topology` listando os níveis hierárquicos de labels de nó (por exemplo: `cloud.provider.com/topology-block` -> `cloud.provider.com/topology-rack` -> `kubernetes.io/hostname`) e referencia `topologyName` no `ResourceFlavor`. Nos Pods do Job, a anotação `kueue.x-k8s.io/podset-required-topology` (ou `preferred-topology`) instrui o Kueue a só admitir o workload quando houver capacidade física contígua naquele nível de topologia.

## Exemplo
```yaml
apiVersion: kueue.x-k8s.io/v1beta2
kind: Topology
metadata:
  name: datacenter-fabric
spec:
  levels:
    - nodeLabel: cloud.provider.com/topology-block
    - nodeLabel: cloud.provider.com/topology-rack
    - nodeLabel: kubernetes.io/hostname
```

## Limites e trade-offs
Quando o `TAS` é utilizado em um `ResourceFlavor`, um `Workload` só é admitido quando satisfaz simultaneamente a `QuotaReservation` na `ClusterQueue` e a disponibilidade física real nos nós agrupados pelo `Topology`.

## Como verificar
Aplique a anotação `kueue.x-k8s.io/podset-required-topology: cloud.provider.com/topology-rack` em um Job e verifique que todos os Pods admitidos recebem seletores para o mesmo rack.

## Conexões
- [[kueue-wait-for-pods-ready-all-or-nothing-partial-admission-reclaim]] — Veja também: Kubernetes Kueue: `waitForPodsReady` (*all-or-nothing*), admissão parcial e reclamação dinâmica de cota.
- [[kueue-multikueue-despacho-jobs-multi-cluster-offloading]] — Veja também: Kubernetes Kueue: despacho multi-cluster de cargas de trabalho com `MultiKueue`.

## Fontes
- [Kubernetes Kueue GitHub — README.md (Job Queueing, Resource Flavor Fungibility, Fair Sharing, AdmissionChecks, TAS, MultiKueue & v1beta2 Readiness)](https://kueue.sigs.k8s.io/docs/concepts/) — README oficial do kubernetes-sigs/kueue detalhando recursos de fila, admissão parcial, ProvisioningRequest, MultiKueue e integrações com JobSet/Ray/Kubeflow; consultado em 2026-10-03.
- [Kubernetes Kueue Official Documentation — Core Concepts (ResourceFlavor, ClusterQueue, LocalQueue, Workload, Cohort, Preemption & DRA)](https://raw.githubusercontent.com/kubernetes-sigs/kueue/main/README.md) — Documentação oficial de conceitos do Kueue explicando Quota Reservation, Admission, WorkloadPriorityClass, Topology-Aware Scheduling e Dynamic Resource Allocation; consultado em 2026-10-03.
- [Kubernetes Kueue — Official GitHub Repository](https://github.com/kubernetes-sigs/kueue) — Repositório oficial Apache-2.0 do Kubernetes SIG-Scheduling Kueue; consultado em 2026-10-03.
