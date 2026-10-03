---
id: software.devops.tranche01.000096
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

# Governança de evolução da API: `api_compatibility_policy.md`, `docs/deprecations.md` e guias de migração `v1`

## Em uma frase
Nas seções Read the docs e Migrating do `README.md` oficial, o projeto reúne quatro documentos de estabilidade e transição de versão: a política de compatibilidade da API em `api_compatibility_policy.md`, a tabela oficial de recursos depreciados com a data mais cedo de remoção em `docs/deprecations.md`, o guia de migração `v1beta1 to v1` (`./docs/migrating-v1beta1-to-v1.md`) e o guia histórico `v1alpha1 to v1beta1` (`./docs/migrating-v1alpha1-to-v1beta1.md`).

## Por que importa
Em plataformas de CI/CD compartilhadas por dezenas de equipes, atualizar o controlador do Tekton sem checar a tabela `docs/deprecations.md` pode desativar campos que algum pipeline ainda utiliza; a tabela informa antecipadamente o que foi depreciado e a data mínima em que será removido.

## Como funciona
Consulte `api_compatibility_policy.md` para conhecer as garantias de cada estágio da API, audite seus manifestos contra `docs/deprecations.md` antes de cada upgrade do Tekton e siga `./docs/migrating-v1beta1-to-v1.md` para padronizar todas as Tasks e Pipelines em `v1`.

## Exemplo
O guia `migrating-v1beta1-to-v1.md` destaca especificamente as mudanças em CRDs e campos da spec ocorridas na promoção para `v1`, incluindo o CRD `ClusterTask` e os campos de `PipelineResources`.

## Limites e trade-offs
Ao consultar a documentação na branch principal (`Docs @ HEAD` em `/docs/README.md`), lembre-se de que ela reflete o código mais recente em desenvolvimento; para uma release fixa em produção, use os links versionados em `releases.md`.

## Como verificar
Conferi as seções Read the docs e Migrating no `README.md` oficial de `tektoncd/pipeline`.

## Conexões
- [[tekton-kubernetes-minimum-version-progression]] — Veja também: Matriz oficial de versão mínima do Kubernetes exigida pelo Tekton Pipelines (até `v0.61.x` -> Kubernetes 1.28+).
- [[tekton-workspaces-auth-and-variable-substitution]] — Veja também: Compartilhamento de dados, credenciais e parametrização: Workspaces, Authentication e Variable Substitutions.

## Fontes
- [Tekton Pipelines — README oficial](https://raw.githubusercontent.com/tektoncd/pipeline/main/README.md) — README oficial do Tekton Pipelines com os três pilares (Cloud Native, Decoupled e Typed), tabela de versão mínima do Kubernetes (até v0.61.x -> K8s 1.28+), api_compatibility_policy.md, deprecations.md e guias de migração para v1.; consultado em 2026-10-03.
- [Tekton Pipelines — Tasks and Pipelines (docs/README.md)](https://raw.githubusercontent.com/tektoncd/pipeline/main/docs/README.md) — Visão geral oficial em docs/README.md com a tabela das seis entidades (Task, TaskRun, Pipeline, PipelineRun, PipelineResource Deprecated e Run alpha), os 13 guias temáticos e licenças CC-BY-4.0 / Apache 2.0.; consultado em 2026-10-03.
