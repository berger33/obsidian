---
id: software.testes.tranche22.001594
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

# FluentAssertions: AssertionScope acumula falhas

## Em uma frase
Um AssertionScope batcha várias asserções num bloco using: em vez de parar na primeira quebra, ele acumula e lança uma única exceção no dispose reunindo todos os erros do escopo.

## Por que importa
Em testes de mapeamento DTO com vinte campos, descobrir um erro por execução é tortura; o escopo dá as vinte divergências de uma vez.

## Como funciona
Envolva as asserções em using (new AssertionScope()) { ... } e as mensagens aparecem empilhadas no dispose, como "Expected value to be 10, but found 5 (difference of -5)." seguido da divergência de string.

## Exemplo
Escopos nomeados aninham e compõem o prefixo da falha: using var outerScope = new AssertionScope("Test1"); using var innerScope = new AssertionScope("Test2"); produz "Expected Test1/Test2/nonEmptyList to be empty, but found at least one item {1}."

## Limites e trade-offs
Se você esquecer o using/dispose (por exemplo em escopo estático), o comportamento de acumulação muda silenciosamente para fora do lugar esperado; o bloco é o contrato.

## Como verificar
Duplique duas asserções conflitantes dentro de um mesmo escopo e confirme que nenhuma exceção sai até o fim do using.

## Conexões
- [[fa-which-chaining]] — Veja também: FluentAssertions: Which entra no grafo de objetos.
- [[fa-framework-detection]] — Veja também: FluentAssertions: detecta o framework de teste por baixo.

## Fontes
- [FluentAssertions — Introduction](https://www.fluentassertions.com/introduction) — chaining, frameworks detectados, subject identification e AssertionScope; consultado em 2026-10-03.
- [FluentAssertions — Object graphs](https://www.fluentassertions.com/objectgraphs/) — BeEquivalentTo, recursão, tipagem, exclusões e auto-conversão; consultado em 2026-10-03.
