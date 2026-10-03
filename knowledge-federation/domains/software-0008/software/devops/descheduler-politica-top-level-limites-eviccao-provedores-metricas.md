---
id: software.devops.tranche07.000672
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

# Kubernetes Descheduler: configuração top-level da DeschedulerPolicy, limites de evicção e metricsProviders

## Em uma frase
A configuração de nível superior da `DeschedulerPolicy` (`descheduler/v1alpha2`) define limites globais de segurança (`maxNoOfPodsToEvictPerNode`, `maxNoOfPodsToEvictPerNamespace`, `maxNoOfPodsToEvictTotal`), `gracePeriodSeconds` e provedores de métricas (`KubernetesMetrics` e `Prometheus`).

## Por que importa
Executar um ciclo de desagendamento sem limites máximos de evicção pode despejar centenas de pods simultaneamente em um nó ou namespace durante uma mudança de topologia, causando indisponibilidade em cascata. Segundo a documentação oficial do Descheduler, as chaves top-level da política aplicam travas de segurança transversais a todas as estratégias habilitadas e configuram a coleta de utilização real de recursos.

## Como funciona
No topo do objeto `DeschedulerPolicy`, o administrador pode restringir o impacto de cada ciclo de rescheduling com `maxNoOfPodsToEvictPerNode` (máximo de pods despejados de cada nó somando todas as estratégias), `maxNoOfPodsToEvictPerNamespace` (máximo por namespace) e `maxNoOfPodsToEvictTotal` (máximo total por ciclo), além de `nodeSelector`, `evictionFailureEventNotification` e `gracePeriodSeconds`. Para estratégias que baseiam decisões no consumo real de recursos em vez de apenas `requests`, o campo `metricsProviders` (que substitui o campo depreciado `metricsCollector`) permite habilitar duas fontes: `KubernetesMetrics` (Kubernetes Metrics Server) e `Prometheus` (apontando para `prometheus.url` com autenticação via token in-cluster ou `secretReference` contendo a chave `prometheusAuthToken`).

## Exemplo
```yaml
# Configuração top-level de uma DeschedulerPolicy com limites de evicção e provedor Prometheus
apiVersion: "descheduler/v1alpha2"
kind: "DeschedulerPolicy"
maxNoOfPodsToEvictPerNode: 10
maxNoOfPodsToEvictPerNamespace: 20
maxNoOfPodsToEvictTotal: 50
gracePeriodSeconds: 60
metricsProviders:
  - source: Prometheus
    prometheus:
      url: http://prometheus-kube-prometheus-prometheus.prom.svc.cluster.local
      authToken:
        secretReference:
          namespace: "kube-system"
          name: "authtoken"
```

## Limites e trade-offs
Conforme documentado na tabela de configuração top-level do Descheduler, a configuração padrão de RBAC do Descheduler permite ler Secrets apenas no namespace `kube-system`; portanto, se `prometheus.authToken.secretReference.namespace` apontar para um Secret em outro namespace (como `monitoring`), é obrigatório estender explicitamente as regras de `ClusterRole`/`Role` do Descheduler para evitar erros de permissão.

## Como verificar
Aplique o ConfigMap contendo a `DeschedulerPolicy` e valide nos logs do Descheduler que os limites `maxNoOfPodsToEvict*` e a conexão com os `metricsProviders` foram inicializados sem avisos de depreciação ou falhas de autenticação.

## Conexões
- [[descheduler-rebalanceamento-pods-kubernetes-kube-scheduler]] — Veja também: Kubernetes Descheduler: rebalanceamento contínuo de clusters via evicção coordenada com o kube-scheduler.
- [[descheduler-default-evictor-pod-protections-filtros]] — Veja também: Kubernetes Descheduler: plugin DefaultEvictor, políticas podProtections e filtros de nodeFit e minReplicas.
- [[descheduler-low-high-node-utilization-thresholds-balanceamento]] — Referência cruzada direta com descheduler-low-high-node-utilization-thresholds-balanceamento.

## Fontes
- [Kubernetes Descheduler GitHub — README.md (DeschedulerPolicy, DefaultEvictor & Strategy Plugins)](https://raw.githubusercontent.com/kubernetes-sigs/descheduler/master/README.md) — README oficial do Kubernetes Descheduler detalhando configurações top-level, DefaultEvictor com podProtections e plugins dos pontos de extensão Deschedule e Balance; consultado em 2026-10-03.
- [Kubernetes Descheduler Official Helm Chart — README.md](https://github.com/kubernetes-sigs/descheduler/blob/master/charts/descheduler/README.md) — Documentação oficial do Helm chart do Kubernetes Descheduler para implantação como CronJob, Job ou Deployment no kube-system; consultado em 2026-10-03.
- [Kubernetes Descheduler — Official GitHub Repository](https://github.com/kubernetes-sigs/descheduler) — Repositório oficial do projeto kubernetes-sigs/descheduler; consultado em 2026-10-03.
