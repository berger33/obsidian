---
id: software.testes.tranche23.001679
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-23.md"
fontes: ["https://github.com/junit-team/junit4/wiki/Parameterized-tests", "https://junit.org/junit4/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Parameterized: o produto cartesiano entre testes e dados

## Em uma frase
O runner customizado Parameterized roda, conforme a página oficial, "instances are created for the cross-product of the test methods and the test data elements": o método estático anotado @Parameters devolve uma Collection de vetores de Object, e cada instância do teste é construída pelo construtor que recebe os valores de uma linha.

## Por que importa
Tabelas de casos são o formato mais denso de especificação para lógica com fronteiras — o exemplo oficial cobre Fibonacci de 0 a 6 numa suíte que, sem o runner, viraria sete métodos idênticos.

## Como funciona
A página documenta três refinamentos: injeção por campo com @Parameter(n) em campos públicos como alternativa ao construtor, desde o 4.12-beta-3 dados de parâmetro único sem wrapper de array, e nomes de caso via @Parameters(name) com placeholders index e posições — aspas simples viram duas aspas para escapar.

## Exemplo
Converta três testes similares em um classe Parameterized com name "{index}: fib(0)={1}" e confirme na saída os nomes gerados no formato [3: fib(3)=2], documentado como exemplo na página.

## Limites e trade-offs
O runner pertence a uma linha em modo manutenção — para novos recursos, a página About remete ao desenvolvimento no repositório junit-framework; além disso, a página registra um bug do Eclipse antigo que truncava nomes com parênteses, lembrando que a visualização IDE do parametrizado tem história própria.

## Como verificar
Abra a página Parameterized tests do wiki do junit4 e confira a frase do cross-product, o @Parameter de campos públicos, o parágrafo de parâmetro único e o exemplo de name com o formato gerado.

## Conexões
- [[junit4-rules-collection]] — Veja também: O kit de regras: ExternalResource, ErrorCollector, Verifier, TestWatcher.

## Fontes
- [JUnit 4 — Parameterized tests (wiki)](https://github.com/junit-team/junit4/wiki/Parameterized-tests) — cross-product, @Parameter, nome de casos e parâmetro único; consultado em 2026-10-03.
- [JUnit 4 — página oficial About](https://junit.org/junit4/) — modo manutenção, exemplo @Test com Hamcrest e índice de referências; consultado em 2026-10-03.
