---
id: software.devops.tranche01.000036
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
fontes: ["https://raw.githubusercontent.com/opentofu/opentofu/main/README.md", "https://github.com/opentofu/opentofu"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Builds noturnos (`nightlies.opentofu.org`), retenção de 30 dias e automação via `latest.json`

## Em uma frase
A seção Nightly Builds do README oficial documenta que builds noturnos estão disponíveis para testar as últimas alterações da branch `main` em `https://nightlies.opentofu.org/nightlies`, que cada build é removido após **30 dias**, e que para quem deseja automatizar testes com ferramentas o endpoint `https://nightlies.opentofu.org/nightlies/latest.json` é mantido atualizado com as informações do último build (com detalhes adicionais em `RELEASE.md#nightly-builds`).

## Por que importa
Autores de provedores, módulos e ferramentas do ecossistema precisam testar suas integrações contra o código mais recente da branch `main` antes do lançamento de uma versão estável; ter um endpoint JSON fixo (`latest.json`) permite que pipelines de CI baixem automaticamente a última nightly sem scraping HTML.

## Como funciona
Em pipelines de teste de compatibilidade de provedores ou módulos contra a branch `main`, consuma `https://nightlies.opentofu.org/nightlies/latest.json` para descobrir e baixar a build noturna atual.

## Exemplo
Um workflow de CI agendado pode ler `latest.json` diariamente para detectar regressões de integração semanas antes de uma release oficial do OpenTofu.

## Limites e trade-offs
O próprio README adverte expressamente: os nightly builds são experimentais, **não** se destinam ao uso em produção e cada artefato é expurgado após 30 dias (portanto, nunca fixe uma URL de nightly específica em scripts de longo prazo).

## Como verificar
Conferi a seção Nightly Builds no README oficial de `opentofu/opentofu`.

## Conexões
- [[opentofu-change-automation-minimal-human-error]] — Veja também: Automação de mudanças (`Change Automation`): aplicação previsível de changesets complexos.
- [[opentofu-security-policy-and-copyright-liaison]] — Veja também: Políticas formais de reporte de vulnerabilidades de segurança e questões de copyright.

## Fontes
- [OpenTofu — README oficial](https://raw.githubusercontent.com/opentofu/opentofu/main/README.md) — README oficial do OpenTofu com definição OSS, quatro Key features (IaC, Execution Plans, Resource Graph e Change Automation), Nightly Builds (30 dias e latest.json), Security Policy, liaison@opentofu.org, Registry Policy, reuniões e licença MPL-2.0.; consultado em 2026-10-03.
- [Repositório oficial opentofu/opentofu](https://github.com/opentofu/opentofu) — Repositório oficial do OpenTofu no GitHub com código-fonte, RELEASE.md, CONTRIBUTING.md e LICENSE (MPL-2.0).; consultado em 2026-10-03.
