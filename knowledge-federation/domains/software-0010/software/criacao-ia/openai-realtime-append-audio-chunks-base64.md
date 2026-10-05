---
id: software.criacao_ia.tranche05.000443
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

# OpenAI Realtime: transmitir input_audio_buffer.append em chunks Base64 limitados

## Em uma frase
A entrada de áudio por WebSocket pode ser enviada com `input_audio_buffer.append`, cujo campo de áudio contém bytes codificados em Base64 e tem limite por chunk.

## Por que importa
Codificação e tamanho do payload são parte do protocolo; buffers grandes sem divisão elevam memória, latência e risco de rejeição da mensagem.

## Como funciona
Converta áudio para o formato configurado na sessão, codifique cada trecho em Base64 e envie eventos append sucessivos; a documentação limita cada chunk a 15 MB. Faça commit no fim quando a política de turno exigir.

## Exemplo
Um relé de microfone lê blocos PCM16, codifica cada bloco separadamente e só envia o evento de commit quando a captura do usuário termina.

## Limites e trade-offs
Base64 aumenta o volume transportado e o guia trata append como gravação em buffer temporário; não interprete o envio de um chunk como confirmação de transcrição ou de resposta.

## Como verificar
Teste áudio curto e longo, confirme formato e taxa de amostragem configurados, mantenha cada evento abaixo do limite e valide o resultado após commit.

## Conexões
- [[openai-realtime-push-to-talk-sem-vad]] — OpenAI Realtime: implementar push-to-talk com buffer, commit e response.create.
- [[openai-realtime-transcricao-item-id]] — OpenAI Realtime transcription: correlacionar deltas e transcrições finais por item_id.

## Fontes
- [OpenAI Realtime — Managing conversations](https://developers.openai.com/api/docs/guides/realtime-conversations) — Descreve chunks Base64, limite de tamanho e fluxo de append por WebSocket. Consulta: 2026-10-04.
- [OpenAI Realtime — Client events](https://developers.openai.com/api/reference/resources/realtime/client-events) — Especifica os eventos cliente usados para escrever e confirmar o buffer de áudio. Consulta: 2026-10-04.
