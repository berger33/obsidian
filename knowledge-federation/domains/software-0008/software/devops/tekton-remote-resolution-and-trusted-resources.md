---
id: software.devops.tranche01.000099
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

# Reutilização remota e segurança da cadeia de suprimentos: `resolution.md` e `trusted-resources.md`

## Em uma frase
Os dois últimos tópicos da seção Understanding Tekton Pipelines em `docs/README.md` abordam a distribuição segura de definições de CI/CD: `Remote resolution of Pipelines and Tasks` (`resolution.md`) e `Trusted Resources` (`trusted-resources.md`).

## Por que importa
Em organizações com dezenas de repositórios, obrigar cada aplicação a copiar ou aplicar manualmente todas as `Tasks` no cluster antes de rodar um pipeline gera duplicação; a resolução remota (`resolution.md`) permite buscar `Pipelines` e `Tasks` de fontes remotas (como repositórios Git ou bundles), enquanto `Trusted Resources` (`trusted-resources.md`) permite verificar criptograficamente que aquelas definições de `Task` e `Pipeline` não foram adulteradas.

## Como funciona
Utilize `Remote resolution of Pipelines and Tasks` (`resolution.md`) para consumir catálogos centralizados de `Tasks` e `Pipelines` sem instalá-los manualmente em cada namespace, e habilite `Trusted Resources` (`trusted-resources.md`) para validar a integridade e autenticidade dos recursos antes da execução.

## Exemplo
Combinar resolução remota com `Trusted Resources` impede que um artefato remoto comprometido injete passos maliciosos no runner de CI/CD do cluster.

## Limites e trade-offs
Verifique os requisitos de configuração de chaves e políticas em `trusted-resources.md` ao implantar verificação de assinatura de recursos em ambientes de produção.

## Como verificar
Conferi os itens `Remote resolution of Pipelines and Tasks` e `Trusted Resources` na seção Understanding Tekton Pipelines de `docs/README.md`.

## Conexões
- [[tekton-observability-labels-logs-and-metrics]] — Veja também: Observabilidade de execuções de CI/CD no Tekton: `labels.md`, `logs.md` e `metrics.md`.
- [[tekton-contributing-development-and-licenses]] — Veja também: Guia de contribuição, arquitetura interna (`docs/developers/README.md`) e duplo licenciamento CC-BY-4.0 / Apache 2.0.

## Fontes
- [Tekton Pipelines — Tasks and Pipelines (docs/README.md)](https://raw.githubusercontent.com/tektoncd/pipeline/main/docs/README.md) — Visão geral oficial em docs/README.md com a tabela das seis entidades (Task, TaskRun, Pipeline, PipelineRun, PipelineResource Deprecated e Run alpha), os 13 guias temáticos e licenças CC-BY-4.0 / Apache 2.0.; consultado em 2026-10-03.
- [Tekton Pipelines — README oficial](https://raw.githubusercontent.com/tektoncd/pipeline/main/README.md) — README oficial do Tekton Pipelines com os três pilares (Cloud Native, Decoupled e Typed), tabela de versão mínima do Kubernetes (até v0.61.x -> K8s 1.28+), api_compatibility_policy.md, deprecations.md e guias de migração para v1.; consultado em 2026-10-03.
