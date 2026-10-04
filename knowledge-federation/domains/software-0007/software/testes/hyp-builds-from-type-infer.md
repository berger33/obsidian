---
id: software.testes.tranche12.000563
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-12.md"
fontes: ["https://hypothesis.readthedocs.io/en/latest/reference/api.html", "https://hypothesis.readthedocs.io/en/latest/reference/strategies.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Hypothesis: inferir argumentos com `builds()`

## Em uma frase
`builds()` pode criar instâncias de uma classe chamando seu construtor e, quando autorizado, inferindo estratégias a partir de anotações de tipo.

## Por que importa
A inferência reduz boilerplate para objetos simples, porém depende da assinatura que Hypothesis consegue inspecionar e não substitui uma estratégia explícita quando o domínio tem regras próprias.

## Como funciona
Passe a classe ou função alvo a `st.builds`, declare estratégias para parâmetros especiais e use `infer` ou `...` somente nos argumentos cuja anotação descreve a geração desejada.

## Exemplo
Um `Invoice` pode receber valores de `Decimal` e uma lista de itens gerada por estratégias, enquanto um identificador com formato restrito recebe uma estratégia declarada diretamente.

## Limites e trade-offs
`@given` não infere automaticamente todos os argumentos obrigatórios a partir de anotações; confiar nessa suposição pode deixar uma função incompatível com a assinatura do teste.

## Como verificar
Compare os tipos construídos com os limites reais do objeto e execute um caso com cada parâmetro anotado antes de depender da inferência em uma suíte inteira.

## Conexões
- [[hyp-data-draw-dinamico]] — Veja também: Hypothesis: draws dinâmicos com `data()`.
- [[hyp-valid-collections-cardinality]] — Veja também: Hypothesis: gerar coleções válidas sem rejeição excessiva.

## Fontes
- [Hypothesis — API Reference](https://hypothesis.readthedocs.io/en/latest/reference/api.html) — @given, exemplos, inferência, settings, HealthCheck e configuração pública; consultado em 2026-10-02.
- [Hypothesis — Strategies Reference](https://hypothesis.readthedocs.io/en/latest/reference/strategies.html) — estratégias primitivas, compositores, builds, coleções, exemplos e filtros; consultado em 2026-10-02.
