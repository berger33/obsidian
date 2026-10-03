---
id: software.devops.tranche13.001210
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-13.md"
fontes: ["https://raw.githubusercontent.com/kubernetes/node-problem-detector/master/README.md", "https://raw.githubusercontent.com/kubernetes/node-problem-detector/master/config/kernel-monitor.json", "https://github.com/kubernetes/node-problem-detector"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Node Problem Detector: Integração com Sistemas de Auto-Remediação (Draino, Kured e Cluster API Node HealthCheck)

## Em uma frase
O Node Problem Detector atua como a camada de detecção para sistemas de remediação automatizada (`Remedy Systems`), como Draino, Kured, Karpenter, Cluster API `MachineHealthCheck` e o Node Auto-Repair do GKE/AKS, que observam `NodeConditions` como `KernelDeadlock=True` ou `ReadonlyFilesystem=True` para isolar, drenar, reiniciar ou substituir o nó defeituoso.

## Por que importa
Detectar que um nó entrou em `ReadonlyFilesystem` ou `XfsShutdown` sem automatizar o `cordon`, `drain` e substituição da máquina ainda exige intervenção humana manual para salvar as cargas de trabalho afetadas.

## Como funciona
Ao configurar um `MachineHealthCheck` da Cluster API (ou o controlador Draino/Karpenter) para monitorar as condições publicadas pelo NPD (`KernelDeadlock`, `ReadonlyFilesystem`, `CperHardwareErrorFatal`, `KubeletUnhealthy`), qualquer condição que permaneça `Status: True` além do timeout aciona automaticamente a evacuação dos Pods e o reprovisionamento do nó.

## Exemplo
```yaml
apiVersion: cluster.x-k8s.io/v1beta1
kind: MachineHealthCheck
metadata:
  name: worker-npd-healthcheck
  namespace: default
spec:
  clusterName: prod-cluster
  selector:
    matchLabels:
      nodepool: workers
  unhealthyConditions:
    - type: KernelDeadlock
      status: "True"
      timeout: 5m
    - type: ReadonlyFilesystem
      status: "True"
      timeout: 5m
```

## Limites e trade-offs
Acionar auto-reparo/exterminação automática de máquinas a partir de `NodeConditions` do NPD sem configurar um limite máximo de nós simultaneamente não-saudáveis (`maxUnhealthy`) pode destruir toda a frota se um bug de configuração marcar todos os nós como defeituosos ao mesmo tempo.

## Como verificar
Configure sempre `maxUnhealthy` (por exemplo, `20%`) ou um disjuntor de concorrência no sistema de remediação que consome as `NodeConditions` do NPD.

## Conexões
- [[npd-hostname-override-node-name-downward-api-rbac]] — Veja também: Node Problem Detector: Identificação de Nó (--hostname-override e NODE_NAME) e RBAC de Mínimo Privilégio.

## Fontes
- [Kubernetes Node Problem Detector GitHub — README.md (Problem Daemons, System Log Monitor, Custom Plugin Monitor & Exporters)](https://raw.githubusercontent.com/kubernetes/node-problem-detector/master/README.md) — README oficial do kubernetes/node-problem-detector detalhando Problem Daemons (SystemLogMonitor, SystemStatsMonitor, CustomPluginMonitor, HealthChecker), Exporters (Kubernetes, Prometheus, Stackdriver) e flags de CLI; consultado em 2026-10-03.
- [Node Problem Detector Official Config — config/kernel-monitor.json (KernelOops, OOMKilled, Ext4Error & TaskHung Rules)](https://raw.githubusercontent.com/kubernetes/node-problem-detector/master/config/kernel-monitor.json) — Arquivo oficial de regras do kernel-monitor.json do Node Problem Detector definindo condições permanentes e eventos temporários a partir do kmsg; consultado em 2026-10-03.
- [Kubernetes Node Problem Detector — Official GitHub Repository](https://github.com/kubernetes/node-problem-detector) — Repositório oficial do Node Problem Detector no projeto Kubernetes; consultado em 2026-10-03.
