---
id: software.devops.tranche01.000019
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
fontes: ["https://raw.githubusercontent.com/argoproj/argo-cd/master/README.md", "https://raw.githubusercontent.com/argoproj/argo-cd/master/docs/getting_started.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Integração no ecossistema Argo e GitOps: Rollouts, Workflows, Events, ApplicationSet e Crossplane

## Em uma frase
A seção Blogs and Presentations e os badges do README oficial mostram como o Argo CD se conecta ao restante da família `argoproj` e ao ecossistema cloud-native: distribuição via Helm no Artifact HUB (`artifacthub.io/packages/helm/argo/argo-cd`), lista curada `Awesome-Argo`, automação de tags de imagem com `ArgoCD Image Updater`, geração automática de aplicações com `ApplicationSet`, entrega progressiva com `Argo Rollouts` e Istio, combinação com `Argo Events` e `Argo Workflows` e provisionamento de infraestrutura combinando Argo CD com `Crossplane` e `KubeVela`.

## Por que importa
Em plataformas de engenharia modernas, o Argo CD raramente atua sozinho: `ApplicationSet` automatiza a criação de dezenas de `Applications` (por exemplo, ambientes efêmeros por Pull Request), `Argo Rollouts` adiciona canary/blue-green e `Crossplane` estende o mesmo loop GitOps para recursos de nuvem fora do cluster.

## Como funciona
Consulte o catálogo oficial no README e o chart no Artifact HUB ao desenhar fluxos que combinem o Argo CD com `ApplicationSet` (para ambientes de preview por PR), `ArgoCD Image Updater` ou `Crossplane`.

## Exemplo
Entre os casos práticos listados no README estão a criação de ambientes temporários de preview baseados em Pull Requests, o gerenciamento de clusters de banco de dados (Couchbase) e GitOps para pipelines de Machine Learning (Kubeflow).

## Limites e trade-offs
Recursos como `ApplicationSet` possuem CRDs extensos — justamente o exemplo citado no Getting Started para justificar o uso de `kubectl apply --server-side`.

## Como verificar
Conferi os badges e a seção Blogs and Presentations no README oficial de `argoproj/argo-cd`.

## Conexões
- [[argocd-guestbook-example-and-multi-arch-note]] — Veja também: Criação de aplicações a partir do repositório `argocd-example-apps` e compatibilidade de arquitetura.
- [[argocd-community-governance-and-meetings]] — Veja também: Comunidade, lista oficial de adotantes `USERS.md` e reuniões sob o Código de Conduta da CNCF.

## Fontes
- [Argo CD — README oficial](https://raw.githubusercontent.com/argoproj/argo-cd/master/README.md) — README oficial do Argo CD com definição GitOps para Kubernetes, os dois motivos centrais em Why Argo CD?, USERS.md, documentação, live demo, integrações do ecossistema e canais da comunidade.; consultado em 2026-10-03.
- [Argo CD — Getting Started (docs/getting_started.md)](https://raw.githubusercontent.com/argoproj/argo-cd/master/docs/getting_started.md) — Guia oficial Getting Started do Argo CD: instalação com --server-side --force-conflicts (limite de 262 KB), modo core, segredo argocd-redis, LoadBalancer/Ingress/port-forward, argocd-initial-admin-secret e argocd cluster add.; consultado em 2026-10-03.
