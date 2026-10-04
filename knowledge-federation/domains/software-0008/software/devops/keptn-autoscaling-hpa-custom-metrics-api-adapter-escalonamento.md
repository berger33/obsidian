---
id: software.devops.tranche20.001988
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

# Keptn com HorizontalPodAutoscaler (`HPA`): escalonamento de Pods no Kubernetes baseado em `KeptnMetric` via Custom Metrics API

## Em uma frase
Graças ao adaptador integrado do Keptn para a **Kubernetes Custom Metrics API** (`custom.metrics.k8s.io/v1beta2`), qualquer métrica definida em um recurso **`KeptnMetric`** (seja vinda do Prometheus, Thanos, Datadog, Dynatrace ou Elastic) pode ser usada diretamente como métrica do tipo `Object` em um **`HorizontalPodAutoscaler` (`autoscaling/v2`)** padrão do Kubernetes.

## Por que importa
Normalmente, escalar um Deployment no HPA usando uma métrica do Datadog em um cluster e uma métrica do Thanos em outro exige instalar e manter adaptadores de métricas proprietários diferentes em cada cluster.

## Como funciona
Com o Keptn Metrics Operator instalado, o HPA referencia sempre o mesmo objeto padrão: `describedObject: { apiVersion: metrics.keptn.sh/v1beta1, kind: KeptnMetric, name: <metric-name> }`. Se você trocar o provedor de observabilidade de Prometheus para Thanos ou Datadog amanhã, basta atualizar o `KeptnMetricsProvider` sem alterar uma única linha dos manifestos de HPA!

## Exemplo
```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: checkout-hpa
  namespace: prod
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: checkout-service
  minReplicas: 2
  maxReplicas: 15
  metrics:
    - type: Object
      object:
        metric:
          name: checkout-p95-latency-ms
        describedObject:
          apiVersion: metrics.keptn.sh/v1beta1
          kind: KeptnMetric
          name: checkout-p95-latency-ms
        target:
          type: Value
          value: "200"
```

## Limites e trade-offs
Verifique se a API agregada `v1beta2.custom.metrics.k8s.io` está registrada e disponível no cluster antes de aplicar o HPA.

## Como verificar
Execute `kubectl get --raw "/apis/custom.metrics.k8s.io/v1beta2/namespaces/prod/keptnmetrics.metrics.keptn.sh/checkout-p95-latency-ms/checkout-p95-latency-ms"` para validar a exposição da métrica na Custom Metrics API.

## Conexões
- [[keptn-observabilidade-opentelemetry-traces-deployments-dora-metrics]] — Veja também: Keptn Observabilidade de Deployments: geração nativa de Traces OpenTelemetry de releases e Métricas DORA.
- [[keptn-certificate-operator-webhooks-tls-integracao-cert-manager]] — Veja também: Keptn Certificate Manager vs `cert-manager`: gerenciamento de certificados TLS para os webhooks e APIs do Keptn.

## Fontes
- [Keptn Lifecycle Toolkit GitHub — README.md (Cloud-Native Application Lifecycle Orchestration, Metrics, OpenTelemetry Observability & Helm Install)](https://keptn.sh/stable/docs/core-concepts/) — README oficial do keptn/lifecycle-toolkit descrevendo os três pilares (Metrics, Observability, Release Lifecycle Management), instalação Helm e matriz de componentes; consultado em 2026-10-03.
- [Keptn Official Documentation — Core Concepts (KeptnApp, KeptnWorkload, Pre/Post Deployment Tasks & Evaluations, Multi-Source Metrics & OpenTelemetry)](https://raw.githubusercontent.com/keptn/lifecycle-toolkit/main/README.md) — Documentação oficial de conceitos centrais do Keptn explicando o fluxo de pré/pós-deploy, execução paralela/sequencial de KeptnTask, SLOs e Custom Metrics API para HPA; consultado em 2026-10-03.
- [Keptn Lifecycle Toolkit — Official GitHub Repository](https://github.com/keptn/lifecycle-toolkit) — Repositório oficial Apache-2.0 do Keptn na CNCF; consultado em 2026-10-03.
