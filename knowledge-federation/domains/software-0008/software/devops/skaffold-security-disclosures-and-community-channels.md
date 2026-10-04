---
id: software.devops.tranche02.000200
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-02.md"
fontes: ["https://raw.githubusercontent.com/GoogleContainerTools/skaffold/main/README.md", "https://github.com/GoogleContainerTools/skaffold"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Processo de divulgação de segurança (SECURITY.md), avisos no GitHub e canais da comunidade

## Em uma frase
As seções `Community` e `Security Disclosures` do README listam os canais oficiais de interação — o canal `#skaffold` no Slack do Kubernetes e a lista de discussão `skaffold-users` no Google Groups — e apontam para o processo de divulgação de falhas em `SECURITY.md` e para a página centralizada de avisos de segurança no GitHub (`github.com/GoogleContainerTools/skaffold/security/advisories`), além da licença Apache-2.0 do projeto.

## Por que importa
Equipes de DevSecOps que distribuem o binário `skaffold` para centenas de estações de desenvolvedores e agentes de CI precisam monitorar avisos oficiais de segurança (`security/advisories`) e saber como reportar falhas de forma privada via `SECURITY.md`.

## Como funciona
Monitore os avisos em `GoogleContainerTools/skaffold/security/advisories`, utilize `SECURITY.md` para relatos responsáveis de vulnerabilidades e participe do canal `#skaffold` no Slack do Kubernetes para dúvidas operacionais.

## Exemplo
A automação de segurança da empresa acompanha os GitHub Security Advisories de `GoogleContainerTools/skaffold` para disparar a atualização do binário nos ambientes de CI sempre que uma correção de segurança é publicada.

## Limites e trade-offs
Nunca publique detalhes de vulnerabilidades de segurança não corrigidas no canal público `#skaffold` ou na lista `skaffold-users`; siga sempre o fluxo privado descrito em `SECURITY.md`.

## Como verificar
Conferi os badges de topo e as seções Community e Security Disclosures no README oficial de `GoogleContainerTools/skaffold`.

## Conexões
- [[skaffold-examples-catalog-and-contribution-guide]] — Veja também: Catálogo oficial de exemplos no repositório e guia de contribuição.

## Fontes
- [Skaffold — GitHub README](https://raw.githubusercontent.com/GoogleContainerTools/skaffold/main/README.md) — Visão geral do Skaffold (desenvolvimento contínuo para Kubernetes e blocos de CI/CD), features (source-to-deploy, skaffold render, skaffold init, client-side only), Cloud Code e Deprecation Policy.; consultado em 2026-10-03.
- [Skaffold — Repositório Oficial no GitHub](https://github.com/GoogleContainerTools/skaffold) — Repositório oficial do Skaffold com código-fonte, diretório examples/, SECURITY.md e security advisories.; consultado em 2026-10-03.
