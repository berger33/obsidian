---
id: software.testes.tranche11.000500
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-11.md"
fontes: ["https://xunit.net/docs/getting-started/v3/getting-started", "https://api.xunit.net/v3/3.0.0/Xunit.Assert.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# xUnit: escolher Fact ou Theory conforme número de exemplos

## Em uma frase
Fact representa um caso individual; Theory associa a um método conjuntos de dados que produzem invocações parametrizadas.

## Por que importa
xUnit.net cria casos a partir de Facts/Theories e gerencia instâncias e fixtures com regras próprias de escopo e paralelismo; o nome familiar de um atributo não dispensa entender o lifecycle. Uma tabela dentro de Fact pode interromper a execução no primeiro erro e esconder qual entrada falhou no relatório.

## Como funciona
Use test class instance para estado novo por caso, fixtures compartilhadas só quando o custo justificar, dados nomeáveis e determinísticos e coleções para proteger recursos compartilhados. Use Fact para comportamento sem parâmetro e Theory quando valores distintos são exemplos do mesmo contrato.

## Exemplo
A regra de desconto é uma Theory com valores de pedido e desconto esperado; erro identifica argumento do exemplo.

## Limites e trade-offs
Detalhes de fixtures, runner e modos de paralelismo variam entre xUnit v2 e v3 e entre versões do runner. Compartilhar fixture não a torna thread-safe, e ordem do teste não é contrato entre casos. Theory não gera combinações automaticamente nem prova entradas que não foram declaradas ou fornecidas pela fonte.

## Como verificar
Confira a descoberta do runner e confirme que cada conjunto de dados aparece com valores de argumento no relatório.

## Conexões
- [[xunit-inline-data-casos-visíveis]] — Veja também: xUnit: manter InlineData pequeno e representar cada linha no relatório.

## Fontes
- [xUnit.net v3 — Getting Started](https://xunit.net/docs/getting-started/v3/getting-started) — Fact, Theory, dados inline, descoberta e execução de casos; consultado em 2026-10-02.
- [xUnit.net v3 — Assert API (v3.0.0)](https://api.xunit.net/v3/3.0.0/Xunit.Assert.html) — referência da classe Assert, incluindo Throws, ThrowsAsync e outras assertions síncronas/assíncronas; consultado em 2026-10-02.
