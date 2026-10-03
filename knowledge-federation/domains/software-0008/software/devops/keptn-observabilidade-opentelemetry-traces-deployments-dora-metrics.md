---
id: software.devops.tranche20.001987
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-20.md"
fontes: ["https://keptn.sh/stable/docs/core-concepts/", "https://raw.githubusercontent.com/keptn/lifecycle-toolkit/main/README.md", "https://github.com/keptn/lifecycle-toolkit"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Keptn Observabilidade de Deployments: geração nativa de Traces OpenTelemetry de releases e Métricas DORA

## Em uma frase
O Keptn torna cada implantação no Kubernetes observável de ponta a ponta emitindo automaticamente **Traces OpenTelemetry**, **Métricas DORA** (*Deployment Frequency*, *Lead Time for Changes*, *Change Failure Rate*, *Time to Restore*), **Kubernetes Events** e **CloudEvents** para todas as fases de cada `KeptnAppVersion` e `KeptnWorkloadVersion`.

## Por que importa
Quando um deploy no Kubernetes demora 12 minutos ou falha na metade, investigar `kubectl describe` de dezenas de Pods e Jobs sem um trace distribuído unificado torna difícil saber quanto tempo foi gasto nas tarefas pré-deploy, no pull de imagem, na prontidão dos Pods ou nas avaliações pós-deploy.

## Como funciona
Configurando o recurso `KeptnConfig` apontando `otelCollectorUrl` para o seu **OpenTelemetry Collector** (Jaeger, Tempo, Grafana), o Keptn cria um trace raiz para o deploy da `KeptnApp` e spans filhos para cada `KeptnTask`, `KeptnEvaluation` e fase de rollout do `KeptnWorkload`, propagando inclusive o `traceparent` W3C para os containers das tarefas.

## Exemplo
```yaml
apiVersion: options.keptn.sh/v1alpha1
kind: KeptnConfig
metadata:
  name: keptn-config
  namespace: keptn-system
spec:
  otelCollectorUrl: "otel-collector.monitoring.svc.cluster.local:4317"
  keptnAppCreationRequestTimeoutSeconds: 30
```

## Limites e trade-offs
As métricas DORA e de ciclo de vida (`keptn_deployment_count`, `keptn_deployment_duration`, `keptn_deployment_interval`) ficam imediatamente disponíveis para visualização em dashboards padrão do **Grafana**.

## Como verificar
Aplique o `KeptnConfig` com `otelCollectorUrl` e verifique no Jaeger/Grafana Tempo a árvore completa de spans gerada durante um deploy.

## Conexões
- [[keptn-metrics-operator-keptnmetricsprovider-keptnmetric-multi-source]] — Veja também: Keptn Metrics Operator: unificação de `Prometheus`, `Thanos`, `Cortex`, `Dynatrace`, `Datadog` e `Elastic` via `KeptnMetricsProvider` e `KeptnMetric`.
- [[keptn-autoscaling-hpa-custom-metrics-api-adapter-escalonamento]] — Veja também: Keptn com HorizontalPodAutoscaler (`HPA`): escalonamento de Pods no Kubernetes baseado em `KeptnMetric` via Custom Metrics API.

## Fontes
- [Keptn Lifecycle Toolkit GitHub — README.md (Cloud-Native Application Lifecycle Orchestration, Metrics, OpenTelemetry Observability & Helm Install)](https://keptn.sh/stable/docs/core-concepts/) — README oficial do keptn/lifecycle-toolkit descrevendo os três pilares (Metrics, Observability, Release Lifecycle Management), instalação Helm e matriz de componentes; consultado em 2026-10-03.
- [Keptn Official Documentation — Core Concepts (KeptnApp, KeptnWorkload, Pre/Post Deployment Tasks & Evaluations, Multi-Source Metrics & OpenTelemetry)](https://raw.githubusercontent.com/keptn/lifecycle-toolkit/main/README.md) — Documentação oficial de conceitos centrais do Keptn explicando o fluxo de pré/pós-deploy, execução paralela/sequencial de KeptnTask, SLOs e Custom Metrics API para HPA; consultado em 2026-10-03.
- [Keptn Lifecycle Toolkit — Official GitHub Repository](https://github.com/keptn/lifecycle-toolkit) — Repositório oficial Apache-2.0 do Keptn na CNCF; consultado em 2026-10-03.
