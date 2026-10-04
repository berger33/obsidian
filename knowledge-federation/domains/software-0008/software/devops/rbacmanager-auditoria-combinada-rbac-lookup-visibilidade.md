---
id: software.devops.tranche12.001158
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

# Fairwinds RBAC Manager: Auditoria de Permissões Efetivas em Conjunto com rbac-lookup

## Em uma frase
A documentação oficial do RBAC Manager recomenda parear a gestão declarativa via `RBACDefinition` com a ferramenta complementar open-source `rbac-lookup` (`FairwindsOps/rbac-lookup`) para consultar rapidamente quais `Roles` e `ClusterRoles` estão vinculados a qualquer usuário, grupo ou `ServiceAccount` no cluster.

## Por que importa
Como uma única `RBACDefinition` com `namespaceSelector` pode gerar dezenas de `RoleBindings` distribuídos pelo cluster (além dos bindings nativos criados por charts Helm), visualizar a superfície total de acesso de um sujeito apenas com `kubectl get rolebindings` é trabalhoso.

## Como funciona
Enquanto o `rbac-manager` atua como o controlador que materializa o estado desejado a partir das `RBACDefinitions`, o `rbac-lookup` consulta a API do cluster e exibe em uma tabela consolidada o `SUBJECT`, `SCOPE` (namespace ou `cluster-wide`) e `ROLE`, indicando também a origem do vínculo.

## Exemplo
```bash
kubectl get rbacdefinitions.rbacmanager.reactiveops.io -A
kubectl auth can-i --list --namespace=web --as=dave@example.com
```

## Limites e trade-offs
Assumir que apenas as permissões declaradas nas `RBACDefinitions` existem no cluster ignora `ClusterRoleBindings` permissivos criados diretamente por operadores de terceiros fora do controle do RBAC Manager.

## Como verificar
Audite regularmente tanto as `RBACDefinitions` quanto a lista global de `RoleBindings` e `ClusterRoleBindings` do cluster usando `kubectl auth can-i` e ferramentas de visibilidade de RBAC.

## Conexões
- [[rbacmanager-integracao-oidc-grupos-idp-eks-gke-aks]] — Veja também: Fairwinds RBAC Manager: Mapeamento de Grupos OIDC e IAM em Clusters EKS, GKE e AKS.
- [[rbacmanager-seguranca-escalacao-privilegios-controle-acesso-crd]] — Veja também: Fairwinds RBAC Manager: Prevenção de Escalação de Privilégios no Acesso à CRD RBACDefinition.

## Fontes
- [Fairwinds RBAC Manager Official Documentation — Introduction & RBACDefinitions (RoleRef Updates, Binding Removal & Dynamic namespaceSelector)](https://rbac-manager.docs.fairwinds.com/introduction/) — Documentação oficial do RBAC Manager explicando a CRD RBACDefinition (rbacmanager.reactiveops.io/v1beta1), recriação automática de RoleBindings, revogação por ownerReferences e namespaceSelector com matchLabels/matchExpressions; consultado em 2026-10-03.
- [Fairwinds RBAC Manager GitHub — README.md (Operator Overview & v1.10.0+ Signed Immutable Registry Migration)](https://rbac-manager.docs.fairwinds.com/rbacdefinitions/) — README oficial do FairwindsOps/rbac-manager documentando a arquitetura do operador e a migração na v1.10.0+ para us-docker.pkg.dev/fairwinds-ops/oss/rbac-manager; consultado em 2026-10-03.
- [Fairwinds RBAC Manager — Official Documentation Portal](https://raw.githubusercontent.com/FairwindsOps/rbac-manager/master/README.md) — Portal oficial do Fairwinds RBAC Manager; consultado em 2026-10-03.
