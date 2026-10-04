---
id: software.devops.tranche12.001154
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-12.md"
fontes: ["https://rbac-manager.docs.fairwinds.com/rbacdefinitions/", "https://rbac-manager.docs.fairwinds.com/introduction/", "https://raw.githubusercontent.com/FairwindsOps/rbac-manager/master/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Fairwinds RBAC Manager: RoleBindings Dinâmicos com namespaceSelector (matchLabels e matchExpressions)

## Em uma frase
O RBAC Manager suporta o campo `namespaceSelector` (com `matchLabels` e `matchExpressions`) em vez de um `namespace` fixo nas entradas de `roleBindings`, criando automaticamente os `RoleBindings` em qualquer namespace atual ou futuro que corresponda aos labels.

## Por que importa
Em plataformas com namespaces efêmeros de preview por Pull Request ou multi-tenancy dinâmico por equipe (`team=payments`, `env=staging`), criar `RoleBindings` manualmente a cada novo namespace atrasa o fluxo e exige automação extra.

## Como funciona
O controlador do RBAC Manager observa eventos de criação e atualização de `Namespaces` no cluster. Assim que um namespace recebe o label correspondente ao `namespaceSelector` (por exemplo, `ci: edit` ou `app in (web, queue)`), o operador provisiona instantaneamente os `RoleBindings` declarados na `RBACDefinition` dentro daquele namespace.

## Exemplo
```yaml
apiVersion: rbacmanager.reactiveops.io/v1beta1
kind: RBACDefinition
metadata:
  name: dynamic-team-rbac
rbacBindings:
  - name: ci-deployer
    subjects:
      - kind: ServiceAccount
        name: ci-bot
        namespace: ci-system
    roleBindings:
      - clusterRole: edit
        namespaceSelector:
          matchExpressions:
            - key: environment
              operator: In
              values: ["dev", "staging"]
```

## Limites e trade-offs
Permitir que usuários sem privilégio administrativo editem os labels do próprio `Namespace` (por exemplo, adicionando `team=admin-target`) quando há `RBACDefinitions` baseadas em `namespaceSelector` pode permitir movimentação lateral de permissões.

## Como verificar
Restrinja a edição de labels de `Namespaces` via política de admissão (Kyverno/Gatekeeper) e verifique a criação automática de bindings ao rotular um namespace de teste.

## Conexões
- [[rbacmanager-revogacao-acesso-remocao-bindings-ownerreferences]] — Veja também: Fairwinds RBAC Manager: Revogação Automática de Acessos e Limpeza de RoleBindings Órfãos.
- [[rbacmanager-gestao-serviceaccounts-automacao-bots-ci]] — Veja também: Fairwinds RBAC Manager: Provisionamento Declarativo de ServiceAccounts e Bindings Associados.

## Fontes
- [Fairwinds RBAC Manager Official Documentation — Introduction & RBACDefinitions (RoleRef Updates, Binding Removal & Dynamic namespaceSelector)](https://rbac-manager.docs.fairwinds.com/rbacdefinitions/) — Documentação oficial do RBAC Manager explicando a CRD RBACDefinition (rbacmanager.reactiveops.io/v1beta1), recriação automática de RoleBindings, revogação por ownerReferences e namespaceSelector com matchLabels/matchExpressions; consultado em 2026-10-03.
- [Fairwinds RBAC Manager GitHub — README.md (Operator Overview & v1.10.0+ Signed Immutable Registry Migration)](https://rbac-manager.docs.fairwinds.com/introduction/) — README oficial do FairwindsOps/rbac-manager documentando a arquitetura do operador e a migração na v1.10.0+ para us-docker.pkg.dev/fairwinds-ops/oss/rbac-manager; consultado em 2026-10-03.
- [Fairwinds RBAC Manager — Official Documentation Portal](https://raw.githubusercontent.com/FairwindsOps/rbac-manager/master/README.md) — Portal oficial do Fairwinds RBAC Manager; consultado em 2026-10-03.
