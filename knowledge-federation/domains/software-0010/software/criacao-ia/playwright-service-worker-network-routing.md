---
id: software.criacao_ia.tranche03.000274
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-03.md"
fontes: ["https://playwright.dev/docs/service-workers", "https://playwright.dev/docs/api/class-browsercontext"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Playwright: service workers mudam visibilidade de network routing

## Em uma frase
Requests controladas ou interceptadas por Service Workers não se comportam como requests comuns da página para routing e eventos.

## Por que importa
Bloquear Service Workers pode simplificar mocks, mas remove o componente que define comportamento offline e cache do produto. Em contrapartida, deixar workers ativos pode fazer um request escapar do handler esperado ou gerar eventos associados ao worker, não a uma frame.

## Como funciona
A documentação indica que `browserContext.route()` não intercepta requests interceptadas por Service Worker e recomenda `serviceWorkers: 'block'` quando a intenção é interceptação geral. Se o worker precisa ser testado, mantenha-o ativo, escute eventos de contexto, identifique `request.serviceWorker()` e considere que `request.frame()` pode lançar para esse request.

## Exemplo
Um teste de fallback offline habilita Service Worker, aguarda sua ativação e verifica resposta cacheada. Um teste independente de mock REST bloqueia workers para testar a página sem depender do código de cache, deixando explícito que o comportamento validado é diferente.

## Limites e trade-offs
Documentação atual declara suporte de Service Workers apenas em browsers baseados em Chromium. Desativá-los melhora previsibilidade, mas muda o comportamento do app se o worker fizer parte do caminho de produção.

## Como verificar
Execute a mesma request com worker permitido e bloqueado, compare eventos de page e context e confirme se `fromServiceWorker()` é verdadeiro. Teste fluxo offline e de atualização do cache no browser alvo.

## Conexões
- [[playwright-route-fallback-versus-continue]] — Playwright Route: preservar a cadeia com fallback.
- [[playwright-trace-retencao-e-dados-de-debug]] — Playwright Trace: coletar diagnóstico sem expor dados de teste.

## Fontes
- [Playwright — Service Workers](https://playwright.dev/docs/service-workers) — documenta requests de worker, eventos de contexto, route e restrição de browser Consulta: 2026-10-04.
- [Playwright — BrowserContext API](https://playwright.dev/docs/api/class-browsercontext) — explica limitação de route para requests interceptadas por Service Worker Consulta: 2026-10-04.
