---
id: software.testes.tranche14.000803
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

# Rails: validar encoding e corpo de resposta JSON

## Em uma frase
`IntegrationTest` permite declarar formato de request e inspecionar corpo parseado para testar um endpoint JSON dentro da aplicação.

## Por que importa
Assertions sobre status e conteúdo detectam incompatibilidades de contrato que um teste somente de controller poderia deixar passar.

## Como funciona
Envie parâmetros com `as: :json`, confira o status e use o parser de resposta associado ao MIME type retornado.

## Exemplo
Um POST de artigo envia atributos JSON e valida o objeto parseado com identificador e título retornados.

## Limites e trade-offs
O suporte padrão a encoding e parser depende do MIME type e extensões registradas pela aplicação.

## Como verificar
Teste código de status, estrutura e campos relevantes sem comparar strings JSON inteiras que variam em ordem ou formatação.

## Conexões
- [[rails-integration-test-full-stack-flow]] — Veja também: Rails: usar IntegrationTest para percorrer um fluxo HTTP.
- [[rails-system-test-browser-scope]] — Veja também: Rails: reservar system tests para comportamento de navegador.

## Fontes
- [Rails 8.1 — ActionDispatch::IntegrationTest](https://api.rubyonrails.org/classes/ActionDispatch/IntegrationTest.html) — fluxos HTTP entre componentes, sessões, redirects e respostas JSON; consultado em 2026-10-02.
- [Rails 8.1 — Testing Rails Applications](https://guides.rubyonrails.org/testing.html) — ambiente, fixtures, testes funcionais, integração, system tests e paralelismo; consultado em 2026-10-02.
