---
id: software.testes.tranche12.000562
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
fontes: ["https://hypothesis.readthedocs.io/en/latest/reference/strategies.html#hypothesis.strategies.data", "https://hypothesis.readthedocs.io/en/latest/reference/strategies.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Hypothesis: draws dinâmicos com `data()`

## Em uma frase
`st.data()` fornece ao teste uma interface para sortear valores adicionais durante a execução a partir de estratégias escolhidas pelo próprio caso gerado.

## Por que importa
Draw dinâmico é útil quando a quantidade ou o tipo dos próximos dados depende de um valor que o teste já recebeu, situação difícil de descrever com argumentos independentes.

## Como funciona
Passe uma estratégia `data()` ao teste e chame `draw()` dentro dele para obter valores; mantenha explícita a dependência entre cada decisão e o dado que ela habilita.

## Exemplo
Um teste pode gerar uma lista de opções e, a seguir, sortear um índice dentro dos limites daquela lista para validar a seleção em um componente.

## Limites e trade-offs
Se o teste chama `draw()` em muitos ramos opcionais, a propriedade pode ficar difícil de ler e a distribuição efetiva deixar áreas importantes sem exploração.

## Como verificar
Revise a sequência de sorteios como um cenário documentável e adicione um caso explícito para cada ramo cuja ausência alteraria a interpretação da propriedade.

## Conexões
- [[hyp-composite-dependent-strategies]] — Veja também: Hypothesis: estratégias próprias com `@composite`.
- [[hyp-builds-from-type-infer]] — Veja também: Hypothesis: inferir argumentos com `builds()`.

## Fontes
- [Hypothesis — strategies.data()](https://hypothesis.readthedocs.io/en/latest/reference/strategies.html#hypothesis.strategies.data) — draws dinâmicos e acesso a dados gerados durante a execução de um teste; consultado em 2026-10-02.
- [Hypothesis — Strategies Reference](https://hypothesis.readthedocs.io/en/latest/reference/strategies.html) — estratégias primitivas, compositores, builds, coleções, exemplos e filtros; consultado em 2026-10-02.
