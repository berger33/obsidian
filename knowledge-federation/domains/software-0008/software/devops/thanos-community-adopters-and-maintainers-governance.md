---
id: software.devops.tranche02.000160
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
fontes: ["https://raw.githubusercontent.com/thanos-io/thanos/main/README.md", "https://github.com/thanos-io/thanos"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Comunidade no CNCF Slack, lista de adotantes em adopters.yml e MAINTAINERS.md

## Em uma frase
As seções finais `Contributing`, `Community`, `Adopters` e `Maintainers` do README apontam para o guia `CONTRIBUTING.md`, o canal `#thanos` no Slack da CNCF (`slack.cncf.io`), o rastreador de issues no GitHub (`thanos-io/thanos/issues`), a lista estruturada de adotantes em `website/data/adopters.yml` e a relação de mantenedores em `MAINTAINERS.md`, além de registrar eventos da comunidade como a ThanosCon co-localizada na KubeCon EU.

## Por que importa
Saber onde consultar a lista real de empresas usuárias (`website/data/adopters.yml`), os mantenedores responsáveis (`MAINTAINERS.md`) e o canal oficial `#thanos` no Slack da CNCF apoia tanto a avaliação corporativa quanto o suporte comunitário em incidentes complexos.

## Como funciona
Utilize o canal `#thanos` no Slack da CNCF e o GitHub Issues para discutir comportamentos observados em produção e siga `CONTRIBUTING.md` ao submeter melhorias ao repositório.

## Exemplo
Uma equipe de observabilidade consulta `website/data/adopters.yml` para conhecer arquiteturas de referência de outras organizações que operam Thanos em grande escala.

## Limites e trade-offs
Ao abrir uma issue em `thanos-io/thanos/issues`, inclua a versão exata do Thanos, o comando/flags de execução e as métricas relevantes do componente afetado.

## Como verificar
Conferi o banner inicial e as seções Contributing, Community, Adopters e Maintainers no README oficial de `thanos-io/thanos`.

## Conexões
- [[thanos-design-docs-proposals-and-integrations]] — Veja também: Documentação de partida: Getting Started, Design, Proposals e Integrations.

## Fontes
- [Thanos — GitHub README](https://raw.githubusercontent.com/thanos-io/thanos/main/README.md) — Visão geral do Thanos (CNCF Incubating), objetivos sobre o formato Prometheus 2.0, deduplicação HA, Store API gRPC, arquiteturas Sidecar vs Receive, filosofia UNIX/Go e releases a cada 6 semanas.; consultado em 2026-10-03.
- [Thanos — Repositório Oficial no GitHub](https://github.com/thanos-io/thanos) — Repositório oficial do Thanos com código-fonte em Go, docs/proposals-done, docs/integrations.md e website/data/adopters.yml.; consultado em 2026-10-03.
