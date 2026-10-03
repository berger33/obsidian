---
id: software.testes.tranche21.001499
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

# Sinon: asserções próprias, sem refém do framework

## Em uma frase
Além das propriedades booleanas dos dublês, o Sinon expõe um conjunto sinon.assert com falhas descritivas que funcionam com qualquer executor.

## Por que importa
Testes em AVA, mocha ou tap ganham mensagens de erro igualmente boas sobre chamadas esperadas sem o time padronizar asserções de interação.

## Como funciona
Prefira sinon.assert.calledWith(spy, args) quando quiser o relatório no vocabulário do Sinon, ou use spy.calledWith dentro da asserção nativa.

## Exemplo
A falha de calledWith mostra a lista completa de chamadas reais recebidas, não apenas um esperado/obtido seco.

## Limites e trade-offs
Assertivas de Sinon cobrem o diálogo com o dublê, não o resultado do sistema: usá-las como teste principal afina demais o acoplamento à implementação.

## Como verificar
Quebre o argumento esperado de um assert chamado e confirme que a mensagem lista as chamadas efetivamente registradas.

## Conexões
- [[sinon-sandbox-restore]] — Veja também: Sinon: sandbox para devolver os originais.

## Fontes
- [Sinon.JS — página oficial](https://sinonjs.org/) — instalação, escopo e início rápido; consultado em 2026-10-03.
- [Sinon.JS — repositório oficial](https://github.com/sinonjs/sinon) — código-fonte, guias de API e releases do projeto; consultado em 2026-10-03.
- [Sinon.JS — releases publicadas](https://github.com/sinonjs/sinon/releases) — notas de versão e mudanças da API; consultado em 2026-10-03.
