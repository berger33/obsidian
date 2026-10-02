---
id: software.testes.tranche13.000663
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
fontes: ["https://jasmine.github.io/api/7.0/Clock", "https://jasmine.github.io/api/7.0/jasmine"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Jasmine: alinhar new Date ao relógio simulado

## Em uma frase
O relógio de Jasmine pode ser instruído a simular a data que `new Date()` retorna.

## Por que importa
Código que mistura timeout e data do calendário pode produzir fronteiras diferentes entre execução local e CI se só uma das fontes de tempo for controlada.

## Como funciona
Instale o clock, configure `mockDate()` com um instante explícito antes de chamar o código e avance timers com `tick` quando a lógica também depender de decurso de tempo.

## Exemplo
Uma expiração de sessão pode partir de uma data fixa e ser verificada antes e depois do prazo sem aguardar o relógio da máquina.

## Limites e trade-offs
Fixar Date não simula relógio de banco, serviço remoto ou bibliotecas que capturam APIs antes da instalação. Use valores em UTC e restaure o clock ao terminar.

## Como verificar
Repita o spec em fusos e instantes conhecidos e compare `Date` observada e disparo de timeout após instalar e remover o mock.

## Conexões
- [[jasmine-clock-tick-cleanup]] — Veja também: Jasmine: avançar relógio falso e restaurá-lo.
- [[jasmine-spy-through-vs-stub]] — Veja também: Jasmine: distinguir spy que observa de spy com resposta.

## Fontes
- [Jasmine 7 — Clock](https://jasmine.github.io/api/7.0/Clock) — mock clock installation, mockDate, tick and uninstall; consultado em 2026-10-02.
- [Jasmine 7 — jasmine namespace](https://jasmine.github.io/api/7.0/jasmine) — spy helpers, clock access and default timeout; consultado em 2026-10-02.
