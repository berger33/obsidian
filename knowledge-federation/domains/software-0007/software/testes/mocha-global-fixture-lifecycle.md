---
id: software.testes.tranche13.000659
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
fontes: ["https://mochajs.org/features/global-fixtures/", "https://mochajs.org/features/hooks/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Mocha: separar fixture global de hooks de suite

## Em uma frase
Global fixtures oferecem configuração e limpeza uma vez para a execução do Mocha, ao passo que hooks pertencem às suites e seus testes.

## Por que importa
A escolha correta evita abrir repetidamente um recurso caro ou, no extremo oposto, compartilhar estado de caso sem isolamento.

## Como funciona
Use fixture global apenas para infraestrutura que realmente dura o run inteiro; mantenha dados de negócio em hooks por teste e assegure teardown mesmo quando a suíte falhar.

## Exemplo
A CI pode iniciar um servidor auxiliar no começo do run, enquanto cada caso cria e remove seus próprios registros para não depender do caso anterior.

## Limites e trade-offs
Uma fixture única não torna seguro compartilhar dados mutáveis com workers concorrentes, e o término de processo pode interromper limpeza que dependa de sinalização.

## Como verificar
Force uma falha no meio da execução e observe se a fixture global fecha o recurso, depois rode dois casos e confira que seus dados não se misturam.

## Conexões
- [[mocha-reporter-parallel-output]] — Veja também: Mocha: combinar reporter com o modo de execução.

## Fontes
- [Mocha — Global Fixtures](https://mochajs.org/features/global-fixtures/) — once-per-run setup and teardown; consultado em 2026-10-02.
- [Mocha — Hooks](https://mochajs.org/features/hooks/) — nested setup/teardown hooks and async hook behavior; consultado em 2026-10-02.
