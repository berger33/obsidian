---
id: software.testes.tranche25.001950
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

# Codeception: um único framework PHP para as suítes Unit, Functional e Acceptance

## Em uma frase
A página oficial Introduction da documentação do Codeception 5 explica que, para aplicações web, testar apenas controller ou model não prova que a aplicação funciona como um todo, e que uma das principais vantagens do Codeception é não obrigar a equipe a escolher apenas um tipo de teste: ele organiza o projeto em três suítes — Unit suite (`Unit.suite.yml`), Functional suite (`Functional.suite.yml`) e Acceptance suite (`Acceptance.suite.yml`) — escritas num estilo descritivo e coerente sobre o PHPUnit.

## Por que importa
Em muitos projetos PHP, testes unitários, testes de requisição em memória e testes de navegador usam ferramentas, sintaxes e executores diferentes; reunir as três camadas sob a mesma arquitetura de suítes e atores reduz a curva de aprendizado e padroniza relatórios e execução no CI.

## Como funciona
Inicialize o Codeception no projeto para gerar a pasta `/tests` com os três diretórios (`Unit`, `Functional`, `Acceptance`) e seus respectivos arquivos `.suite.yml`, alocando cada cenário na suíte cujo custo e escopo façam sentido.

## Exemplo
Um fluxo crítico de cadastro pode ter um teste de aceitação no navegador (`AcceptanceTester`), um teste funcional rápido que inspeciona e-mail e banco (`FunctionalTester`) e testes unitários de domínio (`testSavingUser`) dentro do mesmo repositório de testes.

## Limites e trade-offs
A própria introdução ressalta que na maioria dos casos testes não garantem 100% de ausência de falhas diante de todos os cenários imprevisíveis, mas cobrem as partes mais importantes da aplicação para dar confiança a cada commit.

## Como verificar
Conferi a página oficial codeception.com/docs/Introduction e o início de codeception.com/docs/GettingStarted.

## Conexões
- [[codeception-comparison-table-seven-dimensions]] — Veja também: A tabela oficial de sete dimensões entre Unit, Functional e Acceptance Tests.

## Fontes
- [Codeception 5 — Introduction (documentação oficial)](https://codeception.com/docs/Introduction) — Capítulo 01 Introduction da documentação oficial do Codeception 5 com as três suítes (Unit, Functional, Acceptance), tabela comparativa de sete dimensões e exemplos com AcceptanceTester, FunctionalTester e PHPUnit.; consultado em 2026-10-03.
- [Codeception 5 — Getting Started (documentação oficial)](https://codeception.com/docs/GettingStarted) — Capítulo 02 Getting Started da documentação oficial do Codeception 5 com regras de sintaxe (Actions, Assertions see/dontSee, Grabbers), Actors e Modules (PhpBrowser, codecept build), formato Cest, codecept run --steps e BDD.; consultado em 2026-10-03.
