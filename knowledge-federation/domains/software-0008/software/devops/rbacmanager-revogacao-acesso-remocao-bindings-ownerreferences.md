---
id: software.devops.tranche12.001153
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

# Fairwinds RBAC Manager: Revogação Automática de Acessos e Limpeza de RoleBindings Órfãos

## Em uma frase
Cada `RBACDefinition` é proprietária (`ownerReference`) de todos os `RoleBindings`, `ClusterRoleBindings` e `ServiceAccounts` que instancia, comparando continuamente o estado desejado atual com os recursos existentes no cluster para revogar e excluir imediatamente qualquer permissão removida do YAML.

## Por que importa
Em repositórios onde cada `RoleBinding` é um arquivo YAML separado aplicado via CI, remover um arquivo do Git nem sempre deleta o objeto do cluster se o pipeline não tiver poda (`prune`) perfeitamente configurada, deixando acessos revogados ativos indefinidamente.

## Como funciona
Ao remover um usuário da lista `subjects` ou excluir uma entrada de `roleBindings` dentro da `RBACDefinition` e aplicar o manifesto atualizado, o RBAC Manager consulta os recursos no cluster marcados com seus labels e `ownerReferences` e apaga prontamente os bindings que deixaram de constar na definição.

## Exemplo
```bash
kubectl get rolebindings -n web -l rbac-manager=reactiveops
# Apos remover um item de roleBindings na RBACDefinition e aplicar:
kubectl apply -f rbacdefinition.yaml
kubectl get rolebindings -n web -l rbac-manager=reactiveops
```

## Limites e trade-offs
Deletar a CRD `RBACDefinition` sem planejar a migração prévia dos bindings remove em cascata (via garbage collection do Kubernetes) todos os `RoleBindings` e `ServiceAccounts` filhos, cortando o acesso de usuários e bots imediatamente.

## Como verificar
Antes de excluir uma `RBACDefinition` em produção, revise todos os objetos dependentes listados por `kubectl get rolebindings,clusterrolebindings,sa -A -l rbac-manager=reactiveops`.

## Conexões
- [[rbacmanager-atualizacao-imutavel-roleref-recriacao-automatica]] — Veja também: Fairwinds RBAC Manager: Recriação Automática de RoleBindings ao Alterar roleRef.
- [[rbacmanager-namespaceselector-matchlabels-matchexpressions-dinamico]] — Veja também: Fairwinds RBAC Manager: RoleBindings Dinâmicos com namespaceSelector (matchLabels e matchExpressions).

## Fontes
- [Fairwinds RBAC Manager Official Documentation — Introduction & RBACDefinitions (RoleRef Updates, Binding Removal & Dynamic namespaceSelector)](https://rbac-manager.docs.fairwinds.com/introduction/) — Documentação oficial do RBAC Manager explicando a CRD RBACDefinition (rbacmanager.reactiveops.io/v1beta1), recriação automática de RoleBindings, revogação por ownerReferences e namespaceSelector com matchLabels/matchExpressions; consultado em 2026-10-03.
- [Fairwinds RBAC Manager GitHub — README.md (Operator Overview & v1.10.0+ Signed Immutable Registry Migration)](https://rbac-manager.docs.fairwinds.com/rbacdefinitions/) — README oficial do FairwindsOps/rbac-manager documentando a arquitetura do operador e a migração na v1.10.0+ para us-docker.pkg.dev/fairwinds-ops/oss/rbac-manager; consultado em 2026-10-03.
- [Fairwinds RBAC Manager — Official Documentation Portal](https://raw.githubusercontent.com/FairwindsOps/rbac-manager/master/README.md) — Portal oficial do Fairwinds RBAC Manager; consultado em 2026-10-03.
