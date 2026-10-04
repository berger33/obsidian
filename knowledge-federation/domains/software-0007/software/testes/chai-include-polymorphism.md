---
id: software.testes.tranche21.001489
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-21.md"
fontes: ["https://www.chaijs.com/api/bdd/", "https://github.com/chaijs/chai"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Chai: .include muda conforme o alvo

## Em uma frase
Em string, .include verifica substring; em array, membro presente; em objeto, subconjunto de propriedades; em Set ou WeakSet, membro por SameValueZero; em Map, um dos valores.

## Por que importa
Uma única palavra cobre cinco contratos de continência distintos, e o guia recomenda verificar o tipo antes exatamente por isso.

## Como funciona
Combine an(tipo) com include(val) e use .deep quando a comparação estrutural for necessária em arrays e propriedades de objeto.

## Exemplo
expect({a: 1, b: 2, c: 3}).to.include({a: 1, b: 2}) afirma o subconjunto sem enumerar o resto.

## Limites e trade-offs
.deep.include não suporta alvos WeakSet, e confiar no comportamento sem declarar o tipo faz o teste significar outra coisa quando o payload mudar de forma.

## Como verificar
Altere um payload de array para Map no código produzido e confirme que a asserção include existente passa ou falha de modo inesperado antes do ajuste.

## Conexões
- [[chai-type-a-an]] — Veja também: Chai: verificar tipo antes do resto com .a.

## Fontes
- [Chai — API BDD (expect/should)](https://www.chaijs.com/api/bdd/) — correntes de linguagem, negação, deep, nested, own, ordered, keys, tipos e include; consultado em 2026-10-03.
- [Chai — repositório oficial](https://github.com/chaijs/chai) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
