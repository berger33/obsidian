---
id: software.devops.tranche20.001986
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

# Keptn Metrics Operator: unificação de `Prometheus`, `Thanos`, `Cortex`, `Dynatrace`, `Datadog` e `Elastic` via `KeptnMetricsProvider` e `KeptnMetric`

## Em uma frase
O **Keptn Metrics Operator** padroniza o acesso a dados de observabilidade de múltiplos provedores e múltiplas instâncias no mesmo cluster por meio de dois CRDs (`metrics.keptn.sh/v1beta1`): **`KeptnMetricsProvider`** (que configura o endpoint e credenciais da fonte: Prometheus, Thanos, Cortex, Dynatrace, Datadog, Elastic ou AWS CloudWatch) e **`KeptnMetric`** (que define a query e o intervalo de coleta).

## Por que importa
Em empresas grandes onde métricas de infraestrutura estão no Prometheus local, métricas de APM estão no Datadog/Dynatrace e métricas de negócio estão no Elastic/CloudWatch, consultar cada sistema com adaptadores proprietários impede que o HPA ou o Argo Rollouts tomem decisões unificadas.

## Como funciona
Uma vez criado um `KeptnMetric`, o Metrics Operator consulta o `KeptnMetricsProvider` periodicamente (`fetchIntervalSeconds`) e expõe o valor atualizado tanto no `status.value` do próprio CRD quanto através da **Kubernetes Custom Metrics API** (`custom.metrics.k8s.io`), permitindo que o **HorizontalPodAutoscaler (HPA)**, **KEDA**, **Argo Rollouts** ou **Flux** consumam qualquer métrica como um recurso nativo do Kubernetes!

## Exemplo
```yaml
apiVersion: metrics.keptn.sh/v1beta1
kind: KeptnMetricsProvider
metadata:
  name: cluster-prometheus
  namespace: prod
spec:
  type: prometheus
  targetServer: "http://prometheus-k8s.monitoring.svc.cluster.local:9090"
---
apiVersion: metrics.keptn.sh/v1beta1
kind: KeptnMetric
metadata:
  name: checkout-p95-latency-ms
  namespace: prod
spec:
  provider:
    name: cluster-prometheus
  query: 'histogram_quantile(0.95, sum(rate(http_request_duration_ms_bucket{service="checkout"}[5m])) by (le))'
  fetchIntervalSeconds: 15
```

## Limites e trade-offs
Armazene tokens de API de provedores externos (como Datadog ou Dynatrace) em um `Secret` do Kubernetes e referencie-o em `spec.secretKeyRef` do `KeptnMetricsProvider`.

## Como verificar
Execute `kubectl get keptnmetrics -n prod` para visualizar na saída padrão o valor numérico atual coletado pela query.

## Conexões
- [[keptn-evaluation-definition-slo-validation-pre-post-deployment]] — Veja também: Keptn `KeptnEvaluationDefinition`: validação declarativa de SLOs e saúde de aplicação antes e depois do deploy.
- [[keptn-observabilidade-opentelemetry-traces-deployments-dora-metrics]] — Veja também: Keptn Observabilidade de Deployments: geração nativa de Traces OpenTelemetry de releases e Métricas DORA.

## Fontes
- [Keptn Lifecycle Toolkit GitHub — README.md (Cloud-Native Application Lifecycle Orchestration, Metrics, OpenTelemetry Observability & Helm Install)](https://keptn.sh/stable/docs/core-concepts/) — README oficial do keptn/lifecycle-toolkit descrevendo os três pilares (Metrics, Observability, Release Lifecycle Management), instalação Helm e matriz de componentes; consultado em 2026-10-03.
- [Keptn Official Documentation — Core Concepts (KeptnApp, KeptnWorkload, Pre/Post Deployment Tasks & Evaluations, Multi-Source Metrics & OpenTelemetry)](https://raw.githubusercontent.com/keptn/lifecycle-toolkit/main/README.md) — Documentação oficial de conceitos centrais do Keptn explicando o fluxo de pré/pós-deploy, execução paralela/sequencial de KeptnTask, SLOs e Custom Metrics API para HPA; consultado em 2026-10-03.
- [Keptn Lifecycle Toolkit — Official GitHub Repository](https://github.com/keptn/lifecycle-toolkit) — Repositório oficial Apache-2.0 do Keptn na CNCF; consultado em 2026-10-03.
