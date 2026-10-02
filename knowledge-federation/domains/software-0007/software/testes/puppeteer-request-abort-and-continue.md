---
id: software.testes.tranche15.000854
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
fontes: ["https://pptr.dev/guides/network-interception", "https://pptr.dev/api/puppeteer.page"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Puppeteer: concluir toda requisição interceptada

## Em uma frase
Cada requisição capturada precisa terminar em `continue`, `abort` ou `respond`; enquanto isso não acontece, a navegação permanece pendente aguardando a decisão.

## Por que importa
Bloquear recursos pesados acelera a suíte, mas esquecer um tipo de recurso deixa a página travada e gera timeout que não indica a causa real do problema.

## Como funciona
Trate os casos por `resourceType()` ou padrão de URL e mantenha um caminho padrão que libere a requisição; para simular backend sem rede, responda com status e corpo diretamente.

## Exemplo
Bloquear fontes pode ser feito com `if (req.url().endsWith('.woff2')) return req.abort(); req.continue();`, preservando scripts e imagens necessários ao fluxo.

## Limites e trade-offs
Abortar recursos altera o comportamento da página; pular scripts pode esconder defeitos reais quando o fluxo sob teste depende justamente daquele carregamento.

## Como verificar
Aborte um recurso específico e confirme que a página continua carregando, que o log registra a falha da requisição e que nenhuma chamada ficou pendente.

## Conexões
- [[puppeteer-network-interception-cooperative]] — Veja também: Puppeteer: resolver interceptação de rede de forma cooperativa.
- [[puppeteer-bidi-vs-cdp]] — Veja também: Puppeteer: escolher entre CDP e WebDriver BiDi.

## Fontes
- [Puppeteer — Network interception](https://pptr.dev/guides/network-interception) — interceptação de requisições, resolução cooperativa e prioridades; consultado em 2026-10-02.
- [Puppeteer — Page API](https://pptr.dev/api/puppeteer.page) — navegação, seleção de elementos, avaliação na página e eventos; consultado em 2026-10-02.
