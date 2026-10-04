---
id: software.devops.tranche13.001204
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

# Node Problem Detector: HealthChecker para Saúde do Kubelet e Container Runtime (containerd e Docker)

## Em uma frase
O sub-daemon `HealthChecker` do Node Problem Detector verifica ativamente a saúde do `kubelet` e do runtime de containers (`containerd` ou `docker`), reportando as condições permanentes `KubeletUnhealthy` e `ContainerRuntimeUnhealthy` quando os daemons deixam de responder.

## Por que importa
Mesmo quando o kernel Linux está ativo, um travamento interno no daemon `containerd` ou no `kubelet` impede a criação e limpeza de Pods no nó; detectar exatamente qual componente travou acelera o diagnóstico e permite reparo direcionado.

## Como funciona
Configurado por arquivos como `config/health-checker-kubelet.json` e `config/health-checker-containerd.json`, o `HealthChecker` executa sondagens periódicas contra o endpoint local de saúde do `kubelet` ou invoca verificações do runtime de containers, atualizando a `NodeCondition` correspondente se o serviço permanecer irresponsivo além do limiar configurado.

## Exemplo
```bash
# Verificar condicoes de saude do kubelet e container runtime no objeto Node:
kubectl get node -o json | jq '.items[].status.conditions[] | select(.type | test("Kubelet|ContainerRuntime|Deadlock|Readonly"))'
```

## Limites e trade-offs
Habilitar simultaneamente `health-checker-docker.json` e `health-checker-containerd.json` em nós modernos que executam apenas `containerd` (sem daemon `dockerd`) gera condição falsa permanente `ContainerRuntimeUnhealthy` por ausência do Docker.

## Como verificar
Monte e habilite no NPD apenas o arquivo de `HealthChecker` correspondente ao runtime efetivamente utilizado pelos nós do cluster (`containerd`).

## Conexões
- [[npd-kernel-monitor-deadlock-xfsshutdown-cper-hardware-oomkilling]] — Veja também: Node Problem Detector: Regras do kernel-monitor.json (KernelDeadlock, XfsShutdown, CperHardwareError e OOMKilling).
- [[npd-custom-plugin-monitor-scripts-ntp-hardware-gpu-checks]] — Veja também: Node Problem Detector: CustomPluginMonitor para Scripts Customizados (NTP, Rede, Disco e GPUs).

## Fontes
- [Kubernetes Node Problem Detector GitHub — README.md (Problem Daemons, System Log Monitor, Custom Plugin Monitor & Exporters)](https://raw.githubusercontent.com/kubernetes/node-problem-detector/master/README.md) — README oficial do kubernetes/node-problem-detector detalhando Problem Daemons (SystemLogMonitor, SystemStatsMonitor, CustomPluginMonitor, HealthChecker), Exporters (Kubernetes, Prometheus, Stackdriver) e flags de CLI; consultado em 2026-10-03.
- [Node Problem Detector Official Config — config/kernel-monitor.json (KernelOops, OOMKilled, Ext4Error & TaskHung Rules)](https://raw.githubusercontent.com/kubernetes/node-problem-detector/master/config/kernel-monitor.json) — Arquivo oficial de regras do kernel-monitor.json do Node Problem Detector definindo condições permanentes e eventos temporários a partir do kmsg; consultado em 2026-10-03.
- [Kubernetes Node Problem Detector — Official GitHub Repository](https://github.com/kubernetes/node-problem-detector) — Repositório oficial do Node Problem Detector no projeto Kubernetes; consultado em 2026-10-03.
