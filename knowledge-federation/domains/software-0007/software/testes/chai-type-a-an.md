---
id: software.testes.tranche21.001488
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
fontes: ["https://www.chaijs.com/api/bdd/", "https://github.com/chaijs/type-detect"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Chai: verificar tipo antes do resto com .a

## Em uma frase
A asserção .a (ou .an) compara o tipo detectado com a string informada, é insensível a maiúsculas e respeita o Symbol.toStringTag de objetos customizados.

## Por que importa
Várias asserções mudam de significado conforme o tipo do alvo; fixar o tipo primeiro evita que uma asserção faça "outra coisa do que se imagina".

## Como funciona
Encadeie expect(valor).to.be.an('array') antes de include, e confirme tipos como null, undefined, error, promise, float32array e symbol.

## Exemplo
expect([1, 2, 3]).to.be.an('array').that.includes(2) deixa explícito que o include se refere a membro de array.

## Limites e trade-offs
Tipos definidos por Symbol.toStringTag enganam quem assume typeof puro; a própria documentação orienta checar antes de prosseguir.

## Como verificar
Passe um Set para uma asserção que exige array e confirme que a checagem de tipo falha com mensagem antes do teste inteiro.

## Conexões
- [[chai-any-all-keys]] — Veja também: Chai: .any e .all em chaves.
- [[chai-include-polymorphism]] — Veja também: Chai: .include muda conforme o alvo.

## Fontes
- [Chai — API BDD (expect/should)](https://www.chaijs.com/api/bdd/) — correntes de linguagem, negação, deep, nested, own, ordered, keys, tipos e include; consultado em 2026-10-03.
- [Chai type-detect — projeto](https://github.com/chaijs/type-detect) — algoritmo de detecção de tipos citado pela API; consultado em 2026-10-03.
