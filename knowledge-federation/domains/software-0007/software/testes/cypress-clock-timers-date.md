---
id: software.testes.tranche09.000257
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
fontes: ["https://docs.cypress.io/api/commands/clock", "https://docs.cypress.io/app/component-testing/get-started"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Cypress: controlar relógio sem mascarar espera externa

## Em uma frase
cy.clock e cy.tick ajudam a testar Date e timers JavaScript controlados no contexto da janela da aplicação.

## Por que importa
O Cypress limpa e repete partes do estado de teste no navegador, mas cada mecanismo cobre somente uma fronteira específica. Esperar vários segundos reais para observar debounce, timeout visual ou expiração local deixa testes lentos e menos determinísticos.

## Como funciona
Comece pelo comportamento observável, prepare dados independentes para cada teste e registre rotas antes de provocar as requisições que serão verificadas. Instale o clock antes do código da aplicação que agenda o timer e avance o tempo somente até a fronteira relevante.

## Exemplo
Uma busca com debounce usa clock controlado, recebe entrada, avança o intervalo previsto e então valida a chamada produzida.

## Limites e trade-offs
Um teste verde com browser e servidor simulado não prova que todos os serviços reais, storages ou integrações estejam corretos. Tempo virtual não avança automaticamente jobs do servidor, rede real ou schedulers fora do escopo controlado.

## Como verificar
Compare a contagem de chamadas antes e depois de cy.tick e execute outro caso com relógio real para o caminho de integração.

## Conexões
- [[cypress-cross-origin-cy-origin]] — Veja também: Cypress: cruzar origens com cy.origin no mesmo teste.
- [[cypress-component-testing-boundary]] — Veja também: Cypress: separar component testing de cobertura end-to-end.

## Fontes
- [Cypress — cy.clock()](https://docs.cypress.io/api/commands/clock) — controle de Date e temporizadores no ambiente de teste; consultado em 2026-10-02.
- [Cypress — Component testing](https://docs.cypress.io/app/component-testing/get-started) — montagem de componentes em navegador real e configuração do dev server; consultado em 2026-10-02.
