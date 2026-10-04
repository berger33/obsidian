---
id: software.testes.tranche12.000557
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-12.md"
fontes: ["https://playwright.dev/docs/api/class-apirequestcontext", "https://playwright.dev/docs/api-testing"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Playwright Test: cookies em APIRequestContext

## Em uma frase
O `APIRequestContext` ligado ao browser context usa o mesmo jar de cookies; uma instância criada isoladamente mantém armazenamento próprio.

## Por que importa
Essa diferença determina se uma requisição de API representa a sessão já aberta no browser ou funciona como ferramenta independente para preparar dados.

## Como funciona
Use `page.request` ou `browserContext.request` quando a chamada deve compartilhar cookies do browser; crie um contexto via `apiRequest.newContext()` quando o teste precisa separar autenticação e estado.

## Exemplo
Um teste pode criar um carrinho por API com a sessão do browser e depois verificar a interface; outro pode usar um cliente isolado para criar uma conta sem alterar cookies da página.

## Limites e trade-offs
Compartilhar cookies também compartilha efeitos de autenticação e pode fazer um teste depender da sessão de outro. Contextos isolados precisam ser descartados quando terminarem de ser usados.

## Como verificar
Inspecione o cookie jar antes e depois de uma resposta de API e compare o comportamento com uma instância isolada criada para o mesmo endpoint.

## Conexões
- [[playwright-download-save-context]] — Veja também: Playwright Test: persistir downloads antes de fechar o contexto.
- [[playwright-test-step-relatorio]] — Veja também: Playwright Test: steps nomeados para tornar falhas legíveis.

## Fontes
- [Playwright — APIRequestContext](https://playwright.dev/docs/api/class-apirequestcontext) — contextos de request associados ao browser, isolamento e jar de cookies; consultado em 2026-10-02.
- [Playwright — API testing](https://playwright.dev/docs/api-testing) — APIRequestContext para setup e pós-condições em testes de browser; consultado em 2026-10-02.
