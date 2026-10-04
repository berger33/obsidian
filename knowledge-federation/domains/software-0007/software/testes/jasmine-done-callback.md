---
id: software.testes.tranche13.000661
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
fontes: ["https://jasmine.github.io/tutorials/async", "https://jasmine.github.io/api/7.0/global"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Jasmine: encerrar callback uma única vez

## Em uma frase
Ao declarar argumento `done`, o spec ou hook usa o callback entregue por Jasmine para sinalizar conclusão.

## Por que importa
Essa forma integra código legado baseado em callbacks, mas exige cuidado porque uma assertion tardia ou um `done()` prematuro pode dissociar erro e spec.

## Como funciona
Chame `done` apenas após todas as expectativas; trate erro passando-o ou usando `done.fail`, e garanta que caminhos de sucesso e falha não o invoquem duas vezes.

## Exemplo
Um adaptador de callback pode chamar `done.fail(err)` na falha do serviço e `done()` somente quando a resposta validada chega.

## Limites e trade-offs
Não misture callback de conclusão com função que retorna promise; escolha um contrato por teste para o runner não receber sinais conflitantes.

## Como verificar
Teste sucesso, rejeição e timeout com callbacks controlados e confirme que cada caminho produz exatamente um resultado associado ao spec original.

## Conexões
- [[jasmine-promise-completion]] — Veja também: Jasmine: devolver promessa para aguardar operação.
- [[jasmine-clock-tick-cleanup]] — Veja também: Jasmine: avançar relógio falso e restaurá-lo.

## Fontes
- [Jasmine — Testing Async Code](https://jasmine.github.io/tutorials/async) — async/await, promises, callbacks and failure propagation; consultado em 2026-10-02.
- [Jasmine 7 — Global API](https://jasmine.github.io/api/7.0/global) — specs, suites, focus, hooks and async timeout; consultado em 2026-10-02.
