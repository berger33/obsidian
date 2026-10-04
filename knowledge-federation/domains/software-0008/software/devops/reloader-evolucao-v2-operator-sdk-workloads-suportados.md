---
id: software.devops.tranche11.001038
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-11.md"
fontes: ["https://raw.githubusercontent.com/stakater/Reloader/master/README.md", "https://docs.stakater.com/reloader/latest/", "https://github.com/stakater/Reloader"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Arquitetura do Reloader v2 (Operator SDK) e matriz de workloads suportados (Deployment, StatefulSet, DaemonSet, CronJob, Job e DeploymentConfig)

## Em uma frase
O Reloader v2 foi reconstruído sobre o **Operator SDK** (`controller-runtime`) como evolução da branch `v1` (congelada para novas funcionalidades) e suporta `Deployment`, `StatefulSet`, `DaemonSet`, `Argo Rollout`, `CronJob`, `Job` e `DeploymentConfig` (auto-detectado no OpenShift).

## Por que importa
Compreender a transição arquitetural entre o Reloader v1 (branch `master`, que recebe apenas correções críticas e de segurança) e o Reloader v2 (branch `v2`, onde ocorre todo o novo desenvolvimento sobre o Operator SDK), bem como quais tipos de controladores de workload são suportados, evita abrir issues/PRs na branch errada ou tentar usar anotações em recursos não suportados.

## Como funciona
Conforme documentam o README oficial e a tabela *Supported workloads* (`docs.stakater.com/reloader/latest/`): (1) `Deployment`, `StatefulSet` e `DaemonSet` possuem suporte completo nativo; (2) `Argo Rollout` é suportado mediante `reloader.isArgoRollouts: true`; (3) `CronJob` e `Job` são suportados para disparar execuções quando configurações mudam; e (4) `DeploymentConfig` é suportado exclusivamente no Red Hat OpenShift e detectado automaticamente pelo controlador. Na arquitetura v2 baseada no Operator SDK, o gerenciamento de informers, caches, reconciliação e leader election segue o padrão moderno do ecossistema Kubernetes.

## Exemplo
```yaml
# Exemplo de StatefulSet e DaemonSet anotados para receber rolling updates automáticos do Reloader
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: cache-cluster
  annotations:
    configmap.reloader.stakater.com/reload: "cache-tuning-config"
---
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: log-collector
  annotations:
    secret.reloader.stakater.com/reload: "log-sink-credentials"
```

## Limites e trade-offs
Para `StatefulSets` e `DaemonSets`, o Reloader delega o reinício à estratégia de atualização configurada no próprio recurso (`updateStrategy.type`); se um `StatefulSet` estiver configurado com `updateStrategy.type: OnDelete` em vez de `RollingUpdate`, o patch do Reloader atualizará o template do pod, mas o Kubernetes não recriará os pods automaticamente até que sejam deletados.

## Como verificar
Confira `kubectl get statefulset cache-cluster -o jsonpath='{.spec.updateStrategy.type}'` (confirmando `RollingUpdate`) antes de habilitar o Reloader sobre o StatefulSet.

## Conexões
- [[reloader-escopo-namespaces-rbac-alta-disponibilidade-metricas]] — Veja também: Operação do Reloader em produção: escopo de namespaces, ignorar tipos de recursos, eleição de líder HA e métricas Prometheus.
- [[reloader-mecanismo-deteccao-dados-sha1-patch-pod-template]] — Veja também: Mecânica interna do Reloader: comparação de dados reais (SHA1) versus metadados e estratégias de patch no Pod Template.
- [[reloader-controlador-kubernetes-rollout-configmaps-secrets]] — Referência cruzada direta com reloader-controlador-kubernetes-rollout-configmaps-secrets.
- [[reloader-integracao-gitops-argocd-argo-rollouts-estrategias]] — Referência cruzada direta com reloader-integracao-gitops-argocd-argo-rollouts-estrategias.

## Fontes
- [Stakater Reloader GitHub — README.md (Reloader v2 Operator SDK, Annotations, Search/Match, Argo Rollouts, Pause & CSI Support)](https://raw.githubusercontent.com/stakater/Reloader/master/README.md) — README oficial do stakater/Reloader detalhando anotações auto/named/search+match/ignore, estratégia restart para Argo Rollouts, alertas webhook, pause-period e integração com Secrets Store CSI Driver; consultado em 2026-10-03.
- [Stakater Reloader Official Documentation — Overview & Mechanics (Watch API, SHA1 Data Check, Workloads & GitOps)](https://docs.stakater.com/reloader/latest/) — Documentação oficial do Reloader explicando a detecção de mudança de dados reais via watch API, patch SHA1 no pod template, workloads suportados e integração com ESO, Sealed Secrets, cert-manager e Argo CD; consultado em 2026-10-03.
- [Stakater Reloader — Official GitHub Repository](https://github.com/stakater/Reloader) — Repositório oficial Apache-2.0 do Stakater Reloader; consultado em 2026-10-03.
