---
id: software.testes.tranche22.001590
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
fontes: ["https://www.fluentassertions.com/introduction", "https://www.fluentassertions.com/objectgraphs/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# FluentAssertions: asserções como frases em C#

## Em uma frase
O FluentAssertions é um conjunto de métodos de extensão .NET que deixa especificar o resultado esperado de um teste TDD ou BDD de forma natural, começando sempre pelo using FluentAssertions que injeta as extensões no escopo.

## Por que importa
Testes falham para gente ler; trocar Assert.AreEqual por uma frase legível encarece a mentira no código e barateia o diagnóstico no log do CI.

## Como funciona
Chame .Should() no sujeito e encadeie verbos de expectativa; o próprio site abre com actual.Should().StartWith("AB").And.EndWith("HI").And.Contain("EF").And.HaveLength(9).

## Exemplo
A mensagem de uma quebra é autoexplicativa: "Expected numbers to contain 4 item(s) because we thought we put four items in the collection, but found 3."

## Limites e trade-offs
É uma biblioteca de asserções, não um framework de teste: precisa de um executor por baixo e detecta qual automaticamente (ver nota própria).

## Como verificar
Monte um teste mínimo em NUnit ou xUnit só com Should() e veja a exceção específica do framework aparecer sem nenhuma configuração.

## Conexões
- [[fa-collections-predicate]] — Veja também: FluentAssertions: coleções com predicado e because.

## Fontes
- [FluentAssertions — Introduction](https://www.fluentassertions.com/introduction) — chaining, frameworks detectados, subject identification e AssertionScope; consultado em 2026-10-03.
- [FluentAssertions — Object graphs](https://www.fluentassertions.com/objectgraphs/) — BeEquivalentTo, recursão, tipagem, exclusões e auto-conversão; consultado em 2026-10-03.
