---
id: software.testes.tranche15.000855
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
fontes: ["https://pptr.dev/webdriver-bidi", "https://pptr.dev/api/puppeteer.launchoptions"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Puppeteer: escolher entre CDP e WebDriver BiDi

## Em uma frase
O Puppeteer controla navegadores por DevTools Protocol ou por WebDriver BiDi, com BiDi como padrão no Firefox e CDP ainda como padrão no Chrome.

## Por que importa
Nem toda capacidade implementada em CDP tem equivalente em BiDi; escolher um protocolo sem conferir a cobertura produz erro de operação não suportada em vez de comportamento previsível.

## Como funciona
Selecione o protocolo nas opções de lançamento quando a compatibilidade importar e verifique na lista oficial se o recurso utilizado existe no caminho escolhido.

## Exemplo
`puppeteer.launch({ browser: 'chrome', protocol: 'webDriverBiDi' })` força o caminho padronizado no Chrome para exercitar a mesma automação usada no Firefox.

## Limites e trade-offs
O suporte a BiDi cobre um subconjunto em evolução, e a lista muda entre versões; recursos avançados podem exigir CDP ou uma alternativa documentada.

## Como verificar
Rode o mesmo fluxo nos dois protocolos e registre quais operações falham com erro de operação não suportada antes de padronizar a suíte.

## Conexões
- [[puppeteer-request-abort-and-continue]] — Veja também: Puppeteer: concluir toda requisição interceptada.
- [[puppeteer-headless-modes]] — Veja também: Puppeteer: distinguir os modos headless.

## Fontes
- [Puppeteer — WebDriver BiDi support](https://pptr.dev/webdriver-bidi) — protocolos suportados, padrão por navegador e operações incompatíveis; consultado em 2026-10-02.
- [Puppeteer — Launch options](https://pptr.dev/api/puppeteer.launchoptions) — opções de lançamento, headless, protocolo, produto e argumentos; consultado em 2026-10-02.
