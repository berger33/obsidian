---
id: software.testes.tranche21.001486
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

# Chai: ordem exigida com .ordered

## Em uma frase
O elo .ordered faz asserções members exigirem a mesma sequência dos elementos, e combinado com include a verificação começa alinhada ao início dos dois arrays.

## Por que importa
Conjuntos esperados com semântica de lista (passos de workflow, resultados paginados) perdem todo o sentido se o teste aceitar qualquer ordenação.

## Como funciona
Use have.members para indiferença deliberada de ordem e have.ordered.members quando a posição for parte do contrato.

## Exemplo
expect([1, 2]).to.have.ordered.members([1, 2]) passa, e a mesma asserção com [2, 1] esperado falha por definição documentada.

## Limites e trade-offs
Incluir ordenação onde o contrato não a garante acopla o teste a um detalhe de implementação que varia entre versões da lib consultada.

## Como verificar
Troque a ordem de um resultado paginado estável e confirme que o teste ordenado falha enquanto o simples continua passando.

## Conexões
- [[chai-own-versus-inherited]] — Veja também: Chai: .own ignora propriedades herdadas.
- [[chai-any-all-keys]] — Veja também: Chai: .any e .all em chaves.

## Fontes
- [Chai — API BDD (expect/should)](https://www.chaijs.com/api/bdd/) — correntes de linguagem, negação, deep, nested, own, ordered, keys, tipos e include; consultado em 2026-10-03.
- [Chai — repositório oficial](https://github.com/chaijs/chai) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
