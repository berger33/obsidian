---
id: software.devops.tranche03.000239
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
fontes: ["https://raw.githubusercontent.com/open-policy-agent/gatekeeper/master/README.md", "https://raw.githubusercontent.com/open-policy-agent/gatekeeper/master/website/docs/howto.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Biblioteca oficial Gatekeeper Policy Library e suporte a dados externos

## Em uma frase
O README oficial destaca o repositório e site da **Gatekeeper policy library** (`open-policy-agent.github.io/gatekeeper-library/website/`), que reúne uma coleção de `ConstraintTemplates` e exemplos de `Constraints` prontos para uso, além de listar na seção inicial o suporte a dados externos (`External data support`).

## Por que importa
Em vez de escrever código Rego complexo do zero para validações comuns do Kubernetes (como proibir containers privilegiados, exigir probes, restringir capabilities Linux ou validar repositórios de imagens), reutilizar os templates auditados da `gatekeeper-library` reduz bugs de lógica em políticas.

## Como funciona
Consulte o catálogo em `open-policy-agent.github.io/gatekeeper-library/website/` antes de criar um novo `ConstraintTemplate` customizado e utilize o recurso de `External data` quando a decisão de política depender de fontes externas ao API Server (como verificadores de assinatura ou inventários externos).

## Exemplo
A equipe de segurança importa da `gatekeeper-library` os templates padrão de segurança de pods e instancia apenas as `Constraints` com os parâmetros da organização.

## Limites e trade-offs
Provedores de `External data` são chamados durante o fluxo de avaliação; garanta baixa latência e alta disponibilidade do provedor externo para não degradar o tempo de resposta dos webhooks de admissão.

## Como verificar
Conferi as seções How is Gatekeeper different from OPA? e Policy Library no README oficial de open-policy-agent/gatekeeper.

## Conexões
- [[gatekeeper-enforcement-action-deny-dryrun-warn]] — Veja também: Modos de ação em violações (`enforcementAction`): deny, dryrun e warn.
- [[gatekeeper-cncf-governance-security-and-opa-version]] — Veja também: Governança sob o Código de Conduta da CNCF, processo de segurança e versão do motor OPA.

## Fontes
- [OPA Gatekeeper — GitHub README](https://raw.githubusercontent.com/open-policy-agent/gatekeeper/master/README.md) — Visão geral do Gatekeeper em comparação ao OPA com sidecar kube-mgmt (Gatekeeper v1.0), CRDs de constraints/templates/mutação, auditoria, external data e biblioteca de políticas.; consultado em 2026-10-03.
- [OPA Gatekeeper Documentation — How to use Gatekeeper (howto.md)](https://raw.githubusercontent.com/open-policy-agent/gatekeeper/master/website/docs/howto.md) — Guia oficial do Gatekeeper detalhando OPA Constraint Framework, ConstraintTemplate (openAPIV3Schema e Rego), Constraint, os 7 seletores de match, escopo Cluster vs Namespaced e enforcementAction (deny, dryrun, warn).; consultado em 2026-10-03.
