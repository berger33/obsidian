---
id: software.devops.tranche03.000237
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-03.md"
fontes: ["https://raw.githubusercontent.com/open-policy-agent/gatekeeper/master/website/docs/howto.md", "https://raw.githubusercontent.com/open-policy-agent/gatekeeper/master/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Validação de tipos de spec.parameters pelo API Server e objeto input.review no Rego

## Em uma frase
As subseções `The parameters field` e `Input Review` de `website/docs/howto.md` explicam que o Gatekeeper popula `input.parameters` no código Rego com os valores declarados em `spec.parameters` da Constraint, que o API Server do Kubernetes rejeita imediatamente na criação qualquer Constraint cujo `spec.parameters` viole o esquema `openAPIV3Schema` definido no `ConstraintTemplate` (exemplificando o erro `spec.parameters in body must be of type object: "array"`), e que o objeto inspecionado chega ao Rego via `input.review` (detalhado em `input.md`).

## Por que importa
Validar os parâmetros da própria política no momento em que o administrador aplica a Constraint impede que erros de digitação no YAML da política (como passar uma lista onde o Rego espera um objeto) entrem silenciosamente no cluster e desativem a proteção.

## Como funciona
Modele sempre o esquema OpenAPI v3 completo em `ConstraintTemplate` para que o API Server valide cada `Constraint` aplicada e escreva suas regras Rego inspecionando os campos de `input.review.object` e `input.parameters`.

## Exemplo
Quando um operador tenta aplicar uma Constraint passando `- labels: ["gatekeeper"]` (array) em vez de `labels: ["gatekeeper"]` (objeto), o API Server recusa o manifesto imediatamente com erro de validação de esquema.

## Limites e trade-offs
Ao testar regras Rego localmente com `opa test`, estruture os mocks de entrada reproduzindo fielmente os campos `input.review.object` e `input.parameters` usados pelo Gatekeeper.

## Como verificar
Conferi as subseções The parameters field e Input Review em `website/docs/howto.md` de open-policy-agent/gatekeeper.

## Conexões
- [[gatekeeper-empty-matcher-and-cluster-scoped-gotcha]] — Veja também: Armadilha de escopo: match vazio (inclusivo para tudo) e impacto sobre recursos Cluster-scoped.
- [[gatekeeper-enforcement-action-deny-dryrun-warn]] — Veja também: Modos de ação em violações (`enforcementAction`): deny, dryrun e warn.

## Fontes
- [OPA Gatekeeper Documentation — How to use Gatekeeper (howto.md)](https://raw.githubusercontent.com/open-policy-agent/gatekeeper/master/website/docs/howto.md) — Guia oficial do Gatekeeper detalhando OPA Constraint Framework, ConstraintTemplate (openAPIV3Schema e Rego), Constraint, os 7 seletores de match, escopo Cluster vs Namespaced e enforcementAction (deny, dryrun, warn).; consultado em 2026-10-03.
- [OPA Gatekeeper — GitHub README](https://raw.githubusercontent.com/open-policy-agent/gatekeeper/master/README.md) — Visão geral do Gatekeeper em comparação ao OPA com sidecar kube-mgmt (Gatekeeper v1.0), CRDs de constraints/templates/mutação, auditoria, external data e biblioteca de políticas.; consultado em 2026-10-03.
