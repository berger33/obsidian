---
id: software.testes.tranche15.000921
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
data_revisao_ia: "2026-10-02"
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://mswjs.io/api/setup-server/listen", "https://mswjs.io/guides/integrations/node"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# MSW: falhar ou avisar para frames de rede sem handler

## Em uma frase
`server.listen` aceita `onUnhandledFrame` para tratar frames sem handler, incluindo requests HTTP e conexões WebSocket.

## Por que importa
A estratégia padrão `warn` avisa e deixa o frame prosseguir; `error` registra erro e interrompe o frame, enquanto `bypass` segue sem aviso.

## Como funciona
Uma callback personalizada recebe o protocolo e o frame para uma decisão específica.

## Exemplo
Use `server.listen({ onUnhandledFrame: "error" })` numa suíte fechada em que todo tráfego esperado tenha handler e acrescente exceções estreitas para assets se necessário.

## Limites e trade-offs
Uma callback personalizada substitui o comportamento padrão que ignora assets comuns; se isso importar, use `isCommonAssetRequest()` explicitamente e considere os protocolos HTTP e WebSocket.

## Como verificar
Em um teste de laboratório, envie uma URL sem handler e confirme a estratégia escolhida; faça o mesmo com frame permitido para validar a exceção sem abrir acesso geral.

## Conexões
- [[msw-setup-server-nao-cria-servidor-http]] — Veja também: MSW em Node.js: entender o que setupServer realmente intercepta.
- [[msw-use-como-override-de-comportamento]] — Veja também: MSW: usar server.use para acrescentar overrides locais a um cenário.

## Fontes
- [MSW — listen()](https://mswjs.io/api/setup-server/listen) — início da interceptação e estratégias para frames sem handler; consultado em 2026-10-02.
- [MSW — Node.js integration](https://mswjs.io/guides/integrations/node) — setupServer e ciclo listen/reset/close em testes; consultado em 2026-10-02.
