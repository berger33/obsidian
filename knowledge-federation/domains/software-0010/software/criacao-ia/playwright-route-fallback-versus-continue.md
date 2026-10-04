---
id: software.criacao_ia.tranche03.000273
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
fontes: ["https://playwright.dev/docs/api/class-route", "https://playwright.dev/docs/api/class-browsercontext#browser-context-route"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Playwright Route: preservar a cadeia com fallback

## Em uma frase
`route.continue()` envia imediatamente ao network e encerra a cadeia de handlers; `route.fallback()` permite que outro handler correspondente decida depois.

## Por que importa
Camadas de roteamento frequentemente separam bloqueio de analytics, fixture específica e lógica compartilhada. Uma chamada prematura a continue impede que handlers seguintes substituam ou rejeitem a request, enquanto fallback preserva composição intencional.

## Como funciona
Quando várias rotas correspondem ao mesmo padrão, os handlers rodam na ordem oposta à de registro: a última registrada executa primeiro. Use fallback para passar controle ao próximo handler, opcionalmente com overrides; use continue apenas quando a request deve chegar à rede sem consultar handlers restantes. Route de página também tem precedência própria sobre route do browser context.

## Exemplo
Um handler específico modifica um endpoint de fixture e chama fallback para permitir que camada de auditoria valide método. Se a request não se aplica ao fixture, a camada pode continuar para rede somente quando chegar ao handler final.

## Limites e trade-offs
Headers proibidos podem não ser substituídos por continue, e redirects carregam alguns overrides de modo diferente. Cadeia de rotas deve evitar loops e garantir que todo caminho termina em fulfill, abort, continue ou fallback.

## Como verificar
Registre handlers com nomes e ordem, gere requests cobertas e não cobertas, e confirme sequência em logs. Teste redirect, override de header e uma rota que intencionalmente interrompe a cadeia.

## Conexões
- [[playwright-websocketroute-mock-ou-proxy]] — Playwright WebSocketRoute: escolher mock completo ou interceptação.
- [[playwright-service-worker-network-routing]] — Playwright: service workers mudam visibilidade de network routing.

## Fontes
- [Playwright — Route API](https://playwright.dev/docs/api/class-route) — especifica continue imediato, fallback e ordem inversa de handlers Consulta: 2026-10-04.
- [Playwright — BrowserContext.route](https://playwright.dev/docs/api/class-browsercontext#browser-context-route) — define precedência entre route de page/context e efeito de habilitar roteamento Consulta: 2026-10-04.
