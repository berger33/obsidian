---
id: software.devops.tranche13.001207
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

# Node Problem Detector: Exporters (Kubernetes Exporter, Prometheus Exporter e Stackdriver)

## Em uma frase
A camada de saída do Node Problem Detector é composta por Exporters independentes — **Kubernetes exporter** (atualiza `NodeCondition` e emite `Event` no API server), **Prometheus exporter** (expõe métricas HTTP locais de problemas e estatísticas) e **Stackdriver exporter** (envia telemetria para a API do Google Cloud Monitoring).

## Por que importa
Em clusters grandes com milhares de nós, emitir um objeto `Event` na API do Kubernetes para cada ocorrência repetida de aviso de kernel pode sobrecarregar o `etcd` e o `kube-apiserver`, tornando essencial exportar contadores agregados via Prometheus.

## Como funciona
O Kubernetes exporter controla a taxa de atualização contra o API server (com suporte a QPS/burst e heartbeat), enquanto o Prometheus exporter expõe nativamente métricas como `problem_counter` (total acumulado de ocorrências de cada `reason`, como `OOMKilling` ou `Ext4Error`) e `problem_gauge` (estado atual `0` ou `1` das condições permanentes) sem pressionar o `etcd`.

## Exemplo
```bash
# Verificar contadores de problemas por motivo (reason) no endpoint Prometheus do NPD:
curl -s http://127.0.0.1:20257/metrics | grep -E "problem_counter|problem_gauge"
```

## Limites e trade-offs
Depender exclusivamente de objetos `Event` do Kubernetes (que expiram e são removidos do `etcd` após o TTL padrão de 1 hora) para auditoria histórica de `OOMKilling` ou `IOError` faz perder a visibilidade de longo prazo.

## Como verificar
Configure um `PodMonitor` ou `ServiceMonitor` para coletar `problem_counter` e `problem_gauge` do Prometheus exporter do NPD e crie alertas baseados em `rate(problem_counter[5m])`.

## Conexões
- [[npd-system-stats-monitor-metricas-disco-cpu-memoria-host]] — Veja também: Node Problem Detector: SystemStatsMonitor para Coleta de Estatísticas de Saúde do Host como Métricas.
- [[npd-systemd-monitor-frequent-restarts-kubelet-containerd-docker]] — Veja também: Node Problem Detector: Detecção de Reinícios Frequentes (FrequentKubeletRestart e FrequentContainerdRestart).

## Fontes
- [Kubernetes Node Problem Detector GitHub — README.md (Problem Daemons, System Log Monitor, Custom Plugin Monitor & Exporters)](https://raw.githubusercontent.com/kubernetes/node-problem-detector/master/README.md) — README oficial do kubernetes/node-problem-detector detalhando Problem Daemons (SystemLogMonitor, SystemStatsMonitor, CustomPluginMonitor, HealthChecker), Exporters (Kubernetes, Prometheus, Stackdriver) e flags de CLI; consultado em 2026-10-03.
- [Node Problem Detector Official Config — config/kernel-monitor.json (KernelOops, OOMKilled, Ext4Error & TaskHung Rules)](https://raw.githubusercontent.com/kubernetes/node-problem-detector/master/config/kernel-monitor.json) — Arquivo oficial de regras do kernel-monitor.json do Node Problem Detector definindo condições permanentes e eventos temporários a partir do kmsg; consultado em 2026-10-03.
- [Kubernetes Node Problem Detector — Official GitHub Repository](https://github.com/kubernetes/node-problem-detector) — Repositório oficial do Node Problem Detector no projeto Kubernetes; consultado em 2026-10-03.
