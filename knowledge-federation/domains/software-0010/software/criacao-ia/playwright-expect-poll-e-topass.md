---
id: software.criacao_ia.tranche03.000277
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-03.md"
fontes: ["https://playwright.dev/docs/test-assertions", "https://playwright.dev/docs/test-timeouts"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Playwright assertions: escolher expect.poll ou expect.toPass

## Em uma frase
`expect.poll` repete uma leitura até um valor satisfazer matcher; `expect.toPass` repete um bloco que contém uma ou mais verificações.

## Por que importa
Um sleep fixo aguarda tempo mesmo quando a condição já ocorreu e falha cedo ou tarde conforme variação do ambiente. Polling de condição expressa diretamente o resultado esperado, enquanto o bloco retry permite uma sequência de verificações correlacionadas.

## Como funciona
Use auto-retrying locator assertions para estado de DOM, `expect.poll` para recuperar e comparar um valor assíncrono, e `expect.toPass` para repetir uma sequência. Defina `timeout` e `intervals` apropriados. Importante: `toPass` tem timeout 0 por padrão e não herda o timeout global de expect; configure-o explicitamente para evitar que comportamento ilimitado passe despercebido.

## Exemplo
Um endpoint eventual retorna status 202 antes de 200; `expect.poll` consulta status com intervalos crescentes e timeout delimitado. Para uma sequência onde criação e consulta de job precisam ser verificadas juntas, `toPass` envolve o bloco inteiro com tempo limite definido.

## Limites e trade-offs
Retries podem repetir chamadas com efeitos colaterais se o callback não for idempotente. Um polling agressivo adiciona carga ao sistema; use intervalos e observabilidade que respeitam limites de API.

## Como verificar
Teste condição imediata, eventual e impossível, verifique número de sondagens e saída no timeout. Faça a ação de escrita fora do callback de retry ou proteja-a com identificador idempotente.

## Conexões
- [[playwright-video-context-close-artifact]] — Playwright video: fechar browser context para salvar o arquivo.
- [[playwright-timeouts-escopos-separados]] — Playwright Test: diagnosticar timeouts por escopo.

## Fontes
- [Playwright — Assertions](https://playwright.dev/docs/test-assertions) — documenta expect.poll, toPass, intervals e timeout padrão de toPass Consulta: 2026-10-04.
- [Playwright — Timeouts](https://playwright.dev/docs/test-timeouts) — distingue timeout de assertion do timeout total do teste Consulta: 2026-10-04.
