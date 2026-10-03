---
id: software.devops.tranche20.001982
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

# Keptn `KeptnApp` e `KeptnWorkload`: agrupamento lógico de múltiplos microsserviços em uma unidade coesa de release

## Em uma frase
No Keptn, além de monitorar recursos individuais do Kubernetes (`Deployment`, `StatefulSet`, `DaemonSet`) por meio de **`KeptnWorkload`**, o Custom Resource **`KeptnApp`** agrupa múltiplos workloads logicamente relacionados em uma única aplicação versionada para executar verificações, avaliações e traces no nível da aplicação inteira.

## Por que importa
Em uma arquitetura de microsserviços onde um e-commerce é formado por 4 Deployments (`frontend`, `cart`, `checkout`, `payment`), validar apenas cada Pod isoladamente não garante que a versão combinada da aplicação inteira esteja pronta para receber tráfego.

## Como funciona
Quando você anota seus Deployments/StatefulSets com as anotações do Keptn (`keptn.sh/app: ecommerce`, `keptn.sh/workload: checkout`, `keptn.sh/version: 2.1.0` ou labels equivalentes `app.kubernetes.io/part-of`), o operador gera/reconcilia automaticamente os objetos `KeptnWorkload`, `KeptnWorkloadVersion` e `KeptnAppVersion`, orquestrando o ciclo de vida em dois níveis: primeiro as checagens pré-deploy da `KeptnApp`, depois o agendamento dos Pods e as checagens de cada `KeptnWorkload`, e por fim as avaliações pós-deploy da `KeptnApp`.

## Exemplo
```yaml
apiVersion: lifecycle.keptn.sh/v1beta1
kind: KeptnAppContext
metadata:
  name: ecommerce
  namespace: prod
spec:
  preDeploymentTasks:
    - verify-db-migrations
  postDeploymentEvaluations:
    - checkout-slo-evaluation
```

## Limites e trade-offs
O recurso `KeptnAppContext` permite anexar tarefas, avaliações e metadados extras de span OpenTelemetry a um `KeptnApp` descoberto automaticamente sem precisar escrever a lista manual de workloads.

## Como verificar
Execute `kubectl get keptnapps,keptnappversions,keptnworkloads,keptnworkloadversions -A` para inspecionar o estado de cada revisão da aplicação.

## Conexões
- [[keptn-arquitetura-cncf-cloud-native-application-lifecycle-observability]] — Veja também: Keptn: arquitetura CNCF Incubating para orquestração de ciclo de vida de releases, avaliações de SLO e observabilidade OpenTelemetry.
- [[keptn-scheduler-plugin-gate-pre-deployment-bloqueio-pods]] — Veja também: Keptn Pre-Deployment Gates: como o scheduler do Keptn retém o agendamento de Pods até que tarefas e avaliações pré-deploy passem.

## Fontes
- [Keptn Lifecycle Toolkit GitHub — README.md (Cloud-Native Application Lifecycle Orchestration, Metrics, OpenTelemetry Observability & Helm Install)](https://keptn.sh/stable/docs/core-concepts/) — README oficial do keptn/lifecycle-toolkit descrevendo os três pilares (Metrics, Observability, Release Lifecycle Management), instalação Helm e matriz de componentes; consultado em 2026-10-03.
- [Keptn Official Documentation — Core Concepts (KeptnApp, KeptnWorkload, Pre/Post Deployment Tasks & Evaluations, Multi-Source Metrics & OpenTelemetry)](https://raw.githubusercontent.com/keptn/lifecycle-toolkit/main/README.md) — Documentação oficial de conceitos centrais do Keptn explicando o fluxo de pré/pós-deploy, execução paralela/sequencial de KeptnTask, SLOs e Custom Metrics API para HPA; consultado em 2026-10-03.
- [Keptn Lifecycle Toolkit — Official GitHub Repository](https://github.com/keptn/lifecycle-toolkit) — Repositório oficial Apache-2.0 do Keptn na CNCF; consultado em 2026-10-03.
