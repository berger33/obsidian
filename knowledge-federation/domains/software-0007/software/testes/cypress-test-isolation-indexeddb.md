---
id: software.testes.tranche09.000250
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-09.md"
fontes: ["https://docs.cypress.io/app/core-concepts/test-isolation", "https://docs.cypress.io/api/commands/session"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Cypress: entender o alcance do test isolation

## Em uma frase
Com test isolation ativo, Cypress limpa cookies, localStorage e sessionStorage, mas não todos os storages do navegador.

## Por que importa
O Cypress limpa e repete partes do estado de teste no navegador, mas cada mecanismo cobre somente uma fronteira específica. IndexedDB e estado mantido pelo servidor podem sobreviver e contaminar um caso seguinte, mesmo com a página reiniciada.

## Como funciona
Comece pelo comportamento observável, prepare dados independentes para cada teste e registre rotas antes de provocar as requisições que serão verificadas. Liste cada armazenamento usado pela aplicação e remova explicitamente somente o estado persistente que o cenário exige zerar.

## Exemplo
Um teste grava cache offline no IndexedDB; o teste seguinte verifica primeiro uma instalação limpa e depois a restauração do cache de forma intencional.

## Limites e trade-offs
Um teste verde com browser e servidor simulado não prova que todos os serviços reais, storages ou integrações estejam corretos. A documentação cita outros storages que não são limpos; limpeza customizada depende das APIs e do navegador usado.

## Como verificar
Rode o teste isoladamente, em ordem aleatória e repetidamente; inspecione cookies, storages, IndexedDB e dados do backend entre execuções.

## Conexões
- [[cypress-query-retry-sem-repetir-efeitos]] — Veja também: Cypress: distinguir retryability de queries e efeitos.

## Fontes
- [Cypress — Test isolation](https://docs.cypress.io/app/core-concepts/test-isolation) — escopo do isolamento do navegador e estado que não é limpo automaticamente; consultado em 2026-10-02.
- [Cypress — cy.session()](https://docs.cypress.io/api/commands/session) — cache/restore de cookies e storage e validação de sessão; consultado em 2026-10-02.
