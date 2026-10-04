---
id: software.testes.tranche08.000157
tipo: tecnica
dominio: software
subdominio: testes
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-08.md"
fontes: ["https://playwright.dev/docs/test-retries", "https://playwright.dev/docs/writing-tests"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Playwright: retries como sinal de flakiness, não correção

## Em uma frase
Use retries para coletar evidência sobre falhas intermitentes, nunca para converter silenciosamente um teste instável em sinal verde.

## Por que importa
Uma aprovação apenas na segunda tentativa indica que o resultado dependeu de timing, estado ou ambiente e merece investigação.

## Como funciona
Registre tentativa inicial e retry, preserve traces e classifique a falha intermitente. Investigue isolamento, sincronização e rede antes de mudar limites ou aceitar o comportamento.

## Exemplo
A pipeline mantém o teste como flaky quando a primeira tentativa falha e a seguinte passa, publica o trace e acompanha a taxa por commit.

## Limites e trade-offs
Retry aumenta duração e pode mascarar defeito se o pipeline só exibir o resultado final. Não substitui assertions determinísticas nem setup correto.

## Como verificar
Introduza uma execução repetida, confira o relatório por tentativa e confirme que o estado flaky fica visível e acionável no CI.

## Conexões
- [[playwright-locators-assertions-web-first]] — Veja também: Playwright: locators resilientes e assertions web-first.
- [[playwright-status-http-vs-falha-transporte]] — Veja também: Playwright: distinguir erro HTTP de falha de transporte.

## Fontes
- [Playwright — Retries](https://playwright.dev/docs/test-retries) — reexecução, classificação flaky e isolamento de worker; consultado em 2026-10-02.
- [Playwright — Writing tests](https://playwright.dev/docs/writing-tests) — ações, locators, auto-wait e assertions assíncronas; consultado em 2026-10-02.
