---
id: software.testes.tranche21.001490
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
fontes: ["https://sinonjs.org/", "https://github.com/sinonjs/sinon", "https://github.com/sinonjs/sinon/releases"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Sinon: dublês para qualquer framework

## Em uma frase
O Sinon é uma biblioteca de stubbing, spying e mocking para testes em JavaScript que funciona com qualquer framework de teste unitário.

## Por que importa
Separar os dublês do executor de testes permite padronizar spies e stubs em projetos que usam AVA, mocha, Jest ou fitas diferentes sem trocar o vocabulário.

## Como funciona
Instale com npm install sinon, importe a biblioteca e construa espiões, stubs ou mocks em torno do objeto sob teste dentro de qualquer caso.

## Exemplo
Um teste com tap cria sinon.spy(myAPI, "doSomething"), aciona o método e afirma que o espião foi chamado uma vez.

## Limites e trade-offs
Poder total de dublês convida a testar interações em vez de comportamento; o próprio guia limita o Sinon ao lado que precisa de observação.

## Como verificar
Crie um espião em um método qualquer e confirme que a chamada original continua produzindo o efeito antigo.

## Conexões
- [[sinon-spy-observation]] — Veja também: Sinon: observar chamadas com spies.

## Fontes
- [Sinon.JS — página oficial](https://sinonjs.org/) — instalação, escopo e início rápido; consultado em 2026-10-03.
- [Sinon.JS — repositório oficial](https://github.com/sinonjs/sinon) — código-fonte, guias de API e releases do projeto; consultado em 2026-10-03.
- [Sinon.JS — releases publicadas](https://github.com/sinonjs/sinon/releases) — notas de versão e mudanças da API; consultado em 2026-10-03.
