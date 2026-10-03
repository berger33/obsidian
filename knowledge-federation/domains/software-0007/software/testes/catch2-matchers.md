---
id: software.testes.tranche19.001263
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
fontes: ["https://github.com/catchorg/Catch2/blob/devel/docs/matchers.md", "https://github.com/catchorg/Catch2/blob/devel/docs/assertions.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Catch2: usar correspondências expressivas

## Em uma frase
Matchers compõem verificações sobre propriedades de valores, incluindo conteúdo, faixa, comparação aproximada e predicados próprios.

## Por que importa
Correspondências declaram a intenção da verificação e produzem mensagens mais claras do que comparações compostas à mão.

## Como funciona
Prefira matchers para coleções e texto, combine-os para expressar conjunções e declare predicados próprios quando necessário.

## Exemplo
A verificação pode exigir que uma lista contenha exatamente os elementos esperados em qualquer ordem, sem escrever a ordenação manualmente.

## Limites e trade-offs
Matchers encadeados em excesso reduzem a legibilidade, e a mensagem de falha pode omitir o valor concreto que causou o problema.

## Como verificar
Substitua uma comparação composta por matcher equivalente e compare a clareza da mensagem de falha produzida.

## Conexões
- [[catch2-generators]] — Veja também: Catch2: gerar dados de entrada.
- [[catch2-floating-point]] — Veja também: Catch2: comparar números de ponto flutuante.

## Fontes
- [Catch2 — Matchers](https://github.com/catchorg/Catch2/blob/devel/docs/matchers.md) — correspondências para texto, coleções, faixas e predicados; consultado em 2026-10-03.
- [Catch2 — Assertions](https://github.com/catchorg/Catch2/blob/devel/docs/assertions.md) — macros de asserção fatais e não fatais e comparações; consultado em 2026-10-03.
