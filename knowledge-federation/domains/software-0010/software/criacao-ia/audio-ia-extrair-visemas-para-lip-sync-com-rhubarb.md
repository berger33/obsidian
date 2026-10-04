---
id: software.criacao_ia.tranche02.000173
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

# Lip Sync com IA: extrair visemas fonéticos de áudio com Rhubarb

## Em uma frase
A extração automatizada de visemas e fonemas a partir de ondas sonoras viabiliza sincronia labial precisa em personagens 3D.

## Por que importa
Animar manualmente a boca de personagens para milhares de linhas de diálogo procedural é inviável em projetos de grande escala.

## Como funciona
Processe o arquivo de áudio com a ferramenta Rhubarb Lip Sync ou plugins de fonética, gerando uma trilha de dados contendo marcadores temporais com visemas padronizados (bocas em formato A, B, C, D, E, F, G, H, X).

## Exemplo
```bash
# Extraindo marcadores de sincronia labial para JSON com Rhubarb Lip Sync
rhubarb -f json -r phonetic speech_npc_01.wav -o speech_npc_01_lipsync.json
```

## Limites e trade-offs
Arquivos de áudio com música de fundo pesada ou ruídos de vento podem gerar falsos visemas ou dessincronizar a fala.

## Como verificar
Execute a extração de visemas exclusivamente sobre a trilha limpa de voz isolada antes da mixagem final.

## Conexões
- [[audio-ia-armazenar-linhas-de-voz-em-cache-local]] — Veja também: Áudio com IA: armazenar falas geradas em cache de disco local.
- [[audio-ia-mapear-visemas-a-blend-shapes-faciais]] — Veja também: Animação Facial: mapear visemas fonéticos a blend shapes do modelo 3D.
- [[legendas-sincronizar-texto-com-timestamps-de-palavras]] — Conexão temática direta com legendas-sincronizar-texto-com-timestamps-de-palavras.
- [[unity-animation-rigging-orientar-olhar-com-multi-aim]] — Conexão temática direta com unity-animation-rigging-orientar-olhar-com-multi-aim.

## Fontes
- [ElevenLabs API Reference — Text to Speech](https://elevenlabs.io/docs/api-reference/text-to-speech) — Especificação oficial de endpoints rest para síntese de voz, timestamps por palavra e controle de prosódia. Consulta: 2026-10-04.
- [FMOD Studio Documentation](https://fmod.com/docs/2.02/studio/welcome-to-fmod-studio.html) — Manual cobrindo roteamento de barramentos de diálogo, efeitos de ambiente, espacialização 3d e sidechain ducking. Consulta: 2026-10-04.
