---
id: software.devops.tranche01.000014
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

# Instalação da CLI `argocd` e acesso direto via `--port-forward-namespace argocd` / `ARGOCD_OPTS`

## Em uma frase
As seções 2, 3 e 4 de `docs/getting_started.md` mostram como instalar a CLI `argocd` (pelas releases oficiais do GitHub ou com `brew install argocd` no macOS, Linux e WSL) e como fazê-la conversar com o API server quando o serviço `argocd-server` não está exposto externamente: além de rodar `kubectl port-forward svc/argocd-server -n argocd 8080:443` manualmente, você pode passar a flag `--port-forward-namespace argocd` em cada comando da CLI ou exportar `export ARGOCD_OPTS='--port-forward-namespace argocd'`.

## Por que importa
Configurar `ARGOCD_OPTS='--port-forward-namespace argocd'` permite usar todos os subcomandos da CLI `argocd` sem precisar manter um terminal separado preso num processo `kubectl port-forward` nem expor o serviço publicamente na nuvem.

## Como funciona
Instale a CLI com `brew install argocd` (ou baixe o binário da página de releases) e, em ambientes sem Ingress ou LoadBalancer, exporte `export ARGOCD_OPTS='--port-forward-namespace argocd'` na sua sessão de shell.

## Exemplo
Com `kubectl port-forward svc/argocd-server -n argocd 8080:443`, o servidor da API responde localmente em `https://localhost:8080`.

## Limites e trade-offs
Como a instalação padrão gera um certificado TLS autoassinado, é preciso configurar um certificado válido (`operator-manual/tls.md`), confiar no certificado autoassinado no sistema operacional cliente ou passar `--insecure` nas operações de teste do guia.

## Como verificar
Conferi as seções 1, 2, 3 e 4 em `docs/getting_started.md`.

## Conexões
- [[argocd-core-install-and-redis-secret]] — Veja também: Instalação enxuta (`core`) sem UI/SSO e autenticação padrão do Redis em `argocd-redis`.
- [[argocd-exposing-server-loadbalancer-ingress]] — Veja também: Três modos de expor o `argocd-server`: Service `LoadBalancer`, Ingress e Port Forwarding.

## Fontes
- [Argo CD — Getting Started (docs/getting_started.md)](https://raw.githubusercontent.com/argoproj/argo-cd/master/docs/getting_started.md) — Guia oficial Getting Started do Argo CD: instalação com --server-side --force-conflicts (limite de 262 KB), modo core, segredo argocd-redis, LoadBalancer/Ingress/port-forward, argocd-initial-admin-secret e argocd cluster add.; consultado em 2026-10-03.
- [Argo CD — README oficial](https://raw.githubusercontent.com/argoproj/argo-cd/master/README.md) — README oficial do Argo CD com definição GitOps para Kubernetes, os dois motivos centrais em Why Argo CD?, USERS.md, documentação, live demo, integrações do ecossistema e canais da comunidade.; consultado em 2026-10-03.
