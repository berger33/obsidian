---
id: software.devops.tranche20.001983
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

# Keptn Pre-Deployment Gates: como o scheduler do Keptn retém o agendamento de Pods até que tarefas e avaliações pré-deploy passem

## Em uma frase
Para executar tarefas e avaliações **antes** que o novo container da aplicação entre em execução no cluster, o Keptn intercepta a criação dos Pods via mutating webhook e utiliza um plugin de agendamento do Kubernetes que mantém os Pods retidos (*gated*) até que todas as **`preDeploymentTasks`** e **`preDeploymentEvaluations`** sejam aprovadas.

## Por que importa
Se o Kubernetes iniciasse os novos Pods da versão `v2` imediatamente enquanto o banco de dados ainda não concluiu a migração de schema ou enquanto o serviço de pagamento upstream está fora do ar, os Pods entrariam em `CrashLoopBackOff` imediato.

## Como funciona
Com o Keptn ativo no namespace, quando um `Deployment` é aplicado pelo Argo CD ou `kubectl`: 1) as avaliações e tarefas pré-deploy no nível do `KeptnApp` e `KeptnWorkload` são executadas; 2) somente após todas concluírem com `Succeeded`, o Keptn libera o gate para que o scheduler agende os Pods nos nós; e 3) assim que os Pods ficam prontos, o Keptn dispara as tarefas e avaliações **pós-deploy**.

## Exemplo
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: checkout-service
  namespace: prod
  annotations:
    keptn.sh/app: ecommerce
    keptn.sh/workload: checkout-service
    keptn.sh/version: "2.1.0"
    keptn.sh/pre-deployment-tasks: check-db-ready
    keptn.sh/post-deployment-evaluations: latency-slo-check
```

## Limites e trade-offs
Se uma avaliação pré-deploy falhar (ex.: o cluster ou serviço dependente não atende aos pré-requisitos após as retentativas configuradas), o `KeptnWorkloadVersion` entra em estado `Failed` e os Pods da revisão defeituosa não consomem recursos de aplicação.

## Como verificar
Inspecione a fase atual do rollout com `kubectl get keptnworkloadversions -n prod -o wide`.

## Conexões
- [[keptn-crd-keptnapp-keptnworkload-agrupamento-logico-microsservicos]] — Veja também: Keptn `KeptnApp` e `KeptnWorkload`: agrupamento lógico de múltiplos microsserviços em uma unidade coesa de release.
- [[keptn-task-definition-keptntask-containers-deno-python-paralelismo]] — Veja também: Keptn `KeptnTaskDefinition` e `KeptnTask`: execução paralela e sequencial de tarefas pré/pós-deploy e promoção.

## Fontes
- [Keptn Lifecycle Toolkit GitHub — README.md (Cloud-Native Application Lifecycle Orchestration, Metrics, OpenTelemetry Observability & Helm Install)](https://keptn.sh/stable/docs/core-concepts/) — README oficial do keptn/lifecycle-toolkit descrevendo os três pilares (Metrics, Observability, Release Lifecycle Management), instalação Helm e matriz de componentes; consultado em 2026-10-03.
- [Keptn Official Documentation — Core Concepts (KeptnApp, KeptnWorkload, Pre/Post Deployment Tasks & Evaluations, Multi-Source Metrics & OpenTelemetry)](https://raw.githubusercontent.com/keptn/lifecycle-toolkit/main/README.md) — Documentação oficial de conceitos centrais do Keptn explicando o fluxo de pré/pós-deploy, execução paralela/sequencial de KeptnTask, SLOs e Custom Metrics API para HPA; consultado em 2026-10-03.
- [Keptn Lifecycle Toolkit — Official GitHub Repository](https://github.com/keptn/lifecycle-toolkit) — Repositório oficial Apache-2.0 do Keptn na CNCF; consultado em 2026-10-03.
