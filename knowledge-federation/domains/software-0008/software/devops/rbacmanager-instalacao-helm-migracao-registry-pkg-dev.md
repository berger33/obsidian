---
id: software.devops.tranche12.001156
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

# Fairwinds RBAC Manager: Instalação via Helm e Migração para Imagens Assinadas em us-docker.pkg.dev

## Em uma frase
O RBAC Manager é instalado no cluster via Helm chart (`fairwinds-stable/rbac-manager`) e, a partir da versão `v1.10.0`, utiliza imagens assinadas e tags imutáveis hospedadas em `us-docker.pkg.dev/fairwinds-ops/oss/rbac-manager`, substituindo o repositório legado depreciado `quay.io/reactiveops/rbac-manager`.

## Por que importa
Manter implantações antigas apontando para `quay.io/reactiveops/rbac-manager` ou dependendo de tags flutuantes (`v1`, `v1.9`, `latest`) impede a aplicação de correções de segurança e viola políticas de imutabilidade de imagens em produção.

## Como funciona
A instalação padrão adiciona o repositório Helm `https://charts.fairwinds.com/stable` e instala o chart no namespace `rbac-manager`, registrando a CRD `rbacdefinitions.rbacmanager.reactiveops.io` e subindo o Deployment do operador com imagem pinada por versão semântica completa (`v<major>.<minor>.<patch>`) ou digest `@sha256`.

## Exemplo
```bash
helm repo add fairwinds-stable https://charts.fairwinds.com/stable
helm repo update
helm upgrade --install rbac-manager fairwinds-stable/rbac-manager \
  --namespace rbac-manager --create-namespace \
  --set image.repository=us-docker.pkg.dev/fairwinds-ops/oss/rbac-manager
kubectl get pods -n rbac-manager
```

## Limites e trade-offs
Desinstalar o Helm release do `rbac-manager` com remoção da CRD `rbacdefinitions` apaga todas as `RBACDefinitions` e, por consequência das `ownerReferences`, destrói todos os `RoleBindings` gerenciados no cluster.

## Como verificar
Ao atualizar o chart Helm do `rbac-manager`, verifique sempre que a CRD `rbacdefinitions.rbacmanager.reactiveops.io` permanece intacta e que a imagem vem de `us-docker.pkg.dev/fairwinds-ops/oss/rbac-manager`.

## Conexões
- [[rbacmanager-gestao-serviceaccounts-automacao-bots-ci]] — Veja também: Fairwinds RBAC Manager: Provisionamento Declarativo de ServiceAccounts e Bindings Associados.
- [[rbacmanager-integracao-oidc-grupos-idp-eks-gke-aks]] — Veja também: Fairwinds RBAC Manager: Mapeamento de Grupos OIDC e IAM em Clusters EKS, GKE e AKS.

## Fontes
- [Fairwinds RBAC Manager Official Documentation — Introduction & RBACDefinitions (RoleRef Updates, Binding Removal & Dynamic namespaceSelector)](https://raw.githubusercontent.com/FairwindsOps/rbac-manager/master/README.md) — Documentação oficial do RBAC Manager explicando a CRD RBACDefinition (rbacmanager.reactiveops.io/v1beta1), recriação automática de RoleBindings, revogação por ownerReferences e namespaceSelector com matchLabels/matchExpressions; consultado em 2026-10-03.
- [Fairwinds RBAC Manager GitHub — README.md (Operator Overview & v1.10.0+ Signed Immutable Registry Migration)](https://rbac-manager.docs.fairwinds.com/introduction/) — README oficial do FairwindsOps/rbac-manager documentando a arquitetura do operador e a migração na v1.10.0+ para us-docker.pkg.dev/fairwinds-ops/oss/rbac-manager; consultado em 2026-10-03.
- [Fairwinds RBAC Manager — Official Documentation Portal](https://rbac-manager.docs.fairwinds.com/rbacdefinitions/) — Portal oficial do Fairwinds RBAC Manager; consultado em 2026-10-03.
