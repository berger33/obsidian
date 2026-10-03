---
id: software.devops.tranche01.000016
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

# Senha inicial em `argocd-initial-admin-secret`, rotação e exclusão recomendada do Secret

## Em uma frase
A seção 4 (Log in Using The CLI) de `docs/getting_started.md` detalha o ciclo de vida da credencial inicial: a senha da conta `admin` é gerada automaticamente e guardada em texto claro no campo `password` do Secret `argocd-initial-admin-secret`, recuperada com `argocd admin initial-password -n argocd`; após fazer `argocd login <ARGOCD_SERVER>` e trocar a senha com `argocd account update-password`, o aviso oficial orienta excluir o Secret `argocd-initial-admin-secret` do namespace.

## Por que importa
O próprio alerta WARNING do guia explica que `argocd-initial-admin-secret` não tem nenhuma outra finalidade além de guardar a senha inicial gerada em texto claro; deixá-lo no cluster após a troca mantém a credencial inicial exposta a qualquer leitor de Secrets no namespace.

## Como funciona
Recupere a senha inicial com `argocd admin initial-password -n argocd`, autentique-se como `admin`, execute `argocd account update-password` para definir uma senha forte e apague `argocd-initial-admin-secret` em seguida.

## Exemplo
O guia tranquiliza o operador quanto à exclusão: o Secret pode ser removido com segurança a qualquer momento e será recriado sob demanda pelo próprio Argo CD caso uma nova senha de admin precise ser gerada novamente no futuro.

## Limites e trade-offs
Nunca mantenha a senha autoassinada inicial sem rotação quando o `argocd-server` estiver acessível fora de `localhost`.

## Como verificar
Conferi a seção 4. Log in Using The CLI em `docs/getting_started.md`.

## Conexões
- [[argocd-exposing-server-loadbalancer-ingress]] — Veja também: Três modos de expor o `argocd-server`: Service `LoadBalancer`, Ingress e Port Forwarding.
- [[argocd-external-cluster-registration-and-rbac]] — Veja também: Registro de clusters externos (`argocd cluster add`), `argocd-manager` e privilégios mínimos de RBAC.

## Fontes
- [Argo CD — Getting Started (docs/getting_started.md)](https://raw.githubusercontent.com/argoproj/argo-cd/master/docs/getting_started.md) — Guia oficial Getting Started do Argo CD: instalação com --server-side --force-conflicts (limite de 262 KB), modo core, segredo argocd-redis, LoadBalancer/Ingress/port-forward, argocd-initial-admin-secret e argocd cluster add.; consultado em 2026-10-03.
- [Argo CD — README oficial](https://raw.githubusercontent.com/argoproj/argo-cd/master/README.md) — README oficial do Argo CD com definição GitOps para Kubernetes, os dois motivos centrais em Why Argo CD?, USERS.md, documentação, live demo, integrações do ecossistema e canais da comunidade.; consultado em 2026-10-03.
