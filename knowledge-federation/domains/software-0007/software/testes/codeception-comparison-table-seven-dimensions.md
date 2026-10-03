---
id: software.testes.tranche25.001951
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

# A tabela oficial de sete dimensões entre Unit, Functional e Acceptance Tests

## Em uma frase
A seção Introduction apresenta uma tabela comparativa direta entre Unit Tests, Functional Tests e Acceptance Tests ao longo de sete critérios: (1) escopo do teste (classe PHP única vs. framework PHP com rotas/banco vs. página no navegador Chrome/Firefox/PhpBrowser), (2) necessidade de acesso aos arquivos PHP do projeto (Yes, Yes, No), (3) necessidade de servidor web (No, No, Yes), (4) suporte a JavaScript (No, No, Yes), (5) software adicional exigido (None, None, chromedriver/geckodriver), (6) velocidade de execução (Very fast, Fast, Slow) e (7) arquivo de configuração (`Unit.suite.yml`, `Functional.suite.yml`, `Acceptance.suite.yml`).

## Por que importa
Essa matriz transforma a escolha do tipo de teste numa decisão objetiva de engenharia: se o cenário depende de JavaScript ou testa um site externo sem acesso ao código-fonte PHP, ele precisa ir para Acceptance; se precisa validar rota, controlador e banco com rapidez sem abrir navegador nem servidor web, cabe em Functional.

## Como funciona
Use as sete linhas da tabela oficial para distribuir a pirâmide de testes do projeto: mantenha a maior parte das regras de classe em `Unit.suite.yml`, os fluxos de requisição/banco em `Functional.suite.yml` e os fluxos visuais/JS em `Acceptance.suite.yml`.

## Exemplo
Como Acceptance Tests têm "Testing computer needs access to project's PHP files: No" e "Webserver required: Yes", a suíte de aceitação pode testar até mesmo um CMS exótico ou aplicação já publicada em um servidor de staging.

## Limites e trade-offs
Quando a suíte de aceitação usa o módulo `PhpBrowser` (emulador HTTP sem navegador real) em vez de chromedriver/geckodriver, ela continua exigindo um servidor web HTTP, mas não executa JavaScript no cliente.

## Como verificar
Conferi a tabela comparativa completa na página oficial codeception.com/docs/Introduction.

## Conexões
- [[codeception-what-it-is-and-three-suites]] — Veja também: Codeception: um único framework PHP para as suítes Unit, Functional e Acceptance.
- [[codeception-acceptance-tests-user-perspective]] — Veja também: Acceptance Tests: testar qualquer site pela perspectiva do usuário no navegador.

## Fontes
- [Codeception 5 — Introduction (documentação oficial)](https://codeception.com/docs/Introduction) — Capítulo 01 Introduction da documentação oficial do Codeception 5 com as três suítes (Unit, Functional, Acceptance), tabela comparativa de sete dimensões e exemplos com AcceptanceTester, FunctionalTester e PHPUnit.; consultado em 2026-10-03.
- [Codeception 5 — Getting Started (documentação oficial)](https://codeception.com/docs/GettingStarted) — Capítulo 02 Getting Started da documentação oficial do Codeception 5 com regras de sintaxe (Actions, Assertions see/dontSee, Grabbers), Actors e Modules (PhpBrowser, codecept build), formato Cest, codecept run --steps e BDD.; consultado em 2026-10-03.
