---
id: software.testes.tranche18.001161
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

# Cypress: escolher seletores estáveis

## Em uma frase
As consultas aceitam seletores de estilo, atributos dedicados à automação e textos visíveis, com estabilidade diferente entre eles.

## Por que importa
Seletores ligados ao estilo quebram a cada ajuste visual, e textos mudam com tradução e revisão de conteúdo.

## Como funciona
Prefira atributos dedicados à automação ou identificadores de testabilidade e evite posições estruturais na árvore.

## Exemplo
Um botão de confirmação pode ser consultado por atributo dedicado, mantendo o teste estável quando a classe de estilo mudar.

## Limites e trade-offs
Consultas por texto podem encontrar vários elementos e falhar por ambiguidade, e caminhos estruturais dependem de cada elemento intermediário.

## Como verificar
Renomeie uma classe de estilo do elemento e confirme que os testes que usam atributo dedicado continuam passando.

## Conexões
- [[cypress-session-caching]] — Veja também: Cypress: reaproveitar sessões de autenticação.
- [[cypress-fixtures]] — Veja também: Cypress: servir dados com arquivos de apoio.

## Fontes
- [Cypress — Best practices](https://docs.cypress.io/guides/references/best-practices) — seletores estáveis, independência entre testes e dados de apoio; consultado em 2026-10-03.
- [Cypress — API](https://docs.cypress.io/api/table-of-contents) — comandos, asserções, comandos próprios e opções de execução; consultado em 2026-10-03.
