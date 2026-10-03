---
id: software.testes.tranche22.001646
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-22.md"
fontes: ["https://docs.hoverfly.io/en/latest/index.html", "https://docs.hoverfly.io/en/latest/pages/introduction/gettingstarted.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Hoverfly: o mapa dos Key Concepts

## Em uma frase
A documentação organiza o produto em conceitos nomeados: uso como proxy server e como webserver, modos, simulações, estratégias de matching, caching, templating, estado, destination filtering, middleware, post serve action e a CLI hoverctl — um índice que espelha o vocabulário do produto.

## Por que importa
Ferramenta de simulação com essa superfície só é dominável por índice: templating e matching decidem como respostas casuísticas são devolvidas, e middleware é a costura com código seu.

## Como funciona
O índice de reference da doc lista hoverctl commands, hoverfly commands, request matchers, REST API e simulation schema como as quatro portas de consulta.

## Exemplo
As páginas de proxy server versus webserver separam os dois modos de se expor ao teste — escolher a porta de entrada é a primeira decisão de arquitetura.

## Limites e trade-offs
É um mapa de documentação, não garantia de estabilidade: o sumário é versionado (latest e stable convivem com v1.4.0 e mais antigos).

## Como verificar
Percorra a página Key Concepts e confirme que cada termo que seu pipeline usa hoje tem página própria no índice.

## Conexões
- [[hoverfly-simulate-mode]] — Veja também: Hoverfly: simulate é o replay sem rede.
- [[hoverfly-troubleshooting]] — Veja também: Hoverfly: os problemas que a doc já prevê.

## Fontes
- [Hoverfly — documentação inicial](https://docs.hoverfly.io/en/latest/index.html) — conceitos-chave, reference e troubleshooting do v1.12.15; consultado em 2026-10-03.
- [Hoverfly — Getting Started](https://docs.hoverfly.io/en/latest/pages/introduction/gettingstarted.html) — binários hoverfly/hoverctl, start, logs e stop; consultado em 2026-10-03.
