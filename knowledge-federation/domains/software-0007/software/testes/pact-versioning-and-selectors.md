---
id: software.testes.tranche17.001133
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-17.md"
fontes: ["https://docs.pact.io/pact_broker/advanced_topics/consumer_version_selectors", "https://docs.pact.io/pact_broker"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Pact: controlar versões e seleção de contratos

## Em uma frase
Os seletores definem quais contratos o provedor verifica, combinando ramos, etiquetas, ambiente ou contratos em andamento.

## Por que importa
Sem seleção criteriosa, o provedor verifica contratos antigos e irrelevantes, e a esteira fica lenta sem ganho de confiança.

## Como funciona
Selecione contratos do ramo em desenvolvimento e do que está publicado no ambiente, e trate contratos de trabalho em andamento separadamente.

## Exemplo
Um provedor pode verificar os contratos do ramo principal e, ao mesmo tempo, os do ramo do consumidor em revisão.

## Limites e trade-offs
Etiquetas reutilizadas apontam para versões diferentes com o tempo, e a falta de seleção faz a verificação ignorar contratos novos.

## Como verificar
Liste os contratos escolhidos na execução e compare com os ramos esperados antes de investigar qualquer falha.

## Conexões
- [[pact-can-i-deploy]] — Veja também: Pact: autorizar implantação pelo histórico.
- [[pact-webhooks-and-pending]] — Veja também: Pact: automatizar avisos e tratar contratos novos.

## Fontes
- [Pact — Consumer version selectors](https://docs.pact.io/pact_broker/advanced_topics/consumer_version_selectors) — seleção de contratos por ramo, etiqueta e ambiente; consultado em 2026-10-03.
- [Pact — Broker](https://docs.pact.io/pact_broker) — publicação de contratos, histórico e metadados de versão; consultado em 2026-10-03.
