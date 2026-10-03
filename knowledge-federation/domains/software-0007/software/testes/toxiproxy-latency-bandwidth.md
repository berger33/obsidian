---
id: software.testes.tranche21.001543
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

# Toxiproxy: latência e banda pelos toxic latency e bandwidth

## Em uma frase
O toxic latency adiciona atraso igual a latency com variação jitter em milissegundos, e bandwidth limita a conexão a um máximo de KB por segundo.

## Por que importa
Retardo e estreitamento são as duas condições de rede mais frequentes em incidentes reais, e ambas devem mudar o tempo do teste, não o seu resultado — quando o cliente respeita os prazos.

## Como funciona
Aplique latency a uma chamada de leitura no Redis do teste e confirme que o gasto mínimo coincide com o valor configurado, ou corte a banda e meça o tempo de download.

## Exemplo
Toxiproxy[:mysql_master].downstream(:latency, latency: 1000).apply faz a consulta demorar pelo menos um segundo dentro do bloco.

## Limites e trade-offs
jitter alto demais faz o atraso mínimo deixar de ser garantia, e bandwidth em KB/s mede o fluxo, não o round trip — testes de timeout precisam converter as unidades com cuidado.

## Como verificar
Remova o toxic após o bloco e confirme que a latência extra desaparece da chamada seguinte.

## Conexões
- [[toxiproxy-populate-proxies]] — Veja também: Toxiproxy: popular os proxies no boot.
- [[toxiproxy-timeout-reset-peer]] — Veja também: Toxiproxy: conexões que apodrecem com timeout e reset_peer.

## Fontes
- [Toxiproxy — README oficial](https://github.com/Shopify/toxiproxy) — proposta, instalação, populate, toxics e HTTP API; consultado em 2026-10-03.
- [Toxiproxy — cliente Ruby](https://github.com/Shopify/toxiproxy-ruby) — exemplos de populate, down e apply; consultado em 2026-10-03.
