---
id: software.devops.tranche12.001151
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
fontes: ["https://raw.githubusercontent.com/FairwindsOps/rbac-manager/master/README.md", "https://rbac-manager.docs.fairwinds.com/introduction/", "https://rbac-manager.docs.fairwinds.com/rbacdefinitions/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Fairwinds RBAC Manager: Operador Declarativo e CRD RBACDefinition no Kubernetes

## Em uma frase
O Fairwinds RBAC Manager é um operador Kubernetes open-source que simplifica a gestão de autorização em escala por meio da Custom Resource Definition `RBACDefinition` (`apiVersion: rbacmanager.reactiveops.io/v1beta1`), permitindo declarar `ClusterRoleBindings`, `RoleBindings` e `ServiceAccounts` desejados em um único recurso conciso.

## Por que importa
Gerenciar dezenas de objetos `RoleBinding` e `ClusterRoleBinding` nativos separadamente por usuário, grupo e namespace gera repetição massiva de YAML e dificulta auditar quem possui qual acesso no cluster.

## Como funciona
O controlador do RBAC Manager observa recursos `RBACDefinition` no cluster e reconcilia continuamente a lista `rbacBindings`. Para cada entrada, ele cria, atualiza ou remove os `ServiceAccounts`, `RoleBindings` e `ClusterRoleBindings` correspondentes, registrando `ownerReferences` para manter o estado real sincronizado com a especificação declarada.

## Exemplo
```yaml
apiVersion: rbacmanager.reactiveops.io/v1beta1
kind: RBACDefinition
metadata:
  name: platform-team-access
rbacBindings:
  - name: sres
    subjects:
      - kind: Group
        name: oidc:sre-team
    clusterRoleBindings:
      - clusterRole: view
  - name: app-devs
    subjects:
      - kind: User
        name: alice@example.com
    roleBindings:
      - namespace: checkout
        clusterRole: edit
```

## Limites e trade-offs
Editar manualmente um `RoleBinding` que foi criado e possui `ownerReference` apontando para uma `RBACDefinition` faz com que a alteração manual seja revertida pelo operador na próxima reconciliação.

## Como verificar
Aplique sempre mudanças de permissão na `RBACDefinition` de origem e verifique os recursos gerados com `kubectl get rolebindings,clusterrolebindings -A -l rbac-manager=reactiveops`.

## Conexões
- [[rbacmanager-atualizacao-imutavel-roleref-recriacao-automatica]] — Veja também: Fairwinds RBAC Manager: Recriação Automática de RoleBindings ao Alterar roleRef.

## Fontes
- [Fairwinds RBAC Manager Official Documentation — Introduction & RBACDefinitions (RoleRef Updates, Binding Removal & Dynamic namespaceSelector)](https://raw.githubusercontent.com/FairwindsOps/rbac-manager/master/README.md) — Documentação oficial do RBAC Manager explicando a CRD RBACDefinition (rbacmanager.reactiveops.io/v1beta1), recriação automática de RoleBindings, revogação por ownerReferences e namespaceSelector com matchLabels/matchExpressions; consultado em 2026-10-03.
- [Fairwinds RBAC Manager GitHub — README.md (Operator Overview & v1.10.0+ Signed Immutable Registry Migration)](https://rbac-manager.docs.fairwinds.com/introduction/) — README oficial do FairwindsOps/rbac-manager documentando a arquitetura do operador e a migração na v1.10.0+ para us-docker.pkg.dev/fairwinds-ops/oss/rbac-manager; consultado em 2026-10-03.
- [Fairwinds RBAC Manager — Official Documentation Portal](https://rbac-manager.docs.fairwinds.com/rbacdefinitions/) — Portal oficial do Fairwinds RBAC Manager; consultado em 2026-10-03.
