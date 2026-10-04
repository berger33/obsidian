---
id: software.criacao_ia.tranche02.000176
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

# Áudio 3D: configurar atenuação logarítmica e posicionamento espacial

## Em uma frase
A espacialização tridimensional e o cálculo de atenuação por distância situam a origem da fala do NPC com precisão acústica no mundo virtual.

## Por que importa
Vozes reproduzidas em estéreo simples impedem que o jogador localize visualmente qual personagem está falando em uma multidão.

## Como funciona
Configure curvas de atenuação logarítmica com distâncias mínima e máxima bem delimitadas e ative processamento binaural (HRTF) na fonte de áudio do NPC.

## Exemplo
```csharp
// Configurando atenuacao logaritmica em uma fonte de audio 3D
AudioSource source = GetComponent<AudioSource>();
source.spatialBlend = 1.0f; // 100% 3D espacial
source.rolloffMode = AudioRolloffMode.Logarithmic;
source.minDistance = 2.0f;
source.maxDistance = 25.0f;
```

## Limites e trade-offs
Distâncias mínimas muito curtas causam quedas bruscas de volume se o jogador der apenas dois passos para trás durante a conversa.

## Como verificar
Caminhe em círculos ao redor do personagem falante com fones de ouvido e valide o balanço binaural nos canais esquerdo e direito.

## Conexões
- [[fmod-rotear-vozes-de-ia-para-barramentos-de-dialogo]] — Veja também: FMOD: rotear vozes sintéticas para barramentos de diálogo com efeitos.
- [[mixagem-aplicar-audio-ducking-durante-vozes-de-ia]] — Veja também: Mixagem de Som: aplicar audio ducking automático durante falas de IA.
- [[godot-propagar-eventos-sonoros-para-audicao-de-npcs]] — Conexão temática direta com godot-propagar-eventos-sonoros-para-audicao-de-npcs.

## Fontes
- [ElevenLabs API Reference — Text to Speech](https://elevenlabs.io/docs/api-reference/text-to-speech) — Especificação oficial de endpoints rest para síntese de voz, timestamps por palavra e controle de prosódia. Consulta: 2026-10-04.
- [FMOD Studio Documentation](https://fmod.com/docs/2.02/studio/welcome-to-fmod-studio.html) — Manual cobrindo roteamento de barramentos de diálogo, efeitos de ambiente, espacialização 3d e sidechain ducking. Consulta: 2026-10-04.
