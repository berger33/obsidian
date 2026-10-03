---
id: software.testes.tranche21.001544
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

# Toxiproxy: conexões que apodrecem com timeout e reset_peer

## Em uma frase
O toxic timeout bloqueia todo o tráfego e fecha a conexão após timeout milissegundos, ou mantém a queda indefinida com zero; o reset_peer simula TCP RESET imediato ou após o prazo dado.

## Por que importa
Há diferença clínica entre o socket que congela e o que devolve erro de reset, e só o segundo dispara certo tipo de erro de conexão nos clientes.

## Como funciona
Use timeout=0 para hang do link sem erro no cliente e reset_peer para testar o tratamento de Connection reset by peer.

## Exemplo
Um pool de conexão que não reage ao RESET fica exposto pelo reset_peer em milissegundos, não por horas de pipeline entupido.

## Limites e trade-offs
timeout com valor alto ocupa o worker de teste pelo prazo inteiro; reset_peer pode contornar o retry e chegar ao teste como sucesso de reconexão — leia qual exceção o seu cliente produz.

## Como verificar
Estabeleça o reset_peer com timeout pequeno e confirme o erro de conexão esperado no log do teste.

## Conexões
- [[toxiproxy-latency-bandwidth]] — Veja também: Toxiproxy: latência e banda pelos toxic latency e bandwidth.
- [[toxiproxy-slicer-limit-data]] — Veja também: Toxiproxy: pacotes miúdos e conexões cortadas por tamanho.

## Fontes
- [Toxiproxy — README oficial](https://github.com/Shopify/toxiproxy) — proposta, instalação, populate, toxics e HTTP API; consultado em 2026-10-03.
- [Toxiproxy — cliente Ruby](https://github.com/Shopify/toxiproxy-ruby) — exemplos de populate, down e apply; consultado em 2026-10-03.
