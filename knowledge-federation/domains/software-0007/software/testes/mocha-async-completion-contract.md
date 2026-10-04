---
id: software.testes.tranche13.000652
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
fontes: ["https://mochajs.org/features/asynchronous-code/", "https://mochajs.org/features/hooks/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Mocha: escolher uma única forma de concluir teste assíncrono

## Em uma frase
Mocha reconhece teste síncrono, callback `done`, promessa retornada e função `async` que devolve promessa.

## Por que importa
Declarar corretamente a conclusão impede que o runner avance antes da assertion ou trate um erro tardio como resultado de outro teste.

## Como funciona
Em código baseado em callback, aceite `done` e invoque-o após verificar o resultado; com `async`, use `await`; com promessa direta, retorne a cadeia. Não combine `done` com uma promessa retornada.

## Exemplo
Um teste de leitura de arquivo pode retornar a promessa de `readFile()` e validar o texto no mesmo encadeamento, sem chamar um callback paralelo de término.

## Limites e trade-offs
Uma promessa criada mas não retornada não mantém o teste aberto. Também evite chamar `done()` antes de terminar trabalho que ainda pode lançar exceção.

## Como verificar
Force uma rejeição e uma falha de assertion; ambas devem ser atribuídas ao teste atual e o processo não deve terminar com execução assíncrona pendente.

## Conexões
- [[mocha-hooks-nested-order]] — Veja também: Mocha: controlar ordem e escopo de hooks aninhados.
- [[mocha-root-hooks-plugin]] — Veja também: Mocha: instalar root hooks por plugin reutilizável.

## Fontes
- [Mocha — Asynchronous Code](https://mochajs.org/features/asynchronous-code/) — callbacks, promises and async test completion; consultado em 2026-10-02.
- [Mocha — Hooks](https://mochajs.org/features/hooks/) — nested setup/teardown hooks and async hook behavior; consultado em 2026-10-02.
