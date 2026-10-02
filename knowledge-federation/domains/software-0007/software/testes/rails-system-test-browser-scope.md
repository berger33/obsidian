---
id: software.testes.tranche14.000804
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
fontes: ["https://guides.rubyonrails.org/testing.html", "https://api.rubyonrails.org/classes/ActionDispatch/IntegrationTest.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Rails: reservar system tests para comportamento de navegador

## Em uma frase
Rails system tests usam Capybara para exercitar a aplicação no browser, inclusive comportamento JavaScript percebido pelo usuário.

## Por que importa
Esse nível detecta integração do front-end que requests simulados não avaliam, mas aumenta tempo e dependências de browser.

## Como funciona
Concentre-os em jornadas representativas, escolha driver apropriado ao CI e deixe lógica de negócio em testes mais rápidos.

## Exemplo
Um fluxo de checkout pode verificar a interação de modal, teclado e atualização do resumo no navegador real ou headless.

## Limites e trade-offs
Um system test não deve duplicar cada combinação de regra de negócio nem depender de serviços remotos sem controle.

## Como verificar
Confirme setup do driver, captura de screenshot ou logs e encerramento do browser quando a assertion falhar.

## Conexões
- [[rails-integration-json-response-contract]] — Veja também: Rails: validar encoding e corpo de resposta JSON.
- [[rails-parallel-process-test-isolation]] — Veja também: Rails: isolar banco e recursos entre workers paralelos.

## Fontes
- [Rails 8.1 — Testing Rails Applications](https://guides.rubyonrails.org/testing.html) — ambiente, fixtures, testes funcionais, integração, system tests e paralelismo; consultado em 2026-10-02.
- [Rails 8.1 — ActionDispatch::IntegrationTest](https://api.rubyonrails.org/classes/ActionDispatch/IntegrationTest.html) — fluxos HTTP entre componentes, sessões, redirects e respostas JSON; consultado em 2026-10-02.
