---
id: software.testes.tranche14.000802
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-14.md"
fontes: ["https://api.rubyonrails.org/classes/ActionDispatch/IntegrationTest.html", "https://guides.rubyonrails.org/testing.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Rails: usar IntegrationTest para percorrer um fluxo HTTP

## Em uma frase
`ActionDispatch::IntegrationTest` exercita vários controllers e o caminho completo entre dispatcher, aplicação e banco.

## Por que importa
Um teste de fluxo captura falhas de integração entre partes que passariam individualmente em testes isolados.

## Como funciona
Envie requests com helpers como `get` e `post`, acompanhe redirects quando relevantes e faça assertions sobre status, caminho e resposta.

## Exemplo
Um fluxo de login publica credenciais, segue o redirect e verifica que a sessão chegou à página inicial.

## Limites e trade-offs
Abranger a stack custa mais que chamar uma função diretamente e ainda não representa um browser real com JavaScript.

## Como verificar
Escolha o nível pelo risco coberto e mantenha assertions que expliquem qual transição do fluxo falhou.

## Conexões
- [[rails-test-environment-database-boundary]] — Veja também: Rails: manter banco de teste separado do ambiente local.
- [[rails-integration-json-response-contract]] — Veja também: Rails: validar encoding e corpo de resposta JSON.

## Fontes
- [Rails 8.1 — ActionDispatch::IntegrationTest](https://api.rubyonrails.org/classes/ActionDispatch/IntegrationTest.html) — fluxos HTTP entre componentes, sessões, redirects e respostas JSON; consultado em 2026-10-02.
- [Rails 8.1 — Testing Rails Applications](https://guides.rubyonrails.org/testing.html) — ambiente, fixtures, testes funcionais, integração, system tests e paralelismo; consultado em 2026-10-02.
