---
id: software.devops.tranche12.001152
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

# Fairwinds RBAC Manager: Recriação Automática de RoleBindings ao Alterar roleRef

## Em uma frase
Na API nativa de RBAC do Kubernetes (`rbac.authorization.k8s.io/v1`), o campo `roleRef` de um `RoleBinding` ou `ClusterRoleBinding` é estritamente imutável após a criação, e o RBAC Manager resolve essa limitação deletando e recriando automaticamente o binding quando o papel muda na `RBACDefinition`.

## Por que importa
Em fluxos GitOps ou pipelines CI/CD tradicionais, alterar o papel de um grupo de `edit` para `view` em um manifesto `RoleBinding` falha no `kubectl apply` com erro de campo imutável (`cannot change roleRef`), exigindo intervenção manual para deletar o objeto antes de reaplicar.

## Como funciona
Quando o operador RBAC Manager detecta que o campo `clusterRole` ou `role` dentro de `roleBindings` ou `clusterRoleBindings` de uma `RBACDefinition` foi modificado, ele executa de forma transparente a remoção do `RoleBinding` antigo e a criação imediata do novo `RoleBinding` com o `roleRef` atualizado.

## Exemplo
```bash
# Ao alterar clusterRole de 'edit' para 'view' na RBACDefinition:
kubectl apply -f rbacdefinition-devs.yaml
kubectl get events -n rbac-manager --sort-by='.lastTimestamp'
kubectl get rolebinding -n checkout -o wide
```

## Limites e trade-offs
Manter tanto um manifesto `RoleBinding` estático quanto uma `RBACDefinition` tentando gerenciar o mesmo nome de binding no mesmo namespace gera conflitos contínuos de propriedade.

## Como verificar
Deixe o ciclo de vida completo dos `RoleBindings` sob responsabilidade exclusiva da `RBACDefinition` e valide nos logs do controlador a recriação limpa ao trocar `clusterRole`.

## Conexões
- [[rbacmanager-operador-declarativo-rbacdefinition-crd]] — Veja também: Fairwinds RBAC Manager: Operador Declarativo e CRD RBACDefinition no Kubernetes.
- [[rbacmanager-revogacao-acesso-remocao-bindings-ownerreferences]] — Veja também: Fairwinds RBAC Manager: Revogação Automática de Acessos e Limpeza de RoleBindings Órfãos.

## Fontes
- [Fairwinds RBAC Manager Official Documentation — Introduction & RBACDefinitions (RoleRef Updates, Binding Removal & Dynamic namespaceSelector)](https://rbac-manager.docs.fairwinds.com/introduction/) — Documentação oficial do RBAC Manager explicando a CRD RBACDefinition (rbacmanager.reactiveops.io/v1beta1), recriação automática de RoleBindings, revogação por ownerReferences e namespaceSelector com matchLabels/matchExpressions; consultado em 2026-10-03.
- [Fairwinds RBAC Manager GitHub — README.md (Operator Overview & v1.10.0+ Signed Immutable Registry Migration)](https://rbac-manager.docs.fairwinds.com/rbacdefinitions/) — README oficial do FairwindsOps/rbac-manager documentando a arquitetura do operador e a migração na v1.10.0+ para us-docker.pkg.dev/fairwinds-ops/oss/rbac-manager; consultado em 2026-10-03.
- [Fairwinds RBAC Manager — Official Documentation Portal](https://raw.githubusercontent.com/FairwindsOps/rbac-manager/master/README.md) — Portal oficial do Fairwinds RBAC Manager; consultado em 2026-10-03.
