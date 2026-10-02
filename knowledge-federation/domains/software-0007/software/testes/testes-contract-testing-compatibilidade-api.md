---
id: software.testes.tranche07.000146
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-01
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-07.md"
fontes: ["https://docs.pact.io/getting_started/how_pact_works", "https://spec.openapis.org/oas/v3.1.1.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Testes de contrato para compatibilidade de API", "Teste: Testes de contrato para compatibilidade de API"]
lote: software-testes-2000-0001
---

# Testes de contrato para compatibilidade de API

## Em uma frase
Combine validação de schema com interações que representam necessidades reais de consumidores para detectar incompatibilidades antes do deploy.

## Por que importa
Um schema válido não prova que provedor e consumidor concordam sobre campos, estados e comportamento; mudanças aparentemente aditivas também podem quebrar clientes.

## Como funciona
Defina exemplos mínimos por interação, rode teste no consumidor e verificação no provedor, publique versão do contrato e aplique política de compatibilidade. Inclua mudanças de tipo, campo obrigatório, status, autenticação e comportamento relevante.

## Exemplo
Consumidor declara que consulta uma fatura e usa total e moeda; provedor verifica que responde com os campos mínimos e estado de fixture exigido antes de promover a alteração.

## Limites e trade-offs
Consumer-driven contracts cobrem apenas interações declaradas e não substituem testes end-to-end, requisitos de segurança ou testes de carga. Dados de provider state precisam ser determinísticos.

## Como verificar
Rode os contratos na pipeline de ambos os lados, valide resultado contra versão do schema e mantenha compatibilidade com consumidores ativos antes da implantação do provedor.

## Conexões
- [[contract-testing-consumer-provider]] — aprofundamento relacionado.
- [[schema-based-api-testing-schemathesis-openapi]] — aprofundamento relacionado.

## Fontes
- [Pact Docs — How Pact works](https://docs.pact.io/getting_started/how_pact_works) — interações mínimas de consumidor e verificação pelo provedor; consultado em 2026-10-01.
- [OpenAPI Specification 3.1.1](https://spec.openapis.org/oas/v3.1.1.html) — descrição estruturada e validável do contrato HTTP; consultado em 2026-10-01.
