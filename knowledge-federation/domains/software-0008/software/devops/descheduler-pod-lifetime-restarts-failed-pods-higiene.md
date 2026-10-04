---
id: software.devops.tranche07.000678
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

# Kubernetes Descheduler: higiene operacional de pods com PodLifeTime, RemovePodsHavingTooManyRestarts e RemoveFailedPods

## Em uma frase
Os plugins `PodLifeTime`, `RemovePodsHavingTooManyRestarts` e `RemoveFailedPods` automatizam a higiene operacional do cluster despejando ou limpando pods antigos, pods presos em loops de reinicialização (`CrashLoopBackOff`) e pods em fase `Failed`.

## Por que importa
Em clusters de longa duração, pods em fase `Failed` (de Jobs ou execuções antigas) acumulam objetos na API do Kubernetes, pods com vazamentos lentos de recursos ou caches estagnados beneficiam-se de reciclagem periódica por idade (`PodLifeTime`), e pods sofrendo dezenas de restarts consecutivos em um nó com problema local intermitente precisam ser movidos para outro nó (`RemovePodsHavingTooManyRestarts`). O README oficial do Descheduler detalha esses três plugins do ponto de extensão `deschedule`.

## Como funciona
(1) **`PodLifeTime`** despeja pods mais antigos que `maxPodLifeTimeSeconds`, permitindo filtrar por estados/condições (como `Pending`, `Running`, `ContainerCreating`, `PodInitializing`), códigos de saída e tipos de controladores; (2) **`RemovePodsHavingTooManyRestarts`** despeja pods cuja soma de reinicializações de containers (incluindo opcionalmente initContainers via `includingInitContainers: true`) atinge ou supera `podRestartThreshold`, podendo restringir por estados de execução; e (3) **`RemoveFailedPods`** remove pods que terminaram na fase `Failed`, filtrando por razões específicas (`reasons`, como `NodeAffinity`, `Evicted`, `OutOfcpu`), códigos de saída (`exitCodes`), idade mínima (`minPodLifetimeSeconds`) e exclusão de `ownerKinds`.

## Exemplo
```yaml
# Configuração dos plugins de higiene operacional (restarts excessivos, tempo de vida e pods falhos)
    pluginConfig:
      - name: "RemovePodsHavingTooManyRestarts"
        args:
          podRestartThreshold: 50
          includingInitContainers: true
      - name: "PodLifeTime"
        args:
          maxPodLifeTimeSeconds: 604800 # 7 dias
      - name: "RemoveFailedPods"
        args:
          minPodLifetimeSeconds: 3600
          includingInitContainers: true
```

## Limites e trade-offs
Usar `RemovePodsHavingTooManyRestarts` quando um pod está em `CrashLoopBackOff` por causa de um bug de código ou variável de ambiente inválida (e não por falha do nó local) fará com que o pod seja despejado e continue falhando no novo nó; por isso, configure um `podRestartThreshold` razoável (ex.: 50 ou 100) em conjunto com `minPodAge` no `DefaultEvictor`.

## Como verificar
Verifique nos logs do Descheduler a limpeza de pods em fase `Failed` com mais de 1 hora e a reciclagem ordenada de pods que atingiram `maxPodLifeTimeSeconds` respeitando os `PodDisruptionBudgets`.

## Conexões
- [[descheduler-violacoes-affinity-anti-affinity-node-taints]] — Veja também: Kubernetes Descheduler: correção de violações de afinidade, anti-afinidade e taints de nós.
- [[descheduler-implantacao-job-cronjob-deployment-helm-kustomize]] — Veja também: Kubernetes Descheduler: modos de implantação (Job, CronJob, Deployment) via Helm, Kustomize e alinhamento de versão.
- [[descheduler-rebalanceamento-pods-kubernetes-kube-scheduler]] — Referência cruzada direta com descheduler-rebalanceamento-pods-kubernetes-kube-scheduler.
- [[descheduler-default-evictor-pod-protections-filtros]] — Referência cruzada direta com descheduler-default-evictor-pod-protections-filtros.
- [[descheduler-pontos-extensao-deschedule-balance-perfis]] — Referência cruzada direta com descheduler-pontos-extensao-deschedule-balance-perfis.

## Fontes
- [Kubernetes Descheduler GitHub — README.md (DeschedulerPolicy, DefaultEvictor & Strategy Plugins)](https://raw.githubusercontent.com/kubernetes-sigs/descheduler/master/README.md) — README oficial do Kubernetes Descheduler detalhando configurações top-level, DefaultEvictor com podProtections e plugins dos pontos de extensão Deschedule e Balance; consultado em 2026-10-03.
- [Kubernetes Descheduler Official Helm Chart — README.md](https://github.com/kubernetes-sigs/descheduler/blob/master/charts/descheduler/README.md) — Documentação oficial do Helm chart do Kubernetes Descheduler para implantação como CronJob, Job ou Deployment no kube-system; consultado em 2026-10-03.
- [Kubernetes Descheduler — Official GitHub Repository](https://github.com/kubernetes-sigs/descheduler) — Repositório oficial do projeto kubernetes-sigs/descheduler; consultado em 2026-10-03.
