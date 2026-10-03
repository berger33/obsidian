---
id: software.devops.tranche12.001159
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

# Fairwinds RBAC Manager: Prevenção de Escalação de Privilégios no Acesso à CRD RBACDefinition

## Em uma frase
Como o controlador do RBAC Manager possui permissões amplas no cluster para criar `ClusterRoleBindings` (incluindo vínculo com `cluster-admin`) e `RoleBindings` em qualquer namespace, o acesso de escrita (`create`, `update`, `patch`, `delete`) sobre a CRD `rbacdefinitions.rbacmanager.reactiveops.io` é equivalente a administrador total do cluster.

## Por que importa
Conceder permissão de edição em `rbacdefinitions` a desenvolvedores ou a um pipeline de CI de aplicação permite que qualquer usuário crie um `clusterRoleBinding` vinculando sua própria conta ao papel `cluster-admin`.

## Como funciona
O RBAC do próprio cluster deve restringir os verbos `create`, `update`, `patch` e `delete` no recurso `rbacdefinitions` (grupo `rbacmanager.reactiveops.io`) exclusivamente ao controlador GitOps da plataforma (Argo CD / Flux) e aos administradores de segurança, concedendo no máximo `get` e `list` para auditoria.

## Exemplo
```bash
# Verificar quem pode modificar RBACDefinitions no cluster:
kubectl auth can-i create rbacdefinitions.rbacmanager.reactiveops.io --as=system:serviceaccount:default:default
kubectl auth can-i update rbacdefinitions.rbacmanager.reactiveops.io --as-group=system:authenticated
```

## Limites e trade-offs
Incluir `apiGroups: ["*"]` ou `resources: ["*"]` em uma `Role` ou `ClusterRole` delegada a equipes de desenvolvimento expõe inadvertidamente a CRD `RBACDefinition` (que é um recurso cluster-scoped), abrindo vetor direto de escalação de privilégio.

## Como verificar
Certifique-se de que nenhuma `ClusterRole` não administrativa inclua `rbacmanager.reactiveops.io` ou curingas `*`, e valide o bloqueio com `kubectl auth can-i create rbacdefinitions`.

## Conexões
- [[rbacmanager-auditoria-combinada-rbac-lookup-visibilidade]] — Veja também: Fairwinds RBAC Manager: Auditoria de Permissões Efetivas em Conjunto com rbac-lookup.
- [[rbacmanager-padroes-gitops-separacao-roles-customizadas-bindings]] — Veja também: Fairwinds RBAC Manager: Padrão GitOps Separando Definição de Roles/ClusterRoles e RBACDefinitions.

## Fontes
- [Fairwinds RBAC Manager Official Documentation — Introduction & RBACDefinitions (RoleRef Updates, Binding Removal & Dynamic namespaceSelector)](https://rbac-manager.docs.fairwinds.com/rbacdefinitions/) — Documentação oficial do RBAC Manager explicando a CRD RBACDefinition (rbacmanager.reactiveops.io/v1beta1), recriação automática de RoleBindings, revogação por ownerReferences e namespaceSelector com matchLabels/matchExpressions; consultado em 2026-10-03.
- [Fairwinds RBAC Manager GitHub — README.md (Operator Overview & v1.10.0+ Signed Immutable Registry Migration)](https://rbac-manager.docs.fairwinds.com/introduction/) — README oficial do FairwindsOps/rbac-manager documentando a arquitetura do operador e a migração na v1.10.0+ para us-docker.pkg.dev/fairwinds-ops/oss/rbac-manager; consultado em 2026-10-03.
- [Fairwinds RBAC Manager — Official Documentation Portal](https://raw.githubusercontent.com/FairwindsOps/rbac-manager/master/README.md) — Portal oficial do Fairwinds RBAC Manager; consultado em 2026-10-03.
