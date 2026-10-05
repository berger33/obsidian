---
id: software.criacao_ia.tranche05.000444
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
fontes: ["https://developers.openai.com/api/docs/guides/realtime-transcription", "https://developers.openai.com/api/reference/resources/realtime/server-events"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# OpenAI Realtime transcription: correlacionar deltas e transcrições finais por item_id

## Em uma frase
Eventos de transcrição incremental e final devem ser associados ao item de áudio por `item_id`, pois conclusões de turnos diferentes podem chegar fora de ordem.

## Por que importa
Uma interface com vários turnos ou buffers simultâneos pode exibir texto final na linha errada se usar somente a ordem de chegada.

## Como funciona
Consuma eventos `.delta` para atualização temporária e `.completed` para o texto final; guarde `item_id` junto ao buffer de cada mensagem e não presuma ordenação global entre turnos.

## Exemplo
Um painel cria uma linha provisória para cada item de áudio, anexa deltas pela chave `item_id` e substitui o rascunho pelo campo `transcript` na conclusão.

## Limites e trade-offs
Os eventos de transcrição pertencem ao fluxo e modelo de transcrição configurados; eles não oferecem necessariamente timestamps por palavra, rótulos de falante ou scores de confiança.

## Como verificar
Envie dois turnos com finalizações próximas, embaralhe a ordem de evento no teste do consumidor e confirme que cada texto fica associado ao item correto.

## Conexões
- [[openai-realtime-append-audio-chunks-base64]] — OpenAI Realtime: transmitir input_audio_buffer.append em chunks Base64 limitados.
- [[openai-realtime-audio-output-delta-vs-done]] — OpenAI Realtime: obter bytes de áudio em output_audio.delta, não em response.done.

## Fontes
- [OpenAI Realtime — Realtime transcription](https://developers.openai.com/api/docs/guides/realtime-transcription) — Define delta, completed, item_id e ressalva que conclusões entre turnos podem não ser ordenadas. Consulta: 2026-10-04.
- [OpenAI Realtime — Server events](https://developers.openai.com/api/reference/resources/realtime/server-events) — Descreve campos de eventos de áudio e identificadores dos itens da conversa. Consulta: 2026-10-04.
