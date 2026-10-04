---
id: software.criacao_ia.tranche02.000178
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

# Legendas: sincronizar exibição de texto com timestamps por palavra

## Em uma frase
A sincronização precisa de legendas com timestamps de palavras melhora a acessibilidade e a retenção do diálogo.

## Por que importa
Exibir blocos longos de texto antes do tempo correto revela spoilers prematuramente e quebra o ritmo dramático da cena.

## Como funciona
Capture os metadados de alinhamento temporal (*word-level timestamps*) retornados pela API de TTS e atualize as palavras na tela em sincronia com o cursor de reprodução do áudio.

## Exemplo
```json
// Estrutura de timestamps por palavra retornada pela API
{
  "alignment": {
    "characters": ["O", "l", "a", " ", "v", "i", "a", "j", "a", "n", "t", "e"],
    "character_start_times_seconds": [0.0, 0.05, 0.1, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6]
  }
}
```

## Limites e trade-offs
Dessincronizações entre o clock de reprodução do motor e os timestamps da API geram legendas adiantadas ou atrasadas em relação ao som.

## Como verificar
Valide a correspondência temporal reproduzindo o áudio com as legendas destacadas em tempo real na tela de teste de UI.

## Conexões
- [[mixagem-aplicar-audio-ducking-durante-vozes-de-ia]] — Veja também: Mixagem de Som: aplicar audio ducking automático durante falas de IA.
- [[audio-ia-modular-prosodia-e-estabilidade-por-emocao]] — Veja também: Áudio com IA: modular parâmetros de prosódia e estilo por emoção.
- [[audio-ia-extrair-visemas-para-lip-sync-com-rhubarb]] — Conexão temática direta com audio-ia-extrair-visemas-para-lip-sync-com-rhubarb.
- [[documentacao-tornar-resultado-e-verificacao-explicitos]] — Conexão temática direta com documentacao-tornar-resultado-e-verificacao-explicitos.

## Fontes
- [ElevenLabs API Reference — Text to Speech](https://elevenlabs.io/docs/api-reference/text-to-speech) — Especificação oficial de endpoints rest para síntese de voz, timestamps por palavra e controle de prosódia. Consulta: 2026-10-04.
- [FMOD Studio Documentation](https://fmod.com/docs/2.02/studio/welcome-to-fmod-studio.html) — Manual cobrindo roteamento de barramentos de diálogo, efeitos de ambiente, espacialização 3d e sidechain ducking. Consulta: 2026-10-04.
