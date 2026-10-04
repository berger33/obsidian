---
id: software.devops.tranche13.001203
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
fontes: ["https://raw.githubusercontent.com/kubernetes/node-problem-detector/master/config/kernel-monitor.json", "https://raw.githubusercontent.com/kubernetes/node-problem-detector/master/README.md", "https://github.com/kubernetes/node-problem-detector"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Node Problem Detector: Regras do kernel-monitor.json (KernelDeadlock, XfsShutdown, CperHardwareError e OOMKilling)

## Em uma frase
A configuração oficial `config/kernel-monitor.json` do NPD lê `/dev/kmsg` com o plugin `kmsg` para monitorar três condições permanentes (`KernelDeadlock`, `XfsShutdown` e `CperHardwareErrorFatal`) e dezenas de eventos temporários de kernel (`OOMKilling`, `TaskHung`, `UnregisterNetDevice`, `KernelOops`, `Ext4Error`, `IOError` e `MemoryReadError`).

## Por que importa
Quando o OOM Killer do kernel Linux mata um processo dentro de um container ou no host, ou quando o firmware UEFI reporta erros de hardware CPER (`Corrected`, `Recoverable` ou `Fatal`), o SRE precisa distinguir imediatamente uma falha recuperável de memória ECC de um erro fatal de barramento/CPU.

## Como funciona
O `kernel-monitor.json` declara o estado saudável inicial de cada condição no array `conditions` (`KernelHasNoDeadlock`, `XfsHasNotShutDown`, `CperHardwareHasNoFatalError`) e transiciona a condição para `True` quando uma regra `type: "permanent"` casa no `/dev/kmsg`, enquanto regras `type: "temporary"` geram eventos Kubernetes e incrementam contadores de métricas (`metricsReporting: true`).

## Exemplo
```json
{
  "plugin": "kmsg",
  "logPath": "/dev/kmsg",
  "lookback": "5m",
  "source": "kernel-monitor",
  "conditions": [
    {
      "type": "KernelDeadlock",
      "reason": "KernelHasNoDeadlock",
      "message": "kernel has no deadlock"
    }
  ]
}
```

## Limites e trade-offs
Executar o container do NPD sem montar `/dev/kmsg` do host (ou sem privilégio de leitura sobre o dispositivo de caracteres do kernel) impede o plugin `kmsg` de capturar eventos de `OOMKilling` e erros de disco.

## Como verificar
Confirme que `/dev/kmsg` está montado em modo leitura no Pod do NPD e verifique os eventos emitidos com `source: kernel-monitor`.

## Conexões
- [[npd-system-log-monitor-kmsg-filelog-journald-regras-regex]] — Veja também: Node Problem Detector: SystemLogMonitor para kmsg, filelog, abrt e systemd.
- [[npd-healthchecker-kubelet-containerd-docker-unhealthy]] — Veja também: Node Problem Detector: HealthChecker para Saúde do Kubelet e Container Runtime (containerd e Docker).

## Fontes
- [Kubernetes Node Problem Detector GitHub — README.md (Problem Daemons, System Log Monitor, Custom Plugin Monitor & Exporters)](https://raw.githubusercontent.com/kubernetes/node-problem-detector/master/config/kernel-monitor.json) — README oficial do kubernetes/node-problem-detector detalhando Problem Daemons (SystemLogMonitor, SystemStatsMonitor, CustomPluginMonitor, HealthChecker), Exporters (Kubernetes, Prometheus, Stackdriver) e flags de CLI; consultado em 2026-10-03.
- [Node Problem Detector Official Config — config/kernel-monitor.json (KernelOops, OOMKilled, Ext4Error & TaskHung Rules)](https://raw.githubusercontent.com/kubernetes/node-problem-detector/master/README.md) — Arquivo oficial de regras do kernel-monitor.json do Node Problem Detector definindo condições permanentes e eventos temporários a partir do kmsg; consultado em 2026-10-03.
- [Kubernetes Node Problem Detector — Official GitHub Repository](https://github.com/kubernetes/node-problem-detector) — Repositório oficial do Node Problem Detector no projeto Kubernetes; consultado em 2026-10-03.
