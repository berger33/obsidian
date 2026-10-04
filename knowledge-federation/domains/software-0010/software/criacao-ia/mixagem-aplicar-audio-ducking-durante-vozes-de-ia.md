---
id: software.criacao_ia.tranche02.000177
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

# Mixagem de Som: aplicar audio ducking automático durante falas de IA

## Em uma frase
O audio ducking reduz automaticamente o volume da trilha musical e dos efeitos sonoros durante a reprodução de diálogos importantes.

## Por que importa
Música alta ou efeitos estridentes de combate mascaram a voz do NPC e prejudicam a compreensão da história pelo jogador.

## Como funciona
Configure um compressor com entrada lateral (*sidechain ducking*) no barramento de música, disparado pelo nível de sinal presente no barramento de vozes sintéticas.

## Exemplo
```text
// Grafo de Sidechain Ducking no Mixer
[Barramento de Vozes] ──► [Sidechain Send]
                                │
                                ▼
[Barramento de Musica] ──► [Compressor (Recebe Sidechain: atenua -6dB)]
```

## Limites e trade-offs
Atenuações excessivas ou tempos de recuperação (*release*) muito rápidos causam efeito de bombeamento sonoro desconfortável na música.

## Como verificar
Reproduza uma fala de IA sobreposta à trilha de ação e confirme se a música atenua suavemente em 6dB sem cortes bruscos.

## Conexões
- [[audio-ia-configurar-espacializacao-3d-e-atenuacao]] — Veja também: Áudio 3D: configurar atenuação logarítmica e posicionamento espacial.
- [[legendas-sincronizar-texto-com-timestamps-de-palavras]] — Veja também: Legendas: sincronizar exibição de texto com timestamps por palavra.
- [[fmod-rotear-vozes-de-ia-para-barramentos-de-dialogo]] — Conexão temática direta com fmod-rotear-vozes-de-ia-para-barramentos-de-dialogo.
- [[audio-ia-sintetizar-falas-dinamicas-de-npcs]] — Conexão temática direta com audio-ia-sintetizar-falas-dinamicas-de-npcs.

## Fontes
- [ElevenLabs API Reference — Text to Speech](https://elevenlabs.io/docs/api-reference/text-to-speech) — Especificação oficial de endpoints rest para síntese de voz, timestamps por palavra e controle de prosódia. Consulta: 2026-10-04.
- [FMOD Studio Documentation](https://fmod.com/docs/2.02/studio/welcome-to-fmod-studio.html) — Manual cobrindo roteamento de barramentos de diálogo, efeitos de ambiente, espacialização 3d e sidechain ducking. Consulta: 2026-10-04.
