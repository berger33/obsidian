---
id: software.testes.tranche09.000258
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
fontes: ["https://docs.cypress.io/app/component-testing/get-started", "https://docs.cypress.io/app/core-concepts/testing-types"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Cypress: separar component testing de cobertura end-to-end

## Em uma frase
Component tests montam um componente em navegador real com servidor de desenvolvimento, enquanto E2E percorre a aplicação integrada.

## Por que importa
O Cypress limpa e repete partes do estado de teste no navegador, mas cada mecanismo cobre somente uma fronteira específica. A camada mais rápida não cobre por si só roteamento final, autenticação completa ou todos os serviços remotos.

## Como funciona
Comece pelo comportamento observável, prepare dados independentes para cada teste e registre rotas antes de provocar as requisições que serão verificadas. Teste estados e interações locais no componente; reserve fluxos prioritários para end-to-end com inicialização de aplicação e backend apropriados.

## Exemplo
Um componente de pagamento valida loading e erro com stubs; o checkout completo também é executado em ambiente de integração.

## Limites e trade-offs
Um teste verde com browser e servidor simulado não prova que todos os serviços reais, storages ou integrações estejam corretos. Bibliotecas de montagem, bundler e framework suportados variam por versão; valide a configuração do projeto.

## Como verificar
Confirme a montagem visual do componente e mantenha ao menos um teste de fluxo que cruza fronteiras realmente críticas.

## Conexões
- [[cypress-clock-timers-date]] — Veja também: Cypress: controlar relógio sem mascarar espera externa.
- [[cypress-test-retries-diagnostico]] — Veja também: Cypress: interpretar test retries como sinal de flakiness.

## Fontes
- [Cypress — Component testing](https://docs.cypress.io/app/component-testing/get-started) — montagem de componentes em navegador real e configuração do dev server; consultado em 2026-10-02.
- [Cypress — Testing types](https://docs.cypress.io/app/core-concepts/testing-types) — distinção entre component testing e end-to-end testing; consultado em 2026-10-02.
