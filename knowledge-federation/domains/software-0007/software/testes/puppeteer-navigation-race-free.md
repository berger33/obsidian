---
id: software.testes.tranche15.000857
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
fontes: ["https://pptr.dev/api/puppeteer.page", "https://pptr.dev/guides/locators"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Puppeteer: evitar corrida entre ação e navegação

## Em uma frase
Uma ação que dispara navegação deve ser aguardada em conjunto com a espera pelo resultado, para que o observador exista antes de o evento acontecer.

## Por que importa
Esperar a navegação somente depois do clique perde o evento em páginas rápidas e produz falha intermitente que não corresponde a nenhum defeito do produto.

## Como funciona
Combine a promessa de espera e a ação no mesmo `Promise.all`, ou aguarde uma condição posterior observável, como um seletor estável da página seguinte.

## Exemplo
`const [resposta] = await Promise.all([page.waitForNavigation(), page.click('a#next')]);` garante o listener registrado antes de o clique ser processado.

## Limites e trade-offs
Aplicações de página única podem não emitir o evento clássico de navegação, e nesse caso a condição correta é uma mudança de URL ou um seletor da nova visão.

## Como verificar
Repita o fluxo com rede rápida e lenta para verificar a ausência de corrida e simule uma transição sem recarregamento para validar a condição alternativa.

## Conexões
- [[puppeteer-headless-modes]] — Veja também: Puppeteer: distinguir os modos headless.
- [[puppeteer-screenshots-artifacts]] — Veja também: Puppeteer: capturar evidências com screenshot.

## Fontes
- [Puppeteer — Page API](https://pptr.dev/api/puppeteer.page) — navegação, seleção de elementos, avaliação na página e eventos; consultado em 2026-10-02.
- [Puppeteer — Locators](https://pptr.dev/guides/locators) — locators com espera automática por elemento e por ação; consultado em 2026-10-02.
