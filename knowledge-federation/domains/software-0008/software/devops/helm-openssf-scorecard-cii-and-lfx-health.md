---
id: software.devops.tranche01.000029
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
fontes: ["https://raw.githubusercontent.com/helm/helm/main/README.md", "https://github.com/helm/helm"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Postura de segurança e saúde do projeto: CII Best Practices, OpenSSF Scorecard e LFX Health Score

## Em uma frase
O cabeçalho do README oficial expõe três indicadores públicos de governança, segurança e saúde de código aberto: o selo CII Best Practices (`bestpractices.coreinfrastructure.org/projects/3131`), o OpenSSF Scorecard (`api.scorecard.dev/projects/github.com/helm/helm`) e o LFX Health Score da Linux Foundation (`insights.linuxfoundation.org/project/helm`).

## Por que importa
Como o cliente Helm executa templates e aplica recursos diretamente contra a API do Kubernetes com as credenciais do operador ou do runner de CI/CD, auditar continuamente as práticas de desenvolvimento seguro do repositório via OpenSSF Scorecard e CII Best Practices é essencial para conformidade corporativa.

## Como funciona
Consulte o painel do OpenSSF Scorecard (`scorecard.dev/viewer/?uri=github.com/helm/helm`) e a ficha CII Best Practices (projeto 3131) quando precisar comprovar a postura de segurança upstream do Helm em revisões de arquitetura ou auditorias de cadeia de suprimentos.

## Exemplo
Junto com o LFX Health Score, essas métricas permitem acompanhar a vitalidade de manutenção e a aderência a práticas seguras de engenharia da linha v4 na branch `main`.

## Limites e trade-offs
As métricas do Scorecard avaliam o repositório oficial do cliente Helm; a segurança dos Charts consumidos pela sua equipe continua dependendo da revisão dos templates e das imagens referenciadas em cada Chart.

## Como verificar
Conferi os badges no cabeçalho do README oficial de `helm/helm`.

## Conexões
- [[helm-roadmap-milestones-and-release-workflow]] — Veja também: Rastreamento de roadmap por GitHub Milestones e automação de releases.
- [[helm-community-slack-channels-and-dev-call]] — Veja também: Canais oficiais no Kubernetes Slack (`#helm-users`, `#helm-dev`, `#charts`), lista de e-mail e Developer Call.

## Fontes
- [Helm — README oficial](https://raw.githubusercontent.com/helm/helm/main/README.md) — README oficial do Helm com definição de Charts, cinco casos de uso, Chart.yaml e templates/, suporte Helm v4 (main) vs Helm v3 (dev-v3 até jul/nov 2026), sete gerenciadores de pacotes, roadmap e canais da comunidade.; consultado em 2026-10-03.
- [Repositório oficial helm/helm](https://github.com/helm/helm) — Repositório oficial do Helm no GitHub com código-fonte v4, milestones, CONTRIBUTING.md, code-of-conduct.md e releases.; consultado em 2026-10-03.
