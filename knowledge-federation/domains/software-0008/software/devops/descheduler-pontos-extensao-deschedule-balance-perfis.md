---
id: software.devops.tranche07.000674
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-07.md"
fontes: ["https://raw.githubusercontent.com/kubernetes-sigs/descheduler/master/README.md", "https://github.com/kubernetes-sigs/descheduler/blob/master/charts/descheduler/README.md", "https://github.com/kubernetes-sigs/descheduler"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Kubernetes Descheduler: arquitetura de perfis e pontos de extensão Deschedule versus Balance

## Em uma frase
A `DeschedulerPolicy` organiza as estratégias em perfis (`profiles`) que implementam dois pontos de extensão principais além dos filtros do Evictor: `Deschedule` (avaliação sequencial pod a pod) e `Balance` (avaliação coletiva de grupos e distribuição entre nós).

## Por que importa
Algumas regras de reagendamento dependem exclusivamente do estado individual de um pod (por exemplo, se ele violou um taint de nó, teve muitos restarts ou excedeu seu tempo de vida), enquanto outras exigem olhar para o conjunto de réplicas ou para a distribuição de carga entre todos os nós do cluster (como espalhar duplicatas ou equilibrar utilização de nós). O README oficial do Descheduler separa claramente essas duas categorias nos extension points `deschedule` e `balance`.

## Como funciona
Dentro de `profiles[]`, cada perfil define sua lista `pluginConfig` (argumentos passados para cada plugin) e ativa os plugins desejados nos pontos de extensão sob `plugins`: `filter` e `preEvictionFilter` (onde o `DefaultEvictor` vem habilitado por padrão), `deschedule` e `balance`. Os **Deschedule Plugins** processam os pods um a um sequencialmente (`RemovePodsViolatingInterPodAntiAffinity`, `RemovePodsViolatingNodeAffinity`, `RemovePodsViolatingNodeTaints`, `RemovePodsHavingTooManyRestarts`, `PodLifeTime`, `RemoveFailedPods`). Já os **Balance Plugins** analisam todos os pods ou grupos de pods para decidir quais despejar com base na distribuição desejada (`RemoveDuplicates`, `LowNodeUtilization`, `HighNodeUtilization`, `RemovePodsViolatingTopologySpreadConstraint`).

## Exemplo
```yaml
# Estrutura de um perfil na DeschedulerPolicy habilitando plugins nos pontos deschedule e balance
apiVersion: "descheduler/v1alpha2"
kind: "DeschedulerPolicy"
profiles:
  - name:ProducaoRebalance
    pluginConfig:
      - name: "DefaultEvictor"
        args:
          nodeFit: true
      - name: "RemoveDuplicates"
      - name: "RemovePodsViolatingNodeTaints"
    plugins:
      deschedule:
        enabled:
          - "RemovePodsViolatingNodeTaints"
      balance:
        enabled:
          - "RemoveDuplicates"
```

## Limites e trade-offs
Ao combinar múltiplos perfis ou múltiplos plugins `deschedule` e `balance` na mesma execução, a ordem de declaração importa: os plugins são executados na sequência definida e compartilham os tetos globais de evicção (`maxNoOfPodsToEvictPerNode` / `Total`); se o primeiro plugin atingir o limite máximo de evicções do nó, os plugins subsequentes não poderão despejar mais pods naquele nó até o próximo ciclo.

## Como verificar
Verifique nos logs de execução do Descheduler a ordem de invocação de cada perfil e confirme que os plugins listados em `plugins.deschedule.enabled` e `plugins.balance.enabled` foram executados sem erros de configuração.

## Conexões
- [[descheduler-default-evictor-pod-protections-filtros]] — Veja também: Kubernetes Descheduler: plugin DefaultEvictor, políticas podProtections e filtros de nodeFit e minReplicas.
- [[descheduler-low-high-node-utilization-thresholds-balanceamento]] — Veja também: Kubernetes Descheduler: estratégias de balanceamento de recursos LowNodeUtilization e HighNodeUtilization.
- [[descheduler-rebalanceamento-pods-kubernetes-kube-scheduler]] — Referência cruzada direta com descheduler-rebalanceamento-pods-kubernetes-kube-scheduler.
- [[descheduler-remove-duplicates-topology-spread-constraints]] — Referência cruzada direta com descheduler-remove-duplicates-topology-spread-constraints.

## Fontes
- [Kubernetes Descheduler GitHub — README.md (DeschedulerPolicy, DefaultEvictor & Strategy Plugins)](https://raw.githubusercontent.com/kubernetes-sigs/descheduler/master/README.md) — README oficial do Kubernetes Descheduler detalhando configurações top-level, DefaultEvictor com podProtections e plugins dos pontos de extensão Deschedule e Balance; consultado em 2026-10-03.
- [Kubernetes Descheduler Official Helm Chart — README.md](https://github.com/kubernetes-sigs/descheduler/blob/master/charts/descheduler/README.md) — Documentação oficial do Helm chart do Kubernetes Descheduler para implantação como CronJob, Job ou Deployment no kube-system; consultado em 2026-10-03.
- [Kubernetes Descheduler — Official GitHub Repository](https://github.com/kubernetes-sigs/descheduler) — Repositório oficial do projeto kubernetes-sigs/descheduler; consultado em 2026-10-03.
