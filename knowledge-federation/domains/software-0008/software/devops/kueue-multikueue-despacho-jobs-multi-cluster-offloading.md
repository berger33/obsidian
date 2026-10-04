---
id: software.devops.tranche16.001599
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

# Kubernetes Kueue: despacho multi-cluster de cargas de trabalho com `MultiKueue`

## Em uma frase
O `MultiKueue` é o mecanismo nativo de federação de filas do Kueue que permite a um cluster gerenciador (*Management Cluster*) enfileirar jobs localmente e despachá-los automaticamente para execução no cluster worker (*Worker Cluster*) que tiver cota e capacidade disponíveis.

## Por que importa
Grandes organizações operam múltiplos clusters de GPU em diferentes regiões ou provedores de nuvem; obrigar cientistas de dados a descobrir manualmente qual cluster tem GPUs livres e trocar de `kubeconfig` gera fragmentação e filas desbalanceadas.

## Como funciona
Configurado por meio de um `AdmissionCheck` do controlador `kueue.x-k8s.io/multikueue`, `MultiKueueConfig` e `MultiKueueCluster` (apontando para os `kubeconfigs` dos clusters workers), o `MultiKueue` espelha o `Workload` nas filas dos clusters workers candidatos. O primeiro cluster worker que reservar cota para o `Workload` recebe o Job real para execução e sincroniza o status e a conclusão de volta para o cluster gerenciador.

## Exemplo
```yaml
apiVersion: kueue.x-k8s.io/v1beta2
kind: MultiKueueConfig
metadata:
  name: global-gpu-pool
spec:
  clusters:
    - worker-us-east
    - worker-eu-west
```

## Limites e trade-offs
No cluster gerenciador, o Job submetido pelo usuário permanece sem criar Pods locais: os Pods são criados exclusivamente no cluster worker selecionado pelo `MultiKueue`, enquanto o objeto `Job`/`Workload` no cluster central reflete o status remoto.

## Como verificar
Inspecione `kubectl get multikueuecluster` para validar a conectividade (`Active: True`) com os clusters workers e verifique no `Workload` em qual cluster remoto o job foi admitido.

## Conexões
- [[kueue-topology-aware-scheduling-tas-hierarquia-racks-blocos]] — Veja também: Kubernetes Kueue: *Topology-Aware Scheduling* (`TAS`) com CRD `Topology` para comunicação Pod-a-Pod.
- [[kueue-integracao-ecossistema-kubeflow-ray-jobset-deployments-dra]] — Veja também: Kubernetes Kueue: integração com `JobSet`, Kubeflow, KubeRay, `Deployment`/`StatefulSet` e DRA (`v1beta2`).

## Fontes
- [Kubernetes Kueue GitHub — README.md (Job Queueing, Resource Flavor Fungibility, Fair Sharing, AdmissionChecks, TAS, MultiKueue & v1beta2 Readiness)](https://raw.githubusercontent.com/kubernetes-sigs/kueue/main/README.md) — README oficial do kubernetes-sigs/kueue detalhando recursos de fila, admissão parcial, ProvisioningRequest, MultiKueue e integrações com JobSet/Ray/Kubeflow; consultado em 2026-10-03.
- [Kubernetes Kueue Official Documentation — Core Concepts (ResourceFlavor, ClusterQueue, LocalQueue, Workload, Cohort, Preemption & DRA)](https://kueue.sigs.k8s.io/docs/concepts/) — Documentação oficial de conceitos do Kueue explicando Quota Reservation, Admission, WorkloadPriorityClass, Topology-Aware Scheduling e Dynamic Resource Allocation; consultado em 2026-10-03.
- [Kubernetes Kueue — Official GitHub Repository](https://github.com/kubernetes-sigs/kueue) — Repositório oficial Apache-2.0 do Kubernetes SIG-Scheduling Kueue; consultado em 2026-10-03.
