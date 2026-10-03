---
id: software.testes.tranche15.000888
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
data_revisao_ia: "2026-10-02"
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://pestphp.com/docs/browser-testing", "https://playwright.dev/docs/actionability"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Pest 5: calibrar o timeout e entender o auto-wait do Playwright

## Em uma frase
O plugin browser do Pest documenta timeout padrão de 5 segundos e permite configurá-lo; ações e assertions de locator do Playwright têm espera automática com limites próprios.

## Por que importa
Um limite maior pode acomodar uma condição legítima mais lenta, mas não transforma um seletor incorreto em sincronização confiável.

## Como funciona
Playwright aguarda verificações de actionability para ações e repete locator assertions; não é correto generalizar isso para qualquer espera ou elemento.

## Exemplo
Se a aplicação de teste realmente precisa de mais tempo, configure `pest()->browser()->timeout(10000)` e mantenha uma locator assertion sobre o estado que a ação deveria produzir.

## Limites e trade-offs
Timeout alto prolonga falhas reais; a actionability depende da ação e do locator, e condições externas como rede ou animações ainda podem causar flakiness.

## Como verificar
Atrase a renderização no servidor de teste e confirme a locator assertion dentro do timeout; em outro caso mantenha o elemento ausente e confirme uma falha limitada, sem substituir espera por sleep fixo.

## Conexões
- [[pest-browser-testes-reais-com-playwright]] — Veja também: Pest 5: reservar browser tests para fluxos que exigem navegador real.
- [[pest-arquitetura-tests-propriedade-de-regras]] — Veja também: Pest 5: expressar regras arquiteturais como testes executáveis.

## Fontes
- [Pest 5 — Browser Testing](https://pestphp.com/docs/browser-testing) — Playwright, navegação, seletores, browsers, timeout e diagnóstico; consultado em 2026-10-02.
- [Playwright — Auto-waiting](https://playwright.dev/docs/actionability) — verificações de actionability de locators e retry de assertions com timeout; consultado em 2026-10-02.
