---
id: software.criacao_ia.tranche02.000174
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

# Animação Facial: mapear visemas fonéticos a blend shapes do modelo 3D

## Em uma frase
O mapeamento de dados fonéticos para blend shapes faciais interpola a abertura de lábios e movimentos de mandíbula em tempo real.

## Por que importa
Visemas aplicados de forma binária e sem suavização causam estalos e deformações faciais robóticas durante a fala do personagem.

## Como funciona
Crie uma tabela de equivalência associando cada letra de visema (ex.: Viseme A = `JawOpen`, Viseme B = `LipsTogether`) aos blend shapes da malha e interpole os pesos com suavização (*smooth damp*).

## Exemplo
```csharp
// Atualizando peso do Blend Shape facial conforme o visema ativo
public void UpdateLipSync(SkinnedMeshRenderer faceMesh, string currentViseme, float weight)
{
    int blendIndex = faceMesh.sharedMesh.GetBlendShapeIndex("viseme_" + currentViseme);
    if (blendIndex >= 0)
    {
        faceMesh.SetBlendShapeWeight(blendIndex, Mathf.Lerp(faceMesh.GetBlendShapeWeight(blendIndex), weight * 100f, Time.deltaTime * 20f));
    }
}
```

## Limites e trade-offs
Excesso de blend shapes ativados simultaneamente pode deformar a geometria ao redor das bochechas e nariz de forma estranha.

## Como verificar
Execute o áudio sincronizado na cena e verifique se as transições de abertura de boca coincidem com as vogais e consoantes pronunciadas.

## Conexões
- [[audio-ia-extrair-visemas-para-lip-sync-com-rhubarb]] — Veja também: Lip Sync com IA: extrair visemas fonéticos de áudio com Rhubarb.
- [[fmod-rotear-vozes-de-ia-para-barramentos-de-dialogo]] — Veja também: FMOD: rotear vozes sintéticas para barramentos de diálogo com efeitos.
- [[unity-playablegraph-mesclar-animacoes-procedurais]] — Conexão temática direta com unity-playablegraph-mesclar-animacoes-procedurais.
- [[blender-preservar-acoes-com-nla]] — Conexão temática direta com blender-preservar-acoes-com-nla.

## Fontes
- [ElevenLabs API Reference — Text to Speech](https://elevenlabs.io/docs/api-reference/text-to-speech) — Especificação oficial de endpoints rest para síntese de voz, timestamps por palavra e controle de prosódia. Consulta: 2026-10-04.
- [FMOD Studio Documentation](https://fmod.com/docs/2.02/studio/welcome-to-fmod-studio.html) — Manual cobrindo roteamento de barramentos de diálogo, efeitos de ambiente, espacialização 3d e sidechain ducking. Consulta: 2026-10-04.
