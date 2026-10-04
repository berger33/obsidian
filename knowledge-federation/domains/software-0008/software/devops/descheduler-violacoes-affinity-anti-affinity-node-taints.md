---
id: software.devops.tranche07.000677
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

# Kubernetes Descheduler: correção de violações de afinidade, anti-afinidade e taints de nós

## Em uma frase
Os plugins `RemovePodsViolatingNodeAffinity`, `RemovePodsViolatingInterPodAntiAffinity` e `RemovePodsViolatingNodeTaints` despejam pods cujas regras originais de posicionamento deixaram de ser satisfeitas após mudanças em labels, taints ou vizinhança de pods.

## Por que importa
No Kubernetes, regras como `requiredDuringSchedulingIgnoredDuringExecution` (para `nodeAffinity` e `podAntiAffinity`) e taints com efeito `NoSchedule` ou `PreferNoSchedule` são avaliadas apenas no agendamento (`DuringScheduling`) e ignoradas durante a execução (`IgnoredDuringExecution`). Segundo o README oficial do Descheduler, quando administradores alteram labels/taints nos nós ou novos pods mudam a vizinhança, esses três plugins `deschedule` impõem o cumprimento das regras em tempo de execução.

## Como funciona
(1) **`RemovePodsViolatingNodeAffinity`** avalia pods com `nodeAffinity` do tipo `requiredDuringSchedulingIgnoredDuringExecution` (ou `preferredDuringSchedulingIgnoredDuringExecution` se configurado) e os despeja caso o nó atual não satisfaça mais os seletores de rótulos ou caso surja um nó que atenda à preferência; (2) **`RemovePodsViolatingInterPodAntiAffinity`** identifica pods que possuem regras de anti-afinidade entre pods e estão co-localizados no mesmo nó/topologia com pods conflitantes, despejando-os para separar os pares; e (3) **`RemovePodsViolatingNodeTaints`** despeja pods que estão rodando em nós que receberam taints `NoSchedule` (ou `PreferNoSchedule` quando `includePreferNoSchedule: true`) para os quais o pod não possui `tolerations` correspondentes.

## Exemplo
```yaml
# Habilitação dos plugins de correção de afinidade, anti-afinidade e taints na DeschedulerPolicy
    pluginConfig:
      - name: "RemovePodsViolatingNodeAffinity"
        args:
          nodeAffinityType:
            - "requiredDuringSchedulingIgnoredDuringExecution"
      - name: "RemovePodsViolatingInterPodAntiAffinity"
      - name: "RemovePodsViolatingNodeTaints"
        args:
          includePreferNoSchedule: true
    plugins:
      deschedule:
        enabled:
          - "RemovePodsViolatingNodeAffinity"
          - "RemovePodsViolatingInterPodAntiAffinity"
          - "RemovePodsViolatingNodeTaints"
```

## Limites e trade-offs
Ao habilitar `RemovePodsViolatingNodeTaints` ou `RemovePodsViolatingNodeAffinity`, é crucial que `nodeFit: true` esteja ativo no `DefaultEvictor`; caso contrário, se um administrador aplicar um taint `NoSchedule` ou remover um label de todos os nós do pool por engano, o Descheduler despejará os pods mesmo não havendo nenhum outro nó elegível no cluster para recebê-los.

## Como verificar
Adicione um taint `manutencao=true:NoSchedule` a um nó worker onde roda um Deployment de teste sem toleration correspondente, execute o Descheduler e confirme que o pod é despejado e reagendado em um nó sem o taint.

## Conexões
- [[descheduler-remove-duplicates-topology-spread-constraints]] — Veja também: Kubernetes Descheduler: espalhamento de réplicas com RemoveDuplicates e RemovePodsViolatingTopologySpreadConstraint.
- [[descheduler-pod-lifetime-restarts-failed-pods-higiene]] — Veja também: Kubernetes Descheduler: higiene operacional de pods com PodLifeTime, RemovePodsHavingTooManyRestarts e RemoveFailedPods.
- [[descheduler-rebalanceamento-pods-kubernetes-kube-scheduler]] — Referência cruzada direta com descheduler-rebalanceamento-pods-kubernetes-kube-scheduler.
- [[descheduler-default-evictor-pod-protections-filtros]] — Referência cruzada direta com descheduler-default-evictor-pod-protections-filtros.

## Fontes
- [Kubernetes Descheduler GitHub — README.md (DeschedulerPolicy, DefaultEvictor & Strategy Plugins)](https://raw.githubusercontent.com/kubernetes-sigs/descheduler/master/README.md) — README oficial do Kubernetes Descheduler detalhando configurações top-level, DefaultEvictor com podProtections e plugins dos pontos de extensão Deschedule e Balance; consultado em 2026-10-03.
- [Kubernetes Descheduler Official Helm Chart — README.md](https://github.com/kubernetes-sigs/descheduler/blob/master/charts/descheduler/README.md) — Documentação oficial do Helm chart do Kubernetes Descheduler para implantação como CronJob, Job ou Deployment no kube-system; consultado em 2026-10-03.
- [Kubernetes Descheduler — Official GitHub Repository](https://github.com/kubernetes-sigs/descheduler) — Repositório oficial do projeto kubernetes-sigs/descheduler; consultado em 2026-10-03.
