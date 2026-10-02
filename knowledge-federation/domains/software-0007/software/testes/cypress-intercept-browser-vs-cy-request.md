---
id: software.testes.tranche09.000252
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
fontes: ["https://docs.cypress.io/app/guides/network-requests", "https://docs.cypress.io/api/commands/intercept"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Cypress: cy.intercept observa tráfego do app, não cy.request

## Em uma frase
cy.intercept observa e pode alterar requisições feitas pelo aplicativo no browser; cy.request é uma chamada iniciada diretamente pelo teste.

## Por que importa
O Cypress limpa e repete partes do estado de teste no navegador, mas cada mecanismo cobre somente uma fronteira específica. Esperar um alias de intercept depois de cy.request cria uma expectativa sobre tráfego que aquela API não produz no fluxo usual.

## Como funciona
Comece pelo comportamento observável, prepare dados independentes para cada teste e registre rotas antes de provocar as requisições que serão verificadas. Use intercept para observar a navegação real do usuário e verifique a resposta direta de cy.request no objeto retornado pelo próprio comando.

## Exemplo
O teste usa cy.request para criar um registro por API e, em seguida, intercepta separadamente a requisição GET que a tela dispara.

## Limites e trade-offs
Um teste verde com browser e servidor simulado não prova que todos os serviços reais, storages ou integrações estejam corretos. As duas operações podem atingir o mesmo endpoint, mas pertencem a caminhos diferentes e não devem ser confundidas.

## Como verificar
Registre os aliases, examine o Command Log e confirme qual origem emitiu cada chamada antes de afirmar que houve tráfego do navegador.

## Conexões
- [[cypress-query-retry-sem-repetir-efeitos]] — Veja também: Cypress: distinguir retryability de queries e efeitos.
- [[cypress-register-intercept-before-trigger]] — Veja também: Cypress: registrar intercept antes da ação que dispara a rede.

## Fontes
- [Cypress — Intercepting network requests](https://docs.cypress.io/app/guides/network-requests) — interceptação, stubs, respostas reais e requisições iniciadas pelo aplicativo; consultado em 2026-10-02.
- [Cypress — cy.intercept()](https://docs.cypress.io/api/commands/intercept) — sintaxe e ciclo de vida de rotas e aliases de rede; consultado em 2026-10-02.
