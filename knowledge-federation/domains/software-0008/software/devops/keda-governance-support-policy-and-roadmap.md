---
id: software.devops.tranche03.000260
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-03.md"
fontes: ["https://raw.githubusercontent.com/kedacore/keda/main/README.md", "https://raw.githubusercontent.com/kedacore/keda/main/BUILD.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Governança em kedacore/governance, política de suporte em keda.sh/support e ROADMAP.md

## Em uma frase
As seções `Community`, `Adopters`, `Governance & Policies`, `Support` e `Roadmap` do README apontam para o repositório de governança (`github.com/kedacore/governance`), a política oficial de suporte de versões (`keda.sh/support/`), o arquivo `ROADMAP.md` (construído sobre o backlog de GitHub issues), a lista de usuários em produção (`keda.sh/community/#users`) e o canal `#KEDA` no Slack do Kubernetes.

## Por que importa
Antes de adotar o KEDA para cargas críticas de missão, equipes de plataforma precisam verificar a janela de versões suportadas em `keda.sh/support/` e a compatibilidade com a versão do Kubernetes do cluster.

## Como funciona
Consulte `keda.sh/support/` e a página de `releases` (`github.com/kedacore/keda/releases`) ao planejar atualizações periódicas do KEDA e participe do canal `#KEDA` no Slack do Kubernetes ou das reuniões comunitárias em `keda.sh/community/`.

## Exemplo
Durante o planejamento semestral da plataforma, a equipe confere a política de suporte em `keda.sh/support/` e o `ROADMAP.md` para alinhar o upgrade do KEDA ao upgrade do Kubernetes.

## Limites e trade-offs
Não deixe instalações do KEDA em versões fora da janela documentada em `keda.sh/support/`, pois atualizações de APIs de métricas e HPA do Kubernetes exigem versões compatíveis do operador.

## Como verificar
Conferi as seções Community, Adopters, Governance & Policies, Support, Roadmap e Releases no README oficial de kedacore/keda.

## Conexões
- [[keda-ci-workflows-and-testing-strategy]] — Veja também: Workflows de build principal e testes end-to-end noturnos (TESTING.md).

## Fontes
- [KEDA — GitHub README](https://raw.githubusercontent.com/kedacore/keda/main/README.md) — Visão geral do KEDA (Kubernetes-based Event Driven Autoscaling graduado na CNCF, scale to/from zero, integração com HPA na nuvem e borda, QuickStarts com ScaledObject/ScaledJob, deploy Helm/Operator Hub/YAML e governança).; consultado em 2026-10-03.
- [KEDA — Build & Deploy Guide (BUILD.md)](https://raw.githubusercontent.com/kedacore/keda/main/BUILD.md) — Guia oficial de build e deploy do KEDA detalhando Operator SDK, Dev Containers, GOPROXY/GOSUMDB, execução local fora do cluster com /certs, imagens customizadas e pontos de entrada cmd/operator/main.go e cmd/adapter/main.go.; consultado em 2026-10-03.
