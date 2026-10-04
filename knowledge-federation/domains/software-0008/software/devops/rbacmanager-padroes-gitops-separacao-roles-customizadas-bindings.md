---
id: software.devops.tranche12.001160
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

# Fairwinds RBAC Manager: Padrão GitOps Separando Definição de Roles/ClusterRoles e RBACDefinitions

## Em uma frase
Como o RBAC Manager gerencia `RoleBindings`, `ClusterRoleBindings` e `ServiceAccounts` — mas não substitui a definição de `Roles` e `ClusterRoles` em si —, a arquitetura GitOps recomendada mantém um catálogo enxuto de `ClusterRoles` reutilizáveis versionado junto às `RBACDefinitions` que atribuem esses papéis aos sujeitos.

## Por que importa
Tentar declarar regras de verbos e recursos (`rules: [apiGroups, resources, verbs]`) diretamente dentro de uma `RBACDefinition` falha porque o escopo deliberado do operador é simplificar o vínculo (`binding`) entre sujeitos e papéis existentes.

## Como funciona
No repositório GitOps da plataforma, definem-se primeiro as `ClusterRoles` padrão da organização (além das nativas `view`, `edit` e `admin` do Kubernetes) e, em seguida, aplicam-se as `RBACDefinitions` por unidade organizacional ou por classe de automação, referenciando essas `ClusterRoles` em `roleBindings` (com escopo de namespace) ou `clusterRoleBindings` (escopo global).

## Exemplo
```yaml
# Referenciando uma ClusterRole em escopo de namespace via roleBindings:
apiVersion: rbacmanager.reactiveops.io/v1beta1
kind: RBACDefinition
metadata:
  name: squad-payments-rbac
rbacBindings:
  - name: payments-devs
    subjects:
      - kind: Group
        name: oidc:squad-payments
    roleBindings:
      - clusterRole: edit
        namespaceSelector:
          matchLabels:
            squad: payments
```

## Limites e trade-offs
Referenciar em `roleBindings` ou `clusterRoleBindings` de uma `RBACDefinition` uma `ClusterRole` customizada que ainda não foi aplicada no cluster deixa o binding apontando para um papel inexistente (que não concede permissão alguma no Kubernetes).

## Como verificar
Aplique sempre `ClusterRoles` e `Roles` antes (ou na mesma onda de sincronização GitOps) das `RBACDefinitions` e verifique os logs do pod `rbac-manager` para confirmar reconciliação sem erros.

## Conexões
- [[rbacmanager-seguranca-escalacao-privilegios-controle-acesso-crd]] — Veja também: Fairwinds RBAC Manager: Prevenção de Escalação de Privilégios no Acesso à CRD RBACDefinition.

## Fontes
- [Fairwinds RBAC Manager Official Documentation — Introduction & RBACDefinitions (RoleRef Updates, Binding Removal & Dynamic namespaceSelector)](https://rbac-manager.docs.fairwinds.com/rbacdefinitions/) — Documentação oficial do RBAC Manager explicando a CRD RBACDefinition (rbacmanager.reactiveops.io/v1beta1), recriação automática de RoleBindings, revogação por ownerReferences e namespaceSelector com matchLabels/matchExpressions; consultado em 2026-10-03.
- [Fairwinds RBAC Manager GitHub — README.md (Operator Overview & v1.10.0+ Signed Immutable Registry Migration)](https://rbac-manager.docs.fairwinds.com/introduction/) — README oficial do FairwindsOps/rbac-manager documentando a arquitetura do operador e a migração na v1.10.0+ para us-docker.pkg.dev/fairwinds-ops/oss/rbac-manager; consultado em 2026-10-03.
- [Fairwinds RBAC Manager — Official Documentation Portal](https://raw.githubusercontent.com/FairwindsOps/rbac-manager/master/README.md) — Portal oficial do Fairwinds RBAC Manager; consultado em 2026-10-03.
