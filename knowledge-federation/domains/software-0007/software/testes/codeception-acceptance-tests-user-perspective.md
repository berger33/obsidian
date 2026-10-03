---
id: software.testes.tranche25.001952
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

# Acceptance Tests: testar qualquer site pela perspectiva do usuário no navegador

## Em uma frase
Na subseção Acceptance Tests da página Introduction, a documentação define que os testes de aceitação reproduzem como um cliente sabe que o site funciona — abrindo o navegador, acessando o site, clicando em links, preenchendo formulários e vendo o conteúdo na página —, destacando em citação que qualquer website pode ser coberto com testes de aceitação, mesmo se usar um CMS ou framework muito exótico.

## Por que importa
Como o teste de aceitação conversa com a aplicação exclusivamente por HTTP/navegador como um usuário externo, ele independe da arquitetura interna do código PHP e valida a integração real entre servidor web, rotas, templates e ativos.

## Como funciona
Escreva métodos que recebam `AcceptanceTester $I` e encadeie navegação (`amOnPage`), interação (`click`, `fillField` ou `submitForm`) e verificação visual (`see`) contra a URL configurada em `Acceptance.suite.yml`.

## Exemplo
O exemplo oficial `trySignupForm(AcceptanceTester $I): void` executa `$I->amOnPage('/');`, `$I->click('Sign Up');`, `$I->submitForm('#signup', ['username' => 'MilesDavis', 'email' => 'miles@example.com']);` e `$I->see('Thank you for Signing Up!');`.

## Limites e trade-offs
Por exigirem servidor web ativo e, quando configurados com navegador real, chromedriver ou geckodriver, os testes de aceitação são classificados na tabela oficial como lentos ("Slow") em comparação aos testes funcionais e unitários.

## Como verificar
Conferi a subseção Acceptance Tests e o exemplo `trySignupForm(AcceptanceTester $I)` em codeception.com/docs/Introduction.

## Conexões
- [[codeception-comparison-table-seven-dimensions]] — Veja também: A tabela oficial de sete dimensões entre Unit, Functional e Acceptance Tests.
- [[codeception-functional-tests-no-webserver]] — Veja também: Functional Tests: emular requisições em PHP sem servidor web e inspecionar e-mail e banco.

## Fontes
- [Codeception 5 — Introduction (documentação oficial)](https://codeception.com/docs/Introduction) — Capítulo 01 Introduction da documentação oficial do Codeception 5 com as três suítes (Unit, Functional, Acceptance), tabela comparativa de sete dimensões e exemplos com AcceptanceTester, FunctionalTester e PHPUnit.; consultado em 2026-10-03.
- [Codeception 5 — Getting Started (documentação oficial)](https://codeception.com/docs/GettingStarted) — Capítulo 02 Getting Started da documentação oficial do Codeception 5 com regras de sintaxe (Actions, Assertions see/dontSee, Grabbers), Actors e Modules (PhpBrowser, codecept build), formato Cest, codecept run --steps e BDD.; consultado em 2026-10-03.
