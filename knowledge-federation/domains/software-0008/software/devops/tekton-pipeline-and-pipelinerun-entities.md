---
id: software.devops.tranche01.000093
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-25.md"
fontes: ["https://raw.githubusercontent.com/tektoncd/pipeline/main/docs/README.md", "https://raw.githubusercontent.com/tektoncd/pipeline/main/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Orquestração de ponta a ponta com `Pipeline` e `PipelineRun`

## Em uma frase
Na tabela `Tekton Pipelines entities` de `docs/README.md`, o nível de orquestração é composto por **`Pipeline`** — que define uma série de `Tasks` que cumprem um objetivo específico de build ou entrega, podendo ser acionado por um evento ou invocado a partir de um `PipelineRun` — e por **`PipelineRun`** — que instancia um `Pipeline` para execução com entradas, saídas e parâmetros de execução específicos.

## Por que importa
Assim como `Task` e `TaskRun`, separar o grafo declarativo do fluxo (`Pipeline`) de cada disparo concreto (`PipelineRun`) permite reutilizar exatamente o mesmo `Pipeline` para fazer deploy em qualquer cluster Kubernetes ou contra qualquer repositório Git apenas variando os parâmetros do `PipelineRun`.

## Como funciona
Declare a sequência e o encadeamento de `Tasks` em um objeto `Pipeline` (`docs/pipelines.md`) e submeta objetos `PipelineRun` (`docs/pipelineruns.md`) manualmente via `kubectl` ou automaticamente a partir de gatilhos de eventos.

## Exemplo
Cada `PipelineRun` cria e coordena os `TaskRuns` correspondentes às `Tasks` declaradas no `Pipeline`, mantendo o histórico de cada execução como recursos consultáveis na API do Kubernetes.

## Limites e trade-offs
Ao parametrizar os caminhos de repositórios, imagens e alvos no `PipelineRun`, uma única definição de `Pipeline` atende múltiplos projetos e ambientes sem duplicação de YAML.

## Como verificar
Conferi a tabela `Tekton Pipelines entities` e os tópicos `pipelines.md` e `pipelineruns.md` em `docs/README.md`.

## Conexões
- [[tekton-task-and-taskrun-entities]] — Veja também: As entidades de base `Task` e `TaskRun`: definição de passos em contêineres vs. instanciação de execução.
- [[tekton-deprecated-pipelineresource-and-custom-runs]] — Veja também: Evolução do modelo de entidades: depreciação de `PipelineResource` e introdução de Custom Tasks (`Run` / `CustomRun`).

## Fontes
- [Tekton Pipelines — Tasks and Pipelines (docs/README.md)](https://raw.githubusercontent.com/tektoncd/pipeline/main/docs/README.md) — Visão geral oficial em docs/README.md com a tabela das seis entidades (Task, TaskRun, Pipeline, PipelineRun, PipelineResource Deprecated e Run alpha), os 13 guias temáticos e licenças CC-BY-4.0 / Apache 2.0.; consultado em 2026-10-03.
- [Tekton Pipelines — README oficial](https://raw.githubusercontent.com/tektoncd/pipeline/main/README.md) — README oficial do Tekton Pipelines com os três pilares (Cloud Native, Decoupled e Typed), tabela de versão mínima do Kubernetes (até v0.61.x -> K8s 1.28+), api_compatibility_policy.md, deprecations.md e guias de migração para v1.; consultado em 2026-10-03.
