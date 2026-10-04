---
id: software.testes.tranche22.001599
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
fontes: ["https://www.fluentassertions.com/objectgraphs/", "https://www.fluentassertions.com/introduction"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# FluentAssertions: modelando a equivalência com opções

## Em uma frase
As opções cobrem os cantos do mapeamento real: WithStrictTyping/WithStrictTypingFor/WithoutStrictTyping regulam o rigor de tipo (por path via IObjectInfo), PreferringRuntimeMemberTypes troca o tipo declarado pelo runtime, e Excluding(o => o.Customer.Name) ou Excluding(ctx => ctx.Path == "Level.Level.Text") cortam membros específicos do grafo.

## Por que importa
Testes de equivalência entre camadas vivem de exceções — campos derivados, id técnico, timestamp —; expressar as exceções na opção mantém a asserção como regra e não como colagem de propriedades.

## Como funciona
Desde a v5 a conversão automática entre tipos incompatíveis (string de data casando com DateTime) foi removida de default; reative seletivamente com WithAutoConversionFor(x => x.Path.Contains("Birthdate")).

## Exemplo
ExcludingMembersNamed permite riscar uma propriedade de qualquer nível do grafo só pelo nome, sem lambdas por path.

## Limites e trade-offs
O caso especial de tipo declarado object: como object não expõe propriedades, o nó é comparado pelo tipo runtime mesmo com PreferringDeclaredMemberTypes ativo — arrays multidimensionais dependem desse comportamento.

## Como verificar
Exclua uma propriedade por nome, adicione outra por path lambda e confirme que a mesma suíte passa nos dois modos de exclusão.

## Conexões
- [[fa-value-semantics]] — Veja também: FluentAssertions: por valor ou por membros.

## Fontes
- [FluentAssertions — Object graphs](https://www.fluentassertions.com/objectgraphs/) — BeEquivalentTo, recursão, tipagem, exclusões e auto-conversão; consultado em 2026-10-03.
- [FluentAssertions — Introduction](https://www.fluentassertions.com/introduction) — chaining, frameworks detectados, subject identification e AssertionScope; consultado em 2026-10-03.
