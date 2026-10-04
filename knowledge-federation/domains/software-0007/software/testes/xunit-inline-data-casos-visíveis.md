---
id: software.testes.tranche11.000501
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

# xUnit: manter InlineData pequeno e representar cada linha no relatório

## Em uma frase
InlineData fornece argumentos constantes para Theory e cada linha representa um caso executável.

## Por que importa
Dados embutidos ajudam casos simples, mas expressões complexas e objetos mutáveis em atributos dificultam revisão e diagnóstico.

## Como funciona
Declare entradas legíveis e independentes em InlineData e extraia conjunto extenso para MemberData ou ClassData.

## Exemplo
Theory usa valores 3, 5 e 6; relatório identifica que somente o caso com 6 falha no predicate.

## Limites e trade-offs
InlineData precisa respeitar tipos aceitos pelo atributo e não é adequado a recursos preparados assincronamente.

## Como verificar
Verifique contagem de cases, nome/argumentos no report e execução isolada de uma linha que falha.

## Conexões
- [[xunit-fact-vs-theory-escopo]] — Veja também: xUnit: escolher Fact ou Theory conforme número de exemplos.
- [[xunit-memberdata-classdata-provedor-tipado]] — Veja também: xUnit: mover dados reutilizáveis para MemberData ou ClassData.

## Fontes
- [xUnit.net v3 — Getting Started](https://xunit.net/docs/getting-started/v3/getting-started) — Fact, Theory, dados inline, descoberta e execução de casos; consultado em 2026-10-02.
- [xUnit.net v3 — Assert API (v3.0.0)](https://api.xunit.net/v3/3.0.0/Xunit.Assert.html) — referência da classe Assert, incluindo Throws, ThrowsAsync e outras assertions síncronas/assíncronas; consultado em 2026-10-02.
