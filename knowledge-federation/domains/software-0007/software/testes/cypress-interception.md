---
id: software.testes.tranche18.001159
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
fontes: ["https://docs.cypress.io/api/commands/intercept", "https://docs.cypress.io/api/table-of-contents"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Cypress: controlar a rede com interceptação

## Em uma frase
O comando de interceptação observa, substitui ou atrasa requisições, permitindo simular respostas e aguardar chamadas específicas por apelido.

## Por que importa
Depender de serviços externos torna a suíte lenta e instável, e a interceptação isola o teste do ambiente real preservando o comportamento da aplicação.

## Como funciona
Declare a rota com método e caminho, atribua apelido e aguarde o apelido quando o teste depender da resposta.

## Exemplo
O teste pode responder com lista fixa de produtos e verificar que a interface apresenta exatamente esses itens.

## Limites e trade-offs
Interceptações amplas capturam chamadas de outros fluxos, e esperar pelo apelido errado mascara a ausência da requisição esperada.

## Como verificar
Altere a resposta simulada e confirme que o teste falha no ponto que depende do dado, evidenciando o isolamento.

## Conexões
- [[cypress-retry-ability]] — Veja também: Cypress: aproveitar a repetição automática de asserções.
- [[cypress-session-caching]] — Veja também: Cypress: reaproveitar sessões de autenticação.

## Fontes
- [Cypress — cy.intercept](https://docs.cypress.io/api/commands/intercept) — interceptação de rede, respostas simuladas e espera por apelido; consultado em 2026-10-03.
- [Cypress — API](https://docs.cypress.io/api/table-of-contents) — comandos, asserções, comandos próprios e opções de execução; consultado em 2026-10-03.
