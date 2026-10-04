---
id: software.testes.tranche25.001958
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

# Execução com `codecept run` e relatório passo a passo em inglês com `--steps`

## Em uma frase
Ainda em Writing a Sample Test, a documentação mostra como executar os testes após configurar a URL do servidor local em `tests/Acceptance.suite.yml`: `php vendor/bin/codecept run` roda toda a suíte exibindo o resumo compacto (`✔ SigninCest: sign in successfully`, tempo, memória e `OK (1 test, 1 assertion)`), enquanto `php vendor/bin/codecept run Acceptance --steps` imprime o relatório passo a passo de cada ação executada no cenário (`I am on page "/login"`, `I fill field "Username" "davert"`, `I click "Login"`, `I see "Hello, davert"`, `PASSED`).

## Por que importa
A flag `--steps` traduz automaticamente as chamadas de método PHP (`$I->fillField('Username', 'davert')`) em frases legíveis em inglês no terminal (`I fill field "Username" "davert"`), permitindo diagnosticar em qual passo exato do fluxo do usuário um teste funcional ou de aceitação falhou sem abrir o código-fonte.

## Como funciona
Use `php vendor/bin/codecept run` para execuções rápidas locais e adicione o nome da suíte e `--steps` (`php vendor/bin/codecept run Acceptance --steps`) em logs de CI ou sessões de depuração para registrar a transcrição completa do cenário.

## Exemplo
A saída oficial de `php vendor/bin/codecept run Acceptance --steps` mostra o cabeçalho `Signature: SigninCest.php:signInSuccessfully`, `Test: tests/Acceptance/SigninCest.php:signInSuccessfully` e a seção `Scenario --` listando as cinco frases `I ...` seguidas de `PASSED`.

## Limites e trade-offs
Antes de rodar a suíte `Acceptance` contra `PhpBrowser` ou navegador real, a própria documentação lembra que o site sob teste precisa estar rodando em um servidor web acessível na `url` configurada em `tests/Acceptance.suite.yml`.

## Como verificar
Conferi os blocos de execução `codecept run` e `codecept run Acceptance --steps` em codeception.com/docs/GettingStarted.

## Conexões
- [[codeception-cest-format-generate-and-hooks]] — Veja também: O formato Cest: geração com `generate:cest`, métodos públicos de teste e hooks `_before` / `_after`.
- [[codeception-bdd-gherkin-and-guides-map]] — Veja também: Suporte nativo a BDD/Gherkin e o mapa dos 17 capítulos da documentação oficial.

## Fontes
- [Codeception 5 — Getting Started (documentação oficial)](https://codeception.com/docs/GettingStarted) — Capítulo 02 Getting Started da documentação oficial do Codeception 5 com regras de sintaxe (Actions, Assertions see/dontSee, Grabbers), Actors e Modules (PhpBrowser, codecept build), formato Cest, codecept run --steps e BDD.; consultado em 2026-10-03.
- [Codeception 5 — Introduction (documentação oficial)](https://codeception.com/docs/Introduction) — Capítulo 01 Introduction da documentação oficial do Codeception 5 com as três suítes (Unit, Functional, Acceptance), tabela comparativa de sete dimensões e exemplos com AcceptanceTester, FunctionalTester e PHPUnit.; consultado em 2026-10-03.
