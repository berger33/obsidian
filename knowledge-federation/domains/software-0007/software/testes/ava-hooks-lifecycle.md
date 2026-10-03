---
id: software.testes.tranche21.001477
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-21.md"
fontes: ["https://github.com/avajs/ava/blob/main/docs/01-writing-tests.md", "https://github.com/avajs/ava/blob/main/docs/02-execution-context.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# AVA: ganchos before, after e always

## Em uma frase
O AVA registra test.before, test.after, test.beforeEach, test.afterEach e as variantes .always, que executam preparação e limpeza em torno dos testes do arquivo.

## Por que importa
Sem hooks, cada teste repetiria conexão e fechamento de recursos; com variantes .always, a limpeza acontece mesmo depois de falhas anteriores.

## Como funciona
Prepare o banco em before, restate o estado por caso com beforeEach e coloque a limpeza final em after.always para que rode apesar de falhas.

## Exemplo
O servidor HTTP de teste sobe em before, recebe requisições nos casos e é fechado em after.always mesmo com um teste vermelho no meio.

## Limites e trade-offs
Ganchos beforeEach/afterEach não rodam para testes pulados por .skip, e um teste que crasha por timeout pode impedir até os .always.

## Como verificar
Provoque uma falha no meio da suíte e confirme que o after.always continuou executando a limpeza.

## Conexões
- [[ava-only-skip-todo-failing]] — Veja também: AVA: only, skip, todo e failing.
- [[ava-magic-assert-diffs]] — Veja também: AVA: diagnóstico de falha com magic assert.

## Fontes
- [AVA — Guia Writing tests](https://github.com/avajs/ava/blob/main/docs/01-writing-tests.md) — concorrência, modificadores, hooks e isolamento; consultado em 2026-10-03.
- [AVA — Guia Execution context](https://github.com/avajs/ava/blob/main/docs/02-execution-context.md) — objeto de execução, t.plan e t.teardown; consultado em 2026-10-03.
