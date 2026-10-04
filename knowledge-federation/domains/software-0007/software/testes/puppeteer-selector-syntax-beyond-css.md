---
id: software.testes.tranche15.000852
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

# Puppeteer: usar seletores além do CSS

## Em uma frase
Além de seletores CSS, o Puppeteer aceita extensões como `::-p-text()`, `::-p-aria()` e o combinador `>>>` para atravessar shadow roots abertos.

## Por que importa
Seletores presos a classes e posição quebram com refatorações de estilo, enquanto texto e papel acessível aproximam a busca da forma como a pessoa usuária percebe a tela.

## Como funciona
Combine um seletor estrutural estável com pseudo-seletores de texto ou ARIA para expressar intenção, recorrendo a `>>>` somente quando o alvo estiver encapsulado em shadow DOM aberto.

## Exemplo
`await page.locator('::-p-text(Entrar)').click();` procura pelo texto visível do controle, e `card >>> .price` alcança nó dentro de um componente encapsulado.

## Limites e trade-offs
Textos mudam com idioma e revisão de conteúdo, e pseudo-seletores têm regras próprias de casamento, então eles não substituem identificadores testáveis e estáveis.

## Como verificar
Duplique o texto na tela ou alterne o idioma e confira qual elemento foi escolhido; refine o seletor para eliminar ambiguidade antes de mantê-lo.

## Conexões
- [[puppeteer-page-evaluate-serialization]] — Veja também: Puppeteer: avaliar código no contexto da página.
- [[puppeteer-network-interception-cooperative]] — Veja também: Puppeteer: resolver interceptação de rede de forma cooperativa.

## Fontes
- [Puppeteer — Locators](https://pptr.dev/guides/locators) — locators com espera automática por elemento e por ação; consultado em 2026-10-02.
- [Puppeteer — Page API](https://pptr.dev/api/puppeteer.page) — navegação, seleção de elementos, avaliação na página e eventos; consultado em 2026-10-02.
