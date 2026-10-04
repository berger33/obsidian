---
id: software.testes.tranche09.000256
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
fontes: ["https://docs.cypress.io/app/guides/cross-origin-testing", "https://docs.cypress.io/app/core-concepts/testing-types"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Cypress: cruzar origens com cy.origin no mesmo teste

## Em uma frase
Quando um teste navega entre origens diferentes, comandos destinados à segunda origem precisam ser executados no contexto de cy.origin.

## Por que importa
O Cypress limpa e repete partes do estado de teste no navegador, mas cada mecanismo cobre somente uma fronteira específica. Uma autenticação federada pode redirecionar o browser para um domínio externo e deixar comandos seguintes associados à origem anterior.

## Como funciona
Comece pelo comportamento observável, prepare dados independentes para cada teste e registre rotas antes de provocar as requisições que serão verificadas. Separe a interação com o domínio remoto em cy.origin e retorne ao app principal para validar o redirecionamento final.

## Exemplo
O fluxo visita o app, preenche o provedor de identidade em cy.origin e depois verifica a sessão e a rota de retorno no app.

## Limites e trade-offs
Um teste verde com browser e servidor simulado não prova que todos os serviços reais, storages ou integrações estejam corretos. Cross-origin iframes têm limitações distintas; requisitos atuais podem mudar com a versão e a configuração do Cypress.

## Como verificar
Teste o fluxo com os hosts de staging autorizados e confirme que o contexto correto executa cada comando após a navegação.

## Conexões
- [[cypress-session-cache-validacao]] — Veja também: Cypress: validar uma sessão restaurada por cy.session.
- [[cypress-clock-timers-date]] — Veja também: Cypress: controlar relógio sem mascarar espera externa.

## Fontes
- [Cypress — Cross-origin testing](https://docs.cypress.io/app/guides/cross-origin-testing) — limites de origem e uso explícito de cy.origin(); consultado em 2026-10-02.
- [Cypress — Testing types](https://docs.cypress.io/app/core-concepts/testing-types) — distinção entre component testing e end-to-end testing; consultado em 2026-10-02.
