---
id: software.testes.tranche21.001548
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
fontes: ["https://github.com/Shopify/toxiproxy", "https://github.com/Shopify/toxiproxy/tree/main/client"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Toxiproxy: a API HTTP de controle

## Em uma frase
Toda manipulação passa pela interface JSON na porta 8474: listar e criar proxies, popular lotes, ler e atualizar proxies e toxics por rota própria, além da listagem de endpoints no README.

## Por que importa
Uma API explícita e pequena é o que permite a qualquer linguagem escrever um cliente; não há protocolo binário nem sessão a manter.

## Como funciona
Escreva a automação do teste sobre GET/POST /proxies, /populate para lotes e as rotas de toxics por proxy, ou use o CLI que fala o mesmo dialeto.

## Exemplo
toxiproxy-cli toxic add -t latency -a latency=1000 nome traduz a chamada POST em um argumento de linha de comando.

## Limites e trade-offs
Subir o servidor sem nada no estado não expõe proxies: o populate ou os creates são o que cria a topologia da qual o teste depende.

## Como verificar
Liste os proxies via HTTP e confirme o reflexo de uma criação feita pelo CLI.

## Conexões
- [[toxiproxy-toxic-fields-direction]] — Veja também: Toxiproxy: stream, toxicidade e o down que não é toxic.
- [[toxiproxy-clients-ecosystem]] — Veja também: Toxiproxy: clientes por linguagem e CLI.

## Fontes
- [Toxiproxy — README oficial](https://github.com/Shopify/toxiproxy) — proposta, instalação, populate, toxics e HTTP API; consultado em 2026-10-03.
- [Toxiproxy — cliente Go](https://github.com/Shopify/toxiproxy/tree/main/client) — cliente oficial embutido no repositório; consultado em 2026-10-03.
