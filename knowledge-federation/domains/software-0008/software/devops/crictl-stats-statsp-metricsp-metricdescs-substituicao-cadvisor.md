---
id: software.devops.tranche14.001396
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-14.md"
fontes: ["https://raw.githubusercontent.com/kubernetes-sigs/cri-tools/master/docs/crictl.md", "https://raw.githubusercontent.com/kubernetes-sigs/cri-tools/master/README.md", "https://github.com/kubernetes-sigs/cri-tools"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# crictl: Métricas e Estatísticas de Recursos CRI (stats, statsp, metricsp e metricdescs)

## Em uma frase
O `crictl` disponibiliza quatro subcomandos para telemetria de recursos direto da CRI: `crictl stats` (CPU, memória, disco e inodes por container), `crictl statsp` (estatísticas estruturadas por Pod que atendem ao endpoint `/stats/summary` do Kubelet), `crictl metricsp` (métricas por Pod destinadas a substituir o endpoint `/metrics/cadvisor`) e `crictl metricdescs` (descritores das métricas disponíveis).

## Por que importa
Depender apenas do `top` ou `htop` do Linux em um nó com dezenas de containers torna difícil agrupar o consumo total de memória `workingSetBytes` e CPU por Pod.

## Como funciona
Executando `crictl stats` ou `crictl statsp`, o operador visualiza instantaneamente o uso de CPU (`CPU %`), memória (`MEM`), disco (`DISK`) e inodes de cada container ou Pod no nó, podendo exportar em JSON ou YAML (`-o json`) para automação.

## Exemplo
```bash
crictl stats --all
crictl statsp
crictl metricdescs
```

## Limites e trade-offs
Comparar o valor de `RSS` de um único processo no `ps aux` com a memória reportada em `crictl stats` (`workingSetBytes` do cgroup) gera confusão porque o Kubernetes toma decisões de despejo (eviction) com base em `workingSetBytes`.

## Como verificar
Use sempre `crictl stats` e `crictl statsp` para observar exatamente os valores de memória e disco que o `kubelet` utiliza para decisões de eviction.

## Conexões
- [[crictl-images-pull-rmi-inspecti-imagefsinfo-gestao-disco]] — Veja também: crictl: Gestão de Imagens e Diagnóstico de Disco no Nó (images, inspecti, imagefsinfo, pull e rmi).
- [[crictl-checkpoint-events-runtime-config-live-updates]] — Veja também: crictl: Checkpoint de Containers (checkpoint), Stream de Eventos (events) e Runtime Config.

## Fontes
- [cri-tools Official Documentation — docs/crictl.md (CRI CLI Commands, /etc/crictl.yaml, runtime-endpoint, stats/statsp/metricsp, checkpoint & OpenTelemetry Tracing)](https://raw.githubusercontent.com/kubernetes-sigs/cri-tools/master/docs/crictl.md) — Guia oficial completo do crictl detalhando todos os subcomandos de PodSandbox, containers, imagens e métricas CRI, configuração de /etc/crictl.yaml e flags de tracing/timeout; consultado em 2026-10-03.
- [kubernetes-sigs/cri-tools GitHub — README.md (Project Scope, Kubernetes Version Compatibility Matrix, crictl & critest Installation)](https://raw.githubusercontent.com/kubernetes-sigs/cri-tools/master/README.md) — README oficial do kubernetes-sigs/cri-tools explicando o escopo do crictl e do critest e a matriz de compatibilidade de versões minor com o Kubernetes; consultado em 2026-10-03.
- [Kubernetes SIG Node cri-tools — Official GitHub Repository](https://github.com/kubernetes-sigs/cri-tools) — Repositório oficial Apache-2.0 do cri-tools; consultado em 2026-10-03.
