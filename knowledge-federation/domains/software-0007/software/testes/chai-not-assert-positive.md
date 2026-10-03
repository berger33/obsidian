---
id: software.testes.tranche21.001482
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
fontes: ["https://www.chaijs.com/api/bdd/", "https://www.chaijs.com/guide/styles/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Chai: negar com .not é poder, não dever

## Em uma frase
O elo .not nega toda asserção seguinte na cadeia, mas a documentação recomenda afirmar a saída esperada em vez de negar uma entre muitas inesperadas.

## Por que importa
Assertivas negativas deixam o teste sobreviver a saídas erradas não previstas: dois continua passando se a regra for "não é um".

## Como funciona
Compare com .to.equal(2) o valor correto; reserve .not para quando a ausência for exatamente o contrato verificado.

## Exemplo
expect([1, 2]).to.be.an('array').that.does.not.include(3) expressa uma proibição legítima sobre conteúdo.

## Limites e trade-offs
Excesso de .not transforma a suíte em lista de proibições frouxas que qualquer regressão atravessa sem ser notada.

## Como verificar
Inverta uma asserção de igualdade para .not.equal de um valor errado e veja que ela continua passando apesar do bug.

## Conexões
- [[chai-language-chains]] — Veja também: Chai: correntes de linguagem de leitura.
- [[chai-deep-vs-strict]] — Veja também: Chai: igualdade profunda com .deep.

## Fontes
- [Chai — API BDD (expect/should)](https://www.chaijs.com/api/bdd/) — correntes de linguagem, negação, deep, nested, own, ordered, keys, tipos e include; consultado em 2026-10-03.
- [Chai — Guia de estilos](https://www.chaijs.com/guide/styles/) — comparação entre expect, should e assert; consultado em 2026-10-03.
