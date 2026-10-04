---
id: software.testes.tranche21.001494
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
fontes: ["https://github.com/sinonjs/sinon", "https://sinonjs.org/", "https://github.com/sinonjs/sinon/releases"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Sinon: um stub, vários comportamentos

## Em uma frase
Com .withArgs, um mesmo stub responde diferente conforme os argumentos recebidos, e variantes como .onCall variam a resposta por ordem de chamada.

## Por que importa
Um dublê de uma única resposta obriga o teste a montar vários objetos paralelos; a resposta por argumento mantém a cena coesa.

## Como funciona
Encadeie com withArgs(args).returns(valor) para cada situação esperada e defina um comportamento padrão para o resto das chamadas.

## Exemplo
O mesmo stub de lerConfiguracao devolve o arquivo válido para um caminho e lança para o caminho inexistente que o teste quer provocar.

## Limites e trade-offs
Listas longas de withArgs escondem a intenção e ficam frágeis a mudanças triviais de assinatura; às vezes dois objetos dublês explicam mais.

## Como verificar
Chame o stub com dois conjuntos de argumentos e confirme respostas distintas vindas de um mesmo dublê.

## Conexões
- [[sinon-stub-on-existing-method]] — Veja também: Sinon: aplicar stub a um método real.
- [[sinon-mock-expectations]] — Veja também: Sinon: mocks com expectativas verificadas.

## Fontes
- [Sinon.JS — repositório oficial](https://github.com/sinonjs/sinon) — código-fonte, guias de API e releases do projeto; consultado em 2026-10-03.
- [Sinon.JS — página oficial](https://sinonjs.org/) — instalação, escopo e início rápido; consultado em 2026-10-03.
- [Sinon.JS — releases publicadas](https://github.com/sinonjs/sinon/releases) — notas de versão e mudanças da API; consultado em 2026-10-03.
