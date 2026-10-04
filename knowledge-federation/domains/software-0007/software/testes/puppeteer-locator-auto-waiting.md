---
id: software.testes.tranche15.000850
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://pptr.dev/guides/locators", "https://pptr.dev/api/puppeteer.page"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Puppeteer: usar locator para esperar antes de agir

## Em uma frase
Um locator representa um elemento que pode ainda não existir e só resolve sua localização quando uma ação ou condição é solicitada por meio dele.

## Por que importa
Esperas fixas espalham prazos arbitrários pelo teste e criam corridas quando a interface demora a estabilizar ou responde mais rápido que o previsto.

## Como funciona
Crie o locator com `page.locator()` e encadeie a operação desejada, como `.click()` ou `.wait()`, deixando que a biblioteca aguarde a condição necessária antes de falhar por timeout.

## Exemplo
`await page.locator('button#checkout').click();` aguarda o botão aparecer e ficar clicável antes de disparar o clique, sem `sleep` no teste.

## Limites e trade-offs
A espera automática cobre presença e acionabilidade do elemento, não a intenção de negócio; um alvo visível e errado continua sendo aceito se o seletor for ambíguo.

## Como verificar
Force a página a atrasar a renderização e confirme que a ação espera; remova o elemento e verifique se o timeout aponta o locator usado.

## Conexões
- [[puppeteer-page-evaluate-serialization]] — Veja também: Puppeteer: avaliar código no contexto da página.

## Fontes
- [Puppeteer — Locators](https://pptr.dev/guides/locators) — locators com espera automática por elemento e por ação; consultado em 2026-10-02.
- [Puppeteer — Page API](https://pptr.dev/api/puppeteer.page) — navegação, seleção de elementos, avaliação na página e eventos; consultado em 2026-10-02.
