---
id: software.devops.tranche16.001591
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

# Kubernetes Kueue: arquitetura SIG-Scheduling de enfileiramento no nível de Job, reserva de cota e admissão

## Em uma frase
O Kueue (`kubernetes-sigs/kueue`, mantido pelo Kubernetes SIG Scheduling) é um controlador e conjunto de APIs (`kueue.x-k8s.io/v1beta2`) que atua no nível de *Job* para decidir quando uma carga de trabalho deve ser admitida para iniciar (permitindo a criação de Pods) e quando deve ser suspensa ou preemptada.

## Por que importa
Diferentemente de substituir o `kube-scheduler` inteiro, o Kueue separa a **admissão de cota no nível de Workload/Job** do **agendamento de Pod no nó** (que continua sendo feito pelo `kube-scheduler` padrão e pelo `cluster-autoscaler`), evitando que milhares de Pods impossíveis de agendar inundem a API do Kubernetes.

## Como funciona
Quando um usuário cria um `Job` (ou `RayJob`, `PyTorchJob`, `JobSet`), o webhook do Kueue o inicia com `spec.suspend: true` e cria um objeto interno `Workload` que entra em uma `LocalQueue` vinculada a uma `ClusterQueue`. O Kueue avalia prioridades, cotas e `AdmissionChecks`; somente quando o `Workload` obtém `QuotaReservation` e é **admitido**, o Kueue altera `spec.suspend: false` e injeta os `nodeSelectors` correspondentes ao `ResourceFlavor` alocado.

## Exemplo
```bash
kubectl apply --server-side -f https://github.com/kubernetes-sigs/kueue/releases/latest/download/manifests.yaml
kubectl get pods -n kueue-system
```

## Limites e trade-offs
Como o Kueue modifica recursos existentes e gerencia CRDs grandes, a instalação dos manifestos oficiais deve ser feita com `kubectl apply --server-side` para evitar limites de tamanho da anotação `last-applied-configuration`.

## Como verificar
Verifique que o Deployment `kueue-controller-manager` está `Running` no namespace `kueue-system` e que os CRDs `clusterqueues`, `localqueues`, `resourceflavors` e `workloads` estão registrados.

## Conexões
- [[kueue-resourceflavor-clusterqueue-localqueue-modelo-tres-camadas]] — Veja também: Kubernetes Kueue: modelo de três camadas com `ResourceFlavor`, `ClusterQueue` e `LocalQueue`.

## Fontes
- [Kubernetes Kueue GitHub — README.md (Job Queueing, Resource Flavor Fungibility, Fair Sharing, AdmissionChecks, TAS, MultiKueue & v1beta2 Readiness)](https://raw.githubusercontent.com/kubernetes-sigs/kueue/main/README.md) — README oficial do kubernetes-sigs/kueue detalhando recursos de fila, admissão parcial, ProvisioningRequest, MultiKueue e integrações com JobSet/Ray/Kubeflow; consultado em 2026-10-03.
- [Kubernetes Kueue Official Documentation — Core Concepts (ResourceFlavor, ClusterQueue, LocalQueue, Workload, Cohort, Preemption & DRA)](https://kueue.sigs.k8s.io/docs/concepts/) — Documentação oficial de conceitos do Kueue explicando Quota Reservation, Admission, WorkloadPriorityClass, Topology-Aware Scheduling e Dynamic Resource Allocation; consultado em 2026-10-03.
- [Kubernetes Kueue — Official GitHub Repository](https://github.com/kubernetes-sigs/kueue) — Repositório oficial Apache-2.0 do Kubernetes SIG-Scheduling Kueue; consultado em 2026-10-03.
