---
id: software.testes.tranche21.001545
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

# Toxiproxy: pacotes miúdos e conexões cortadas por tamanho

## Em uma frase
O slicer fatia os dados TCP em pedaços pequenos com delay médio em microssegundos entre fatias, enquanto limit_data fecha a conexão quando o volume transmitido passa do limite em bytes.

## Por que importa
Fragmentação e truncamento são condições que quase nenhum teste de unidade alcança e vários protocolos reais quebram sob elas.

## Como funciona
Configure average_size com uma variação menor que ela mesma e use limit_data para simular um encerramento súbito no meio de uma resposta grande.

## Exemplo
O size_variation modela pacotes desiguais, e o README avisa que deve ficar abaixo do average_size.

## Limites e trade-offs
O delay do slicer é em microssegundos — ordem de grandeza diferente dos demais toxics em milissegundos — fonte de teste mil vezes mais lento do que o pretendido quando a unidade passa batida.

## Como verificar
Force um limit_data pequeno numa resposta conhecida e confirme que o cliente vê a conexão fechada antes do fim.

## Conexões
- [[toxiproxy-timeout-reset-peer]] — Veja também: Toxiproxy: conexões que apodrecem com timeout e reset_peer.
- [[toxiproxy-packet-loss]] — Veja também: Toxiproxy: queda de pacotes com rajadas por packet_loss.

## Fontes
- [Toxiproxy — README oficial](https://github.com/Shopify/toxiproxy) — proposta, instalação, populate, toxics e HTTP API; consultado em 2026-10-03.
- [Toxiproxy — cliente Go](https://github.com/Shopify/toxiproxy/tree/main/client) — cliente oficial embutido no repositório; consultado em 2026-10-03.
