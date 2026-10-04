---
id: software.devops.tranche07.000680
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

# Kubernetes Descheduler: filtragem granular por namespaces, seletores de labels, prioridade e PodDisruptionBudgets

## Em uma frase
O Descheduler permite restringir o escopo de avaliação e evicção usando `namespaceLabelSelector`, `labelSelector`, `priorityThreshold`, anotações `prefer-no-eviction` e respeito nativo a `PodDisruptionBudgets` (PDBs).

## Por que importa
Em um cluster Kubernetes corporativo, nem todos os workloads devem ser submetidos às mesmas regras de rebalanceamento: jobs de treinamento de machine learning ou bancos de dados transacionais não devem ser interrompidos por uma otimização de `LowNodeUtilization`, enquanto microsserviços stateless HTTP podem ser movidos livremente desde que seus `PodDisruptionBudgets` sejam respeitados. O README oficial do Descheduler documenta os múltiplos filtros de escopo e proteção.

## Como funciona
Como a remoção de pods pelo Descheduler utiliza a sub-recurso oficial `Eviction` da API do Kubernetes, o `kube-apiserver` valida automaticamente qualquer `PodDisruptionBudget` (PDB) associado ao pod, rejeitando o despejo caso o orçamento de disrupção esteja esgotado (e o `DefaultEvictor` permite ainda proteger pods sem PDB via `podProtections.extraEnabled: ["PodsWithoutPDB"]`). Adicionalmente, tanto no `DefaultEvictor` quanto em plugins individuais, o administrador pode configurar `namespaceLabelSelector` e `labelSelector` para incluir apenas namespaces/pods específicos, definir `priorityThreshold` para nunca despejar pods acima de determinada `PriorityClass`, e usar `noEvictionPolicy: "Mandatory"` ou `"Preferred"` para pods marcados com a anotação `descheduler.alpha.kubernetes.io/prefer-no-eviction`.

## Exemplo
```yaml
# Filtragem por labels de pod, prioridade máxima e política obrigatória para a anotação prefer-no-eviction
  - name: "DefaultEvictor"
    args:
      nodeFit: true
      noEvictionPolicy: "Mandatory"
      priorityThreshold:
        value: 10000
      labelSelector:
        matchExpressions:
          - key: "tier"
            operator: In
            values: ["stateless-web", "worker"]
```

## Limites e trade-offs
Se um `PodDisruptionBudget` estiver mal configurado no cluster com `maxUnavailable: 0` ou `minAvailable: 100%`, a API de Eviction do Kubernetes bloqueará permanentemente todas as tentativas de despejo daquele Deployment pelo Descheduler (e também bloqueará drenagens de nós via `kubectl drain`), gerando eventos de falha de evicção se `evictionFailureEventNotification: true` estiver habilitado.

## Como verificar
Adicione a anotação `descheduler.alpha.kubernetes.io/prefer-no-eviction: ""` a um pod elegível para despejo com `noEvictionPolicy: "Mandatory"` e confirme nos logs do Descheduler que o pod foi preservado no nó.

## Conexões
- [[descheduler-implantacao-job-cronjob-deployment-helm-kustomize]] — Veja também: Kubernetes Descheduler: modos de implantação (Job, CronJob, Deployment) via Helm, Kustomize e alinhamento de versão.
- [[descheduler-rebalanceamento-pods-kubernetes-kube-scheduler]] — Referência cruzada direta com descheduler-rebalanceamento-pods-kubernetes-kube-scheduler.
- [[descheduler-default-evictor-pod-protections-filtros]] — Referência cruzada direta com descheduler-default-evictor-pod-protections-filtros.
- [[descheduler-pontos-extensao-deschedule-balance-perfis]] — Referência cruzada direta com descheduler-pontos-extensao-deschedule-balance-perfis.

## Fontes
- [Kubernetes Descheduler GitHub — README.md (DeschedulerPolicy, DefaultEvictor & Strategy Plugins)](https://raw.githubusercontent.com/kubernetes-sigs/descheduler/master/README.md) — README oficial do Kubernetes Descheduler detalhando configurações top-level, DefaultEvictor com podProtections e plugins dos pontos de extensão Deschedule e Balance; consultado em 2026-10-03.
- [Kubernetes Descheduler Official Helm Chart — README.md](https://github.com/kubernetes-sigs/descheduler/blob/master/charts/descheduler/README.md) — Documentação oficial do Helm chart do Kubernetes Descheduler para implantação como CronJob, Job ou Deployment no kube-system; consultado em 2026-10-03.
- [Kubernetes Descheduler — Official GitHub Repository](https://github.com/kubernetes-sigs/descheduler) — Repositório oficial do projeto kubernetes-sigs/descheduler; consultado em 2026-10-03.
