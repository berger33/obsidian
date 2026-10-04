---
id: software.criacao_ia.tranche02.000175
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

# FMOD: rotear vozes sintéticas para barramentos de diálogo com efeitos

## Em uma frase
O roteamento de vozes para barramentos (*busses*) dedicados no FMOD garante que falas geradas por IA recebam tratamento acústico coerente.

## Por que importa
Tocar vozes de IA diretamente sem reverb espacial e equalização faz o diálogo soar desconectado da arquitetura da sala do jogo.

## Como funciona
Crie um barramento `Dialog/NPC_Voices` no FMOD Studio e injete as streams de áudio geradas nesse canal, aplicando efeitos de reverberação de ambiente, compressão dinâmica e filtros de oclusão.

## Exemplo
```csharp
// Roteando stream de audio para o barramento de dialogo do FMOD
FMOD.Studio.Bus dialogBus;
dialogBus = FMODUnity.RuntimeManager.GetBus("bus:/Master/Dialog");
// Injetar o program sound ou canal na mixagem
```

## Limites e trade-offs
Efeitos de reverberação muito longos em barramentos de diálogo comprometem a clareza e a inteligibilidade do texto narrado.

## Como verificar
Monitore os medidores de VU no FMOD Mixer durante a fala do NPC para assegurar que o sinal não atinja clipping digital.

## Conexões
- [[audio-ia-mapear-visemas-a-blend-shapes-faciais]] — Veja também: Animação Facial: mapear visemas fonéticos a blend shapes do modelo 3D.
- [[audio-ia-configurar-espacializacao-3d-e-atenuacao]] — Veja também: Áudio 3D: configurar atenuação logarítmica e posicionamento espacial.
- [[mixagem-aplicar-audio-ducking-durante-vozes-de-ia]] — Conexão temática direta com mixagem-aplicar-audio-ducking-durante-vozes-de-ia.
- [[audio-ia-sintetizar-falas-dinamicas-de-npcs]] — Conexão temática direta com audio-ia-sintetizar-falas-dinamicas-de-npcs.

## Fontes
- [ElevenLabs API Reference — Text to Speech](https://elevenlabs.io/docs/api-reference/text-to-speech) — Especificação oficial de endpoints rest para síntese de voz, timestamps por palavra e controle de prosódia. Consulta: 2026-10-04.
- [FMOD Studio Documentation](https://fmod.com/docs/2.02/studio/welcome-to-fmod-studio.html) — Manual cobrindo roteamento de barramentos de diálogo, efeitos de ambiente, espacialização 3d e sidechain ducking. Consulta: 2026-10-04.
