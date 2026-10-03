---
id: software.testes.tranche25.001955
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

# A regra de três famílias de métodos da sintaxe: Actions, Assertions (see/dontSee) e Grabbers (grab)

## Em uma frase
Na seção The Codeception Syntax da página Getting Started, a documentação apresenta as três convenções de nomes que tornam os métodos fáceis de lembrar e ler: (1) Actions começam com um verbo simples em inglês, como `click`, `fillField` ou `pressKey`; (2) Assertions começam sempre com `see` ou `dontSee` (`see`, `seeInTitle`, `seeElement`, `dontSeeElement`, `dontSeeInPageSource`); e (3) Grabbers começam com `grab` (como `grabAttributeFrom`), capturando informações para salvar numa variável e usar depois no teste.

## Por que importa
Padronizar que toda ação é um verbo imperativo, toda verificação começa com `see`/`dontSee` e toda extração de valor começa com `grab` permite descobrir a API pelo autocompletar da IDE e distinguir imediatamente no código o que altera estado do que afirma ou lê dados.

## Como funciona
Em qualquer classe de teste com um ator `$I`, digite `$I->see` ou `$I->dontSee` para procurar asserções disponíveis nos módulos ativos, verbos diretos (`click`, `fillField`) para interagir e `$I->grab...` quando precisar extrair um atributo, texto ou registro para uma variável PHP.

## Exemplo
O exemplo oficial de Grabber extrai o método de um formulário e valida com uma asserção: `$method = $I->grabAttributeFrom('#login-form', 'method');` seguido de `$I->assertSame('post', $method);`.

## Limites e trade-offs
Os métodos concretos disponíveis sob `see*`, `dontSee*` e `grab*` em cada suíte dependem de quais módulos estão listados em `modules: enabled:` no arquivo `.suite.yml` daquela suíte.

## Como verificar
Conferi a seção The Codeception Syntax em codeception.com/docs/GettingStarted.

## Conexões
- [[codeception-unit-tests-on-top-of-phpunit]] — Veja também: Unit Tests sobre o PHPUnit e o uso de `$this->tester`.
- [[codeception-actors-modules-and-codecept-build]] — Veja também: Atores (`UnitTester`, `FunctionalTester`, `AcceptanceTester`), módulos e o comando `codecept build`.

## Fontes
- [Codeception 5 — Getting Started (documentação oficial)](https://codeception.com/docs/GettingStarted) — Capítulo 02 Getting Started da documentação oficial do Codeception 5 com regras de sintaxe (Actions, Assertions see/dontSee, Grabbers), Actors e Modules (PhpBrowser, codecept build), formato Cest, codecept run --steps e BDD.; consultado em 2026-10-03.
- [Codeception 5 — Introduction (documentação oficial)](https://codeception.com/docs/Introduction) — Capítulo 01 Introduction da documentação oficial do Codeception 5 com as três suítes (Unit, Functional, Acceptance), tabela comparativa de sete dimensões e exemplos com AcceptanceTester, FunctionalTester e PHPUnit.; consultado em 2026-10-03.
