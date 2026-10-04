---
id: software.testes.tranche19.001264
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-19.md"
fontes: ["https://github.com/catchorg/Catch2/blob/devel/docs/assertions.md", "https://github.com/catchorg/Catch2/blob/devel/docs/matchers.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Catch2: comparar números de ponto flutuante

## Em uma frase
O framework fornece comparação com tolerância relativa ou absoluta para valores de ponto flutuante e classes aproximadas.

## Por que importa
Comparar igualdade exata em ponto flutuante gera falhas espúrias causadas apenas por arredondamento na representação.

## Como funciona
Declare a margem adequada ao domínio do cálculo e prefira tolerância relativa quando a magnitude varia.

## Exemplo
O resultado de um cálculo de juros pode ser comparado com margem relativa a partir do valor esperado.

## Limites e trade-offs
Margens generosas escondem erros reais de cálculo, e margens apertadas demais reintroduzem a instabilidade que a comparação deveria evitar.

## Como verificar
Ajuste uma margem para o limite e confirme que uma diferença pouco maior passa a ser detectada.

## Conexões
- [[catch2-matchers]] — Veja também: Catch2: usar correspondências expressivas.
- [[catch2-reporters]] — Veja também: Catch2: escolher e combinar relatórios.

## Fontes
- [Catch2 — Assertions](https://github.com/catchorg/Catch2/blob/devel/docs/assertions.md) — macros de asserção fatais e não fatais e comparações; consultado em 2026-10-03.
- [Catch2 — Matchers](https://github.com/catchorg/Catch2/blob/devel/docs/matchers.md) — correspondências para texto, coleções, faixas e predicados; consultado em 2026-10-03.
