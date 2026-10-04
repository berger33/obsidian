---
id: software.testes.tranche25.001959
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

# Suporte nativo a BDD/Gherkin e o mapa dos 17 capítulos da documentação oficial

## Em uma frase
A seção Behavior Driven Development (BDD) e a barra lateral Guides de Getting Started / Introduction mostram que, além dos formatos Cest e PHPUnit, o Codeception permite executar histórias de usuário em formato Gherkin de maneira semelhante ao Cucumber ou ao Behat (capítulo 10, `codeception.com/docs/BDD`), dentro de um mapa de 17 guias oficiais que cobrem Debugging (06), Modules And Helpers (07), Reusing Test Code (08), Advanced Usage (09), Data (12), API Testing (13), Codecoverage (14), Reporting (15), Continuous Integration (16) e Parallel Execution (17).

## Por que importa
Equipes que já adotam o Codeception para testes unitários, funcionais, Cest e de API não precisam instalar uma ferramenta separada quando o time de produto passa a escrever arquivos `.feature` em Gherkin: o mesmo ator `$I` e os mesmos módulos podem alimentar os passos BDD.

## Como funciona
Consulte o capítulo BDD (`codeception.com/docs/BDD`) quando quiser executar arquivos Gherkin sobre os atores do Codeception, e recorra aos capítulos específicos do guia (como `APITesting`, `Data`, `Codecoverage` e `ParallelExecution`) conforme a suíte crescer.

## Exemplo
Uma mesma aplicação PHP pode manter testes unitários em PHPUnit, cenários técnicos em classes Cest, testes de contrato REST no capítulo API Testing e histórias de negócio em Gherkin, todos executados por `php vendor/bin/codecept run`.

## Limites e trade-offs
A página Getting Started apresenta apenas a visão geral da capacidade BDD e da configuração global `codeception.yml`, remetendo aos respectivos capítulos numerados (01 a 17) para as diretivas detalhadas.

## Como verificar
Conferi a seção Behavior Driven Development (BDD) e o índice lateral Guides (01 a 17) em codeception.com/docs/GettingStarted.

## Conexões
- [[codeception-run-and-steps-flag]] — Veja também: Execução com `codecept run` e relatório passo a passo em inglês com `--steps`.

## Fontes
- [Codeception 5 — Getting Started (documentação oficial)](https://codeception.com/docs/GettingStarted) — Capítulo 02 Getting Started da documentação oficial do Codeception 5 com regras de sintaxe (Actions, Assertions see/dontSee, Grabbers), Actors e Modules (PhpBrowser, codecept build), formato Cest, codecept run --steps e BDD.; consultado em 2026-10-03.
- [Codeception 5 — Introduction (documentação oficial)](https://codeception.com/docs/Introduction) — Capítulo 01 Introduction da documentação oficial do Codeception 5 com as três suítes (Unit, Functional, Acceptance), tabela comparativa de sete dimensões e exemplos com AcceptanceTester, FunctionalTester e PHPUnit.; consultado em 2026-10-03.
