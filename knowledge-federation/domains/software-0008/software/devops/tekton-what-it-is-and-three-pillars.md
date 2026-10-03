---
id: software.devops.tranche01.000091
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

# Tekton Pipelines: recursos em estilo Kubernetes para declarar pipelines de CI/CD (Cloud Native, Decoupled e Typed)

## Em uma frase
O README oficial no repositório tektoncd/pipeline define o projeto como um provedor de recursos em estilo Kubernetes (k8s-style resources) para declarar pipelines de CI/CD, organizado em torno de três características centrais: **Cloud Native** (roda no Kubernetes, trata clusters Kubernetes como tipo de primeira classe e usa contêineres como blocos de construção), **Decoupled** (um único Pipeline pode implantar em qualquer cluster k8s, as Tasks que o compõem rodam facilmente em isolamento e recursos como repositórios Git são trocados entre execuções) e **Typed** (implementações para um recurso como `Image` podem ser trocadas facilmente, por exemplo construir com `kaniko` versus `buildkit`).

## Por que importa
Em servidores de CI tradicionais centralizados fora do cluster, os jobs disputam agentes estáticos e misturam a definição das etapas com o repositório ou ambiente onde rodam; no Tekton, cada etapa é um contêiner gerenciado pelo próprio Kubernetes e as tarefas são desacopladas do destino e da ferramenta específica de build.

## Como funciona
Instale a extensão Tekton Pipelines no seu cluster Kubernetes (`docs/install.md`) e modele seus fluxos de build, teste e entrega como Custom Resources manipuláveis via `kubectl` e chamadas de API do Kubernetes.

## Exemplo
Como destaca `docs/README.md`, o Tekton é open-source e faz parte da **CD Foundation** (`cd.foundation`), um projeto da Linux Foundation.

## Limites e trade-offs
Por operar nativamente sobre a API do Kubernetes, os recursos do Tekton convivem com o mesmo controle de acesso, observabilidade e CLI (`kubectl`) usados para pods e demais objetos do cluster.

## Como verificar
Conferi a abertura do `README.md` oficial e o primeiro parágrafo de `docs/README.md` em `tektoncd/pipeline`.

## Conexões
- [[tekton-task-and-taskrun-entities]] — Veja também: As entidades de base `Task` e `TaskRun`: definição de passos em contêineres vs. instanciação de execução.

## Fontes
- [Tekton Pipelines — README oficial](https://raw.githubusercontent.com/tektoncd/pipeline/main/README.md) — README oficial do Tekton Pipelines com os três pilares (Cloud Native, Decoupled e Typed), tabela de versão mínima do Kubernetes (até v0.61.x -> K8s 1.28+), api_compatibility_policy.md, deprecations.md e guias de migração para v1.; consultado em 2026-10-03.
- [Tekton Pipelines — Tasks and Pipelines (docs/README.md)](https://raw.githubusercontent.com/tektoncd/pipeline/main/docs/README.md) — Visão geral oficial em docs/README.md com a tabela das seis entidades (Task, TaskRun, Pipeline, PipelineRun, PipelineResource Deprecated e Run alpha), os 13 guias temáticos e licenças CC-BY-4.0 / Apache 2.0.; consultado em 2026-10-03.
