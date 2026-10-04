---
id: software.testes.tranche22.001591
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

# FluentAssertions: coleções com predicado e because

## Em uma frase
Para coleções, o estilo expressa regra em predicado: numbers.Should().OnlyContain(n => n > 0) afirma que todo elemento satisfaz, e HaveCount aceita um texto "because" que vai direto para a mensagem de erro.

## Por que importa
Asserts de contagem sem contexto viram arqueologia seis meses depois; o because embutido documenta a premissa do caso dentro do relatório de falha.

## Como funciona
Passe a justificativa como argumento formatado e o nome da variável real aparece na saída — a página destaca que a mensagem usa o nome numbers.

## Exemplo
Com IEnumerable<int> numbers = new[] { 1, 2, 3 }, HaveCount(4, "because we thought we put four items in the collection") falha citando os 4 esperados contra os 3 achados.

## Limites e trade-offs
O texto because é decorativo: não afeta o resultado booleano da asserção, então escrever justificativas erradas engana mais que omiti-las.

## Como verificar
Quebre a premissa do exemplo (adicione um elemento negativo) e confira o que OnlyContain reporta como elemento culpado.

## Conexões
- [[fa-what-it-is]] — Veja também: FluentAssertions: asserções como frases em C#.
- [[fa-exceptions-business-rules]] — Veja também: FluentAssertions: exceção como regra de negócio.

## Fontes
- [FluentAssertions — Introduction](https://www.fluentassertions.com/introduction) — chaining, frameworks detectados, subject identification e AssertionScope; consultado em 2026-10-03.
- [FluentAssertions — Object graphs](https://www.fluentassertions.com/objectgraphs/) — BeEquivalentTo, recursão, tipagem, exclusões e auto-conversão; consultado em 2026-10-03.
