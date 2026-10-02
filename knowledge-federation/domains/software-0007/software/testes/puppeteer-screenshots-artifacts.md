---
id: software.testes.tranche15.000858
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
fontes: ["https://pptr.dev/api/puppeteer.page", "https://pptr.dev/api/puppeteer.launchoptions"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Puppeteer: capturar evidências com screenshot

## Em uma frase
`page.screenshot()` grava imagem da viewport, da página inteira ou de uma região delimitada, servindo como evidência de falha e insumo de comparação visual.

## Por que importa
Uma captura só ajuda se o momento e o enquadramento forem reproduzíveis; imagens tiradas durante animações ou carregamento pendente viram ruído no diagnóstico.

## Como funciona
Capture depois de uma condição estável, escolha página inteira ou recorte conforme o objetivo e padronize viewport e densidade de pixels entre execuções.

## Exemplo
`await page.screenshot({ path: 'evidencias/checkout.png', fullPage: true });` registra a confirmação do pedido após o seletor de sucesso aparecer.

## Limites e trade-offs
Páginas longas produzem arquivos pesados e conteúdo animado gera diferenças falsas; a captura também não substitui a asserção que define o resultado esperado.

## Como verificar
Gere duas capturas do mesmo estado e compare bytes ou um diff visual; qualquer diferença deve ser explicada por animação, dado variável ou carregamento pendente.

## Conexões
- [[puppeteer-navigation-race-free]] — Veja também: Puppeteer: evitar corrida entre ação e navegação.
- [[puppeteer-browser-context-isolation]] — Veja também: Puppeteer: isolar estado com contexto de navegador.

## Fontes
- [Puppeteer — Page API](https://pptr.dev/api/puppeteer.page) — navegação, seleção de elementos, avaliação na página e eventos; consultado em 2026-10-02.
- [Puppeteer — Launch options](https://pptr.dev/api/puppeteer.launchoptions) — opções de lançamento, headless, protocolo, produto e argumentos; consultado em 2026-10-02.
