---
id: software.testes.tranche22.001596
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

# FluentAssertions: o nome da variável no erro

## Em uma frase
Para imprimir "Expected username to be "jonas" ... but "dennis" has a length of 6", a biblioteca percorre a stack trace, acha arquivo, linha e coluna da chamada e extrai do código-fonte o nome do sujeito — exige debug symbols e build em modo debug, até no build server.

## Por que importa
Erro que cita a variável do teste encurta a depuração em suítes paramétrizadas onde a mesma asserção roda cem vezes; o preço vem embutido na exigência de PDBs.

## Como funciona
Se você embutir asserts em helpers próprios, anote o método com [CustomAssertion] para o rastreio pular a sua extensão e achar a chamada do teste (myClient, não customer).

## Exemplo
Para marcar um assembly inteiro de asserções customizadas, use [assembly: CustomAssertionsAssembly] num arquivo do projeto, sem anotar método a método.

## Limites e trade-offs
A leitura do arquivo fonte não funciona com PathMap nos test projects, porque a biblioteca confia no caminho devolvido por StackFrame.GetFileName(); builds com path remapado perdem o nome do sujeito.

## Como verificar
Compile em Release sem debug symbols, quebre uma asserção e compare a mensagem com a versão Debug para ver o nome do sujeito desaparecer.

## Conexões
- [[fa-framework-detection]] — Veja também: FluentAssertions: detecta o framework de teste por baixo.
- [[fa-beequivalent-to]] — Veja também: FluentAssertions: BeEquivalentTo entre DTOs.

## Fontes
- [FluentAssertions — Introduction](https://www.fluentassertions.com/introduction) — chaining, frameworks detectados, subject identification e AssertionScope; consultado em 2026-10-03.
- [FluentAssertions — Object graphs](https://www.fluentassertions.com/objectgraphs/) — BeEquivalentTo, recursão, tipagem, exclusões e auto-conversão; consultado em 2026-10-03.
