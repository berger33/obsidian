---
id: software.devops.tranche01.000094
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
fontes: ["https://raw.githubusercontent.com/tektoncd/pipeline/main/README.md", "https://raw.githubusercontent.com/tektoncd/pipeline/main/docs/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Evolução do modelo de entidades: depreciação de `PipelineResource` e introdução de Custom Tasks (`Run` / `CustomRun`)

## Em uma frase
A tabela de entidades e os tópicos de `docs/README.md` (junto à seção Migrating do `README.md` principal) registram duas mudanças importantes no modelo do Tekton: a entidade `PipelineResource (Deprecated)` (que historicamente definia locais de entradas e saídas para `Tasks`) está marcada como depreciada e foi removida/atualizada na migração para `v1`, enquanto a execução de **Custom Tasks** é suportada para lógica que não segue o formato padrão de contêineres em sequência (listada como `Run (alpha)` na tabela e detalhada em `Running a Custom Task` -> `customruns.md`).

## Por que importa
Equipes que consultam tutoriais antigos da época de `v1alpha1`/`v1beta1` ainda encontram exemplos usando `PipelineResource` ou `ClusterTask`; saber que `PipelineResource` foi depreciado e que a migração para `v1` substituiu esses campos evita escrever pipelines sobre APIs descontinuadas.

## Como funciona
Em novos pipelines na API `v1`, utilize Workspaces (`workspaces.md`), parâmetros e resultados de Tasks em vez do antigo `PipelineResource`, e consulte `customruns.md` quando precisar executar uma Custom Task.

## Exemplo
O guia oficial `./docs/migrating-v1beta1-to-v1.md` documenta passo a passo como migrar `ClusterTask` e campos legados de `PipelineResource` da `v1beta1` para a API estável `v1`.

## Limites e trade-offs
Antes de adotar recursos marcados como `alpha` (como extensões experimentais), verifique o nível de estabilidade na política `api_compatibility_policy.md`.

## Como verificar
Conferi a seção Migrating no `README.md` principal e a tabela de entidades e lista de tópicos em `docs/README.md`.

## Conexões
- [[tekton-pipeline-and-pipelinerun-entities]] — Veja também: Orquestração de ponta a ponta com `Pipeline` e `PipelineRun`.
- [[tekton-kubernetes-minimum-version-progression]] — Veja também: Matriz oficial de versão mínima do Kubernetes exigida pelo Tekton Pipelines (até `v0.61.x` -> Kubernetes 1.28+).

## Fontes
- [Tekton Pipelines — README oficial](https://raw.githubusercontent.com/tektoncd/pipeline/main/README.md) — README oficial do Tekton Pipelines com os três pilares (Cloud Native, Decoupled e Typed), tabela de versão mínima do Kubernetes (até v0.61.x -> K8s 1.28+), api_compatibility_policy.md, deprecations.md e guias de migração para v1.; consultado em 2026-10-03.
- [Tekton Pipelines — Tasks and Pipelines (docs/README.md)](https://raw.githubusercontent.com/tektoncd/pipeline/main/docs/README.md) — Visão geral oficial em docs/README.md com a tabela das seis entidades (Task, TaskRun, Pipeline, PipelineRun, PipelineResource Deprecated e Run alpha), os 13 guias temáticos e licenças CC-BY-4.0 / Apache 2.0.; consultado em 2026-10-03.
