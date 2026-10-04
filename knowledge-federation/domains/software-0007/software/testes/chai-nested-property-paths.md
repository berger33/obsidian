---
id: software.testes.tranche21.001484
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

# Chai: caminhos aninhados com .nested

## Em uma frase
Com .nested antes de property ou include, o Chai entende notação de ponto e colchetes no nome da chave, como 'a.b[1]', e permite escapar ponto e colchete literais com barras invertidas duplas.

## Por que importa
Objetos de resposta de API são naturalmente aninhados, e verificar um caminho profundo não deveria exigir descer o objeto na mão antes do expect.

## Como funciona
Aponte o caminho completo dentro de uma única asserção para ler e falhar o teste pelo endereço do dado.

## Exemplo
expect(dados).to.have.nested.property('a.b[1]', 'y') cobre um array interno sem temporários no teste.

## Limites e trade-offs
.nested não convive com .own na mesma cadeia, e nomes reais que contenham ponto exigem o mecanismo de escape, fácil de esquecer.

## Como verificar
Introduza um ponto no nome de uma chave e confirme que a asserção quebra sem escape e volta a passar com ele.

## Conexões
- [[chai-deep-vs-strict]] — Veja também: Chai: igualdade profunda com .deep.
- [[chai-own-versus-inherited]] — Veja também: Chai: .own ignora propriedades herdadas.

## Fontes
- [Chai — API BDD (expect/should)](https://www.chaijs.com/api/bdd/) — correntes de linguagem, negação, deep, nested, own, ordered, keys, tipos e include; consultado em 2026-10-03.
- [Chai — repositório oficial](https://github.com/chaijs/chai) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
