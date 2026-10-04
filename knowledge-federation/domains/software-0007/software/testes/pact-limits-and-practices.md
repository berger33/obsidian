---
id: software.testes.tranche17.001135
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
fontes: ["https://docs.pact.io/getting_started/how_pact_works", "https://docs.pact.io/implementation_guides/javascript/docs/provider"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Pact: reconhecer limites do teste de contrato

## Em uma frase
O contrato cobre a forma da interação acordada, mas não verifica regras de negócio, desempenho nem o comportamento completo do provedor.

## Por que importa
Usar o contrato como substituto de testes funcionais deixa regras complexas sem verificação e cria confiança indevida na suíte.

## Como funciona
Combine a verificação de contratos com testes de integração do provedor e mantenha o contrato restrito ao que o consumidor usa.

## Exemplo
O contrato pode garantir que o campo de total é numérico sem verificar se o cálculo do total está correto.

## Limites e trade-offs
Contratos que replicam toda a lógica do provedor se tornam frágeis e caros, e a cobertura parcial dá sensação de proteção maior do que a real.

## Como verificar
Escolha um contrato existente e liste quais regras de negócio ele não verifica, documentando onde essas regras são testadas.

## Conexões
- [[pact-webhooks-and-pending]] — Veja também: Pact: automatizar avisos e tratar contratos novos.

## Fontes
- [Pact — How Pact works](https://docs.pact.io/getting_started/how_pact_works) — fluxo dirigido pelo consumidor, publicação e verificação de contratos; consultado em 2026-10-03.
- [Pact — Provider verification](https://docs.pact.io/implementation_guides/javascript/docs/provider) — verificação do provedor e implementação de estados; consultado em 2026-10-03.
