---
id: software.devops.tranche03.000236
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

# Armadilha de escopo: match vazio (inclusivo para tudo) e impacto sobre recursos Cluster-scoped

## Em uma frase
No parágrafo final da subseção `The match field`, o guia oficial `website/docs/howto.md` faz dois alertas críticos de operação: (1) um matcher vazio ou um campo `match` não definido é considerado **inclusivo** (casa com absolutamente todos os recursos do cluster); e (2) os seletores `namespaces`, `excludedNamespaces` e `namespaceSelector` **continuarão casando com recursos cluster-scoped** (que não pertencem a nenhum namespace), sendo necessário ajustar `scope: Namespaced` para evitar esse comportamento.

## Por que importa
Esse é um dos erros mais frequentes ao escrever Constraints: um administrador define `excludedNamespaces: ["kube-system"]` achando que restringiu a regra a objetos de namespaces comuns, mas como `scope` tem padrão `*`, a regra passa a avaliar também `ClusterRoles`, `Nodes`, `PersistentVolumes` e `Namespaces` se `kinds` não estiver restrito ou se `scope: Namespaced` não for declarado.

## Como funciona
Sempre defina `kinds` explicitamente e configure `scope: Namespaced` quando criar uma Constraint que utiliza `namespaces`, `excludedNamespaces` ou `namespaceSelector` e deve aplicar-se apenas a recursos dentro de namespaces.

## Exemplo
Uma Constraint que exige um label específico usa `scope: Namespaced` junto com `excludedNamespaces: ["kube-*"]` para garantir que objetos globais do cluster (cluster-scoped) não sejam bloqueados indevidamente.

## Limites e trade-offs
Nunca aplique uma Constraint em produção com o bloco `spec.match` vazio, pois ela interceptará todos os tipos de recursos da API do Kubernetes.

## Como verificar
Conferi o último parágrafo da subseção The match field em `website/docs/howto.md` de open-policy-agent/gatekeeper.

## Conexões
- [[gatekeeper-match-field-selectors-and-glob-support]] — Veja também: Os sete seletores do campo match e suporte a globs baseados em prefixo.
- [[gatekeeper-parameters-validation-and-input-review]] — Veja também: Validação de tipos de spec.parameters pelo API Server e objeto input.review no Rego.

## Fontes
- [OPA Gatekeeper Documentation — How to use Gatekeeper (howto.md)](https://raw.githubusercontent.com/open-policy-agent/gatekeeper/master/website/docs/howto.md) — Guia oficial do Gatekeeper detalhando OPA Constraint Framework, ConstraintTemplate (openAPIV3Schema e Rego), Constraint, os 7 seletores de match, escopo Cluster vs Namespaced e enforcementAction (deny, dryrun, warn).; consultado em 2026-10-03.
- [OPA Gatekeeper — GitHub README](https://raw.githubusercontent.com/open-policy-agent/gatekeeper/master/README.md) — Visão geral do Gatekeeper em comparação ao OPA com sidecar kube-mgmt (Gatekeeper v1.0), CRDs de constraints/templates/mutação, auditoria, external data e biblioteca de políticas.; consultado em 2026-10-03.
