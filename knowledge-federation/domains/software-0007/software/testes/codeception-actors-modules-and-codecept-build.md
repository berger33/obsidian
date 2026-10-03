---
id: software.testes.tranche25.001956
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-25.md"
fontes: ["https://codeception.com/docs/GettingStarted", "https://codeception.com/docs/Introduction"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Atores (`UnitTester`, `FunctionalTester`, `AcceptanceTester`), módulos e o comando `codecept build`

## Em uma frase
A seção Actors de Getting Started explica que o Codeception representa os testes como ações de uma pessoa por meio de três classes de ator — `UnitTester`, `FunctionalTester` e `AcceptanceTester` — cujos métodos vêm dos Codeception Modules configurados no `.suite.yml` de cada suíte (por padrão, `AcceptanceTester` usa o módulo `PhpBrowser` em `tests/Acceptance.suite.yml`); quando a configuração muda, as classes de ator são reconstruídas automaticamente ou manualmente com `php vendor/bin/codecept build`.

## Por que importa
Como cada projeto habilita uma combinação diferente de módulos em cada suíte, gerar o código das classes `AcceptanceTester`, `FunctionalTester` e `UnitTester` a partir do YAML (`codecept build`) entrega autocompletar estático real na IDE para todos os métodos injetados pelos módulos ativos.

## Como funciona
Habilite e configure os módulos necessários em `tests/Acceptance.suite.yml` (como `PhpBrowser` com `url: 'http://localhost/myapp/'`) e execute `php vendor/bin/codecept build` sempre que adicionar ou alterar módulos na configuração para atualizar as classes de ator.

## Exemplo
O bloco padrão mostrado em Getting Started para `tests/Acceptance.suite.yml` define `actor: AcceptanceTester` e, sob `modules: enabled:`, `- PhpBrowser: url: 'http://localhost/myapp/'`.

## Limites e trade-offs
Se você habilitar um módulo novo no `.suite.yml` e a IDE ou o executor reclamar que o método ainda não existe no objeto `$I`, rodar `php vendor/bin/codecept build` regenera a classe do ator imediatamente.

## Como verificar
Conferi a seção Actors em codeception.com/docs/GettingStarted.

## Conexões
- [[codeception-syntax-actions-assertions-grabbers]] — Veja também: A regra de três famílias de métodos da sintaxe: Actions, Assertions (see/dontSee) e Grabbers (grab).
- [[codeception-cest-format-generate-and-hooks]] — Veja também: O formato Cest: geração com `generate:cest`, métodos públicos de teste e hooks `_before` / `_after`.

## Fontes
- [Codeception 5 — Getting Started (documentação oficial)](https://codeception.com/docs/GettingStarted) — Capítulo 02 Getting Started da documentação oficial do Codeception 5 com regras de sintaxe (Actions, Assertions see/dontSee, Grabbers), Actors e Modules (PhpBrowser, codecept build), formato Cest, codecept run --steps e BDD.; consultado em 2026-10-03.
- [Codeception 5 — Introduction (documentação oficial)](https://codeception.com/docs/Introduction) — Capítulo 01 Introduction da documentação oficial do Codeception 5 com as três suítes (Unit, Functional, Acceptance), tabela comparativa de sete dimensões e exemplos com AcceptanceTester, FunctionalTester e PHPUnit.; consultado em 2026-10-03.
