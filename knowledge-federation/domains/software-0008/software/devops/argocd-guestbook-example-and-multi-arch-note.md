---
id: software.devops.tranche01.000018
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

# Criação de aplicações a partir do repositório `argocd-example-apps` e compatibilidade de arquitetura

## Em uma frase
Na seção 6 (Create An Application From A Git Repository) de `docs/getting_started.md`, o guia utiliza o repositório oficial de exemplos `https://github.com/argoproj/argocd-example-apps.git` (contendo a aplicação `guestbook`) para demonstrar a criação e sincronização de uma aplicação pelo Argo CD, trazendo uma nota explícita sobre arquiteturas de CPU: a aplicação de exemplo pode ser compatível apenas com a arquitetura AMD64.

## Por que importa
Desenvolvedores que seguem o tutorial em máquinas Apple Silicon (ARM64), servidores ARM em nuvem ou nós Raspberry Pi (ARMv7) frequentemente esbarram em pods da aplicação de exemplo falhando com erro de formato de executável; o aviso oficial previne que esse erro vem da imagem do exemplo AMD64 e não da instalação do Argo CD.

## Como funciona
Use `https://github.com/argoproj/argocd-example-apps.git` para testar rapidamente o fluxo de criação e sync de aplicações em clusters AMD64, ou substitua por imagens multi-arquitetura / compiladas para ARM64 quando seu cluster rodar sobre nós ARM.

## Exemplo
A nota alerta especificamente que, em arquiteturas diferentes de AMD64 (como ARM64 ou ARMv7), podem ocorrer falhas em dependências ou imagens de contêiner não compiladas para a plataforma.

## Limites e trade-offs
Verifique sempre a arquitetura dos nós do cluster (`kubectl get nodes -o wide`) ao diagnosticar falhas de `ImagePullBackOff` ou `Exec format error` durante tutoriais de implantação.

## Como verificar
Conferi a seção 6. Create An Application From A Git Repository em `docs/getting_started.md`.

## Conexões
- [[argocd-external-cluster-registration-and-rbac]] — Veja também: Registro de clusters externos (`argocd cluster add`), `argocd-manager` e privilégios mínimos de RBAC.
- [[argocd-ecosystem-rollouts-workflows-events-crossplane]] — Veja também: Integração no ecossistema Argo e GitOps: Rollouts, Workflows, Events, ApplicationSet e Crossplane.

## Fontes
- [Argo CD — Getting Started (docs/getting_started.md)](https://raw.githubusercontent.com/argoproj/argo-cd/master/docs/getting_started.md) — Guia oficial Getting Started do Argo CD: instalação com --server-side --force-conflicts (limite de 262 KB), modo core, segredo argocd-redis, LoadBalancer/Ingress/port-forward, argocd-initial-admin-secret e argocd cluster add.; consultado em 2026-10-03.
- [Argo CD — README oficial](https://raw.githubusercontent.com/argoproj/argo-cd/master/README.md) — README oficial do Argo CD com definição GitOps para Kubernetes, os dois motivos centrais em Why Argo CD?, USERS.md, documentação, live demo, integrações do ecossistema e canais da comunidade.; consultado em 2026-10-03.
