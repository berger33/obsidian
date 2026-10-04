---
id: software.devops.tranche16.001600
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

# Kubernetes Kueue: integração com `JobSet`, Kubeflow, KubeRay, `Deployment`/`StatefulSet` e DRA (`v1beta2`)

## Em uma frase
O Kueue suporta nativamente uma ampla gama de tipos de carga de trabalho — `batch/v1 Job`, `JobSet`, Kubeflow (`PyTorchJob`, `TFJob`, `MPIJob`, `XGBoostJob`, `PaddleJob`), KubeRay (`RayJob`, `RayCluster`), `Pod` avulso, grupos de Pods e workloads de serving (`Deployment` e `StatefulSet`) — além de gerenciamento de cotas para Kubernetes *Dynamic Resource Allocation* (`DRA`).

## Por que importa
Plataformas modernas de IA não rodam apenas jobs batch isolados: elas misturam treinamento distribuído (`JobSet`/`PyTorchJob`) e inferência contínua (`Deployment`/`StatefulSet` ou `RayCluster`) competindo pelo mesmo pool de aceleradores e `ResourceClaims` de DRA.

## Como funciona
Ao rotular qualquer um desses objetos com `kueue.x-k8s.io/queue-name`, o controlador de integração correspondente do Kueue intercepta o recurso, calcula os `PodSets` equivalentes (incluindo mapeamento de dispositivos via DRA em `kueue.x-k8s.io/v1beta2`) e governa sua admissão e preempção dentro da mesma `ClusterQueue` e `cohort`, além de expor métricas Prometheus e o endpoint de visibilidade sob demanda de workloads pendentes.

## Exemplo
```yaml
apiVersion: jobset.x-k8s.io/v1alpha2
kind: JobSet
metadata:
  name: distributed-llm-jobset
  labels:
    kueue.x-k8s.io/queue-name: user-queue
spec:
  replicatedJobs:
    - name: workers
      replicas: 2
      template:
        spec:
          parallelism: 4
          completions: 4
          template:
            spec:
              containers:
                - name: trainer
                  image: ghcr.io/org/llm-trainer:v1.0
```

## Limites e trade-offs
Para gerenciar `Deployment`, `StatefulSet` ou `Pod` avulso com o Kueue, certifique-se de que as respectivas integrações (`pod`, `deployment`, `statefulset`) estão listadas em `integrations.frameworks` na configuração do `kueue-controller-manager`.

## Como verificar
Consulte as métricas do Kueue (`kueue_pending_workloads`, `kueue_admitted_workloads_total`) ou `kubectl get workloads -A` para auditar de forma unificada jobs batch e serviços de inferência.

## Conexões
- [[kueue-multikueue-despacho-jobs-multi-cluster-offloading]] — Veja também: Kubernetes Kueue: despacho multi-cluster de cargas de trabalho com `MultiKueue`.

## Fontes
- [Kubernetes Kueue GitHub — README.md (Job Queueing, Resource Flavor Fungibility, Fair Sharing, AdmissionChecks, TAS, MultiKueue & v1beta2 Readiness)](https://raw.githubusercontent.com/kubernetes-sigs/kueue/main/README.md) — README oficial do kubernetes-sigs/kueue detalhando recursos de fila, admissão parcial, ProvisioningRequest, MultiKueue e integrações com JobSet/Ray/Kubeflow; consultado em 2026-10-03.
- [Kubernetes Kueue Official Documentation — Core Concepts (ResourceFlavor, ClusterQueue, LocalQueue, Workload, Cohort, Preemption & DRA)](https://kueue.sigs.k8s.io/docs/concepts/) — Documentação oficial de conceitos do Kueue explicando Quota Reservation, Admission, WorkloadPriorityClass, Topology-Aware Scheduling e Dynamic Resource Allocation; consultado em 2026-10-03.
- [Kubernetes Kueue — Official GitHub Repository](https://github.com/kubernetes-sigs/kueue) — Repositório oficial Apache-2.0 do Kubernetes SIG-Scheduling Kueue; consultado em 2026-10-03.
