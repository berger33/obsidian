---
id: software.devops.tranche20.001985
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

# Keptn `KeptnEvaluationDefinition`: validação declarativa de SLOs e saúde de aplicação antes e depois do deploy

## Em uma frase
O Custom Resource **`KeptnEvaluationDefinition`** permite declarar objetivos de nível de serviço (**SLOs**) e pré-requisitos quantitativos (consultando recursos **`KeptnMetric`**) que são avaliados automaticamente antes do deploy (ex.: "há CPU livre suficiente no cluster?") ou após o deploy (ex.: "a latência P95 está `< 250ms` e a taxa de erro `< 1%`?").

## Por que importa
Sem validação automatizada de SLOs pós-deploy, um deploy pode subir todos os Pods com `Running` (`1/1`) enquanto retorna HTTP `500` em 15% das transações de clientes.

## Como funciona
Cada `objective` dentro de `KeptnEvaluationDefinition.spec.objectives` referencia um `keptnMetricRef` (`name` e `namespace`) e um operador de limiar `evaluationTarget` (como `"<250"`, `">99.5"`, `"<=0.01"`). O controlador executa a avaliação com `retries` e `retryInterval` configuráveis até que todos os objetivos passem.

## Exemplo
```yaml
apiVersion: lifecycle.keptn.sh/v1beta1
kind: KeptnEvaluationDefinition
metadata:
  name: checkout-slo-evaluation
  namespace: prod
spec:
  objectives:
    - keptnMetricRef:
        name: checkout-p95-latency-ms
        namespace: prod
      evaluationTarget: "<250"
    - keptnMetricRef:
        name: checkout-error-rate
        namespace: prod
      evaluationTarget: "<0.01"
```

## Limites e trade-offs
Se uma avaliação pós-deploy falhar após todas as tentativas, o `KeptnWorkloadVersion` / `KeptnAppVersion` registra a falha de SLO, emitindo eventos Kubernetes, CloudEvents e métricas OpenTelemetry para acionar alertas ou rollback no controlador GitOps.

## Como verificar
Execute `kubectl get keptnevaluations -n prod` e `kubectl describe keptnevaluation <nome> -n prod` para ver o valor medido de cada objetivo frente ao `evaluationTarget`.

## Conexões
- [[keptn-task-definition-keptntask-containers-deno-python-paralelismo]] — Veja também: Keptn `KeptnTaskDefinition` e `KeptnTask`: execução paralela e sequencial de tarefas pré/pós-deploy e promoção.
- [[keptn-metrics-operator-keptnmetricsprovider-keptnmetric-multi-source]] — Veja também: Keptn Metrics Operator: unificação de `Prometheus`, `Thanos`, `Cortex`, `Dynatrace`, `Datadog` e `Elastic` via `KeptnMetricsProvider` e `KeptnMetric`.

## Fontes
- [Keptn Lifecycle Toolkit GitHub — README.md (Cloud-Native Application Lifecycle Orchestration, Metrics, OpenTelemetry Observability & Helm Install)](https://keptn.sh/stable/docs/core-concepts/) — README oficial do keptn/lifecycle-toolkit descrevendo os três pilares (Metrics, Observability, Release Lifecycle Management), instalação Helm e matriz de componentes; consultado em 2026-10-03.
- [Keptn Official Documentation — Core Concepts (KeptnApp, KeptnWorkload, Pre/Post Deployment Tasks & Evaluations, Multi-Source Metrics & OpenTelemetry)](https://raw.githubusercontent.com/keptn/lifecycle-toolkit/main/README.md) — Documentação oficial de conceitos centrais do Keptn explicando o fluxo de pré/pós-deploy, execução paralela/sequencial de KeptnTask, SLOs e Custom Metrics API para HPA; consultado em 2026-10-03.
- [Keptn Lifecycle Toolkit — Official GitHub Repository](https://github.com/keptn/lifecycle-toolkit) — Repositório oficial Apache-2.0 do Keptn na CNCF; consultado em 2026-10-03.
