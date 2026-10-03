---
id: software.testes.tranche21.001547
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
fontes: ["https://github.com/Shopify/toxiproxy", "https://github.com/douglas/toxiproxy-python"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Toxiproxy: stream, toxicidade e o down que não é toxic

## Em uma frase
Toxicos têm nome padrão tipo_corrente, stream obrigatório upstream (cliente para servidor) ou downstream (servidor para cliente), toxicidade de probabilidade com default um, e atributos próprios; derrubar o serviço é outro gesto, com enabled falso no proxy.

## Por que importa
Separar pedido de resposta na direção do link permite testar "o servidor demora para responder" sem afetar "o cliente demora para chegar".

## Como funciona
Registre a latência no downstream para simular lentidão de resposta e a toxicidade parcial quando quiser perturbar apenas parte do tráfego.

## Exemplo
Um toxic com toxicidade 0,5 atinge cerca de metade dos dados, aproximando oscilação em vez de pane total.

## Limites e trade-offs
down exige POST em /proxies/{proxy} trocando o campo enabled, não uma entrada na lista de toxics, e mudar listen ou upstream do proxy reinicia o link com suas conexões ativas.

## Como verificar
Defina um stream na direção errada e confirme que a requisição, não a resposta, é a parte atrasada.

## Conexões
- [[toxiproxy-packet-loss]] — Veja também: Toxiproxy: queda de pacotes com rajadas por packet_loss.
- [[toxiproxy-http-api-endpoints]] — Veja também: Toxiproxy: a API HTTP de controle.

## Fontes
- [Toxiproxy — README oficial](https://github.com/Shopify/toxiproxy) — proposta, instalação, populate, toxics e HTTP API; consultado em 2026-10-03.
- [Toxiproxy — cliente Python](https://github.com/douglas/toxiproxy-python) — cliente comunitário linkado pelo projeto; consultado em 2026-10-03.
