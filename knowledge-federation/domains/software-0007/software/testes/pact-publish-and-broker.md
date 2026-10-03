---
id: software.testes.tranche17.001131
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
fontes: ["https://docs.pact.io/pact_broker", "https://github.com/pact-foundation/pact-js"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Pact: publicar contratos no intermediário

## Em uma frase
Os arquivos de contrato gerados pelos testes do consumidor são publicados em um serviço central com versão e identificação do aplicativo.

## Por que importa
O intermediário mantém o histórico de contratos e resultados, permitindo que consumidores e provedores evoluam sem coordenação manual.

## Como funciona
Publique em cada execução do consumidor com versão derivada do repositório, evitando versões genéricas que sobrescrevem histórico.

## Exemplo
Uma versão publicada com identificador de ramo permite selecionar os contratos relevantes e acompanhar quais estão verificados.

## Limites e trade-offs
Versões repetidas ou genéricas confundem o histórico, e a publicação sem metadados dificulta a consulta por ambiente.

## Como verificar
Publique duas versões do mesmo contrato e confirme que o intermediário lista ambas com identificadores distintos.

## Conexões
- [[pact-provider-verification]] — Veja também: Pact: verificar contratos no provedor.
- [[pact-can-i-deploy]] — Veja também: Pact: autorizar implantação pelo histórico.

## Fontes
- [Pact — Broker](https://docs.pact.io/pact_broker) — publicação de contratos, histórico e metadados de versão; consultado em 2026-10-03.
- [Pact — repositório oficial](https://github.com/pact-foundation/pact-js) — implementação de referência em JavaScript e exemplos; consultado em 2026-10-03.
