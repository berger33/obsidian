---
id: software.criacao_ia.tranche05.000459
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-05.md"
fontes: ["https://ai-sdk.dev/docs/ai-sdk-ui/stream-protocol", "https://ai-sdk.dev/docs/ai-sdk-ui/streaming-data"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# AI SDK UI: escolher text stream ou data stream conforme a forma do evento

## Em uma frase
Text streams juntam chunks de texto simples, enquanto data streams usam protocolo SSE de UI para transmitir partes tipadas além do texto.

## Por que importa
Escolher protocolo incompatível faz o cliente descartar ferramentas, metadados ou dados estruturados, ou interpretar eventos JSON como texto visível.

## Como funciona
Use `TextStreamChatTransport` apenas quando precisa de texto básico; use o protocolo de data stream para tool calls, fontes e partes customizadas. Um backend customizado deve enviar o header `x-vercel-ai-ui-message-stream: v1`.

## Exemplo
Um resumo de texto simples retorna chunks plain text; um assistente com tool parts e fontes usa stream de mensagens e envia eventos SSE tipados com o header exigido.

## Limites e trade-offs
Text streams são suportados por hooks específicos, mas não carregam os mesmos tipos de dados de UI; confirme compatibilidade do backend e do transport.

## Como verificar
Execute teste com resposta de texto e outro com parte customizada/tool call; valide parsing, cabeçalho e estado final no cliente escolhido.

## Conexões
- [[ai-sdk-ui-data-parts-persistentes-transient]] — AI SDK UI: separar data parts persistentes de eventos transient de interface.
- [[ai-sdk-ui-status-erro-e-mensagem-publica]] — AI SDK UI: conduzir controles por status e mostrar erro genérico ao usuário.

## Fontes
- [AI SDK UI — Stream Protocols](https://ai-sdk.dev/docs/ai-sdk-ui/stream-protocol) — Compara protocolos de texto e dados e exige header v1 para backend customizado. Consulta: 2026-10-04.
- [AI SDK UI — Streaming Custom Data](https://ai-sdk.dev/docs/ai-sdk-ui/streaming-data) — Mostra entrega de data parts por SSE e uso no array de mensagens. Consulta: 2026-10-04.
