---
id: software.criacao_ia.tranche02.000179
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-02.md"
fontes: ["https://elevenlabs.io/docs/api-reference/text-to-speech", "https://fmod.com/docs/2.02/studio/welcome-to-fmod-studio.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Áudio com IA: modular parâmetros de prosódia e estilo por emoção

## Em uma frase
A modulação dinâmica de parâmetros de estabilidade e estilo vocal reflete o estado emocional do NPC em situações de calma ou perigo.

## Por que importa
Personagens que falam com o mesmo tom monótono durante uma batalha e em um momento de descanso quebram a imersão narrativa.

## Como funciona
Ajuste os parâmetros `stability`, `similarity_boost` e `style` na requisição de síntese de acordo com a variável de estresse ou agressividade da máquina de estados do NPC.

## Exemplo
```json
{
  "voice_settings": {
    "stability": 0.35,
    "similarity_boost": 0.80,
    "style": 0.65,
    "use_speaker_boost": true
  }
}
```

## Limites e trade-offs
Valores de estabilidade excessivamente baixos (`< 0.2`) podem gerar falhas de pronúncia, ruídos na voz ou risos involuntários do modelo de fala.

## Como verificar
Realize testes comparativos de frases com diferentes níveis de estresse e assegure que a voz permaneça inteligível em todas as configurações.

## Conexões
- [[legendas-sincronizar-texto-com-timestamps-de-palavras]] — Veja também: Legendas: sincronizar exibição de texto com timestamps por palavra.
- [[audio-ia-prover-linhas-de-dialogo-de-fallback]] — Veja também: Resiliência de Áudio: prover falas pré-gravadas como fallback de rede.
- [[audio-ia-sintetizar-falas-dinamicas-de-npcs]] — Conexão temática direta com audio-ia-sintetizar-falas-dinamicas-de-npcs.
- [[godot-estruturar-maquina-de-estados-hierarquica]] — Conexão temática direta com godot-estruturar-maquina-de-estados-hierarquica.

## Fontes
- [ElevenLabs API Reference — Text to Speech](https://elevenlabs.io/docs/api-reference/text-to-speech) — Especificação oficial de endpoints rest para síntese de voz, timestamps por palavra e controle de prosódia. Consulta: 2026-10-04.
- [FMOD Studio Documentation](https://fmod.com/docs/2.02/studio/welcome-to-fmod-studio.html) — Manual cobrindo roteamento de barramentos de diálogo, efeitos de ambiente, espacialização 3d e sidechain ducking. Consulta: 2026-10-04.
