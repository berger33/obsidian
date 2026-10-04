---
id: software.devops.tranche01.000097
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-01.md"
fontes: ["https://raw.githubusercontent.com/tektoncd/pipeline/main/docs/README.md", "https://raw.githubusercontent.com/tektoncd/pipeline/main/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Compartilhamento de dados, credenciais e parametrização: Workspaces, Authentication e Variable Substitutions

## Em uma frase
Na seção Understanding Tekton Pipelines de `docs/README.md`, três guias cobrem a passagem de estado, segredos e variáveis entre os passos e tarefas de um pipeline: `Defining Workspaces` (`workspaces.md`), `Configuring authentication` (`auth.md`) e `Variable Substitutions` (`tasks.md#using-variable-substitution`).

## Por que importa
Como cada `Task` roda em seu próprio Pod Kubernetes isolado, duas tarefas consecutivas (por exemplo, clonar/testar o código e depois empacotar a imagem) precisam de um mecanismo explícito de armazenamento compartilhado (`Workspaces`), de credenciais para falar com Git e registries (`auth.md`) e de interpolação segura de parâmetros e resultados nos comandos (`Variable Substitutions`).

## Como funciona
Declare `Workspaces` (`workspaces.md`) para compartilhar sistemas de arquivos, ConfigMaps ou Secrets entre `Tasks`, configure credenciais de Git e registro de imagens seguindo `auth.md` e utilize a sintaxe de substituição de variáveis (`tasks.md#using-variable-substitution`) para parametrizar passos sem hardcoding.

## Exemplo
Combinar `Workspaces` e `Variable Substitutions` permite que a mesma `Task` genérica de build ou teste opere sobre qualquer repositório clonado na etapa anterior.

## Limites e trade-offs
Evite passar segredos sensíveis em texto aberto via parâmetros comuns de substituição de linha de comando que possam aparecer em logs; utilize os mecanismos de autenticação e montagem descritos em `auth.md` e `workspaces.md`.

## Como verificar
Conferi a lista de tópicos da seção Understanding Tekton Pipelines em `docs/README.md`.

## Conexões
- [[tekton-api-compatibility-and-deprecations-table]] — Veja também: Governança de evolução da API: `api_compatibility_policy.md`, `docs/deprecations.md` e guias de migração `v1`.
- [[tekton-observability-labels-logs-and-metrics]] — Veja também: Observabilidade de execuções de CI/CD no Tekton: `labels.md`, `logs.md` e `metrics.md`.

## Fontes
- [Tekton Pipelines — Tasks and Pipelines (docs/README.md)](https://raw.githubusercontent.com/tektoncd/pipeline/main/docs/README.md) — Visão geral oficial em docs/README.md com a tabela das seis entidades (Task, TaskRun, Pipeline, PipelineRun, PipelineResource Deprecated e Run alpha), os 13 guias temáticos e licenças CC-BY-4.0 / Apache 2.0.; consultado em 2026-10-03.
- [Tekton Pipelines — README oficial](https://raw.githubusercontent.com/tektoncd/pipeline/main/README.md) — README oficial do Tekton Pipelines com os três pilares (Cloud Native, Decoupled e Typed), tabela de versão mínima do Kubernetes (até v0.61.x -> K8s 1.28+), api_compatibility_policy.md, deprecations.md e guias de migração para v1.; consultado em 2026-10-03.
