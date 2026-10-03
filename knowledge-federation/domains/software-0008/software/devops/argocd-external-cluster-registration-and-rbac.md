---
id: software.devops.tranche01.000017
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-01.md"
fontes: ["https://raw.githubusercontent.com/argoproj/argo-cd/master/docs/getting_started.md", "https://raw.githubusercontent.com/argoproj/argo-cd/master/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Registro de clusters externos (`argocd cluster add`), `argocd-manager` e privilégios mínimos de RBAC

## Em uma frase
A seção 5 (Register a Cluster to Deploy Apps To) de `docs/getting_started.md` distingue deploys internos (no mesmo cluster onde o Argo CD roda, que devem usar `https://kubernetes.default.svc` como endereço da API Kubernetes) de deploys em clusters externos: para estes, lista-se o contexto com `kubectl config get-contexts -o name` e executa-se `argocd cluster add CONTEXTNAME` (por exemplo `argocd cluster add docker-desktop`), o que instala uma ServiceAccount `argocd-manager` no namespace `kube-system` do cluster alvo vinculada a uma ClusterRole de nível admin.

## Por que importa
Muitas equipes de segurança não aceitam uma ClusterRole irrestrita de cluster-admin em clusters gerenciados; a nota oficial da seção 5 esclarece exatamente até onde é possível restringir a `argocd-manager-role`: os privilégios de `create`, `update`, `patch` e `delete` podem ser limitados a um subconjunto de namespaces, grupos e kinds, mas `get`, `list` e `watch` continuam obrigatórios em escopo de cluster (`cluster-scope`) para o Argo CD funcionar.

## Como funciona
Para implantar no mesmo cluster do Argo CD, aponte o destino da aplicação diretamente para `https://kubernetes.default.svc` sem rodar `argocd cluster add`; para clusters externos, rode `argocd cluster add <contexto>` e, se necessário, restrinja `create`/`update`/`patch`/`delete` na `argocd-manager-role` preservando `get`/`list`/`watch` em nível de cluster.

## Exemplo
Rodar `argocd cluster add docker-desktop` provisiona automaticamente a ServiceAccount `argocd-manager` em `kube-system` e usa seu token para implantar e monitorar recursos naquele cluster.

## Limites e trade-offs
Remover as permissões `get`, `list` ou `watch` em escopo de cluster da `argocd-manager-role` impede que o controlador do Argo CD descubra e monitore o estado dos recursos no cluster externo.

## Como verificar
Conferi a seção 5. Register a Cluster to Deploy Apps To em `docs/getting_started.md`.

## Conexões
- [[argocd-initial-admin-secret-and-password-rotation]] — Veja também: Senha inicial em `argocd-initial-admin-secret`, rotação e exclusão recomendada do Secret.
- [[argocd-guestbook-example-and-multi-arch-note]] — Veja também: Criação de aplicações a partir do repositório `argocd-example-apps` e compatibilidade de arquitetura.

## Fontes
- [Argo CD — Getting Started (docs/getting_started.md)](https://raw.githubusercontent.com/argoproj/argo-cd/master/docs/getting_started.md) — Guia oficial Getting Started do Argo CD: instalação com --server-side --force-conflicts (limite de 262 KB), modo core, segredo argocd-redis, LoadBalancer/Ingress/port-forward, argocd-initial-admin-secret e argocd cluster add.; consultado em 2026-10-03.
- [Argo CD — README oficial](https://raw.githubusercontent.com/argoproj/argo-cd/master/README.md) — README oficial do Argo CD com definição GitOps para Kubernetes, os dois motivos centrais em Why Argo CD?, USERS.md, documentação, live demo, integrações do ecossistema e canais da comunidade.; consultado em 2026-10-03.
