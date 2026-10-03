---
id: software.testes.tranche21.001546
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
fontes: ["https://github.com/Shopify/toxiproxy", "https://github.com/Shopify/toxiproxy/blob/main/CHANGELOG.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Toxiproxy: queda de pacotes com rajadas por packet_loss

## Em uma frase
O toxic packet_loss descarta chunks aleatoriamente com probabilidade loss_rate entre zero e um, e correlation eleva a chance de descarte logo após um descarte anterior, modelando perda em rajada.

## Por que importa
Wi-Fi instável, móvel e satélite não perdem pacotes de forma independente, e um teste calibrado em queda uniforme passa onde a rajada derrubaria a conexão.

## Como funciona
Ajuste uma perda pequena com correlation alto para verter o cliente ao regime de rajadas e observe a política de retentativas.

## Exemplo
A probabilidade padrão é zero — o toxic é inerte até você definir o ritmo, o que facilita deixá-lo instalado na suíte com controle por ambiente.

## Limites e trade-offs
Perda aleatória nunca é determinística: o mesmo caso pode pegar caminhos diferentes em execuções, exigindo margem nas asserções de tempo.

## Como verificar
Suba a perda gradualmente e confirme em que ponto o retry policy do cliente começa a falhar o teste.

## Conexões
- [[toxiproxy-slicer-limit-data]] — Veja também: Toxiproxy: pacotes miúdos e conexões cortadas por tamanho.
- [[toxiproxy-toxic-fields-direction]] — Veja também: Toxiproxy: stream, toxicidade e o down que não é toxic.

## Fontes
- [Toxiproxy — README oficial](https://github.com/Shopify/toxiproxy) — proposta, instalação, populate, toxics e HTTP API; consultado em 2026-10-03.
- [Toxiproxy — CHANGELOG](https://github.com/Shopify/toxiproxy/blob/main/CHANGELOG.md) — histórico de releases e mudanças da API; consultado em 2026-10-03.
