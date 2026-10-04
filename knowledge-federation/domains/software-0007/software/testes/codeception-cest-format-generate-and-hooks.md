---
id: software.testes.tranche25.001957
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

# O formato Cest: geração com `generate:cest`, métodos públicos de teste e hooks `_before` / `_after`

## Em uma frase
Na seção Writing a Sample Test de Getting Started, a documentação apresenta o formato nativo de testes orientados a cenários do Codeception chamado Cest (combinação de "Codecept" e "Test"), criado com o comando `php vendor/bin/codecept generate:cest Acceptance Signin`, que gera `tests/Acceptance/SigninCest.php` contendo uma classe PHP onde cada método público (como `signInSuccessfully(AcceptanceTester $I): void`) é um teste e os métodos especiais `_before(AcceptanceTester $I)` e `_after` executam ações comuns antes e depois de cada teste.

## Por que importa
Ao contrário de scripts lineares soltos, uma classe Cest agrupa vários cenários relacionados do mesmo recurso (por exemplo, login com sucesso, login com senha errada ou CRUD de tarefas em `TaskCrudCest`), compartilhando a navegação ou preparação inicial dentro de `_before(AcceptanceTester $I)`.

## Como funciona
Gere o esqueleto com `php vendor/bin/codecept generate:cest <Suite> <Nome>`, crie um método público recebendo o ator `$I` para cada cenário que quiser testar e mova passos repetidos de abertura de página ou autenticação para o método `_before(AcceptanceTester $I): void`.

## Exemplo
No exemplo `SigninCest` de Getting Started, o método `signInSuccessfully(AcceptanceTester $I): void` executa `$I->amOnPage('/login');`, `$I->fillField('Username', 'davert');`, `$I->fillField('Password', 'qwerty');`, `$I->click('Login');` e `$I->see('Hello, davert');`, enquanto `TaskCrudCest` coloca `$I->amOnPage('/task');` dentro de `_before`.

## Limites e trade-offs
Métodos auxiliares privados ou protegidos (ou prefixados com `_` como `_before` e `_after`) não são executados como testes independentes; apenas métodos públicos comuns da classe Cest viram casos de teste na rodada.

## Como verificar
Conferi a seção Writing a Sample Test em codeception.com/docs/GettingStarted.

## Conexões
- [[codeception-actors-modules-and-codecept-build]] — Veja também: Atores (`UnitTester`, `FunctionalTester`, `AcceptanceTester`), módulos e o comando `codecept build`.
- [[codeception-run-and-steps-flag]] — Veja também: Execução com `codecept run` e relatório passo a passo em inglês com `--steps`.

## Fontes
- [Codeception 5 — Getting Started (documentação oficial)](https://codeception.com/docs/GettingStarted) — Capítulo 02 Getting Started da documentação oficial do Codeception 5 com regras de sintaxe (Actions, Assertions see/dontSee, Grabbers), Actors e Modules (PhpBrowser, codecept build), formato Cest, codecept run --steps e BDD.; consultado em 2026-10-03.
- [Codeception 5 — Introduction (documentação oficial)](https://codeception.com/docs/Introduction) — Capítulo 01 Introduction da documentação oficial do Codeception 5 com as três suítes (Unit, Functional, Acceptance), tabela comparativa de sete dimensões e exemplos com AcceptanceTester, FunctionalTester e PHPUnit.; consultado em 2026-10-03.
