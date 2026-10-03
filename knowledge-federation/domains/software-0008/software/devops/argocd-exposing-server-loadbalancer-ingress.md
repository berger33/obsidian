---
id: software.devops.tranche01.000015
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

# Três modos de expor o `argocd-server`: Service `LoadBalancer`, Ingress e Port Forwarding

## Em uma frase
A seção 3 (Access Argo CD) de `docs/getting_started.md` explica que, por padrão, o Argo CD não é exposto fora do cluster, e documenta três opções para acessá-lo pelo navegador ou pela CLI: (1) alterar o tipo do Service para `LoadBalancer` com `kubectl patch svc argocd-server -n argocd -p '{"spec": {"type": "LoadBalancer"}}'` e consultar o IP em `.status.loadBalancer.ingress[0].ip`; (2) configurar um Ingress seguindo `operator-manual/ingress.md`; ou (3) usar `kubectl port-forward svc/argocd-server -n argocd 8080:443`.

## Por que importa
Não expor o `argocd-server` por padrão segue o princípio de segurança por padrão (secure by default), permitindo que cada organização escolha se prefere um LoadBalancer dedicado, um Ingress corporativo com TLS ou acesso estritamente via túnel Kubernetes.

## Como funciona
Em provedores de nuvem com suporte a balanceadores externos rápidos, aplique o patch `{"spec": {"type": "LoadBalancer"}}` e extraia o IP com `kubectl get svc argocd-server -n argocd -o=jsonpath='{.status.loadBalancer.ingress[0].ip}'`; em produção compartilhada, configure o Ingress conforme o manual do operador.

## Exemplo
Os dois comandos exatos de `kubectl patch svc` e `kubectl get svc ... -o=jsonpath='{.status.loadBalancer.ingress[0].ip}'` permitem automatizar a descoberta do endpoint em scripts de provisionamento.

## Limites e trade-offs
Ao expor o `argocd-server` via LoadBalancer ou Ingress na rede, troque imediatamente a senha inicial do administrador e configure certificados TLS confiáveis em vez de depender do certificado autoassinado inicial.

## Como verificar
Conferi a seção 3. Access Argo CD em `docs/getting_started.md`.

## Conexões
- [[argocd-cli-installation-and-port-forward-opts]] — Veja também: Instalação da CLI `argocd` e acesso direto via `--port-forward-namespace argocd` / `ARGOCD_OPTS`.
- [[argocd-initial-admin-secret-and-password-rotation]] — Veja também: Senha inicial em `argocd-initial-admin-secret`, rotação e exclusão recomendada do Secret.

## Fontes
- [Argo CD — Getting Started (docs/getting_started.md)](https://raw.githubusercontent.com/argoproj/argo-cd/master/docs/getting_started.md) — Guia oficial Getting Started do Argo CD: instalação com --server-side --force-conflicts (limite de 262 KB), modo core, segredo argocd-redis, LoadBalancer/Ingress/port-forward, argocd-initial-admin-secret e argocd cluster add.; consultado em 2026-10-03.
- [Argo CD — README oficial](https://raw.githubusercontent.com/argoproj/argo-cd/master/README.md) — README oficial do Argo CD com definição GitOps para Kubernetes, os dois motivos centrais em Why Argo CD?, USERS.md, documentação, live demo, integrações do ecossistema e canais da comunidade.; consultado em 2026-10-03.
