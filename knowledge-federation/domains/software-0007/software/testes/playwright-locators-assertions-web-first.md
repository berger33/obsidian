---
id: software.testes.tranche08.000159
tipo: tecnica
dominio: software
subdominio: testes
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-08.md"
fontes: ["https://playwright.dev/docs/locators", "https://playwright.dev/docs/test-assertions"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Playwright: locators resilientes e assertions web-first

## Em uma frase
Prefira locators por papel e nome acessível e assertions que aguardam a condição em vez de ler o DOM uma única vez.

## Por que importa
Seletores semânticos refletem melhor a interface usada por pessoas e diminuem dependência de classes ou estrutura interna que muda com refatorações.

## Como funciona
Localize pelo papel, rótulo ou texto visível; faça assertion sobre estado observável usando matcher web-first. Evite sleeps fixos e leituras imediatas antes de a UI estabilizar.

## Exemplo
Após submeter um formulário, aguarde que o alerta com nome acessível indique sucesso em vez de consultar uma classe CSS ou comparar o HTML completo.

## Limites e trade-offs
Locators semânticos dependem de acessibilidade correta; não tornam uma assertion útil se ela verifica conteúdo errado ou se o cenário carece de isolamento.

## Como verificar
Renomeie uma classe de apresentação e confirme que o teste continua; remova temporariamente o rótulo acessível e veja se a falha denuncia o problema de UX.

## Conexões
- [[rtl-consultas-prioridade-role-name]] — Veja também: Testing Library: priorizar consultas por papel e nome.
- [[rtl-async-findby-waitfor-condicao]] — Veja também: Testing Library: aguardar estado assíncrono pela condição.

## Fontes
- [Playwright — Locators](https://playwright.dev/docs/locators) — locators resilientes e localização por semântica; consultado em 2026-10-02.
- [Playwright — Assertions](https://playwright.dev/docs/test-assertions) — expect web-first e estabilização de assertions; consultado em 2026-10-02.
