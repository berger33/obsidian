---
id: software.criacao_ia.tranche02.000180
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

# Resiliência de Áudio: prover falas pré-gravadas como fallback de rede

## Em uma frase
A disponibilização de falas pré-gravadas locais garante continuidade do jogo quando a conexão com a API de voz falhar ou expirar.

## Por que importa
Erros de rede ou lentidão em APIs remotas nunca devem travar a progressão de missões ou deixar NPCs mudos durante a partida.

## Como funciona
Implemente um mecanismo de fallback: se a requisição de TTS não retornar em até 1.5 segundos ou responder com erro HTTP, reproduza imediatamente um áudio pré-gravado padrão em disco.

## Exemplo
```csharp
// Mecanismo de timeout e fallback para falas de NPCs
try
{
    var audio = await FetchSpeechWithTimeout(text, 1500);
    PlayAudio(audio);
}
catch (System.Exception)
{
    // Reproduzir linha de voz generica previamente empacotada no jogo
    PlayFallbackAudio("npc_generic_grunt_01");
}
```

## Limites e trade-offs
Fallbacks com conteúdo excessivamente genérico podem descontextualizar o diálogo se a missão depender de instruções específicas.

## Como verificar
Simule a interrupção da conexão de rede e verifique se o áudio de contingência toca imediatamente sem gerar exceções não tratadas.

## Conexões
- [[audio-ia-modular-prosodia-e-estabilidade-por-emocao]] — Veja também: Áudio com IA: modular parâmetros de prosódia e estilo por emoção.
- [[audio-ia-sintetizar-falas-dinamicas-de-npcs]] — Conexão temática direta com audio-ia-sintetizar-falas-dinamicas-de-npcs.
- [[audio-ia-armazenar-linhas-de-voz-em-cache-local]] — Conexão temática direta com audio-ia-armazenar-linhas-de-voz-em-cache-local.
- [[responses-api-tratar-falhas-e-repeticao]] — Conexão temática direta com responses-api-tratar-falhas-e-repeticao.

## Fontes
- [ElevenLabs API Reference — Text to Speech](https://elevenlabs.io/docs/api-reference/text-to-speech) — Especificação oficial de endpoints rest para síntese de voz, timestamps por palavra e controle de prosódia. Consulta: 2026-10-04.
- [FMOD Studio Documentation](https://fmod.com/docs/2.02/studio/welcome-to-fmod-studio.html) — Manual cobrindo roteamento de barramentos de diálogo, efeitos de ambiente, espacialização 3d e sidechain ducking. Consulta: 2026-10-04.
