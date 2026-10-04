---
id: software.devops.tranche20.001984
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

# Keptn `KeptnTaskDefinition` e `KeptnTask`: execução paralela e sequencial de tarefas pré/pós-deploy e promoção

## Em uma frase
O Custom Resource **`KeptnTaskDefinition`** define ações executáveis (usando containers arbitrários, scripts **Deno/TypeScript** ou **Python**) que o Keptn instancia como objetos **`KeptnTask`** (Jobs Kubernetes) nos estágios de **pre-deployment**, **post-deployment** ou **promotion**.

## Por que importa
Padronizar a execução de testes de fumaça (*smoke tests*), varreduras de imagem, preparação de infraestrutura ou notificações de release diretamente no ciclo de vida do workload no cluster elimina a dependência de pipelines de CI externos que perdem conexão com o cluster.

## Como funciona
Conforme detalhado na documentação de Core Concepts do Keptn: todos os recursos `KeptnTask` definidos no mesmo nível (ex.: duas tarefas listadas em `preDeploymentTasks`) executam **em paralelo**; por outro lado, se um único `KeptnTask` for definido para rodar múltiplos executáveis/funções encadeados, os executáveis dentro daquele `KeptnTask` rodam em **ordem sequencial**.

## Exemplo
```yaml
apiVersion: lifecycle.keptn.sh/v1beta1
kind: KeptnTaskDefinition
metadata:
  name: smoke-test-checkout
  namespace: prod
spec:
  container:
    name: curl-smoke
    image: curlimages/curl:8.7.1
    command:
      - sh
      - -c
      - "curl -fsS --retry 5 http://checkout-service.prod.svc.cluster.local:8080/healthz"
  retries: 3
  timeout: 2m
```

## Limites e trade-offs
Como recomenda a documentação oficial do Keptn, sequências complexas de compilação e build que não fazem parte do workflow de ciclo de vida do deploy no cluster devem continuar na ferramenta de pipeline de CI, reservando o `KeptnTask` para validações e ações de release in-cluster.

## Como verificar
Liste as definições e as execuções de tarefas no namespace com `kubectl get keptntaskdefinitions,keptntasks -n prod`.

## Conexões
- [[keptn-scheduler-plugin-gate-pre-deployment-bloqueio-pods]] — Veja também: Keptn Pre-Deployment Gates: como o scheduler do Keptn retém o agendamento de Pods até que tarefas e avaliações pré-deploy passem.
- [[keptn-evaluation-definition-slo-validation-pre-post-deployment]] — Veja também: Keptn `KeptnEvaluationDefinition`: validação declarativa de SLOs e saúde de aplicação antes e depois do deploy.

## Fontes
- [Keptn Lifecycle Toolkit GitHub — README.md (Cloud-Native Application Lifecycle Orchestration, Metrics, OpenTelemetry Observability & Helm Install)](https://keptn.sh/stable/docs/core-concepts/) — README oficial do keptn/lifecycle-toolkit descrevendo os três pilares (Metrics, Observability, Release Lifecycle Management), instalação Helm e matriz de componentes; consultado em 2026-10-03.
- [Keptn Official Documentation — Core Concepts (KeptnApp, KeptnWorkload, Pre/Post Deployment Tasks & Evaluations, Multi-Source Metrics & OpenTelemetry)](https://raw.githubusercontent.com/keptn/lifecycle-toolkit/main/README.md) — Documentação oficial de conceitos centrais do Keptn explicando o fluxo de pré/pós-deploy, execução paralela/sequencial de KeptnTask, SLOs e Custom Metrics API para HPA; consultado em 2026-10-03.
- [Keptn Lifecycle Toolkit — Official GitHub Repository](https://github.com/keptn/lifecycle-toolkit) — Repositório oficial Apache-2.0 do Keptn na CNCF; consultado em 2026-10-03.
