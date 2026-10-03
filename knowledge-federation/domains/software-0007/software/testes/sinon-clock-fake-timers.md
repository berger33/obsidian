---
id: software.testes.tranche21.001496
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

# Sinon: relógio falso para aguardar sem espera

## Em uma frase
sinon.useFakeTimers congela o relógio do ambiente de teste e avança no ritmo escolhido, disparando timeouts e intervalos sob comando.

## Por que importa
Esperar dez segundos reais num teste de reintentos desperdiça a esteira e adiciona instabilidade; o relógio falso apaga a parede do tempo.

## Como funciona
Instale o relógio antes do código sob teste, execute o fluxo agendado e avance com clock.tick até a próxima janela de disparo.

## Exemplo
Um backoff exponencial pode ser atravessado em três ticks, verificando atrasos de um, dois e quatro segundos sem dormir nada.

## Limites e trade-offs
Relógios falsos não cobrem bibliotecas que capturaram setTimeout em referência no import; o momento da instalação importa demais.

## Como verificar
Avance o relógio artificialmente e confirme que o callback agendado executou exatamente uma vez por período configurado.

## Conexões
- [[sinon-mock-expectations]] — Veja também: Sinon: mocks com expectativas verificadas.
- [[sinon-fake-server-xhr]] — Veja também: Sinon: servidor falso para requisições XHR.

## Fontes
- [Sinon.JS — repositório oficial](https://github.com/sinonjs/sinon) — código-fonte, guias de API e releases do projeto; consultado em 2026-10-03.
- [Sinon.JS — página oficial](https://sinonjs.org/) — instalação, escopo e início rápido; consultado em 2026-10-03.
- [Sinon.JS — releases publicadas](https://github.com/sinonjs/sinon/releases) — notas de versão e mudanças da API; consultado em 2026-10-03.
