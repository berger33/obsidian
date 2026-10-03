---
id: software.testes.tranche22.001592
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

# FluentAssertions: exceção como regra de negócio

## Em uma frase
As asserções de exceção casam com regras de domínio: action.Should().Throw<RuleViolationException>() encadeia WithMessage com curinga e .And para verificar coleções aninhadas, como Violations.Should().Contain(BusinessRule.CannotChangeIngredientQuantity).

## Por que importa
Testar regra de negócio por exceção exige afirmar tipo, mensagem e payload; encadear os três em uma expressão elimina os blocos try/catch verbosos de Assert tradicionais.

## Como funciona
Envolva a chamada proibida num lambda atribuído a action e afirme tipo, mensagem e conteúdo do objeto lançado na mesma corrente.

## Exemplo
recipe.AddIngredient("Milk", 100, Unit.Spoon) lança RuleViolationException e o teste confirma a mensagem com padrão "*change the unit of an existing ingredient*".

## Limites e trade-offs
A comparação de mensagem entre curingas é sensível a rewording da exceção em produção; mensagens longas acopladas ao teste viram frágil de quebrar em refactors.

## Como verificar
Altere o texto da exceção no código de produção e veja exatamente qual dos três elos da corrente quebra primeiro.

## Conexões
- [[fa-collections-predicate]] — Veja também: FluentAssertions: coleções com predicado e because.
- [[fa-which-chaining]] — Veja também: FluentAssertions: Which entra no grafo de objetos.

## Fontes
- [FluentAssertions — Introduction](https://www.fluentassertions.com/introduction) — chaining, frameworks detectados, subject identification e AssertionScope; consultado em 2026-10-03.
- [FluentAssertions — Object graphs](https://www.fluentassertions.com/objectgraphs/) — BeEquivalentTo, recursão, tipagem, exclusões e auto-conversão; consultado em 2026-10-03.
