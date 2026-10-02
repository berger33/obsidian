---
id: software.testes.tranche09.000251
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
fontes: ["https://docs.cypress.io/app/core-concepts/retry-ability", "https://docs.cypress.io/api/commands/intercept"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Cypress: distinguir retryability de queries e efeitos

## Em uma frase
Queries encadeadas e assertions podem ser repetidas até a condição passar ou expirar; uma ação que altera estado não é um retry seguro.

## Por que importa
O Cypress limpa e repete partes do estado de teste no navegador, mas cada mecanismo cobre somente uma fronteira específica. Confundir a nova tentativa de uma leitura com a repetição de um clique pode duplicar submissões ou esconder uma corrida.

## Como funciona
Comece pelo comportamento observável, prepare dados independentes para cada teste e registre rotas antes de provocar as requisições que serão verificadas. Faça a ação uma vez e encadeie uma query/assertion observável que Cypress possa reavaliar enquanto a interface atualiza.

## Exemplo
Após clicar em salvar, a assertion verifica que a linha aparece e contém o valor persistido, sem colocar o clique dentro de uma espera repetida.

## Limites e trade-offs
Um teste verde com browser e servidor simulado não prova que todos os serviços reais, storages ou integrações estejam corretos. Timeout maior não corrige uma ação não idempotente nem substitui a sincronização com o evento correto.

## Como verificar
Force uma atualização lenta e confira no command log quantas vezes a query e a ação ocorreram antes da assertion final.

## Conexões
- [[cypress-test-isolation-indexeddb]] — Veja também: Cypress: entender o alcance do test isolation.
- [[cypress-intercept-browser-vs-cy-request]] — Veja também: Cypress: cy.intercept observa tráfego do app, não cy.request.

## Fontes
- [Cypress — Retry-ability](https://docs.cypress.io/app/core-concepts/retry-ability) — repetição de queries e assertions e fronteira com comandos com efeitos; consultado em 2026-10-02.
- [Cypress — cy.intercept()](https://docs.cypress.io/api/commands/intercept) — sintaxe e ciclo de vida de rotas e aliases de rede; consultado em 2026-10-02.
