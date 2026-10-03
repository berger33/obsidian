---
id: software.devops.tranche01.000095
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
fontes: ["https://raw.githubusercontent.com/tektoncd/pipeline/main/README.md", "https://github.com/tektoncd/pipeline"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Matriz oficial de versão mínima do Kubernetes exigida pelo Tekton Pipelines (até `v0.61.x` -> Kubernetes 1.28+)

## Em uma frase
A subseção Required Kubernetes Version do `README.md` oficial documenta a progressão da versão mínima exigida do cluster Kubernetes ao longo das releases do Tekton: da `v0.24.x` (Kubernetes 1.18+), passando por `v0.27.x` (1.19+), `v0.30.x` (1.20+), `v0.33.x` (1.21+), `v0.39.x` (1.22+), `v0.41.x` (1.23+), `v0.45.x` (1.24+), `v0.51.x` (1.25+) e `v0.59.x` (1.27+), até a marca de que, a partir da release **`v0.61.x` do Tekton**, é exigido **Kubernetes 1.28 ou posterior**.

## Por que importa
Como o controlador do Tekton Pipelines depende de recursos e APIs do próprio Kubernetes (como recursos de Pod, webhooks de validação e CRDs), tentar instalar uma release recente do Tekton em um cluster Kubernetes mais antigo do que o mínimo suportado causa falhas de API ou de instalação.

## Como funciona
Antes de atualizar o Tekton Pipelines no cluster, confira a versão do servidor Kubernetes (`kubectl version`) contra a tabela Required Kubernetes Version do README e a página `releases.md`.

## Exemplo
Para clusters que já operam com versões atuais do Tekton (`v0.61.x` ou superior), garanta que o plano de controle e os nós do Kubernetes estejam pelo menos na versão **1.28 ou posterior**.

## Limites e trade-offs
Links específicos de documentação para cada versão lançada ficam disponíveis na página `releases.md` e no site `https://tekton.dev/docs`.

## Como verificar
Conferi a subseção Required Kubernetes Version no `README.md` oficial de `tektoncd/pipeline`.

## Conexões
- [[tekton-deprecated-pipelineresource-and-custom-runs]] — Veja também: Evolução do modelo de entidades: depreciação de `PipelineResource` e introdução de Custom Tasks (`Run` / `CustomRun`).
- [[tekton-api-compatibility-and-deprecations-table]] — Veja também: Governança de evolução da API: `api_compatibility_policy.md`, `docs/deprecations.md` e guias de migração `v1`.

## Fontes
- [Tekton Pipelines — README oficial](https://raw.githubusercontent.com/tektoncd/pipeline/main/README.md) — README oficial do Tekton Pipelines com os três pilares (Cloud Native, Decoupled e Typed), tabela de versão mínima do Kubernetes (até v0.61.x -> K8s 1.28+), api_compatibility_policy.md, deprecations.md e guias de migração para v1.; consultado em 2026-10-03.
- [Repositório oficial tektoncd/pipeline](https://github.com/tektoncd/pipeline) — Repositório oficial do Tekton Pipelines no GitHub com docs/, examples/, DEVELOPMENT.md e releases.md.; consultado em 2026-10-03.
