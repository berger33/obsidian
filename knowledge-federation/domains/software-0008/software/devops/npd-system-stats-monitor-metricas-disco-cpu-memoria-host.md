---
id: software.devops.tranche13.001206
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

# Node Problem Detector: SystemStatsMonitor para Coleta de Estatísticas de Saúde do Host como Métricas

## Em uma frase
O `SystemStatsMonitor` (`--config.system-stats-monitor`) coleta estatísticas de saúde de baixo nível do sistema operacional (como latência de I/O de disco, contadores de pacotes descartados, uso de inodes e carga de CPU/memória relacionados a falhas) e as expõe como métricas estruturadas.

## Por que importa
Eventos binários (funcionando vs. falhando) muitas vezes só disparam quando o nó já colapsou; monitorar a evolução de métricas de saturação de I/O e erros de subsistema permite identificar degradação progressiva de discos antes de um `XfsShutdown`.

## Como funciona
Ativado via `--config.system-stats-monitor=config/system-stats-monitor.json`, o sub-daemon lê periodicamente os contadores do kernel em `/proc` e `/sys` e publica as séries temporais por meio do Prometheus Exporter embutido no NPD.

## Exemplo
```bash
# Consultar as metricas Prometheus expostas pelo Node Problem Detector:
kubectl -n kube-system port-forward ds/node-problem-detector 20257:20257 &
curl -s http://127.0.0.1:20257/metrics | grep -E "^problem_"
```

## Limites e trade-offs
Coletar estatísticas com intervalo excessivamente curto (por exemplo, a cada 1 segundo) em nós com dezenas de dispositivos de bloco aumenta o consumo de CPU do próprio pod do NPD.

## Como verificar
Mantenha os intervalos padrão de coleta do `system-stats-monitor.json` e configure o scrape do Prometheus para consolidar as métricas `problem_counter` e `problem_gauge`.

## Conexões
- [[npd-custom-plugin-monitor-scripts-ntp-hardware-gpu-checks]] — Veja também: Node Problem Detector: CustomPluginMonitor para Scripts Customizados (NTP, Rede, Disco e GPUs).
- [[npd-exporters-kubernetes-prometheus-stackdriver-configuracao]] — Veja também: Node Problem Detector: Exporters (Kubernetes Exporter, Prometheus Exporter e Stackdriver).

## Fontes
- [Kubernetes Node Problem Detector GitHub — README.md (Problem Daemons, System Log Monitor, Custom Plugin Monitor & Exporters)](https://raw.githubusercontent.com/kubernetes/node-problem-detector/master/README.md) — README oficial do kubernetes/node-problem-detector detalhando Problem Daemons (SystemLogMonitor, SystemStatsMonitor, CustomPluginMonitor, HealthChecker), Exporters (Kubernetes, Prometheus, Stackdriver) e flags de CLI; consultado em 2026-10-03.
- [Node Problem Detector Official Config — config/kernel-monitor.json (KernelOops, OOMKilled, Ext4Error & TaskHung Rules)](https://raw.githubusercontent.com/kubernetes/node-problem-detector/master/config/kernel-monitor.json) — Arquivo oficial de regras do kernel-monitor.json do Node Problem Detector definindo condições permanentes e eventos temporários a partir do kmsg; consultado em 2026-10-03.
- [Kubernetes Node Problem Detector — Official GitHub Repository](https://github.com/kubernetes/node-problem-detector) — Repositório oficial do Node Problem Detector no projeto Kubernetes; consultado em 2026-10-03.
