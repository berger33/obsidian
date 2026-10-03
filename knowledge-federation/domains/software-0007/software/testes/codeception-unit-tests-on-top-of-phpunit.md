---
id: software.testes.tranche25.001954
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

# Unit Tests sobre o PHPUnit e o uso de `$this->tester`

## Em uma frase
Na subseção Unit Tests de Introduction, a documentação afirma que o Codeception é construído sobre o PHPUnit: quem já escreve testes unitários padrão do PHPUnit pode continuar fazendo isso e executando-os normalmente no Codeception, mas ganha acesso às ferramentas dos módulos através da propriedade `$this->tester` (como `$this->tester->seeInDatabase(...)`).

## Por que importa
Em testes unitários e de integração de repositórios/modelos em PHP, a parte mais verbosa costuma ser consultar o banco após chamar `$user->save()`; combinar asserções clássicas do PHPUnit (`$this->assertSame(...)`) com helpers do Codeception (`$this->tester->seeInDatabase(...)`) enxuga o boilerplate sem abandonar o padrão xUnit.

## Como funciona
Escreva métodos `test...()` usando as asserções habituais do PHPUnit (`$this->assertSame`, etc.) e acione `$this->tester` quando precisar de ações ou verificações fornecidas pelos módulos habilitados em `Unit.suite.yml`.

## Exemplo
No exemplo oficial `testSavingUser(): void`, o teste instancia `$user = new User()`, define nome e sobrenome, chama `$user->save()`, verifica `$this->assertSame('Miles Davis', $user->getFullName())` e confirma a persistência com `$this->tester->seeInDatabase('users', ['firstName' => 'Miles', 'lastName' => 'Davis'])`.

## Limites e trade-offs
Para que métodos como `seeInDatabase` estejam disponíveis em `$this->tester` dentro do teste unitário, o módulo correspondente (por exemplo, `Db`) precisa estar habilitado no arquivo `Unit.suite.yml`.

## Como verificar
Conferi a subseção Unit Tests e o exemplo `testSavingUser` em codeception.com/docs/Introduction.

## Conexões
- [[codeception-functional-tests-no-webserver]] — Veja também: Functional Tests: emular requisições em PHP sem servidor web e inspecionar e-mail e banco.
- [[codeception-syntax-actions-assertions-grabbers]] — Veja também: A regra de três famílias de métodos da sintaxe: Actions, Assertions (see/dontSee) e Grabbers (grab).

## Fontes
- [Codeception 5 — Introduction (documentação oficial)](https://codeception.com/docs/Introduction) — Capítulo 01 Introduction da documentação oficial do Codeception 5 com as três suítes (Unit, Functional, Acceptance), tabela comparativa de sete dimensões e exemplos com AcceptanceTester, FunctionalTester e PHPUnit.; consultado em 2026-10-03.
- [Codeception 5 — Getting Started (documentação oficial)](https://codeception.com/docs/GettingStarted) — Capítulo 02 Getting Started da documentação oficial do Codeception 5 com regras de sintaxe (Actions, Assertions see/dontSee, Grabbers), Actors e Modules (PhpBrowser, codecept build), formato Cest, codecept run --steps e BDD.; consultado em 2026-10-03.
