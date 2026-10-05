---
id: software.criacao_ia.tranche05.000442
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

# OpenAI Realtime: implementar push-to-talk com buffer, commit e response.create

## Em uma frase
Com `turn_detection: null`, o cliente assume responsabilidade por delimitar o turno, confirmar o buffer e pedir explicitamente a resposta.

## Por que importa
Push-to-talk oferece controle direto ao usuário e permite validar entrada antes de gerar resposta, mas exige mais eventos do que deixar VAD administrar os turnos.

## Como funciona
Desative VAD por `session.update`; siga o fluxo do transporte escolhido. Em WebSocket, grave a entrada com `input_audio_buffer.append`, conclua com `input_audio_buffer.commit` e emita `response.create`; em WebRTC/SIP, limpe `input_audio_buffer` ao iniciar novo turno, confirme o buffer e crie a resposta. O guia trata o evento de limpeza como necessário para o fluxo WebRTC/SIP.

## Exemplo
Num cliente WebRTC push-to-talk, o pressionar limpa o buffer e começa a captura; ao soltar, o cliente confirma o turno com commit e solicita `response.create`. Em WebSocket, a sequência documentada usa os chunks append antes do commit.

## Limites e trade-offs
`commit` adiciona item do usuário, mas por si só não dispara uma resposta; os passos de limpeza diferem entre os exemplos WebSocket e WebRTC/SIP, então não copie a sequência de um transporte para o outro sem conferir o guia.

## Como verificar
Teste WebSocket e WebRTC separadamente: pressionar/soltar sem áudio, turnos consecutivos, cancelamento antes da resposta e reset do buffer; confirme que cada transporte segue sua sequência documentada e não mistura áudio entre turnos.

## Conexões
- [[openai-realtime-vad-configurar-turn-detection]] — OpenAI Realtime: configurar server_vad ou semantic_vad como política de turnos.
- [[openai-realtime-append-audio-chunks-base64]] — OpenAI Realtime: transmitir input_audio_buffer.append em chunks Base64 limitados.

## Fontes
- [OpenAI Realtime — Managing conversations](https://developers.openai.com/api/docs/guides/realtime-conversations) — Lista a sequência manual de clear, append, commit e response.create para VAD desativado. Consulta: 2026-10-04.
- [OpenAI Realtime — Client events](https://developers.openai.com/api/reference/resources/realtime/client-events) — Define eventos cliente para atualização de sessão e controle de buffer e resposta. Consulta: 2026-10-04.
