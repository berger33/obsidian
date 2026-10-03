---
id: software.testes.tranche15.000934
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

# node:test: preferir mocks vinculados ao contexto para restauração automática

## Em uma frase
Os mocks do test runner podem ser obtidos do contexto do caso, permitindo que o estado de mock seja associado ao lifecycle daquela execução.

## Por que importa
Mocks globais permanecem perigosos quando um teste falha antes de restaurá-los.

## Como funciona
O contexto deixa explícito quem possui o stub e limita vazamento entre casos dentro do mesmo processo.

## Exemplo
Use `context.mock.method(object, 'send', fake)` dentro do callback e faça as assertions de chamada por meio do objeto mockado.

## Limites e trade-offs
Mock não valida automaticamente o contrato do serviço real e trocar módulo ou método compartilhado pode afetar código executado concorrentemente no mesmo arquivo.

## Como verificar
Force uma falha antes do fim do caso e confirme que a implementação restaura o método para o estado original quando o contexto termina.

## Conexões
- [[node-test-t-contexto-para-recursos-descartaveis]] — Veja também: node:test: registrar teardown no contexto do caso.
- [[node-test-fake-timers-com-avanco-explicito]] — Veja também: node:test: avançar fake timers em vez de esperar tempo real.

## Fontes
- [Node.js v26.10 — Test runner](https://nodejs.org/api/test.html) — TestContext, isolamento, hooks, mocks, concorrência e reporters; consultado em 2026-10-02.
- [Node.js v26.10 — Test runner: Mocking](https://nodejs.org/api/test.html#mocking) — MockTracker e MockTimers ligados ao contexto de teste; consultado em 2026-10-02.
