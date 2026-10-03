---
id: software.testes.tranche22.001610
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-22.md"
fontes: ["https://kotest.io/docs/proptest/property-test-functions.html", "https://kotest.io/docs/proptest/property-test-config.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Kotest: propriedades com duas funções, forAll e checkAll

## Em uma frase
O property testing do Kotest se executa por duas funções: forAll recebe uma função n-ária (a, ..., n) -> Boolean que deve ser verdadeira para todos os inputs, e checkAll recebe a mesma aridade devolvendo Unit, onde simplesmente se rodam asserções.

## Por que importa
Em Kotlin, um lambda Boolean por propriedade mantém o teste livre de framework de asserções; o par de funções cobre quem quer devolver verdade e quem quer usar os infixos should do Kotest.

## Como funciona
Os tipos de argumento viram parâmetros de tipo — forAll<String, Int, Boolean> localiza um generator por tipo e sorteia valores adequados, com aridade até 14.

## Exemplo
O exemplo canônico das duas páginas é o mesmo: (a + b).length == a.length + b.length dentro de um FreeSpec, na forma booleana e na forma checkAll com shouldHaveLength.

## Limites e trade-offs
A função Boolean exige disciplina de não lançar: exceção dentro de um forAll vira erro do teste, não falsificação — para cenários que levantam, use checkAll.

## Como verificar
Escreva o mesmo teste nas duas formas e confira que a saída de falha reporta o mesmo par de strings sorteado.

## Conexões
- [[kotest-checkall-assertions]] — Veja também: Kotest: checkAll com asserções infixas.

## Fontes
- [Kotest — Property Test Functions](https://kotest.io/docs/proptest/property-test-functions.html) — forAll, checkAll, iterações e generators; consultado em 2026-10-03.
- [Kotest — Property Test Configuration](https://kotest.io/docs/proptest/property-test-config.html) — PropTestConfig: maxFailure, listeners e saída hex; consultado em 2026-10-03.
