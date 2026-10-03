---
id: software.testes.tranche15.000935
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
fontes: ["https://nodejs.org/api/test.html", "https://nodejs.org/api/test.html#mocking"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# node:test: avançar fake timers em vez de esperar tempo real

## Em uma frase
`MockTimers` permite habilitar APIs de timer selecionadas e avançar o relógio controlado, acelerando testes que verificam atraso, retry ou timeout.

## Por que importa
Um teste pode provar que callback ainda não foi chamado antes do prazo e que roda depois de `tick`, sem dormir segundos de wall-clock.

## Como funciona
O relógio falso deve ser ativado e restaurado dentro do caso que o usa.

## Exemplo
Habilite `context.mock.timers` para `setTimeout`, agende a função e chame `tick(9999)`; verifique contagem antes e depois do avanço.

## Limites e trade-offs
Nem toda fonte de tempo ou API agendada é necessariamente controlada por toda configuração do mock; usar timer fake pode alterar a ordem de callbacks em relação ao sistema real.

## Como verificar
Compare o comportamento esperado antes do avanço, depois do avanço parcial e no prazo exato; restaure timer mock ao encerrar para não afetar outros testes.

## Conexões
- [[node-test-mocks-com-restauracao-do-contexto]] — Veja também: node:test: preferir mocks vinculados ao contexto para restauração automática.
- [[node-test-randomize-seed-para-diagnosticar-ordem]] — Veja também: node:test: repetir uma ordem aleatória com seed registrada.

## Fontes
- [Node.js v26.10 — Test runner](https://nodejs.org/api/test.html) — TestContext, isolamento, hooks, mocks, concorrência e reporters; consultado em 2026-10-02.
- [Node.js v26.10 — Test runner: Mocking](https://nodejs.org/api/test.html#mocking) — MockTracker e MockTimers ligados ao contexto de teste; consultado em 2026-10-02.
