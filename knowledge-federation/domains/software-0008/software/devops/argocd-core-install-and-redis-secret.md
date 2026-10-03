---
id: software.devops.tranche01.000013
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

# Instalação enxuta (`core`) sem UI/SSO e autenticação padrão do Redis em `argocd-redis`

## Em uma frase
As notas da seção 1 de `docs/getting_started.md` destacam dois detalhes arquiteturais da instalação padrão: primeiro, para quem não precisa de UI web, SSO e recursos multi-cluster, é possível instalar apenas os componentes `core` do Argo CD (`operator-manual/core.md#installing`) e autenticar a CLI diretamente com `argocd login --core` (pulando os passos 3 a 5); segundo, a instalação padrão configura o Redis com autenticação por senha, armazenada no Secret Kubernetes `argocd-redis` sob a chave `auth` no namespace de instalação.

## Por que importa
Em clusters dedicados onde todo o gerenciamento é feito via CRDs e linha de comando, o modo `core` reduz a superfície de ataque e o consumo de recursos ao dispensar o servidor de UI/SSO, enquanto o Redis autenticado por padrão evita cache interno aberto dentro do namespace.

## Como funciona
Se desejar operar exclusivamente via Kubernetes API e CLI local sem expor o `argocd-server`, instale a variante core, defina o namespace padrão do contexto (`kubectl config set-context --current --namespace=argocd`) e execute `argocd login --core`.

## Exemplo
Quando `argocd login --core` é utilizado, a CLI conversa diretamente usando o contexto do Kubernetes, dispensando abertura de LoadBalancer, Ingress ou login interativo no `argocd-server`.

## Limites e trade-offs
Para quem roda o Argo CD em Docker Desktop ou outro cluster Kubernetes local de desenvolvimento, o guia aponta o documento específico `developer-guide/running-locally.md`.

## Como verificar
Conferi as notas da seção 1. Install Argo CD em `docs/getting_started.md`.

## Conexões
- [[argocd-install-server-side-apply-262kb-limit]] — Veja também: Instalação com `kubectl apply --server-side --force-conflicts` e o limite de 262 KB dos CRDs.
- [[argocd-cli-installation-and-port-forward-opts]] — Veja também: Instalação da CLI `argocd` e acesso direto via `--port-forward-namespace argocd` / `ARGOCD_OPTS`.

## Fontes
- [Argo CD — Getting Started (docs/getting_started.md)](https://raw.githubusercontent.com/argoproj/argo-cd/master/docs/getting_started.md) — Guia oficial Getting Started do Argo CD: instalação com --server-side --force-conflicts (limite de 262 KB), modo core, segredo argocd-redis, LoadBalancer/Ingress/port-forward, argocd-initial-admin-secret e argocd cluster add.; consultado em 2026-10-03.
- [Argo CD — README oficial](https://raw.githubusercontent.com/argoproj/argo-cd/master/README.md) — README oficial do Argo CD com definição GitOps para Kubernetes, os dois motivos centrais em Why Argo CD?, USERS.md, documentação, live demo, integrações do ecossistema e canais da comunidade.; consultado em 2026-10-03.
