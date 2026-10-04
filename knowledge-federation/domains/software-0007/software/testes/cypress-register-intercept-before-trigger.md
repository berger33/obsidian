---
id: software.testes.tranche09.000253
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
fontes: ["https://docs.cypress.io/api/commands/intercept", "https://docs.cypress.io/app/guides/network-requests"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Cypress: registrar intercept antes da ação que dispara a rede

## Em uma frase
Um intercept deve estar instalado antes do evento da interface que inicia a requisição que o teste quer observar.

## Por que importa
O Cypress limpa e repete partes do estado de teste no navegador, mas cada mecanismo cobre somente uma fronteira específica. Se o evento ocorrer primeiro, uma resposta rápida pode chegar antes da criação da rota e produzir espera sem alias correspondente.

## Como funciona
Comece pelo comportamento observável, prepare dados independentes para cada teste e registre rotas antes de provocar as requisições que serão verificadas. Defina cy.intercept, atribua alias e só então visite ou interaja com a tela que inicia a operação.

## Exemplo
O teste instala a rota para GET de pedidos, clica em atualizar a lista, aguarda o alias e valida status e conteúdo mostrado.

## Limites e trade-offs
Um teste verde com browser e servidor simulado não prova que todos os serviços reais, storages ou integrações estejam corretos. Um alias comprova correspondência com uma chamada observada; não prova sozinho que a tela consumiu corretamente a resposta.

## Como verificar
Atrase a resposta de teste e confirme que a rota está registrada antes da interação e que o teste verifica a atualização renderizada.

## Conexões
- [[cypress-intercept-browser-vs-cy-request]] — Veja também: Cypress: cy.intercept observa tráfego do app, não cy.request.
- [[cypress-stub-versus-real-server-coverage]] — Veja também: Cypress: equilibrar stubs de rede e fluxo com servidor real.

## Fontes
- [Cypress — cy.intercept()](https://docs.cypress.io/api/commands/intercept) — sintaxe e ciclo de vida de rotas e aliases de rede; consultado em 2026-10-02.
- [Cypress — Intercepting network requests](https://docs.cypress.io/app/guides/network-requests) — interceptação, stubs, respostas reais e requisições iniciadas pelo aplicativo; consultado em 2026-10-02.
