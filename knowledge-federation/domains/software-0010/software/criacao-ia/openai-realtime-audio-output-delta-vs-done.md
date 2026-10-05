---
id: software.criacao_ia.tranche05.000445
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
fontes: ["https://developers.openai.com/api/docs/guides/realtime-conversations", "https://developers.openai.com/api/reference/resources/realtime/server-events"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# OpenAI Realtime: obter bytes de áudio em output_audio.delta, não em response.done

## Em uma frase
Em WebSocket, os bytes de áudio são enviados em `response.output_audio.delta`; eventos `response.output_audio.done` e `response.done` não carregam esses bytes.

## Por que importa
Um cliente que espera encontrar áudio apenas no evento terminal consegue detectar conclusão, mas não tem material para tocar ou persistir.

## Como funciona
Decodifique cada delta Base64 e encaminhe os bytes para reprodução ou armazenamento; use eventos done para ciclo de vida e texto associado, não como pacote contendo toda a forma de onda.

## Exemplo
Um serviço de voz agrega deltas em ordem para criar o áudio de uma resposta e marca o arquivo completo somente depois do evento terminal correspondente.

## Limites e trade-offs
A documentação recomenda WebRTC para áudio de saída em clientes como browser; via WebSocket, a aplicação assume responsabilidade por buffer, ordem e reprodução.

## Como verificar
Capture uma resposta curta, confirme chegada de um ou mais deltas e confira que o handler dos eventos done não tenta decodificar bytes inexistentes.

## Conexões
- [[openai-realtime-transcricao-item-id]] — OpenAI Realtime transcription: correlacionar deltas e transcrições finais por item_id.
- [[openai-realtime-interromper-audio-e-truncate]] — OpenAI Realtime: sincronizar áudio interrompido com conversation.item.truncate.

## Fontes
- [OpenAI Realtime — Managing conversations](https://developers.openai.com/api/docs/guides/realtime-conversations) — Especifica deltas Base64 e esclarece que eventos done não contêm os bytes de áudio. Consulta: 2026-10-04.
- [OpenAI Realtime — Server events](https://developers.openai.com/api/reference/resources/realtime/server-events) — Define os campos dos eventos de saída de áudio, inclusive delta e identificadores. Consulta: 2026-10-04.
