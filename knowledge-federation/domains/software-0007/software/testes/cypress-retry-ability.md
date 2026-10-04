---
id: software.testes.tranche18.001158
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-18.md"
fontes: ["https://docs.cypress.io/guides/references/best-practices", "https://docs.cypress.io/api/table-of-contents"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Cypress: aproveitar a repetição automática de asserções

## Em uma frase
Consultas e asserções são repetidas até que a condição se torne verdadeira ou o tempo limite se esgote, sem interromper a cadeia de comandos.

## Por que importa
Esperas fixas escondem o tempo real das operações e tornam a suíte lenta, enquanto a repetição automática acompanha a aplicação.

## Como funciona
Encadeie a asserção logo após a consulta e deixe a repetição trabalhar, aumentando o limite apenas quando a operação for realmente lenta.

## Exemplo
Uma lista alimentada por chamada assíncrona pode ser verificada até conter o item esperado, sem pausa intermediária.

## Limites e trade-offs
Asserções que dependem de estado intermediário podem passar por acaso, e condições sobre valores voláteis causam repetição inútil até o tempo esgotar.

## Como verificar
Remova uma pausa fixa de um caso e confirme que a asserção ainda passa, apenas em menos tempo.

## Conexões
- [[cypress-architecture-in-browser]] — Veja também: Cypress: entender a execução dentro do navegador.
- [[cypress-interception]] — Veja também: Cypress: controlar a rede com interceptação.

## Fontes
- [Cypress — Best practices](https://docs.cypress.io/guides/references/best-practices) — seletores estáveis, independência entre testes e dados de apoio; consultado em 2026-10-03.
- [Cypress — API](https://docs.cypress.io/api/table-of-contents) — comandos, asserções, comandos próprios e opções de execução; consultado em 2026-10-03.
