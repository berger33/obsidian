---
id: software.testes.tranche21.001487
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

# Chai: .any e .all em chaves

## Em uma frase
Para asserções keys, .any exige ao menos uma das chaves listadas e .all exige todas; o comportamento padrão é .all quando a cadeia não escolhe.

## Por que importa
A escolha explícita entre qualquer e todas as chaves é frequentemente o ponto exato do contrato de um payload opcional versus obrigatório.

## Como funciona
Escreva .all mesmo sendo redundante quando a legibilidade ganhar com isso, e reserve .any para contratos de exclusividade ou detecção mínima.

## Exemplo
expect({a: 1, b: 2}).to.not.have.any.keys('c', 'd') proíbe que as chaves vazias apareçam no payload.

## Limites e trade-offs
.any afrouxa silenciosamente um contrato que pretendia ser completo quando alguém adiciona o elo por engano copiando outro teste.

## Como verificar
Duplique uma asserção keys, adicione .any a uma e confirme que casos parcialmente satisfeitos passam apenas na variante frouxa.

## Conexões
- [[chai-ordered-members]] — Veja também: Chai: ordem exigida com .ordered.
- [[chai-type-a-an]] — Veja também: Chai: verificar tipo antes do resto com .a.

## Fontes
- [Chai — API BDD (expect/should)](https://www.chaijs.com/api/bdd/) — correntes de linguagem, negação, deep, nested, own, ordered, keys, tipos e include; consultado em 2026-10-03.
- [Chai — repositório oficial](https://github.com/chaijs/chai) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
