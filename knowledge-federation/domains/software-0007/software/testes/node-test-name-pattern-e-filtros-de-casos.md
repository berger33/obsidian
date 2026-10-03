---
id: software.testes.tranche15.000932
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
fontes: ["https://nodejs.org/api/cli.html", "https://nodejs.org/api/test.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# node:test: usar filtro de nome sem confundir seleção com descoberta

## Em uma frase
`--test-name-pattern` filtra testes por uma expressão regular, e o nome de testes e subtestes pode fazer parte do resultado da seleção.

## Por que importa
Um filtro rápido é útil durante depuração, mas a suíte pode terminar sem cobrir casos importantes se o padrão estiver errado ou não corresponder à estrutura de nomes atual.

## Como funciona
A seleção por arquivo e a seleção por nome são dimensões independentes.

## Exemplo
Rode `node --test --test-name-pattern='validates user'` para iterar sobre uma família e confira o resumo do runner para saber quantos casos foram ignorados.

## Limites e trade-offs
Se também existir `--test-skip-pattern`, um teste precisa satisfazer ambos os requisitos documentados; expressões shell precisam ser citadas para não serem expandidas pelo terminal.

## Como verificar
Passe um padrão conhecido e outro que não corresponda, depois compare a saída com a execução completa antes de usar o filtro em CI.

## Conexões
- [[node-test-concurrency-por-arquivo-e-por-caso]] — Veja também: node:test: separar concorrência de arquivos e subtestes.
- [[node-test-t-contexto-para-recursos-descartaveis]] — Veja também: node:test: registrar teardown no contexto do caso.

## Fontes
- [Node.js v26.10 — Command-line API](https://nodejs.org/api/cli.html) — flags de execução, seleção, reporters, cobertura e sharding; consultado em 2026-10-02.
- [Node.js v26.10 — Test runner](https://nodejs.org/api/test.html) — TestContext, isolamento, hooks, mocks, concorrência e reporters; consultado em 2026-10-02.
