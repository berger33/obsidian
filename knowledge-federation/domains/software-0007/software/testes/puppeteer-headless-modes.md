---
id: software.testes.tranche15.000856
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://pptr.dev/api/puppeteer.launchoptions", "https://pptr.dev/webdriver-bidi"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Puppeteer: distinguir os modos headless

## Em uma frase
O modo headless moderno é o padrão de lançamento, e o binário reduzido `chrome-headless-shell` é solicitado com `headless: 'shell'`, enquanto `headless: false` abre a janela para depuração.

## Por que importa
Modos diferentes oferecem recursos e desempenho diferentes, e depender do padrão da versão instalada faz a execução mudar de comportamento após uma atualização da biblioteca.

## Como funciona
Deixe o padrão para testes funcionais, use modo visível com desaceleração apenas na investigação local e reserve o shell para cenários em que o binário completo não é necessário.

## Exemplo
`await puppeteer.launch({ headless: false, slowMo: 50 })` mostra a janela e desacelera os passos o suficiente para acompanhar a sequência durante o diagnóstico.

## Limites e trade-offs
O modo visível depende de display e não escala em integração contínua, e a desaceleração mascara condições de corrida que o pipeline deveria expor.

## Como verificar
Execute o fluxo nos três modos e compare recursos disponíveis, tempo total e falhas observadas antes de fixar a escolha do projeto.

## Conexões
- [[puppeteer-bidi-vs-cdp]] — Veja também: Puppeteer: escolher entre CDP e WebDriver BiDi.
- [[puppeteer-navigation-race-free]] — Veja também: Puppeteer: evitar corrida entre ação e navegação.

## Fontes
- [Puppeteer — Launch options](https://pptr.dev/api/puppeteer.launchoptions) — opções de lançamento, headless, protocolo, produto e argumentos; consultado em 2026-10-02.
- [Puppeteer — WebDriver BiDi support](https://pptr.dev/webdriver-bidi) — protocolos suportados, padrão por navegador e operações incompatíveis; consultado em 2026-10-02.
