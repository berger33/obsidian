---
id: software.devops.tranche02.000180
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
fontes: ["https://raw.githubusercontent.com/fluent/fluent-bit/master/README.md", "https://github.com/fluent/fluent-bit"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Guia do desenvolvedor, diretrizes de contribuição e canal #fluent-bit no Slack

## Em uma frase
As seções `Contributing` e `Community & Contact` do README apontam para a página da comunidade (`fluentbit.io/community/`), o guia `CONTRIBUTING.md`, o guia técnico `DEVELOPER_GUIDE.md`, o canal `#fluent-bit` no Slack do ecossistema Fluentd (`slack.fluentd.org`) e o perfil oficial no Twitter/X (`@fluentbit`), além da página de contribuidores (`graphs/contributors`).

## Por que importa
Quando uma equipe precisa desenvolver um novo plugin nativo ou depurar o ciclo de eventos interno do coletor, o documento `DEVELOPER_GUIDE.md` e o canal `#fluent-bit` no Slack oferecem o caminho oficial alinhado aos mantenedores da CNCF.

## Como funciona
Consulte `DEVELOPER_GUIDE.md` e `CONTRIBUTING.md` antes de escrever código para o Fluent Bit e participe do canal `#fluent-bit` em `slack.fluentd.org` para tirar dúvidas de arquitetura e operação.

## Exemplo
Um engenheiro de software lê `DEVELOPER_GUIDE.md` para seguir as convenções de alocação de memória e estrutura de plugins ao contribuir com uma melhoria em um plugin de filtro.

## Limites e trade-offs
Ao relatar problemas no GitHub Issues (`fluent/fluent-bit/issues`) ou no Slack, informe a versão exata do Fluent Bit, o sistema operacional, a arquitetura de CPU e um trecho mínimo reproduzível da configuração de Inputs/Filters/Outputs.

## Como verificar
Conferi as seções Contributing, Community & Contact e Authors no README oficial de `fluent/fluent-bit`.

## Conexões
- [[fluentbit-ci-workflows-and-arm-builds]] — Veja também: Fluxos de CI no GitHub Actions: testes unitários, testes de integração, builds Arm e release.

## Fontes
- [Fluent Bit — GitHub README](https://raw.githubusercontent.com/fluent/fluent-bit/master/README.md) — Visão geral do Fluent Bit (agente graduado na CNCF para Logs, Metrics e Traces), suporte multi-plataforma, ciclo de 3–4 meses (v5.1), 70+ plugins, SQL Stream Processing, extensibilidade C/Lua/Go e build CMake.; consultado em 2026-10-03.
- [Fluent Bit — Repositório Oficial no GitHub](https://github.com/fluent/fluent-bit) — Repositório oficial do Fluent Bit com código-fonte, MAINTENANCE.md, DEVELOPER_GUIDE.md e workflows de CI.; consultado em 2026-10-03.
