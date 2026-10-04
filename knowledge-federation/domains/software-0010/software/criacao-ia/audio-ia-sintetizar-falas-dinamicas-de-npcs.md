---
id: software.criacao_ia.tranche02.000171
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

# Áudio com IA: sintetizar falas dinâmicas de NPCs via chamadas assíncronas

## Em uma frase
A geração de áudio dinâmico por Text-to-Speech (TTS) permite que NPCs pronunciem falas personalizadas com base no contexto do jogador.

## Por que importa
Gravações estáticas não conseguem narrar eventos gerados proceduralmente ou citar o nome customizado escolhido pelo jogador.

## Como funciona
Dispare uma requisição HTTP assíncrona para a API de síntese de voz informando o texto da fala, o identificador da voz e o modelo neural, recebendo um stream de áudio em formato PCM ou MP3 para reprodução imediata.

## Exemplo
```csharp
// Exemplo de requisicao assincrona de TTS em Unity C#
using UnityEngine.Networking;
using System.Threading.Tasks;

public async Task<AudioClip> FetchNPCSpeechAsync(string text, string voiceId)
{
    string url = $"https://api.elevenlabs.io/v1/text-to-speech/{voiceId}";
    // Enviar POST com payload JSON e carregar bytes como AudioClip
    return await DownloadAudioStreamAsync(url, text);
}
```

## Limites e trade-offs
Chamadas de rede em tempo real introduzem latência de alguns segundos antes do início da reprodução da fala do NPC.

## Como verificar
Inicie a requisição de geração antes do término do diálogo anterior para ocultar a latência de transferência de dados.

## Conexões
- [[audio-ia-armazenar-linhas-de-voz-em-cache-local]] — Veja também: Áudio com IA: armazenar falas geradas em cache de disco local.
- [[audio-ia-prover-linhas-de-dialogo-de-fallback]] — Conexão temática direta com audio-ia-prover-linhas-de-dialogo-de-fallback.
- [[fmod-rotear-vozes-de-ia-para-barramentos-de-dialogo]] — Conexão temática direta com fmod-rotear-vozes-de-ia-para-barramentos-de-dialogo.

## Fontes
- [ElevenLabs API Reference — Text to Speech](https://elevenlabs.io/docs/api-reference/text-to-speech) — Especificação oficial de endpoints rest para síntese de voz, timestamps por palavra e controle de prosódia. Consulta: 2026-10-04.
- [FMOD Studio Documentation](https://fmod.com/docs/2.02/studio/welcome-to-fmod-studio.html) — Manual cobrindo roteamento de barramentos de diálogo, efeitos de ambiente, espacialização 3d e sidechain ducking. Consulta: 2026-10-04.
