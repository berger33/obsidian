---
id: software.testes.tranche13.000669
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
fontes: ["https://jasmine.github.io/api/7.0/async-matchers", "https://jasmine.github.io/tutorials/async"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Jasmine: aguardar resultado de expectAsync

## Em uma frase
`expectAsync()` cria expectations cujos matchers retornam promises que precisam ser aguardadas ou retornadas.

## Por que importa
A API permite afirmar sobre resolução ou rejeição assíncrona sem converter o spec em callback de baixo nível.

## Como funciona
Use `await expectAsync(promise).toBeResolved()` ou retorne a promise da expectation; encadeie a assertion na função async que Jasmine monitora.

## Exemplo
Um serviço pode testar que uma promise de validação rejeita com o contrato esperado usando um matcher async dentro do spec.

## Limites e trade-offs
Ignorar a promise do matcher deixa a expectation fora do ciclo reconhecido e pode produzir um falso positivo ou erro tardio.

## Como verificar
Troque a promise esperada por resolução e rejeição e confirme que só a forma correta passa quando a matcher promise é aguardada.

## Conexões
- [[jasmine-pending-spec-intent]] — Veja também: Jasmine: registrar pending sem confundir com cobertura.

## Fontes
- [Jasmine 7 — Async Matchers](https://jasmine.github.io/api/7.0/async-matchers) — promise-returning asynchronous expectations; consultado em 2026-10-02.
- [Jasmine — Testing Async Code](https://jasmine.github.io/tutorials/async) — async/await, promises, callbacks and failure propagation; consultado em 2026-10-02.
