---
id: software.devops.tranche16.001596
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

# Kubernetes Kueue: `AdmissionChecks` e integração com `ProvisioningRequest` do Cluster Autoscaler

## Em uma frase
O mecanismo de `AdmissionCheck` do Kueue permite que controladores internos ou externos retenham a liberação dos Pods de um `Workload` (mesmo após a reserva de cota `QuotaReservation`) até que condições físicas externas — como o provisionamento atômico de nós de GPU na nuvem via `ProvisioningRequest` do Cluster Autoscaler — sejam confirmadas.

## Por que importa
Reservar cota lógica em uma `ClusterQueue` não significa que a nuvem pública tenha estoque físico de 64 GPUs H100 naquele instante; liberar os Pods imediatamente faria metade deles subir (gerando cobrança ociosa na nuvem) enquanto a outra metade fica presa por falta de estoque na zona.

## Como funciona
Ao associar um `AdmissionCheck` baseado no controlador `kueue.x-k8s.io/provisioning-request` à `ClusterQueue`, o Kueue reserva a cota do `Workload` e cria um objeto `ProvisioningRequest` (`autoscaling.x-k8s.io`) para o `cluster-autoscaler`. Somente quando o autoscaler provisiona todas as VMs necessárias e marca o check como `Ready`, o Kueue conclui a admissão e libera a criação dos Pods.

## Exemplo
```yaml
apiVersion: kueue.x-k8s.io/v1beta2
kind: AdmissionCheck
metadata:
  name: gpu-Dynamic-provisioning
spec:
  controllerName: kueue.x-k8s.io/provisioning-request
  parametersRef:
    apiGroup: kueue.x-k8s.io
    kind: ProvisioningRequestConfig
    name: gpu-prov-config
```

## Limites e trade-offs
Se o `cluster-autoscaler` falhar ao obter capacidade na nuvem após o número configurado de tentativas (`retryStrategy`), o Kueue pode liberar a reserva ou tentar automaticamente o próximo `ResourceFlavor` disponível na `ClusterQueue`.

## Como verificar
Inspecione `status.admissionChecks` no objeto `Workload` (`kubectl get workload <nome> -o yaml`) para acompanhar o estado (`Pending` -> `Ready`) da solicitação de provisionamento.

## Conexões
- [[kueue-workload-priority-class-independente-pod-priority]] — Veja também: Kubernetes Kueue: `WorkloadPriorityClass` para priorização de fila independente de `PriorityClass` de Pod.
- [[kueue-wait-for-pods-ready-all-or-nothing-partial-admission-reclaim]] — Veja também: Kubernetes Kueue: `waitForPodsReady` (*all-or-nothing*), admissão parcial e reclamação dinâmica de cota.

## Fontes
- [Kubernetes Kueue GitHub — README.md (Job Queueing, Resource Flavor Fungibility, Fair Sharing, AdmissionChecks, TAS, MultiKueue & v1beta2 Readiness)](https://raw.githubusercontent.com/kubernetes-sigs/kueue/main/README.md) — README oficial do kubernetes-sigs/kueue detalhando recursos de fila, admissão parcial, ProvisioningRequest, MultiKueue e integrações com JobSet/Ray/Kubeflow; consultado em 2026-10-03.
- [Kubernetes Kueue Official Documentation — Core Concepts (ResourceFlavor, ClusterQueue, LocalQueue, Workload, Cohort, Preemption & DRA)](https://kueue.sigs.k8s.io/docs/concepts/) — Documentação oficial de conceitos do Kueue explicando Quota Reservation, Admission, WorkloadPriorityClass, Topology-Aware Scheduling e Dynamic Resource Allocation; consultado em 2026-10-03.
- [Kubernetes Kueue — Official GitHub Repository](https://github.com/kubernetes-sigs/kueue) — Repositório oficial Apache-2.0 do Kubernetes SIG-Scheduling Kueue; consultado em 2026-10-03.
