---
id: software.criacao_ia.tranche05.000446
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
fontes: ["https://developers.openai.com/api/docs/guides/realtime-conversations", "https://developers.openai.com/api/reference/resources/realtime/client-events"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# OpenAI Realtime: sincronizar áudio interrompido com conversation.item.truncate

## Em uma frase
Quando o usuário interrompe a fala gerada em WebSocket, o cliente para a reprodução e envia truncamento para remover da conversa o áudio que não foi ouvido.

## Por que importa
Sem sincronizar o playback local com o estado do servidor, o histórico pode conter palavras que o usuário nunca escutou e contaminar o turno seguinte.

## Como funciona
Ao detectar início da fala, interrompa o áudio em reprodução, meça quanto do item foi tocado e envie `conversation.item.truncate` com `item_id`, índice de conteúdo e `audio_end_ms`. WebRTC gerencia seu próprio buffer de saída.

## Exemplo
Um player WebSocket observa `speech_started`, pausa imediatamente, calcula o milissegundo já ouvido e trunca o item de saída para esse ponto antes de continuar o diálogo.

## Limites e trade-offs
A documentação ressalta que o texto de transcrição não pode ser alinhado perfeitamente ao áudio truncado; não mostre um transcript que afirma ser uma transcrição exata do trecho ouvido.

## Como verificar
Interrompa uma fala longa em pontos diferentes, compare playback e histórico do servidor e confirme que WebRTC e WebSocket usam tratamento compatível com seus buffers.

## Conexões
- [[openai-realtime-audio-output-delta-vs-done]] — OpenAI Realtime: obter bytes de áudio em output_audio.delta, não em response.done.
- [[openai-realtime-function-call-execucao-aplicacao]] — OpenAI Realtime: executar function calls no aplicativo e devolver function_call_output.

## Fontes
- [OpenAI Realtime — Managing conversations](https://developers.openai.com/api/docs/guides/realtime-conversations) — Descreve cancelamento, interrupção e truncamento distinto para WebRTC/SIP e WebSocket. Consulta: 2026-10-04.
- [OpenAI Realtime — Client events](https://developers.openai.com/api/reference/resources/realtime/client-events) — Define o evento cliente usado para truncar áudio de um item da conversa. Consulta: 2026-10-04.
