---
id: software.testes.tranche22.001645
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
fontes: ["https://docs.hoverfly.io/en/stable/pages/tutorials/basic/capturingsequences/capturingsequences.html", "https://docs.hoverfly.io/en/latest/index.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Hoverfly: simulate é o replay sem rede

## Em uma frase
Em simulate mode o hoverfly responde direto do catálogo de pares gravados, sem tocar no serviço original — o fluxo de trabalho típico termina em hoverctl mode simulate depois de capturar, para testes repetíveis offline.

## Por que importa
O payoff do capture/simulate aparece aqui: a suíte roda contra o JSON versionado, deterministicamente, no container isolado do CI, sem egress liberado.

## Como funciona
A mesma url do exemplo público roda contra o proxy nos dois modos: no capture ela atravessa até o serviço real; no simulate o proxy local responde sozinho.

## Exemplo
As docs de conceitos tratam "Hoverfly modes" como seção própria (junto com matching strategies e destination filtering) — conhecer os modos é pré-requisito de qualquer pipeline com hoverfly.

## Limites e trade-offs
Simular respostas capturadas de ambiente instável congela o ruído do ambiente na simulação; vale editar o JSON antes de versionar.

## Como verificar
Desligue o acesso externo da máquina, rode a suíte em simulate e confirme que tudo passa sem nenhuma tentativa de conexão real.

## Conexões
- [[hoverfly-stateful-capture]] — Veja também: Hoverfly: sequências para APIs com estado.
- [[hoverfly-concepts-map]] — Veja também: Hoverfly: o mapa dos Key Concepts.

## Fontes
- [Hoverfly — Capturing a stateful sequence](https://docs.hoverfly.io/en/stable/pages/tutorials/basic/capturingsequences/capturingsequences.html) — capture --stateful, requiresState/transitionsState e hoverctl state; consultado em 2026-10-03.
- [Hoverfly — documentação inicial](https://docs.hoverfly.io/en/latest/index.html) — conceitos-chave, reference e troubleshooting do v1.12.15; consultado em 2026-10-03.
