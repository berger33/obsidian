---
id: software.devops.tranche12.001157
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
fontes: ["https://rbac-manager.docs.fairwinds.com/introduction/", "https://rbac-manager.docs.fairwinds.com/rbacdefinitions/", "https://raw.githubusercontent.com/FairwindsOps/rbac-manager/master/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Fairwinds RBAC Manager: Mapeamento de Grupos OIDC e IAM em Clusters EKS, GKE e AKS

## Em uma frase
Combinar `RBACDefinition` com grupos provenientes de provedores OIDC (Keycloak, Dex, Okta, Entra ID) ou mapeamentos IAM em EKS, GKE e AKS permite gerenciar autorização de equipes inteiras no Kubernetes sem listar e-mails individuais sempre que um engenheiro entra ou sai do time.

## Por que importa
Embora ainda seja comum ver `kind: User` nominal em exemplos básicos, manter dezenas de usuários individuais em arquivos YAML exige Pull Requests constantes de onboarding e offboarding no repositório de plataforma.

## Como funciona
Configurada a autenticação do API Server (ou `aws-auth` / EKS Access Entries / GKE Google Groups / AKS Entra ID), a `RBACDefinition` referencia apenas `kind: Group` (por exemplo, `name: platform-admins`, `name: data-engineers`) e distribui `clusterRoleBindings` e `roleBindings` granulares por namespace.

## Exemplo
```yaml
apiVersion: rbacmanager.reactiveops.io/v1beta1
kind: RBACDefinition
metadata:
  name: oidc-groups-authorization
rbacBindings:
  - name: observability-readers
    subjects:
      - kind: Group
        name: oidc:sre-oncall
    roleBindings:
      - namespace: monitoring
        clusterRole: view
      - namespace: logging
        clusterRole: view
```

## Limites e trade-offs
Incluir um prefixo de grupo incorreto na `RBACDefinition` (por exemplo, esquecer o `oidc:` configurado em `--oidc-groups-prefix` no kube-apiserver) faz com que o `RoleBinding` seja criado sem erros, mas nunca coincida com o token JWT do usuário.

## Como verificar
Valide as claims de grupo do token OIDC e teste o acesso efetivo com `kubectl auth can-i get pods -n monitoring --as=usuario --as-group=oidc:sre-oncall`.

## Conexões
- [[rbacmanager-instalacao-helm-migracao-registry-pkg-dev]] — Veja também: Fairwinds RBAC Manager: Instalação via Helm e Migração para Imagens Assinadas em us-docker.pkg.dev.
- [[rbacmanager-auditoria-combinada-rbac-lookup-visibilidade]] — Veja também: Fairwinds RBAC Manager: Auditoria de Permissões Efetivas em Conjunto com rbac-lookup.

## Fontes
- [Fairwinds RBAC Manager Official Documentation — Introduction & RBACDefinitions (RoleRef Updates, Binding Removal & Dynamic namespaceSelector)](https://rbac-manager.docs.fairwinds.com/introduction/) — Documentação oficial do RBAC Manager explicando a CRD RBACDefinition (rbacmanager.reactiveops.io/v1beta1), recriação automática de RoleBindings, revogação por ownerReferences e namespaceSelector com matchLabels/matchExpressions; consultado em 2026-10-03.
- [Fairwinds RBAC Manager GitHub — README.md (Operator Overview & v1.10.0+ Signed Immutable Registry Migration)](https://rbac-manager.docs.fairwinds.com/rbacdefinitions/) — README oficial do FairwindsOps/rbac-manager documentando a arquitetura do operador e a migração na v1.10.0+ para us-docker.pkg.dev/fairwinds-ops/oss/rbac-manager; consultado em 2026-10-03.
- [Fairwinds RBAC Manager — Official Documentation Portal](https://raw.githubusercontent.com/FairwindsOps/rbac-manager/master/README.md) — Portal oficial do Fairwinds RBAC Manager; consultado em 2026-10-03.
