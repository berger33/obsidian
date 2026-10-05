---
id: software.criacao_ia.tranche05.000458
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
fontes: ["https://ai-sdk.dev/docs/ai-sdk-ui/streaming-data", "https://ai-sdk.dev/docs/ai-sdk-ui/chatbot-message-persistence"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# AI SDK UI: separar data parts persistentes de eventos transient de interface

## Em uma frase
Uma parte `data-*` normal aparece em `message.parts` e pode ser persistida, enquanto uma parte marcada `transient` só é exposta durante o stream via `onData`.

## Por que importa
Status temporário, como “processando”, não deve reaparecer como conteúdo permanente se a aplicação pretende armazenar apenas fatos ligados à mensagem.

## Como funciona
Defina schemas de dados de UI, escreva data parts estáveis com ID para reconciliação e marque notificações efêmeras como transient; processe estas últimas no callback `onData` do hook.

## Exemplo
O servidor mantém `weather-1` em `message.parts`, atualiza o mesmo ID de loading para success e envia toast de conclusão como notification transient.

## Limites e trade-offs
A parte transient não existe no histórico `parts`; se for necessária para recuperação ou auditoria, persista-a por um canal de domínio separado.

## Como verificar
Inspecione o array de mensagens após stream, confirme reconciliação pelo mesmo ID e verifique que notificação transient chega em `onData`, mas não ao salvar UIMessage.

## Conexões
- [[ai-sdk-ui-stop-nao-cancela-geracao-retomavel]] — AI SDK UI: em streams retomáveis, distinguir stop local de cancelamento server-side.
- [[ai-sdk-ui-escolher-text-stream-ou-data-stream]] — AI SDK UI: escolher text stream ou data stream conforme a forma do evento.

## Fontes
- [AI SDK UI — Streaming Custom Data](https://ai-sdk.dev/docs/ai-sdk-ui/streaming-data) — Define partes persistentes, transient, callback onData e reconciliação por ID. Consulta: 2026-10-04.
- [AI SDK UI — Chatbot Message Persistence](https://ai-sdk.dev/docs/ai-sdk-ui/chatbot-message-persistence) — Recomenda validar data parts e metadata quando mensagens são carregadas do armazenamento. Consulta: 2026-10-04.
