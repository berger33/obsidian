---
id: software.testes.tranche09.000254
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
fontes: ["https://docs.cypress.io/app/guides/network-requests", "https://docs.cypress.io/app/core-concepts/testing-types"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Cypress: equilibrar stubs de rede e fluxo com servidor real

## Em uma frase
Stubs tornam respostas rápidas e controláveis, enquanto respostas reais exercitam o contrato integrado entre cliente e servidor.

## Por que importa
O Cypress limpa e repete partes do estado de teste no navegador, mas cada mecanismo cobre somente uma fronteira específica. Uma suíte só com stubs pode manter fixtures incompatíveis com o formato efetivamente retornado em produção.

## Como funciona
Comece pelo comportamento observável, prepare dados independentes para cada teste e registre rotas antes de provocar as requisições que serão verificadas. Use stubs para estados raros e bordas difíceis de preparar, e preserve alguns fluxos críticos end-to-end com dados de servidor controlados.

## Exemplo
A lista usa stub para testar vazio e erro 503, e um caminho de compra executa pelo menos uma vez contra API e banco de teste.

## Limites e trade-offs
Um teste verde com browser e servidor simulado não prova que todos os serviços reais, storages ou integrações estejam corretos. O equilíbrio depende de custo de setup e criticidade; stub não substitui testes funcionais do backend.

## Como verificar
Compare fixtures stubadas ao contrato publicado e confirme que caminhos prioritários também exercitam a integração verdadeira.

## Conexões
- [[cypress-register-intercept-before-trigger]] — Veja também: Cypress: registrar intercept antes da ação que dispara a rede.
- [[cypress-session-cache-validacao]] — Veja também: Cypress: validar uma sessão restaurada por cy.session.

## Fontes
- [Cypress — Intercepting network requests](https://docs.cypress.io/app/guides/network-requests) — interceptação, stubs, respostas reais e requisições iniciadas pelo aplicativo; consultado em 2026-10-02.
- [Cypress — Testing types](https://docs.cypress.io/app/core-concepts/testing-types) — distinção entre component testing e end-to-end testing; consultado em 2026-10-02.
