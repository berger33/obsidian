---
id: software.testes.tranche15.000931
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

# node:test: separar concorrência de arquivos e subtestes

## Em uma frase
O runner tem níveis diferentes de concorrência: `--test-concurrency` limita arquivos de teste executados em paralelo, enquanto opções de `test()` controlam casos assíncronos dentro do runner.

## Por que importa
Paralelizar arquivos eleva quantidade de processos; paralelizar subtestes agenda promises no event loop.

## Como funciona
Ajustar uma opção não configura automaticamente a outra, então métricas de saturação precisam apontar para o nível correto.

## Exemplo
Limite arquivos com `node --test --test-concurrency=4` e habilite `concurrency` apenas no conjunto de subtestes que não compartilha estado mutável.

## Limites e trade-offs
Testes continuam no mesmo event loop dentro do processo e concorrência com `true` pode expor race conditions lógicas mesmo sem threads JavaScript.

## Como verificar
Registre quantos arquivos e subtestes estão ativos ao mesmo tempo, rode com limites diferentes e confirme que testes que compartilham recurso ficam sequenciais.

## Conexões
- [[node-test-isolamento-processo-por-arquivo]] — Veja também: node:test: compreender o isolamento padrão entre arquivos de teste.
- [[node-test-name-pattern-e-filtros-de-casos]] — Veja também: node:test: usar filtro de nome sem confundir seleção com descoberta.

## Fontes
- [Node.js v26.10 — Command-line API](https://nodejs.org/api/cli.html) — flags de execução, seleção, reporters, cobertura e sharding; consultado em 2026-10-02.
- [Node.js v26.10 — Test runner](https://nodejs.org/api/test.html) — TestContext, isolamento, hooks, mocks, concorrência e reporters; consultado em 2026-10-02.
