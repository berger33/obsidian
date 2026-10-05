---
id: software.criacao_ia.tranche05.000441
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
fontes: ["https://developers.openai.com/api/docs/guides/realtime-vad", "https://developers.openai.com/api/docs/guides/realtime-conversations"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# OpenAI Realtime: configurar server_vad ou semantic_vad como política de turnos

## Em uma frase
`turn_detection` configura como a API identifica o fim do áudio do usuário; sessões compatíveis usam `server_vad` por padrão e também oferecem `semantic_vad`.

## Por que importa
A decisão de turno afeta latência, cortes de fala e o momento em que uma resposta automática começa, então o default precisa ser uma escolha deliberada do produto.

## Como funciona
Use `session.update` em `session.audio.input.turn_detection`; `server_vad` divide por silêncio e aceita parâmetros de limiar e duração, enquanto `semantic_vad` estima se a pessoa concluiu a frase. `create_response` e `interrupt_response` só se aplicam a conversas speech-to-speech.

## Exemplo
Um assistente em ambiente ruidoso mede falsos inícios com `server_vad` e compara `semantic_vad` em frases que têm pausas naturais antes de escolher uma política para produção.

## Limites e trade-offs
Disponibilidade e default dependem do tipo de sessão e modelo; algumas sessões de transcrição exigem `turn_detection` omitido ou nulo e não aceitam os modos de VAD.

## Como verificar
Teste ruído, pausas, interrupções e transcrição em cada modelo usado; registre `speech_started` e `speech_stopped` e valide que a resposta não é criada em sessões de transcrição incompatíveis.

## Conexões
- [[openai-realtime-push-to-talk-sem-vad]] — OpenAI Realtime: implementar push-to-talk com buffer, commit e response.create.

## Fontes
- [OpenAI Realtime — Voice activity detection](https://developers.openai.com/api/docs/guides/realtime-vad) — Descreve modos server_vad e semantic_vad, default por sessão e campos conversation-only. Consulta: 2026-10-04.
- [OpenAI Realtime — Managing conversations](https://developers.openai.com/api/docs/guides/realtime-conversations) — Explica o estado da sessão e a configuração de eventos do fluxo conversacional. Consulta: 2026-10-04.
