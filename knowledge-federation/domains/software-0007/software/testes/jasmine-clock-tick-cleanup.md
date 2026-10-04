---
id: software.testes.tranche13.000662
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
fontes: ["https://jasmine.github.io/api/7.0/Clock", "https://jasmine.github.io/api/7.0/global"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Jasmine: avançar relógio falso e restaurá-lo

## Em uma frase
`jasmine.clock()` instala relógio simulado que permite avançar timers enfileirados sem esperar tempo real.

## Por que importa
Timer controlado torna testes de debounce e expiração rápidos e reproduzíveis, além de evitar sleeps que aumentam a duração da suíte.

## Como funciona
Instale o clock durante setup, avance com `tick(millis)` até o instante relevante e desinstale em `afterEach` para devolver métodos nativos aos próximos specs.

## Exemplo
Um debounce de busca pode permanecer sem callback após 199 ms e executar depois que o teste avança o relógio para 200 ms.

## Limites e trade-offs
Clock não simula a conclusão de rede nem todas as fontes de tempo externas; o teardown precisa ocorrer mesmo se uma expectation falhar.

## Como verificar
Faça um timer real existir antes do `tick`, verifique quantas vezes foi chamado e confirme em outro spec que relógio e timers nativos foram restaurados.

## Conexões
- [[jasmine-done-callback]] — Veja também: Jasmine: encerrar callback uma única vez.
- [[jasmine-mock-date-time]] — Veja também: Jasmine: alinhar new Date ao relógio simulado.

## Fontes
- [Jasmine 7 — Clock](https://jasmine.github.io/api/7.0/Clock) — mock clock installation, mockDate, tick and uninstall; consultado em 2026-10-02.
- [Jasmine 7 — Global API](https://jasmine.github.io/api/7.0/global) — specs, suites, focus, hooks and async timeout; consultado em 2026-10-02.
