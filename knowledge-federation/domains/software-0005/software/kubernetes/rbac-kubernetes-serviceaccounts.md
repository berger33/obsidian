---
id: software.kubernetes.rbac-serviceaccounts.000001
tipo: tecnica
dominio: software
subdominio: kubernetes
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: aprovada
revisor: usuario-da-sessao
data_revisao_humana: 2026-10-02
fontes: ["https://kubernetes.io/docs/reference/access-authn-authz/rbac/", "https://kubernetes.io/docs/concepts/security/service-accounts/"]
tags: [dominio/software, subdominio/kubernetes, qualidade/candidata]
aliases: [Kubernetes RBAC, RoleBinding, ClusterRoleBinding, ServiceAccount permissions]
lote: software-kubernetes-operacao-0005
---

# RBAC e permissões de ServiceAccount no Kubernetes

## Em uma frase
RBAC associa sujeitos a permissões aditivas; Roles e bindings com escopo adequado limitam o acesso de pessoas e workloads à API Kubernetes.

## Por que importa
Pods que não precisam consultar a API ainda podem herdar uma identidade de serviço configurada no workload. Permissões amplas ampliam o impacto de comprometimento e podem expor Secrets ou permitir alterações em recursos. Separar identidades por aplicação e conceder somente as ações necessárias reduz esse risco.

## Como funciona
`Role` define permissões em um namespace; `ClusterRole` é um recurso não namespaced e pode descrever permissões sobre recursos de cluster ou recursos namespaced. `RoleBinding` concede permissões dentro do namespace do binding e pode referenciar uma Role local ou uma ClusterRole. `ClusterRoleBinding` concede as permissões a nível de cluster. Regras RBAC são aditivas: não existem regras `deny` que removam permissões concedidas por outro binding. Uma ServiceAccount representa uma identidade de workload; o workload recebe permissões por bindings direcionados a essa identidade.

## Exemplo
Um worker que só precisa ler ConfigMaps de um namespace pode usar uma ServiceAccount dedicada e uma Role limitada a `get` nos recursos necessários, ligada por RoleBinding naquele namespace. Evite reutilizar uma conta ampla de implantação no runtime. Para Secrets, restrinja também leitura indireta por Pods que podem referenciá-los.

## Limites e trade-offs
Um RoleBinding para uma ClusterRole continua escopado ao namespace do binding para recursos namespaced; não o confunda com ClusterRoleBinding. Permissão de criar Pods pode permitir acesso a dados montados por outros Pods, mesmo sem `get` direto no Secret. RBAC não controla tráfego de rede, políticas de admission ou autorização dentro da aplicação.

## Como verificar
Liste os bindings efetivos do sujeito e teste as ações mínimas e proibidas com `kubectl auth can-i`. Confira namespace, recursos, sub-recursos e verbos; procure bindings a `cluster-admin` e contas default reutilizadas. Inclua a revisão de permissões no processo de implantação quando a aplicação ganhar uma nova chamada à API Kubernetes.

## Conexões
- [[secrets-kubernetes-protecao-dados]] — leitura direta e indireta de Secrets depende das permissões e do acesso a Pods.
- [[networkpolicy-kubernetes-isolamento]] — RBAC limita a API, NetworkPolicy limita conexões de rede.
- O princípio do menor privilégio também se aplica a identidades de workloads fora do Kubernetes.

## Fontes
- [Kubernetes — Using RBAC Authorization](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) — objetos, escopos e comportamento aditivo; acesso em 2026-10-01.
- [Kubernetes — Service Accounts](https://kubernetes.io/docs/concepts/security/service-accounts/) — identidade de workloads e concessão de permissões; acesso em 2026-10-01.
