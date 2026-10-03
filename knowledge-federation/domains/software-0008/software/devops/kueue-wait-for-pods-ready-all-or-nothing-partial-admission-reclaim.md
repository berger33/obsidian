---
id: software.devops.tranche16.001597
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

# Kubernetes Kueue: `waitForPodsReady` (*all-or-nothing*), admissão parcial e reclamação dinâmica de cota

## Em uma frase
O Kueue oferece três mecanismos para otimizar o uso de cota durante o ciclo de vida dos Pods: `waitForPodsReady` (timeout *all-or-nothing* até que todos os Pods estejam `Ready`), *Partial Admission* (redução elástica de paralelismo para caber na cota livre) e *Dynamic Reclaim* (devolução progressiva de cota conforme Pods individuais concluem).

## Por que importa
Se um Job admitido tiver um Pod travado em `ImagePullBackOff` ou aguardando volume quebrado, ele reteria toda a cota da fila sem progredir; e em um Job paralelo de 100 tarefas independentes, esperar os últimos 2 Pods terminarem mantendo a cota de 100 Pods bloqueada desperdiça capacidade.

## Como funciona
Com `waitForPodsReady` configurado no Kueue, se todos os Pods de um `Workload` admitido não atingirem `Ready` dentro do `timeout`, o workload é suspenso/evictado e re-enfileirado para desbloquear a fila. Já para Jobs elásticos com `kueue.x-k8s.io/max-exec-time` ou admissão parcial habilitada, o Kueue ajusta `spec.parallelism` para caber na cota disponível e reduz o consumo de cota em tempo real à medida que os Pods terminam com `Succeeded`.

## Exemplo
```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: elastic-sweep-job
  labels:
    kueue.x-k8s.io/queue-name: user-queue
  annotations:
    kueue.x-k8s.io/podset-preferred-topology: "kubernetes.io/hostname"
spec:
  parallelism: 10
  completions: 10
  suspend: true
  template:
    spec:
      restartPolicy: Never
      containers:
        - name: worker
          image: ghcr.io/org/sweep:v1.0
```

## Limites e trade-offs
Para que a admissão parcial (*Partial Admission*) redimensione um `batch/v1 Job`, o Job deve habilitar a anotação ou configuração de paralelismo mutável suportada pelo controlador do Kueue.

## Como verificar
Monitore `kubectl get clusterqueue -o wide` durante a execução de um Job com múltiplas completions para observar a liberação incremental de recursos reservados.

## Conexões
- [[kueue-admission-checks-provisioning-request-cluster-autoscaler]] — Veja também: Kubernetes Kueue: `AdmissionChecks` e integração com `ProvisioningRequest` do Cluster Autoscaler.
- [[kueue-topology-aware-scheduling-tas-hierarquia-racks-blocos]] — Veja também: Kubernetes Kueue: *Topology-Aware Scheduling* (`TAS`) com CRD `Topology` para comunicação Pod-a-Pod.

## Fontes
- [Kubernetes Kueue GitHub — README.md (Job Queueing, Resource Flavor Fungibility, Fair Sharing, AdmissionChecks, TAS, MultiKueue & v1beta2 Readiness)](https://raw.githubusercontent.com/kubernetes-sigs/kueue/main/README.md) — README oficial do kubernetes-sigs/kueue detalhando recursos de fila, admissão parcial, ProvisioningRequest, MultiKueue e integrações com JobSet/Ray/Kubeflow; consultado em 2026-10-03.
- [Kubernetes Kueue Official Documentation — Core Concepts (ResourceFlavor, ClusterQueue, LocalQueue, Workload, Cohort, Preemption & DRA)](https://kueue.sigs.k8s.io/docs/concepts/) — Documentação oficial de conceitos do Kueue explicando Quota Reservation, Admission, WorkloadPriorityClass, Topology-Aware Scheduling e Dynamic Resource Allocation; consultado em 2026-10-03.
- [Kubernetes Kueue — Official GitHub Repository](https://github.com/kubernetes-sigs/kueue) — Repositório oficial Apache-2.0 do Kubernetes SIG-Scheduling Kueue; consultado em 2026-10-03.
