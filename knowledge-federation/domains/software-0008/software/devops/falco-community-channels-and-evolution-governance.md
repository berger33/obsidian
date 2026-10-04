---
id: software.devops.tranche03.000250
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
fontes: ["https://raw.githubusercontent.com/falcosecurity/falco/master/README.md", "https://github.com/falcosecurity/falco"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Comunidade no Slack #falco, lista cncf-falco-dev e governança em falcosecurity/evolution

## Em uma frase
As seções `The Falco Project`, `Join the Community` e `How to Contribute` do README reúnem os pontos de participação comunitária e governança: o repositório `falcosecurity/community`, o hub de governança e escopo de repositórios `falcosecurity/evolution` (incluindo `REPOSITORIES.md` e `CODE_OF_CONDUCT.md`), o canal `#falco` no Slack do Kubernetes (`slack.k8s.io`), a lista de discussão `cncf-falco-dev` em `lists.cncf.io` e o guia `CONTRIBUTING.md`.

## Por que importa
A classificação formal dos repositórios em `falcosecurity/evolution` (como escopo `Core` e maturidade `Stable` exibidos nos badges do topo do README) permite que arquitetos saibam exatamente o nível de suporte e maturidade de cada subprojeto da organização `falcosecurity`.

## Como funciona
Consulte `falcosecurity/evolution/blob/main/REPOSITORIES.md` para verificar a maturidade dos subprojetos do ecossistema Falco e utilize o canal `#falco` no Slack do Kubernetes ou a lista `cncf-falco-dev` para suporte comunitário.

## Exemplo
Antes de adotar um plugin ou subprojeto adicional da organização `falcosecurity`, o engenheiro confere seu status oficial no repositório `falcosecurity/evolution`.

## Limites e trade-offs
Siga sempre o guia `CONTRIBUTING.md` e o `CODE_OF_CONDUCT.md` ao abrir issues, propor novas regras ou submeter pull requests.

## Como verificar
Conferi os badges de topo e as seções The Falco Project, Join the Community e How to Contribute no README oficial de falcosecurity/falco.

## Conexões
- [[falco-cpp-architecture-and-performance-rationale]] — Veja também: Motivação arquitetural do uso de C++ no motor do Falco e nas bibliotecas de captura.

## Fontes
- [Falco — GitHub README](https://raw.githubusercontent.com/falcosecurity/falco/master/README.md) — Visão geral do Falco (segurança em tempo de execução no kernel Linux graduada na CNCF, observação de syscalls com metadados de container/Kubernetes, 5 repositórios core, ambiente demo, auditorias em ./audits/ e build CMake com Modern BPF).; consultado em 2026-10-03.
- [Falco — Repositório Oficial no GitHub](https://github.com/falcosecurity/falco) — Repositório oficial do Falco na CNCF com código-fonte C++, chart/falco, docker/docker-compose/ e audits/.; consultado em 2026-10-03.
