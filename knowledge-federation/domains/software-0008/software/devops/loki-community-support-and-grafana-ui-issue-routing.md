---
id: software.devops.tranche02.000170
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
fontes: ["https://raw.githubusercontent.com/grafana/loki/main/README.md", "https://github.com/grafana/loki"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Canais de suporte da comunidade e separação entre issues do Loki e issues de UI no Grafana

## Em uma frase
A seção `Getting Help` do README lista os canais oficiais de ajuda e feedback: o fórum comunitário do Grafana Labs (`community.grafana.com/c/grafana-loki/`), o canal `#loki` no Slack do Grafana (`slack.grafana.com`), a abertura de issues no repositório `grafana/loki/issues/new`, a lista de e-mail `lokiproject@googlegroups.com` e uma regra explícita de roteamento: **issues de interface de usuário (UI) devem ser abertas diretamente no repositório do Grafana** (`github.com/grafana/grafana/issues/new`).

## Por que importa
Como a visualização e exploração visual dos logs do Loki acontece dentro do Grafana, usuários frequentemente abrem bugs de renderização do painel Explore no repositório do backend do Loki; saber distinguir o motor de armazenamento/consulta (`grafana/loki`) da interface web (`grafana/grafana`) agiliza o tratamento do problema.

## Como funciona
Ao encontrar um bug ou sugerir uma funcionalidade, verifique se o comportamento ocorre na API/motor do Loki (`grafana/loki`) ou na interface gráfica do usuário (`grafana/grafana`), registrando a issue no repositório correto.

## Exemplo
Uma falha de execução em uma consulta via `LogCLI` é reportada em `grafana/loki`, enquanto um problema visual no painel de logs do navegador é reportado em `grafana/grafana`.

## Limites e trade-offs
Antes de abrir uma nova thread no fórum ou no Slack `#loki`, consulte a página de `Troubleshooting` oficial e remova dados sensíveis dos exemplos de logs.

## Como verificar
Conferi a seção Getting Help no README oficial de `grafana/loki`.

## Conexões
- [[loki-design-doc-and-architecture-reading]] — Veja também: Documento original de design do Loki e referências históricas de arquitetura.

## Fontes
- [Grafana Loki — GitHub README](https://raw.githubusercontent.com/grafana/loki/main/README.md) — Visão geral do Loki (agregação de logs indexada por labels no estilo Prometheus), pilha Alloy + Loki + Grafana, migração do Helm chart em março de 2026, LogCLI, Loki Canary e build a partir do fonte.; consultado em 2026-10-03.
- [Grafana Loki — Repositório Oficial no GitHub](https://github.com/grafana/loki) — Repositório oficial do Grafana Loki com código-fonte em Go, cmd/loki/loki-local-config.yaml e Makefile.; consultado em 2026-10-03.
