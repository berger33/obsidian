---
id: software.devops.tranche01.000092
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

# As entidades de base `Task` e `TaskRun`: definição de passos em contêineres vs. instanciação de execução

## Em uma frase
A tabela de entidades em `docs/README.md` distingue o bloco reutilizável de sua execução concreta: uma **`Task`** define uma série de passos (`steps`) que acionam ferramentas específicas de build ou entrega para ingerir entradas específicas e produzir saídas específicas; já um **`TaskRun`** instancia uma `Task` para execução com entradas, saídas e parâmetros de execução concretos, podendo ser invocado de forma avulsa (standalone) ou como parte de um `Pipeline`.

## Por que importa
Separar a declaração da receita (`Task`) da sua execução pontual (`TaskRun`) segue o mesmo padrão de design do Kubernetes e permite testar qualquer `Task` isoladamente antes de encadeá-la num pipeline maior.

## Como funciona
Escreva cada `Task` como uma unidade coesa e reutilizável (seguindo `docs/tasks.md`) e dispare um `TaskRun` avulso (`docs/taskruns.md`) durante o desenvolvimento para validar seus passos, entradas e saídas em isolamento.

## Exemplo
Essa capacidade de rodar um `TaskRun` por conta própria materializa o princípio **Decoupled** do README ("The Tasks which make up a Pipeline can easily be run in isolation").

## Limites e trade-offs
Uma `Task` registrada no cluster não executa nenhum contêiner por si só; a criação de pods de trabalho só ocorre quando um `TaskRun` (direto ou criado por um `PipelineRun`) é submetido à API.

## Como verificar
Conferi a tabela `Tekton Pipelines entities` e a lista de guias em `docs/README.md`.

## Conexões
- [[tekton-what-it-is-and-three-pillars]] — Veja também: Tekton Pipelines: recursos em estilo Kubernetes para declarar pipelines de CI/CD (Cloud Native, Decoupled e Typed).
- [[tekton-pipeline-and-pipelinerun-entities]] — Veja também: Orquestração de ponta a ponta com `Pipeline` e `PipelineRun`.

## Fontes
- [Tekton Pipelines — Tasks and Pipelines (docs/README.md)](https://raw.githubusercontent.com/tektoncd/pipeline/main/docs/README.md) — Visão geral oficial em docs/README.md com a tabela das seis entidades (Task, TaskRun, Pipeline, PipelineRun, PipelineResource Deprecated e Run alpha), os 13 guias temáticos e licenças CC-BY-4.0 / Apache 2.0.; consultado em 2026-10-03.
- [Tekton Pipelines — README oficial](https://raw.githubusercontent.com/tektoncd/pipeline/main/README.md) — README oficial do Tekton Pipelines com os três pilares (Cloud Native, Decoupled e Typed), tabela de versão mínima do Kubernetes (até v0.61.x -> K8s 1.28+), api_compatibility_policy.md, deprecations.md e guias de migração para v1.; consultado em 2026-10-03.
