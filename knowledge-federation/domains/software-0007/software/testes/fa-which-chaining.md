---
id: software.testes.tranche22.001593
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

# FluentAssertions: Which entra no grafo de objetos

## Em uma frase
Sobre coleções e grafos, o Which sobe um nível: dictionary.Should().ContainValue(myClass).Which.SomeProperty.Should().BeGreaterThan(0) afirma dentro do membro encontrado, e o encadeamento continua a corrente.

## Por que importa
Asserts que "acham e depois verificam" viravam três asserts imperativos com cast manual; Which transforma a navegação em parte da expressão.

## Como funciona
Combine HaveElement, BeOfType e And para descer em documentos e object graphs: xDocument.Should().HaveElement("child").Which.Should().BeOfType<XElement>().And.HaveAttribute("attr", "1").

## Exemplo
Quando a primeira asserção falha, a mensagem já localiza o caminho: "Expected dictionary["key"].SomeProperty to be greater than 0, but found -2".

## Limites e trade-offs
Correntes Which longas confundem o leitor sobre qual elo falhou se você encadear dezenas de níveis; pare o encadeamento onde a leitura pedir comentário.

## Como verificar
Quebre um nó do meio de uma corrente de três níveis e leia a mensagem para conferir se o caminho relatado bate com o elo errado.

## Conexões
- [[fa-exceptions-business-rules]] — Veja também: FluentAssertions: exceção como regra de negócio.
- [[fa-assertion-scope]] — Veja também: FluentAssertions: AssertionScope acumula falhas.

## Fontes
- [FluentAssertions — Introduction](https://www.fluentassertions.com/introduction) — chaining, frameworks detectados, subject identification e AssertionScope; consultado em 2026-10-03.
- [FluentAssertions — Object graphs](https://www.fluentassertions.com/objectgraphs/) — BeEquivalentTo, recursão, tipagem, exclusões e auto-conversão; consultado em 2026-10-03.
