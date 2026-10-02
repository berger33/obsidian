---
id: software.testes.tranche13.000651
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
fontes: ["https://mochajs.org/features/hooks/", "https://mochajs.org/features/interfaces/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Mocha: controlar ordem e escopo de hooks aninhados

## Em uma frase
`before` e `after` envolvem uma suite, enquanto `beforeEach` e `afterEach` acompanham cada teste daquele escopo.

## Por que importa
Hooks explícitos ajudam a criar fixtures e liberar recursos com uma ordem previsível quando os exemplos têm estados diferentes.

## Como funciona
Coloque a preparação comum no menor `describe()` que realmente a compartilha; em grupos aninhados, revise a ordem de hooks de fora para dentro e faça teardown no sentido inverso.

## Exemplo
Uma suite externa abre uma conexão de teste e uma interna cria uma conta antes de cada caso; a limpeza interna remove a conta antes da suite externa encerrar a conexão.

## Limites e trade-offs
Hook de suite que altera estado pode fazer um exemplo depender do anterior. Para callbacks de cleanup, propague o erro em vez de marcar conclusão antes da operação terminar.

## Como verificar
Introduza uma falha no setup interno e confira no reporter qual hook foi executado e se o teardown dos recursos já criados ainda é seguro.

## Conexões
- [[mocha-bdd-suite-tree]] — Veja também: Mocha: organizar suites BDD com describe e it.
- [[mocha-async-completion-contract]] — Veja também: Mocha: escolher uma única forma de concluir teste assíncrono.

## Fontes
- [Mocha — Hooks](https://mochajs.org/features/hooks/) — nested setup/teardown hooks and async hook behavior; consultado em 2026-10-02.
- [Mocha — Interfaces](https://mochajs.org/features/interfaces/) — BDD, TDD and other suite-definition interfaces; consultado em 2026-10-02.
