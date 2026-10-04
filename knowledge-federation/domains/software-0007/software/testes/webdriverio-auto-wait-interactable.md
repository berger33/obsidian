---
id: software.testes.tranche13.000670
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-13.md"
fontes: ["https://webdriver.io/docs/autowait/", "https://webdriver.io/docs/api/element/waitForDisplayed/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# WebdriverIO: confiar no auto-wait para interação

## Em uma frase
Comandos que interagem diretamente com elemento aguardam que ele esteja visível e interagível antes de agir.

## Por que importa
Esse comportamento elimina muitos sleeps colocados antes de cada clique, mantendo a sincronização perto da operação que precisa dela.

## Como funciona
Use `click()` ou `setValue()` normalmente e recorra a waits explícitos apenas quando a condição de negócio não for coberta pelo estado de interagibilidade do elemento.

## Exemplo
Depois que o botão fica habilitado e clicável, o teste clica nele sem acrescentar atraso fixo de dois segundos ao caminho feliz.

## Limites e trade-offs
Auto-wait não conhece estado de backend ou regra de negócio; uma busca por resultado específico ainda precisa de condição que observe esse resultado.

## Como verificar
Deixe a aplicação renderizar com atraso controlado e confirme que interação aguarda o alvo, mas falha com diagnóstico se ele nunca se tornar interagível.

## Conexões
- [[webdriverio-waituntil-condition]] — Veja também: WebdriverIO: modelar condição temporal com waitUntil.

## Fontes
- [WebdriverIO — Auto-waiting](https://webdriver.io/docs/autowait/) — automatic interactability waits and implicit-timeout caveats; consultado em 2026-10-02.
- [WebdriverIO — waitForDisplayed](https://webdriver.io/docs/api/element/waitForDisplayed/) — explicit element visibility waits; consultado em 2026-10-02.
