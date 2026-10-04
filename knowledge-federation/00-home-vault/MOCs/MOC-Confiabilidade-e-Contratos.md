---
tipo: moc
dominio: software
subdominio: backend
ultima_verificacao: 2026-10-01
status: navigation_only
quality_status: excluded_from_note_gate
tags: [moc, dominio/software, navegacao]
aliases: [Confiabilidade e contratos de software]
---

# MOC — Confiabilidade e contratos de software

> **Este MOC é apenas navegação e está fora do gate de qualidade.** Sua existência não aprova o lote; cada nota listada é avaliada individualmente.

Este mapa aponta para o primeiro lote de oito notas autorais. As oito passaram pelo gate automatizado e tiveram a revisão factual humana confirmada pelo usuário em 2026-10-02; contam como notas válidas. O mapa é navegação e não substitui auditoria.

## Backend e integrações

- [[idempotencia-http-api]] — semântica de repetição segura em APIs.
- [[timeouts-retries-backoff-jitter]] — deadlines, retries limitados e controle de sobrecarga.
- [[contrato-openapi-http]] — descrição legível por máquinas da superfície HTTP.
- [[contract-testing-consumer-provider]] — verificação de interações entre consumidores e provedores.

## Operação e dados

- [[observabilidade-sinais-distribuidos]] — uso complementar de métricas, traces e logs.
- [[sli-slo-orcamento-de-erro]] — objetivos de serviço, indicadores e orçamento de erro.
- [[migracoes-expand-contract]] — compatibilidade de schema durante deploys.
- [[gates-de-qualidade-no-merge]] — checks rastreáveis antes da integração.

## Critério de publicação das notas

Uma nota só deve ser contabilizada como validada após passar pela auditoria automatizada e ter suas afirmações conferidas nas fontes citadas por uma pessoa revisora identificada no frontmatter. O resultado automatizado não substitui revisão de domínio.
