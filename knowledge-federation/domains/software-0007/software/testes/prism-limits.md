---
id: software.testes.tranche16.001044
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-16.md"
fontes: ["https://docs.stoplight.io/docs/prism/83dbbd75532cf-http-mocking", "https://docs.stoplight.io/docs/prism/beeaad4dc0227-prism-cli"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Prism: reconhecer limites da simulação

## Em uma frase
A ferramenta reproduz respostas previstas no contrato, sem manter estado entre chamadas nem aplicar regras de negócio.

## Por que importa
Testes que dependem de sequência de operações ou de autenticação real não podem ser sustentados apenas pela simulação.

## Como funciona
Use a simulação para contratos de rota e forma, e cubra transições de estado com serviço real ou ambiente de teste controlado.

## Exemplo
Fluxos de criação e consulta encadeadas, que dependem de persistência, precisam de outro arranjo para representar o estado acumulado.

## Limites e trade-offs
Asserções contra a simulação validam o cliente em relação ao documento, não o serviço, e podem dar sensação falsa de integração verificada.

## Como verificar
Tente executar um fluxo com estado contra a simulação e documente em que ponto o comportamento deixa de corresponder ao serviço real.

## Conexões
- [[prism-contract-first-workflow]] — Veja também: Prism: sustentar o fluxo de contrato primeiro.

## Fontes
- [Prism — HTTP mocking](https://docs.stoplight.io/docs/prism/83dbbd75532cf-http-mocking) — modos estático e dinâmico, cabeçalho Prefer e respostas de violação; consultado em 2026-10-03.
- [Prism — CLI](https://docs.stoplight.io/docs/prism/beeaad4dc0227-prism-cli) — instalação, subcomandos mock e proxy e opções de validação; consultado em 2026-10-03.
