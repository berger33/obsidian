---
id: software.devops.tranche20.001981
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
fontes: ["https://raw.githubusercontent.com/keptn/lifecycle-toolkit/main/README.md", "https://keptn.sh/stable/docs/core-concepts/", "https://github.com/keptn/lifecycle-toolkit"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Keptn: arquitetura CNCF Incubating para orquestração de ciclo de vida de releases, avaliações de SLO e observabilidade OpenTelemetry

## Em uma frase
O **Keptn** (desenvolvido sob o codinome *Keptn Lifecycle Toolkit — KLT*, projeto **CNCF Incubating** licenciado sob Apache 2.0) traz consciência de aplicação (*application awareness*) para clusters Kubernetes (>= 1.27), complementando ferramentas GitOps (como Argo CD, Flux e GitLab) com **tarefas e avaliações pré/pós-deploy**, **métricas multi-fonte** e **observabilidade OpenTelemetry/DORA nativa**.

## Por que importa
Ferramentas de deploy padrão do Kubernetes consideram um rollout concluído assim que os Pods ficam `Ready`, sem verificar antes do deploy se serviços dependentes e recursos do cluster estão saudáveis, e sem avaliar após o deploy se os SLOs de latência/erro no Prometheus/Datadog continuam verdes.

## Como funciona
Operando como um **Operator Nível 3** declarativo agnóstico à ferramenta de CD, o Keptn organiza suas funcionalidades em três pilares independentes ou combinados: 1) **Metrics** (servidor de métricas unificado e Kubernetes Custom Metrics API); 2) **Observability** (traces OpenTelemetry de ponta a ponta do deployment e métricas **DORA** nativas); e 3) **Release Lifecycle Management** (tarefas `KeptnTaskDefinition` e avaliações `KeptnEvaluationDefinition` envolvendo workloads e `KeptnApp`).

## Exemplo
```bash
helm repo add keptn https://charts.lifecycle.keptn.sh
helm repo update
helm upgrade --install keptn keptn/keptn -n keptn-system --create-namespace --wait
```

## Limites e trade-offs
Conforme documentado no README oficial, o Keptn deve ser instalado em seu próprio namespace dedicado (`keptn-system`) que não execute outros componentes ou deployments de aplicação.

## Como verificar
Execute `kubectl get pods -n keptn-system` para verificar que os operadores do Keptn (`lifecycle-operator`, `metrics-operator`, `certificate-operator`) estão em execução.

## Conexões
- [[keptn-crd-keptnapp-keptnworkload-agrupamento-logico-microsservicos]] — Veja também: Keptn `KeptnApp` e `KeptnWorkload`: agrupamento lógico de múltiplos microsserviços em uma unidade coesa de release.

## Fontes
- [Keptn Lifecycle Toolkit GitHub — README.md (Cloud-Native Application Lifecycle Orchestration, Metrics, OpenTelemetry Observability & Helm Install)](https://raw.githubusercontent.com/keptn/lifecycle-toolkit/main/README.md) — README oficial do keptn/lifecycle-toolkit descrevendo os três pilares (Metrics, Observability, Release Lifecycle Management), instalação Helm e matriz de componentes; consultado em 2026-10-03.
- [Keptn Official Documentation — Core Concepts (KeptnApp, KeptnWorkload, Pre/Post Deployment Tasks & Evaluations, Multi-Source Metrics & OpenTelemetry)](https://keptn.sh/stable/docs/core-concepts/) — Documentação oficial de conceitos centrais do Keptn explicando o fluxo de pré/pós-deploy, execução paralela/sequencial de KeptnTask, SLOs e Custom Metrics API para HPA; consultado em 2026-10-03.
- [Keptn Lifecycle Toolkit — Official GitHub Repository](https://github.com/keptn/lifecycle-toolkit) — Repositório oficial Apache-2.0 do Keptn na CNCF; consultado em 2026-10-03.
