---
id: software.testes.tranche17.001134
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
fontes: ["https://docs.pact.io/pact_broker/webhooks", "https://docs.pact.io/pact_broker"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Pact: automatizar avisos e tratar contratos novos

## Em uma frase
Avisos automáticos podem disparar verificações quando um contrato muda, e contratos em andamento permitem que o provedor os teste sem bloquear o pipeline.

## Por que importa
O fluxo contínuo reduz a defasagem entre mudança de contrato e verificação, e o tratamento de contratos novos evita bloqueio antes de a interação ser revisada.

## Como funciona
Configure avisos para disparar a verificação do provedor, marque contratos novos como provisórios e promova-os quando estiverem estáveis.

## Exemplo
Um contrato recém-publicado dispara a verificação do provedor, que passa a reportar o resultado para o histórico.

## Limites e trade-offs
Avisos mal configurados disparam execuções em excesso e contratos provisórios esquecidos permanecem fora do bloqueio indefinidamente.

## Como verificar
Publique um contrato novo e confirme que a verificação foi disparada e que o resultado aparece associado à versão correta.

## Conexões
- [[pact-versioning-and-selectors]] — Veja também: Pact: controlar versões e seleção de contratos.
- [[pact-limits-and-practices]] — Veja também: Pact: reconhecer limites do teste de contrato.

## Fontes
- [Pact — Webhooks](https://docs.pact.io/pact_broker/webhooks) — avisos automáticos que disparam verificações em mudança de contrato; consultado em 2026-10-03.
- [Pact — Broker](https://docs.pact.io/pact_broker) — publicação de contratos, histórico e metadados de versão; consultado em 2026-10-03.
