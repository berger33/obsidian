---
id: software.devops.tranche03.000238
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

# Modos de ação em violações (`enforcementAction`): deny, dryrun e warn

## Em uma frase
A subseção `The enforcementAction field` de `website/docs/howto.md` documenta que o campo `enforcementAction` define como o Gatekeeper trata violações de uma Constraint: por padrão, `enforcementAction` é definido como `deny` (negando requisições de admissão que apresentem qualquer violação), mas também suporta `dryrun` (avalia e registra para auditoria sem bloquear a requisição) e `warn` (permite a requisição, mas retorna um aviso imediato ao cliente, como na saída do `kubectl`), remetendo a `violations.md` para detalhes.

## Por que importa
Implantar uma política nova diretamente em modo `deny` em um cluster compartilhado por dezenas de pipelines de CI/CD pode interromper deploys urgentes; promover gradualmente de `dryrun` -> `warn` -> `deny` dá visibilidade às equipes antes do bloqueio definitivo.

## Como funciona
Adote um ciclo de rollout em três fases para qualquer nova Constraint: inicie com `enforcementAction: dryrun` para medir o impacto na auditoria, avance para `enforcementAction: warn` para educar os desenvolvedores no terminal/CI e finalize com `deny`.

## Exemplo
Durante duas semanas de transição, os desenvolvedores recebem um `Warning` no `kubectl apply` graças a `enforcementAction: warn`, ajustam seus manifestos Helm/Kustomize e só então a plataforma muda a Constraint para `deny`.

## Limites e trade-offs
Lembre-se de que omitir o campo `enforcementAction` na Constraint ativa automaticamente o comportamento padrão `deny`.

## Como verificar
Conferi a subseção The enforcementAction field em `website/docs/howto.md` de open-policy-agent/gatekeeper.

## Conexões
- [[gatekeeper-parameters-validation-and-input-review]] — Veja também: Validação de tipos de spec.parameters pelo API Server e objeto input.review no Rego.
- [[gatekeeper-policy-library-and-external-data]] — Veja também: Biblioteca oficial Gatekeeper Policy Library e suporte a dados externos.

## Fontes
- [OPA Gatekeeper Documentation — How to use Gatekeeper (howto.md)](https://raw.githubusercontent.com/open-policy-agent/gatekeeper/master/website/docs/howto.md) — Guia oficial do Gatekeeper detalhando OPA Constraint Framework, ConstraintTemplate (openAPIV3Schema e Rego), Constraint, os 7 seletores de match, escopo Cluster vs Namespaced e enforcementAction (deny, dryrun, warn).; consultado em 2026-10-03.
- [OPA Gatekeeper — GitHub README](https://raw.githubusercontent.com/open-policy-agent/gatekeeper/master/README.md) — Visão geral do Gatekeeper em comparação ao OPA com sidecar kube-mgmt (Gatekeeper v1.0), CRDs de constraints/templates/mutação, auditoria, external data e biblioteca de políticas.; consultado em 2026-10-03.
