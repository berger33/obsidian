---
id: software.testes.tranche21.001549
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
fontes: ["https://github.com/Shopify/toxiproxy", "https://github.com/Shopify/toxiproxy-ruby"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Toxiproxy: clientes por linguagem e CLI

## Em uma frase
O projeto mantém cliente Go no repositório e a comunidade atende Ruby, Python, .NET, PHP, Node, Java, Haskell, Rust e Elixir, todos falando com o mesmo daemon.

## Por que importa
Um serviço central de perturbação com clientes finos por linguagem permite que times heterogêneos dividam a mesma topologia em Toxiproxy sem compartilhar código de teste.

## Como funciona
Adote o cliente oficial da sua stack e confirme que ele implementa populate, toxics e o bloco de aplicação temporária dos efeitos.

## Exemplo
O Ruby tem o padrão Toxiproxy[/redis/].down do bloco que derruba só durante o teste — as demais bibliotecas reproduzem o gesto com a própria sintaxe.

## Limites e trade-offs
O suporte por cliente não é uniforme: nem todos expõem cada toxic ou a API de atualização, e o README lista os repositórios para checar antes.

## Como verificar
Rode o exemplo de exemplo do README pelo cliente da sua linguagem e confirme paridade nos efeitos observados.

## Conexões
- [[toxiproxy-http-api-endpoints]] — Veja também: Toxiproxy: a API HTTP de controle.

## Fontes
- [Toxiproxy — README oficial](https://github.com/Shopify/toxiproxy) — proposta, instalação, populate, toxics e HTTP API; consultado em 2026-10-03.
- [Toxiproxy — cliente Ruby](https://github.com/Shopify/toxiproxy-ruby) — exemplos de populate, down e apply; consultado em 2026-10-03.
