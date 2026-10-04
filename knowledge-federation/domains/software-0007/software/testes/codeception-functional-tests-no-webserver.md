---
id: software.testes.tranche25.001953
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
fontes: ["https://codeception.com/docs/Introduction", "https://codeception.com/docs/GettingStarted"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Functional Tests: emular requisições em PHP sem servidor web e inspecionar e-mail e banco

## Em uma frase
A subseção Functional Tests de Introduction explica o papel intermediário: testar a aplicação sem rodá-la num servidor web, emulando uma requisição web (variáveis `$_GET` e `$_POST`) diretamente em PHP que devolve a resposta HTML, o que permite ver exceções detalhadas em caso de erro, rodar mais rápido e verificar banco de dados e e-mails contra resultados esperados usando módulos para os frameworks PHP populares.

## Por que importa
Ao executar dentro do mesmo processo PHP da aplicação via módulo do framework (Symfony, Laravel, Yii, etc.) sem passar por rede nem navegador, o teste funcional combina a sintaxe de alto nível do usuário (`amOnPage`, `click`, `submitForm`) com asserções de estado interno (`seeEmailIsSent`, `seeInDatabase`).

## Como funciona
Configure o módulo do seu framework em `Functional.suite.yml` e escreva cenários com `FunctionalTester $I` que combinem passos de interface com verificações de efeitos colaterais no banco e no mailer.

## Exemplo
No exemplo oficial `trySignupForm(FunctionalTester $I): void`, os quatro primeiros passos são idênticos aos do teste de aceitação, mas o final adiciona `$I->seeEmailIsSent('miles@example.com', 'Thank you for your registration');` e `$I->seeInDatabase('users', ['email' => 'miles@example.com']);`.

## Limites e trade-offs
Diferentemente dos testes de aceitação que funcionam contra qualquer site externo, a documentação ressalva que para testes funcionais a aplicação precisa estar estruturada para rodar em ambiente de teste através de um módulo de framework suportado.

## Como verificar
Conferi a subseção Functional Tests e seu exemplo de código em codeception.com/docs/Introduction.

## Conexões
- [[codeception-acceptance-tests-user-perspective]] — Veja também: Acceptance Tests: testar qualquer site pela perspectiva do usuário no navegador.
- [[codeception-unit-tests-on-top-of-phpunit]] — Veja também: Unit Tests sobre o PHPUnit e o uso de `$this->tester`.

## Fontes
- [Codeception 5 — Introduction (documentação oficial)](https://codeception.com/docs/Introduction) — Capítulo 01 Introduction da documentação oficial do Codeception 5 com as três suítes (Unit, Functional, Acceptance), tabela comparativa de sete dimensões e exemplos com AcceptanceTester, FunctionalTester e PHPUnit.; consultado em 2026-10-03.
- [Codeception 5 — Getting Started (documentação oficial)](https://codeception.com/docs/GettingStarted) — Capítulo 02 Getting Started da documentação oficial do Codeception 5 com regras de sintaxe (Actions, Assertions see/dontSee, Grabbers), Actors e Modules (PhpBrowser, codecept build), formato Cest, codecept run --steps e BDD.; consultado em 2026-10-03.
