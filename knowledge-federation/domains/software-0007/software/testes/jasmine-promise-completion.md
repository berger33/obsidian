---
id: software.testes.tranche13.000660
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

# Jasmine: devolver promessa para aguardar operação

## Em uma frase
Jasmine aguarda a promessa retornada por um spec ou hook e falha o spec quando ela rejeita.

## Por que importa
Um teste precisa manter a assertion ligada ao trabalho assíncrono que a produz, em vez de terminar assim que a função síncrona retorna.

## Como funciona
Use uma função `async` com `await` ou devolva diretamente a promessa encadeada; inclua na cadeia as expectativas que dependem do resultado.

## Exemplo
Um teste de carregamento pode `await` a resposta do cliente e então comparar o estado do modelo dentro do mesmo spec.

## Limites e trade-offs
Criar promessa sem retorná-la permite que Jasmine avance cedo. Uma assertion executada depois que a função terminou pode escapar do resultado correto.

## Como verificar
Substitua a promessa por uma rejeição conhecida e confirme que a execução marca o spec atual como falho e não passa ao próximo antes do settle.

## Conexões
- [[jasmine-done-callback]] — Veja também: Jasmine: encerrar callback uma única vez.

## Fontes
- [Jasmine — Testing Async Code](https://jasmine.github.io/tutorials/async) — async/await, promises, callbacks and failure propagation; consultado em 2026-10-02.
- [Jasmine 7 — Global API](https://jasmine.github.io/api/7.0/global) — specs, suites, focus, hooks and async timeout; consultado em 2026-10-02.
