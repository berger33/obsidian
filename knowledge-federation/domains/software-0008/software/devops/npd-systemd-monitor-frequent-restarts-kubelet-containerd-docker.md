---
id: software.devops.tranche13.001208
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

# Node Problem Detector: Detecção de Reinícios Frequentes (FrequentKubeletRestart e FrequentContainerdRestart)

## Em uma frase
Por meio do arquivo `config/systemd-monitor-counter.json`, o `SystemLogMonitor` do NPD acompanha os logs do `systemd`/`journald` para contabilizar reinicializações repetidas dos serviços críticos do nó e acionar as condições `FrequentKubeletRestart`, `FrequentContainerdRestart` e `FrequentDockerRestart`.

## Por que importa
Quando o `kubelet` ou o `containerd` entra em loop de crash e é reiniciado pelo `systemd` a cada 10 segundos, os checkups pontuais de `NodeReady` podem oscilar ou permanecer `True` entre os reinícios, mascarando a instabilidade severa do nó.

## Como funciona
O monitor `systemd-monitor-counter` observa mensagens de início/parada das units no `journald` dentro de uma janela deslizante; caso o número de reinicializações ultrapasse o limiar configurado, o NPD marca a `NodeCondition` `FrequentKubeletRestart` ou `FrequentContainerdRestart` como `True` até que o serviço estabilize.

## Exemplo
```bash
# Inspecionar se algum no do cluster apresenta condicao de reinicio frequente:
kubectl get nodes -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{range .status.conditions[?(@.status=="True")]}{.type}{" "}{end}{"\n"}{end}'
```

## Limites e trade-offs
Montar `/var/log/journal` no Pod do NPD em distribuições Linux que armazenam o journal do `systemd` apenas em memória volátil (`/run/log/journal`) impede o NPD de ler os eventos de reinicialização das units.

## Como verificar
Monte tanto `/var/log/journal` quanto `/run/log/journal` (somente leitura) no `DaemonSet` do NPD para garantir compatibilidade com qualquer configuração do `systemd-journald`.

## Conexões
- [[npd-exporters-kubernetes-prometheus-stackdriver-configuracao]] — Veja também: Node Problem Detector: Exporters (Kubernetes Exporter, Prometheus Exporter e Stackdriver).
- [[npd-hostname-override-node-name-downward-api-rbac]] — Veja também: Node Problem Detector: Identificação de Nó (--hostname-override e NODE_NAME) e RBAC de Mínimo Privilégio.

## Fontes
- [Kubernetes Node Problem Detector GitHub — README.md (Problem Daemons, System Log Monitor, Custom Plugin Monitor & Exporters)](https://raw.githubusercontent.com/kubernetes/node-problem-detector/master/README.md) — README oficial do kubernetes/node-problem-detector detalhando Problem Daemons (SystemLogMonitor, SystemStatsMonitor, CustomPluginMonitor, HealthChecker), Exporters (Kubernetes, Prometheus, Stackdriver) e flags de CLI; consultado em 2026-10-03.
- [Node Problem Detector Official Config — config/kernel-monitor.json (KernelOops, OOMKilled, Ext4Error & TaskHung Rules)](https://raw.githubusercontent.com/kubernetes/node-problem-detector/master/config/kernel-monitor.json) — Arquivo oficial de regras do kernel-monitor.json do Node Problem Detector definindo condições permanentes e eventos temporários a partir do kmsg; consultado em 2026-10-03.
- [Kubernetes Node Problem Detector — Official GitHub Repository](https://github.com/kubernetes/node-problem-detector) — Repositório oficial do Node Problem Detector no projeto Kubernetes; consultado em 2026-10-03.
