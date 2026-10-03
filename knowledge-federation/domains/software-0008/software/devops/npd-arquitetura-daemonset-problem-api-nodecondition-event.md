---
id: software.devops.tranche13.001201
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

# Node Problem Detector: Arquitetura DaemonSet e Problem API (NodeCondition vs Event)

## Em uma frase
O `node-problem-detector` (NPD) é um daemon oficial do projeto Kubernetes (habilitado por padrão no GKE e na extensão Linux do AKS) que roda em cada nó para detectar anomalias de hardware, kernel, sistema de arquivos e container runtime, tornando-as visíveis ao `kube-apiserver` por meio de `NodeCondition` e `Event`.

## Por que importa
Sem o Node Problem Detector, problemas graves no host subjacente (como deadlock de kernel, sistema de arquivos XFS/EXT4 em modo somente leitura, falhas de memória ECC ou daemon NTP inoperante) permanecem invisíveis para o control plane, que continua agendando novos Pods no nó degradado.

## Como funciona
O NPD agrega múltiplos sub-daemons (`Problem Daemons`) executados como goroutines dentro do binário e despacha os diagnósticos pelos `Exporters` configurados. Pela Problem API do Kubernetes, anomalias permanentes que tornam o nó indisponível para Pods são reportadas como `NodeCondition` (por exemplo, `KernelDeadlock`, `ReadonlyFilesystem`, `XfsShutdown`), enquanto ocorrências transitórias informativas são emitidas como objetos `Event` (por exemplo, `OOMKilling`, `TaskHung`, `KernelOops`).

## Exemplo
```bash
kubectl get daemonset -n kube-system | grep node-problem-detector
kubectl describe node <nome-do-no> | grep -A 15 "Conditions:"
kubectl get events --field-selector source=kernel-monitor -A
```

## Limites e trade-offs
Classificar um evento transitório e frequente como `permanent` (atualizando `NodeCondition` a cada ocorrência) em vez de `temporary` pode acionar controladores de auto-remediação para drenar e recriar nós saudáveis desnecessariamente.

## Como verificar
Verifique no `kubectl describe node` se as condições customizadas (`KernelDeadlock`, `ReadonlyFilesystem`, `FrequentKubeletRestart`) aparecem com `Status: False` nos nós saudáveis.

## Conexões
- [[npd-system-log-monitor-kmsg-filelog-journald-regras-regex]] — Veja também: Node Problem Detector: SystemLogMonitor para kmsg, filelog, abrt e systemd.

## Fontes
- [Kubernetes Node Problem Detector GitHub — README.md (Problem Daemons, System Log Monitor, Custom Plugin Monitor & Exporters)](https://raw.githubusercontent.com/kubernetes/node-problem-detector/master/README.md) — README oficial do kubernetes/node-problem-detector detalhando Problem Daemons (SystemLogMonitor, SystemStatsMonitor, CustomPluginMonitor, HealthChecker), Exporters (Kubernetes, Prometheus, Stackdriver) e flags de CLI; consultado em 2026-10-03.
- [Node Problem Detector Official Config — config/kernel-monitor.json (KernelOops, OOMKilled, Ext4Error & TaskHung Rules)](https://raw.githubusercontent.com/kubernetes/node-problem-detector/master/config/kernel-monitor.json) — Arquivo oficial de regras do kernel-monitor.json do Node Problem Detector definindo condições permanentes e eventos temporários a partir do kmsg; consultado em 2026-10-03.
- [Kubernetes Node Problem Detector — Official GitHub Repository](https://github.com/kubernetes/node-problem-detector) — Repositório oficial do Node Problem Detector no projeto Kubernetes; consultado em 2026-10-03.
