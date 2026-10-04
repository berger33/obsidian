---
id: software.devops.tranche13.001205
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

# Node Problem Detector: CustomPluginMonitor para Scripts Customizados (NTP, Rede, Disco e GPUs)

## Em uma frase
O `CustomPluginMonitor` (`--config.custom-plugin-monitor`) permite estender o Node Problem Detector com scripts executáveis definidos pelo usuário (em Bash, Python ou binários Go) para verificar problemas específicos da infraestrutura, como dessincronização de NTP (`NTPProblem`), falhas de placas GPU/InfiniBand ou degradação de montagem NFS/Lustre.

## Por que importa
Clusters bare-metal ou de treinamento de IA/ML possuem requisitos de saúde de hardware (como verificação de erros Xid em GPUs NVIDIA, cabos RDMA ou daemons de sincronização de relógio `chronyd`/`ntpd`) que não são cobertos pelos logs padrão do kernel.

## Como funciona
No arquivo JSON do `CustomPluginMonitor`, define-se o `timeout` global, o intervalo de execução e a lista de `rules`, onde cada regra aponta para o `path` de um script local. O NPD interpreta o código de saída do script (`0` para OK, `1` para problema detectado, outros códigos para erro desconhecido) e utiliza a primeira linha do `stdout` como mensagem da `NodeCondition` ou do `Event`.

## Exemplo
```json
{
  "plugin": "custom",
  "pluginConfig": {
    "invoke_interval": "30s",
    "timeout": "5s"
  },
  "source": "ntp-custom-plugin",
  "conditions": [
    {
      "type": "NTPProblem",
      "reason": "NTPIsUp",
      "message": "ntp service is up"
    }
  ]
}
```

## Limites e trade-offs
Escrever um script de `CustomPluginMonitor` que faz chamadas de rede sem timeout ou demora mais que o `timeout` configurado no `pluginConfig` faz o NPD matar o processo filho e registrar falha de execução.

## Como verificar
Garanta que todo script customizado seja leve, termine em poucos segundos e retorne estritamente `0` (saudável) ou `1` (problema confirmado) com uma mensagem concisa em `stdout`.

## Conexões
- [[npd-healthchecker-kubelet-containerd-docker-unhealthy]] — Veja também: Node Problem Detector: HealthChecker para Saúde do Kubelet e Container Runtime (containerd e Docker).
- [[npd-system-stats-monitor-metricas-disco-cpu-memoria-host]] — Veja também: Node Problem Detector: SystemStatsMonitor para Coleta de Estatísticas de Saúde do Host como Métricas.

## Fontes
- [Kubernetes Node Problem Detector GitHub — README.md (Problem Daemons, System Log Monitor, Custom Plugin Monitor & Exporters)](https://raw.githubusercontent.com/kubernetes/node-problem-detector/master/README.md) — README oficial do kubernetes/node-problem-detector detalhando Problem Daemons (SystemLogMonitor, SystemStatsMonitor, CustomPluginMonitor, HealthChecker), Exporters (Kubernetes, Prometheus, Stackdriver) e flags de CLI; consultado em 2026-10-03.
- [Node Problem Detector Official Config — config/kernel-monitor.json (KernelOops, OOMKilled, Ext4Error & TaskHung Rules)](https://raw.githubusercontent.com/kubernetes/node-problem-detector/master/config/kernel-monitor.json) — Arquivo oficial de regras do kernel-monitor.json do Node Problem Detector definindo condições permanentes e eventos temporários a partir do kmsg; consultado em 2026-10-03.
- [Kubernetes Node Problem Detector — Official GitHub Repository](https://github.com/kubernetes/node-problem-detector) — Repositório oficial do Node Problem Detector no projeto Kubernetes; consultado em 2026-10-03.
