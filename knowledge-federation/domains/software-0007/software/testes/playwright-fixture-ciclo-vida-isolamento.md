---
id: software.testes.tranche08.000150
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
fontes: ["https://playwright.dev/docs/test-fixtures", "https://playwright.dev/docs/writing-tests"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Playwright: ciclo de vida de fixtures por teste

## Em uma frase
Use fixtures para encapsular preparação, recurso e encerramento de cada cenário, em vez de espalhar setup implícito pelos testes.

## Por que importa
O ciclo de vida explícito reduz dependências ocultas e facilita identificar qual recurso precisa de limpeza quando um teste falha.

## Como funciona
Uma fixture declara dependências e teardown em torno do teste consumidor. Mantenha estado mutável no escopo de teste; reserve escopos maiores para recursos realmente compartilháveis e seguros entre workers.

## Exemplo
Uma fixture cria um registro com identificador exclusivo, fornece o objeto ao teste e o remove em um bloco de finalização mesmo quando uma assertion interrompe o fluxo.

## Limites e trade-offs
Fixtures não tornam automaticamente um teste isolado: estado externo, contas compartilhadas e ordem de execução ainda podem acoplar cenários.

## Como verificar
Execute o teste sozinho e em conjunto, force uma falha depois da criação e confirme a limpeza. Inspecione dependências para detectar fixtures globais que escondem estado.

## Conexões
- [[playwright-teardown-recursos-externos]] — Veja também: Playwright: teardown confiável de recursos externos.
- [[playwright-paralelismo-dados-exclusivos]] — Veja também: Playwright: dados exclusivos para testes paralelos.

## Fontes
- [Playwright — Fixtures](https://playwright.dev/docs/test-fixtures) — isolamento, ciclo de vida e composição de fixtures; consultado em 2026-10-02.
- [Playwright — Writing tests](https://playwright.dev/docs/writing-tests) — ações, locators, auto-wait e assertions assíncronas; consultado em 2026-10-02.
