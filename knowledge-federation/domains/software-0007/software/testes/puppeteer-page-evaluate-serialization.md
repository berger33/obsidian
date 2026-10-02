---
id: software.testes.tranche15.000851
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

# Puppeteer: avaliar código no contexto da página

## Em uma frase
`page.evaluate()` executa uma função dentro do navegador e devolve apenas valores serializáveis para o processo Node que controla a automação.

## Por que importa
Confundir contexto Node com contexto da página produz `undefined` silencioso ou erro de serialização que parece defeito do navegador, mas é efeito da fronteira entre processos.

## Como funciona
Passe uma função autocontida e argumentos serializáveis; para elementos e objetos vivos, obtenha um handle com `evaluateHandle` ou `$` e opere sobre ele em vez de devolver o objeto.

## Exemplo
`const total = await page.evaluate(() => document.querySelectorAll('li').length);` devolve um número; tentar devolver a NodeList crua não atravessa a fronteira.

## Limites e trade-offs
A função roda no navegador e não enxerga variáveis do processo Node; apenas os argumentos passados explicitamente ficam disponíveis no escopo remoto.

## Como verificar
Avalie uma função que devolve `document.body` e observe a falha; troque por um handle e confirme que cliques e leituras funcionam pelo handle.

## Conexões
- [[puppeteer-locator-auto-waiting]] — Veja também: Puppeteer: usar locator para esperar antes de agir.
- [[puppeteer-selector-syntax-beyond-css]] — Veja também: Puppeteer: usar seletores além do CSS.

## Fontes
- [Puppeteer — Page API](https://pptr.dev/api/puppeteer.page) — navegação, seleção de elementos, avaliação na página e eventos; consultado em 2026-10-02.
- [Puppeteer — Locators](https://pptr.dev/guides/locators) — locators com espera automática por elemento e por ação; consultado em 2026-10-02.
