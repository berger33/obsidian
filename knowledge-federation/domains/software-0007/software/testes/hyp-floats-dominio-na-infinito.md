---
id: software.testes.tranche12.000565
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
fontes: ["https://hypothesis.readthedocs.io/en/latest/reference/strategies.html", "https://hypothesis.readthedocs.io/en/latest/reference/api.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Hypothesis: definir o domínio numérico de floats

## Em uma frase
Estratégias de ponto flutuante podem incluir valores especiais como NaN e infinito, além de valores finitos próximos aos limites declarados.

## Por que importa
Operações com números IEEE têm casos que não seguem a intuição de aritmética decimal, então omitir o domínio pode produzir contraexemplos surpreendentes ou deixar uma falha importante fora do teste.

## Como funciona
Use limites inclusivos ou exclusivos conforme o contrato e configure explicitamente `allow_nan` e `allow_infinity` quando a propriedade exigir somente valores finitos.

## Exemplo
Uma função de cálculo de frete pode testar números finitos não negativos, enquanto um parser deve ter casos separados para representar e rejeitar NaN conforme a especificação.

## Limites e trade-offs
Limitar a geração a floats finitos deixa de cobrir comportamento que uma interface pública talvez aceite. Restringir extremos sem justificativa também altera a propriedade avaliada.

## Como verificar
Inclua casos para zero, limites e valores não finitos quando relevantes; confirme que cada restrição deriva do contrato e não apenas da conveniência do gerador.

## Conexões
- [[hyp-valid-collections-cardinality]] — Veja também: Hypothesis: gerar coleções válidas sem rejeição excessiva.
- [[hyp-example-regressao-explicito]] — Veja também: Hypothesis: adicionar regressões com `@example`.

## Fontes
- [Hypothesis — Strategies Reference](https://hypothesis.readthedocs.io/en/latest/reference/strategies.html) — estratégias primitivas, compositores, builds, coleções, exemplos e filtros; consultado em 2026-10-02.
- [Hypothesis — API Reference](https://hypothesis.readthedocs.io/en/latest/reference/api.html) — @given, exemplos, inferência, settings, HealthCheck e configuração pública; consultado em 2026-10-02.
