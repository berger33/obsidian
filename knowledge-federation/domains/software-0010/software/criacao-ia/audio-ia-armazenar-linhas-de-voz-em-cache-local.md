---
id: software.criacao_ia.tranche02.000172
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

# Áudio com IA: armazenar falas geradas em cache de disco local

## Em uma frase
O armazenamento em cache de arquivos de áudio evita chamadas redundantes à API para falas frequentes e reduz custos operacionais.

## Por que importa
Falas comuns de saudação, avisos de combate e respostas padrão de NPCs são repetidas dezenas de vezes durante uma sessão de jogo.

## Como funciona
Gere um hash SHA-256 a partir do texto e do ID da voz para servir como chave de busca. Se o arquivo `.wav` ou `.ogg` correspondente existir no diretório de cache local, carregue-o do disco sem usar a rede.

## Exemplo
```csharp
// Verificando cache local antes de disparar requisicao de audio
string hashKey = GenerateSHA256(voiceId + "_" + text);
string localPath = Path.Combine(Application.persistentDataPath, "AudioCache", hashKey + ".ogg");

if (File.Exists(localPath))
{
    return LoadAudioFromDisk(localPath);
}
```

## Limites e trade-offs
O acúmulo descontrolado de arquivos de voz em cache pode consumir espaço excessivo de armazenamento no dispositivo do jogador.

## Como verificar
Inspecione o diretório de cache em disco após disparar falas repetidas e valide se o tempo de carregamento cai para poucos milissegundos.

## Conexões
- [[audio-ia-sintetizar-falas-dinamicas-de-npcs]] — Veja também: Áudio com IA: sintetizar falas dinâmicas de NPCs via chamadas assíncronas.
- [[audio-ia-extrair-visemas-para-lip-sync-com-rhubarb]] — Veja também: Lip Sync com IA: extrair visemas fonéticos de áudio com Rhubarb.
- [[audio-ia-prover-linhas-de-dialogo-de-fallback]] — Conexão temática direta com audio-ia-prover-linhas-de-dialogo-de-fallback.
- [[legendas-sincronizar-texto-com-timestamps-de-palavras]] — Conexão temática direta com legendas-sincronizar-texto-com-timestamps-de-palavras.

## Fontes
- [ElevenLabs API Reference — Text to Speech](https://elevenlabs.io/docs/api-reference/text-to-speech) — Especificação oficial de endpoints rest para síntese de voz, timestamps por palavra e controle de prosódia. Consulta: 2026-10-04.
- [FMOD Studio Documentation](https://fmod.com/docs/2.02/studio/welcome-to-fmod-studio.html) — Manual cobrindo roteamento de barramentos de diálogo, efeitos de ambiente, espacialização 3d e sidechain ducking. Consulta: 2026-10-04.
