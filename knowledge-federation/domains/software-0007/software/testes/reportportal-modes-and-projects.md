---
id: software.testes.tranche19.001335
tipo: tecnica
dominio: software
subdominio: testes
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-19.md"
fontes: ["https://reportportal.io/docs/", "https://reportportal.io/docs/developers-guides/ReportingDevelopersGuide/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# ReportPortal: separar modos de execução e projetos

## Em uma frase
Um lançamento pode rodar em modo de depuração, visível apenas para o autor, ou no modo padrão do projeto, e a plataforma separa dados por projeto.

## Por que importa
Separar o desenvolvimento da suíte oficial e os dados por time evita poluir indicadores usados para acompanhar a qualidade.

## Como funciona
Use o modo de depuração para experimentos, mantenha o modo padrão para a esteira e escolha o projeto conforme a responsabilidade sobre os dados.

## Exemplo
Um teste novo pode ser depurado no modo restrito antes de ser integrado à execução oficial do time.

## Limites e trade-offs
Publicar experimentos como lançamentos oficiais distorce tendências e alertas, e a mistura de projetos dificulta a atribuição de falhas.

## Como verificar
Compare a visibilidade de um lançamento em modo de depuração e em modo padrão para as demais pessoas do projeto.

## Conexões
- [[reportportal-framework-integration]] — Veja também: ReportPortal: integrar com o framework de testes.
- [[reportportal-dashboards-and-filters]] — Veja também: ReportPortal: acompanhar com filtros e painéis.

## Fontes
- [ReportPortal — Documentação](https://reportportal.io/docs/) — execuções, lançamentos, defeitos, painéis e integrações; consultado em 2026-10-03.
- [ReportPortal — Guia de desenvolvedores](https://reportportal.io/docs/developers-guides/ReportingDevelopersGuide/) — lançamentos, itens, identificadores e histórico; consultado em 2026-10-03.
