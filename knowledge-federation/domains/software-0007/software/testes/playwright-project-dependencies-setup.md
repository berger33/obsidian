---
id: software.testes.tranche12.000551
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-12.md"
fontes: ["https://playwright.dev/docs/test-projects", "https://playwright.dev/docs/test-global-setup-teardown"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Playwright Test: setup como dependência de projeto

## Em uma frase
Uma dependência de projeto permite executar testes de preparação antes dos projetos consumidores e declarar teardown associado.

## Por que importa
Preparação visível no grafo de projetos aparece nos relatórios e pode produzir traces, o que torna falhas de login ou provisionamento menos opacas que setup global manual.

## Como funciona
Crie um projeto de setup com testes próprios, faça os projetos dependentes declararem essa relação e associe teardown quando o recurso puder ser encerrado depois dos consumidores. Use `globalSetup` somente quando as diferenças de integração não forem necessárias.

## Exemplo
Um projeto de autenticação pode gravar o estado de sessão usado depois pelo projeto Chromium; o relatório identifica a etapa que falhou antes dos fluxos de compra.

## Limites e trade-offs
Setup compartilhado pode virar gargalo ou estado comum entre workers se gerar dados mutáveis. Garanta que retry e cleanup não deixem recursos órfãos no serviço externo.

## Como verificar
Force uma falha dentro do projeto preparatório e veja se o relatório o apresenta separadamente; depois confirme que teardown ocorre apenas após a execução dependente.

## Conexões
- [[playwright-projects-browser-matrix]] — Veja também: Playwright Test: projetos para uma matriz de browsers.
- [[playwright-webserver-readiness-reuse]] — Veja também: Playwright Test: prontidão do servidor local.

## Fontes
- [Playwright — Projects](https://playwright.dev/docs/test-projects) — projetos por browser/dispositivo/ambiente, dependências, teardown e parametrização; consultado em 2026-10-02.
- [Playwright — Global setup and teardown](https://playwright.dev/docs/test-global-setup-teardown) — comparação entre dependências de projeto e globalSetup, incluindo fixtures, traces e relatórios; consultado em 2026-10-02.
