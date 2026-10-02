---
id: software.testes.tranche13.000672
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
fontes: ["https://webdriver.io/docs/api/element/waitForDisplayed/", "https://webdriver.io/docs/autowait/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# WebdriverIO: esperar visibilidade sem presumir presença

## Em uma frase
`waitForDisplayed()` aguarda que um elemento esteja exibido, condição diferente de apenas localizar um seletor no DOM.

## Por que importa
Um elemento pode existir antes de se tornar utilizável; testar visibilidade aproxima a espera do que o usuário realmente consegue observar.

## Como funciona
Localize o alvo, chame a espera específica com prazo adequado e só então faça assertion ou interação; use `reverse` apenas para expressar desaparecimento intencional.

## Exemplo
Um toast de confirmação pode aguardar exibição após resposta de gravação e depois ser verificado pelo texto.

## Limites e trade-offs
Visibilidade não garante que a resposta de negócio está correta nem que o elemento está habilitado. Se a condição for outra, prefira waitUntil ou matcher apropriado.

## Como verificar
Controle a animação para atrasar a exibição e confirme que a espera termina no estado previsto, não em presença prematura no DOM.

## Conexões
- [[webdriverio-waituntil-condition]] — Veja também: WebdriverIO: modelar condição temporal com waitUntil.
- [[webdriverio-soft-assertion-aggregation]] — Veja também: WebdriverIO: acumular falhas independentes com soft assertions.

## Fontes
- [WebdriverIO — waitForDisplayed](https://webdriver.io/docs/api/element/waitForDisplayed/) — explicit element visibility waits; consultado em 2026-10-02.
- [WebdriverIO — Auto-waiting](https://webdriver.io/docs/autowait/) — automatic interactability waits and implicit-timeout caveats; consultado em 2026-10-02.
