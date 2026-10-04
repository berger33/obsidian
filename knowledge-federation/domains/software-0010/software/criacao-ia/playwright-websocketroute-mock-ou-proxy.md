---
id: software.criacao_ia.tranche03.000272
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
fontes: ["https://playwright.dev/docs/api/class-websocketroute", "https://playwright.dev/docs/api/class-browsercontext"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Playwright WebSocketRoute: escolher mock completo ou interceptação

## Em uma frase
WebSocket route não conecta ao servidor automaticamente; sem `connectToServer()` ela pode simular toda a conversação dentro do teste.

## Por que importa
Mocks completos isolam cliente de sistema remoto, enquanto interceptação preserva protocolo e modifica mensagens em trânsito. Selecionar o modo errado pode criar um teste que nunca exercita handshake ou estado real do serviço.

## Como funciona
Registre `page.routeWebSocket()` ou `browserContext.routeWebSocket()` antes de a aplicação abrir a conexão. Para mock, responda com `send()` e omita `connectToServer()`. Para interceptação, conecte ao servidor e transforme, bloqueie ou encaminhe mensagens. Depois de registrar `onMessage()` numa direção, a aplicação assume a responsabilidade pelo encaminhamento daquela direção.

## Exemplo
Um teste unitário simula mensagens `subscribe` e `update` sem rede. Um teste de integração chama `connectToServer()`, reescreve somente uma mensagem de pedido e deixa outras passarem, verificando no servidor de teste que a conexão foi realmente estabelecida.

## Limites e trade-offs
O handler WebSocket pode afetar somente conexões abertas depois da rota ser registrada. O mock não valida rede, negociação de protocolo, autenticação ou reconexão real; handler de mensagens muda o encaminhamento default.

## Como verificar
Teste mock sem servidor e proxy com servidor local, crie conexão antes e depois do registro da rota e conte mensagens em ambas direções. Confirme fechamento e códigos de close em caminhos de erro.

## Conexões
- [[playwright-clock-install-order]] — Playwright Clock: instalar relógio antes de APIs temporais.
- [[playwright-route-fallback-versus-continue]] — Playwright Route: preservar a cadeia com fallback.

## Fontes
- [Playwright — WebSocketRoute](https://playwright.dev/docs/api/class-websocketroute) — define mock default, `connectToServer` e encaminhamento de mensagens Consulta: 2026-10-04.
- [Playwright — BrowserContext API](https://playwright.dev/docs/api/class-browsercontext) — documenta nível de contexto para instalar rotas e gerenciar conexões de páginas Consulta: 2026-10-04.
