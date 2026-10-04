---
id: software.devops.tranche13.001202
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

# Node Problem Detector: SystemLogMonitor para kmsg, filelog, abrt e systemd

## Em uma frase
O sub-daemon `SystemLogMonitor` do Node Problem Detector monitora continuamente fontes de log do sistema operacional (`/dev/kmsg`, arquivos de log texto, `abrt` e contadores do `systemd`) aplicando expressões regulares predefinidas para detectar falhas de kernel e reinícios frequentes de daemons.

## Por que importa
Erros críticos de subsistemas de armazenamento (`Buffer I/O error`, `EXT4-fs error`, `XFS Shutting down filesystem`) e travamentos de processos no kernel aparecem primeiro no buffer de mensagens do kernel (`/dev/kmsg`) muito antes de o `kubelet` perder o heartbeat.

## Como funciona
Iniciado via flag `--config.system-log-monitor` (aceitando uma lista separada por vírgulas como `config/kernel-monitor.json,config/systemd-monitor-counter.json`), o NPD instancia um monitor independente para cada arquivo JSON, lendo o histórico recente definido em `lookback` (por exemplo, `"5m"`) e avaliando cada linha contra o array `rules` (`type: "temporary"` ou `type: "permanent"`).

## Exemplo
```bash
# Inspecionar as flags de SystemLogMonitor no pod do NPD:
kubectl -n kube-system get pods -l app=node-problem-detector -o jsonpath='{.items[0].spec.containers[0].command}'
kubectl -n kube-system logs -l app=node-problem-detector --tail=40
```

## Limites e trade-offs
Definir um valor de `lookback` muito longo no `kernel-monitor.json` faz com que um Pod do NPD recém-reiniciado reemita eventos antigos de falhas que já ocorreram horas antes no nó.

## Como verificar
Mantenha `lookback: "5m"` (valor padrão oficial) nos arquivos de configuração de `SystemLogMonitor` para evitar duplicação de alertas históricos após restarts do DaemonSet.

## Conexões
- [[npd-arquitetura-daemonset-problem-api-nodecondition-event]] — Veja também: Node Problem Detector: Arquitetura DaemonSet e Problem API (NodeCondition vs Event).
- [[npd-kernel-monitor-deadlock-xfsshutdown-cper-hardware-oomkilling]] — Veja também: Node Problem Detector: Regras do kernel-monitor.json (KernelDeadlock, XfsShutdown, CperHardwareError e OOMKilling).

## Fontes
- [Kubernetes Node Problem Detector GitHub — README.md (Problem Daemons, System Log Monitor, Custom Plugin Monitor & Exporters)](https://raw.githubusercontent.com/kubernetes/node-problem-detector/master/README.md) — README oficial do kubernetes/node-problem-detector detalhando Problem Daemons (SystemLogMonitor, SystemStatsMonitor, CustomPluginMonitor, HealthChecker), Exporters (Kubernetes, Prometheus, Stackdriver) e flags de CLI; consultado em 2026-10-03.
- [Node Problem Detector Official Config — config/kernel-monitor.json (KernelOops, OOMKilled, Ext4Error & TaskHung Rules)](https://raw.githubusercontent.com/kubernetes/node-problem-detector/master/config/kernel-monitor.json) — Arquivo oficial de regras do kernel-monitor.json do Node Problem Detector definindo condições permanentes e eventos temporários a partir do kmsg; consultado em 2026-10-03.
- [Kubernetes Node Problem Detector — Official GitHub Repository](https://github.com/kubernetes/node-problem-detector) — Repositório oficial do Node Problem Detector no projeto Kubernetes; consultado em 2026-10-03.
