---
id: software.devops.tranche03.000235
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

# Os sete seletores do campo match e suporte a globs baseados em prefixo

## Em uma frase
A subseção `The match field` de `website/docs/howto.md` documenta os sete tipos de seletores suportados em `spec.match`: `kinds` (lista de objetos com `apiGroups` e `kinds`, bastando um match dentro da lista), `scope` (`*`, `Cluster` ou `Namespaced`, com padrão `*`), `namespaces` (lista de namespaces incluídos, suportando glob por prefixo como `kube-*`), `excludedNamespaces` (lista de namespaces excluídos, também suportando glob por prefixo como `kube-*`), `labelSelector` (`matchLabels` e `matchExpressions` combinados com AND), `namespaceSelector` (seletor de labels contra o namespace contenedor ou o próprio Namespace) e `name` (nome do objeto, suportando glob por prefixo como `pod-*`).

## Por que importa
Conhecer a combinação exata desses sete seletores — e o suporte a globs por prefixo como `kube-*` em `namespaces`/`excludedNamespaces` e `pod-*` em `name` — permite excluir namespaces de sistema (como `kube-system` e `kube-public`) sem precisar listar manualmente cada sub-namespace futuro.

## Como funciona
Utilize `excludedNamespaces: ["kube-*"]` e seletores `kinds` explícitos nas suas Constraints para evitar que políticas voltadas a aplicações de usuário bloqueiem pods críticos do plano de controle do Kubernetes.

## Exemplo
Uma Constraint aplica uma política a todos os Deployments, exceto nos namespaces que casam com o glob de prefixo `kube-*`.

## Limites e trade-offs
O guia destaca que, quando múltiplos matchers de topo (`kinds`, `namespaces`, `labelSelector`, etc.) são especificados juntos, o recurso precisa satisfazer **todos** os matchers de topo (lógica AND entre eles) para entrar no escopo da Constraint.

## Como verificar
Conferi a subseção The match field em `website/docs/howto.md` de open-policy-agent/gatekeeper.

## Conexões
- [[gatekeeper-constraint-instantiation-and-listing]] — Veja também: Instanciação declarativa de Constraints (`constraints.gatekeeper.sh/v1beta1`) e inspeção com kubectl get constraints.
- [[gatekeeper-empty-matcher-and-cluster-scoped-gotcha]] — Veja também: Armadilha de escopo: match vazio (inclusivo para tudo) e impacto sobre recursos Cluster-scoped.

## Fontes
- [OPA Gatekeeper Documentation — How to use Gatekeeper (howto.md)](https://raw.githubusercontent.com/open-policy-agent/gatekeeper/master/website/docs/howto.md) — Guia oficial do Gatekeeper detalhando OPA Constraint Framework, ConstraintTemplate (openAPIV3Schema e Rego), Constraint, os 7 seletores de match, escopo Cluster vs Namespaced e enforcementAction (deny, dryrun, warn).; consultado em 2026-10-03.
- [OPA Gatekeeper — GitHub README](https://raw.githubusercontent.com/open-policy-agent/gatekeeper/master/README.md) — Visão geral do Gatekeeper em comparação ao OPA com sidecar kube-mgmt (Gatekeeper v1.0), CRDs de constraints/templates/mutação, auditoria, external data e biblioteca de políticas.; consultado em 2026-10-03.
