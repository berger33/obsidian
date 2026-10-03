---
id: software.devops.tranche07.000679
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

# Kubernetes Descheduler: modos de implantação (Job, CronJob, Deployment) via Helm, Kustomize e alinhamento de versão

## Em uma frase
O Descheduler pode ser implantado no namespace `kube-system` como `Job`, `CronJob` ou `Deployment` (via manifestos base, Kustomize ou Helm chart oficial a partir da v0.18.0), exigindo alinhamento entre a versão da imagem `registry.k8s.io/descheduler/descheduler` e a versão da documentação/cluster.

## Por que importa
Diferentes equipes de plataforma operam o rebalanceamento do cluster em cadências distintas: algumas preferem rodar uma tarefa agendada apenas na janela de madrugada (`CronJob`), outras disparam manualmente após uma manutenção de nós (`Job`), e outras mantêm um loop contínuo com intervalo fixo (`Deployment`). Segundo o README oficial do Descheduler, todos os três formatos são suportados nativamente e empacotados no Helm chart oficial no Artifact Hub.

## Como funciona
Os manifestos oficiais instalam três componentes base no `kube-system`: `rbac.yaml` (ServiceAccount e ClusterRole/ClusterRoleBinding com permissões para listar nós/pods e criar `pods/eviction`), `configmap.yaml` (contendo a `DeschedulerPolicy`) e o manifesto de workload (`job.yaml`, `cronjob.yaml` ou `deployment.yaml`). O pod do Descheduler é configurado como um pod crítico no `kube-system` para não ser despejado por si mesmo nem pelo kubelet. Além disso, o README destaca o mapeamento estrito de versões: cada série `v0.XX.x` do Descheduler (por exemplo, `v0.36.0`, `v0.35.x`, `v0.34.x`) corresponde à branch `release-1.XX` do Kubernetes, devendo-se seguir a sintaxe da `DeschedulerPolicy` da respectiva branch de release.

## Exemplo
```bash
# Implantação manual como CronJob aplicando os manifestos de RBAC, ConfigMap e CronJob
kubectl create -f kubernetes/base/rbac.yaml
kubectl create -f kubernetes/base/configmap.yaml
kubectl create -f kubernetes/cronjob/cronjob.yaml
```

## Limites e trade-offs
Ao atualizar a imagem `registry.k8s.io/descheduler/descheduler` entre versões menores (por exemplo, de `v0.30.x` para `v0.35.x`), campos depreciados da `DeschedulerPolicy` (como flags booleanas antigas do `DefaultEvictor` substituídas por `podProtections` ou mudanças de versão da API de política) podem impedir o binário de iniciar se o `ConfigMap` não for atualizado conforme a tabela de releases do README.

## Como verificar
Confirme a versão da imagem em execução com `kubectl get deploy,cronjob -n kube-system -o wide` e valide que a sintaxe da `DeschedulerPolicy` no `ConfigMap` corresponde exatamente à branch de release da imagem.

## Conexões
- [[descheduler-pod-lifetime-restarts-failed-pods-higiene]] — Veja também: Kubernetes Descheduler: higiene operacional de pods com PodLifeTime, RemovePodsHavingTooManyRestarts e RemoveFailedPods.
- [[descheduler-filtragem-labels-namespaces-prioridade-pdb]] — Veja também: Kubernetes Descheduler: filtragem granular por namespaces, seletores de labels, prioridade e PodDisruptionBudgets.
- [[descheduler-rebalanceamento-pods-kubernetes-kube-scheduler]] — Referência cruzada direta com descheduler-rebalanceamento-pods-kubernetes-kube-scheduler.
- [[descheduler-politica-top-level-limites-eviccao-provedores-metricas]] — Referência cruzada direta com descheduler-politica-top-level-limites-eviccao-provedores-metricas.

## Fontes
- [Kubernetes Descheduler GitHub — README.md (DeschedulerPolicy, DefaultEvictor & Strategy Plugins)](https://raw.githubusercontent.com/kubernetes-sigs/descheduler/master/README.md) — README oficial do Kubernetes Descheduler detalhando configurações top-level, DefaultEvictor com podProtections e plugins dos pontos de extensão Deschedule e Balance; consultado em 2026-10-03.
- [Kubernetes Descheduler Official Helm Chart — README.md](https://github.com/kubernetes-sigs/descheduler/blob/master/charts/descheduler/README.md) — Documentação oficial do Helm chart do Kubernetes Descheduler para implantação como CronJob, Job ou Deployment no kube-system; consultado em 2026-10-03.
- [Kubernetes Descheduler — Official GitHub Repository](https://github.com/kubernetes-sigs/descheduler) — Repositório oficial do projeto kubernetes-sigs/descheduler; consultado em 2026-10-03.
