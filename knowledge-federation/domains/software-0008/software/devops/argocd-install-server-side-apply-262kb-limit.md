---
id: software.devops.tranche01.000012
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-25.md"
fontes: ["https://raw.githubusercontent.com/argoproj/argo-cd/master/docs/getting_started.md", "https://raw.githubusercontent.com/argoproj/argo-cd/master/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Instalação com `kubectl apply --server-side --force-conflicts` e o limite de 262 KB dos CRDs

## Em uma frase
Na seção 1 (Install Argo CD) de `docs/getting_started.md`, o comando oficial de instalação cria o namespace `argocd` e aplica o manifesto com `kubectl apply -n argocd --server-side --force-conflicts -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml`; a nota explicativa detalha que `--server-side` é obrigatório porque alguns CRDs do Argo CD (como o `ApplicationSet`) excedem o limite de 262 KB para o tamanho da anotação `last-applied-configuration` imposta pelo `kubectl apply` client-side.

## Por que importa
Sem `--server-side`, o `kubectl apply` tradicional tenta gravar todo o schema OpenAPI do CRD dentro da anotação `kubectl.kubernetes.io/last-applied-configuration` no objeto e falha imediatamente ao ultrapassar 262 KB; já `--force-conflicts` permite assumir a propriedade de campos antes gerenciados por Helm ou `kubectl apply` client-side durante instalações e upgrades.

## Como funciona
Crie o namespace `argocd`, aplique o manifesto usando `--server-side --force-conflicts` (fixando uma tag de versão específica como `v3.2.0` em produção em vez da branch `stable`) e, se instalar em outro namespace que não `argocd`, atualize as referências de namespace nos recursos `ClusterRoleBinding`.

## Exemplo
O guia explica com precisão o efeito de `--force-conflicts` em upgrades: modificações customizadas feitas em campos que existem no manifesto oficial do Argo CD (como `affinity`, `env` ou `probes`) serão sobrescritas, mas campos não especificados no manifesto oficial (como `resources` limits/requests ou `tolerations`) serão preservados.

## Limites e trade-offs
Antes de instalar em ambientes MicroK8s, a seção Requirements lembra que o CoreDNS é requisito obrigatório e pode ser ativado com `microk8s enable dns && microk8s stop && microk8s start`.

## Como verificar
Conferi as seções Requirements e 1. Install Argo CD em `docs/getting_started.md`.

## Conexões
- [[argocd-what-it-is-and-why]] — Veja também: Argo CD: entrega contínua declarativa GitOps para Kubernetes e seus dois princípios centrais.
- [[argocd-core-install-and-redis-secret]] — Veja também: Instalação enxuta (`core`) sem UI/SSO e autenticação padrão do Redis em `argocd-redis`.

## Fontes
- [Argo CD — Getting Started (docs/getting_started.md)](https://raw.githubusercontent.com/argoproj/argo-cd/master/docs/getting_started.md) — Guia oficial Getting Started do Argo CD: instalação com --server-side --force-conflicts (limite de 262 KB), modo core, segredo argocd-redis, LoadBalancer/Ingress/port-forward, argocd-initial-admin-secret e argocd cluster add.; consultado em 2026-10-03.
- [Argo CD — README oficial](https://raw.githubusercontent.com/argoproj/argo-cd/master/README.md) — README oficial do Argo CD com definição GitOps para Kubernetes, os dois motivos centrais em Why Argo CD?, USERS.md, documentação, live demo, integrações do ecossistema e canais da comunidade.; consultado em 2026-10-03.
