---
id: software.devops.tranche12.001155
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

# Fairwinds RBAC Manager: Provisionamento Declarativo de ServiceAccounts e Bindings Associados

## Em uma frase
Quando um `subject` dentro de `rbacBindings` é declarado com `kind: ServiceAccount` e `namespace`, o RBAC Manager cria automaticamente o objeto `ServiceAccount` caso ele ainda não exista e o vincula aos `roleBindings` e `clusterRoleBindings` especificados.

## Por que importa
Provisionar contas de serviço para agentes de CI/CD, coletores de métricas ou jobs de automação normalmente exige manter manifestos separados de `ServiceAccount`, `RoleBinding` em múltiplos namespaces e `ClusterRoleBinding`.

## Como funciona
Na `RBACDefinition`, basta declarar o `subject` com `kind: ServiceAccount`, `name: ci-bot` e `namespace: rbac-manager` (ou o namespace de automação) e listar os `roleBindings` (fixos ou via `namespaceSelector`). O operador garante a existência da `ServiceAccount` e mantém todos os vínculos de permissão reconciliados.

## Exemplo
```yaml
apiVersion: rbacmanager.reactiveops.io/v1beta1
kind: RBACDefinition
metadata:
  name: automation-service-accounts
rbacBindings:
  - name: release-bot
    subjects:
      - kind: ServiceAccount
        name: helm-deployer
        namespace: cicd-system
    roleBindings:
      - clusterRole: admin
        namespaceSelector:
          matchLabels:
            managed-by: helm-deployer
```

## Limites e trade-offs
Especificar um `namespace` inexistente no `subject` do `ServiceAccount` impede a criação da conta de serviço até que o namespace seja criado, pois o RBAC Manager gerencia RBAC e ServiceAccounts, mas não cria objetos `Namespace`.

## Como verificar
Garanta que o namespace de hospedagem do `ServiceAccount` exista previamente e confirme a criação com `kubectl get sa -n cicd-system helm-deployer`.

## Conexões
- [[rbacmanager-namespaceselector-matchlabels-matchexpressions-dinamico]] — Veja também: Fairwinds RBAC Manager: RoleBindings Dinâmicos com namespaceSelector (matchLabels e matchExpressions).
- [[rbacmanager-instalacao-helm-migracao-registry-pkg-dev]] — Veja também: Fairwinds RBAC Manager: Instalação via Helm e Migração para Imagens Assinadas em us-docker.pkg.dev.

## Fontes
- [Fairwinds RBAC Manager Official Documentation — Introduction & RBACDefinitions (RoleRef Updates, Binding Removal & Dynamic namespaceSelector)](https://rbac-manager.docs.fairwinds.com/rbacdefinitions/) — Documentação oficial do RBAC Manager explicando a CRD RBACDefinition (rbacmanager.reactiveops.io/v1beta1), recriação automática de RoleBindings, revogação por ownerReferences e namespaceSelector com matchLabels/matchExpressions; consultado em 2026-10-03.
- [Fairwinds RBAC Manager GitHub — README.md (Operator Overview & v1.10.0+ Signed Immutable Registry Migration)](https://rbac-manager.docs.fairwinds.com/introduction/) — README oficial do FairwindsOps/rbac-manager documentando a arquitetura do operador e a migração na v1.10.0+ para us-docker.pkg.dev/fairwinds-ops/oss/rbac-manager; consultado em 2026-10-03.
- [Fairwinds RBAC Manager — Official Documentation Portal](https://raw.githubusercontent.com/FairwindsOps/rbac-manager/master/README.md) — Portal oficial do Fairwinds RBAC Manager; consultado em 2026-10-03.
