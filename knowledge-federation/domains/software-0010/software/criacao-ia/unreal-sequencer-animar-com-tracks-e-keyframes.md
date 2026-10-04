---
id: software.criacao_ia.tranche01.000072
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-01.md"
fontes: ["https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-sequencer-movie-tool-overview", "https://dev.epicgames.com/documentation/en-us/unreal-engine/movie-render-pipeline-in-unreal-engine"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Unreal Sequencer: animar com tracks e keyframes

## Em uma frase

Tracks registram propriedades ou atores ao longo do tempo, e keyframes definem seus valores em pontos da linha do tempo.

## Por que importa

Organizar propriedades por track torna uma cena de jogo editável sem misturar todo movimento num script específico.

## Como funciona

Adicione somente canais necessários, ajuste keyframes e verifique se interpolação e faixa temporal correspondem à intenção.

## Exemplo

Uma luz diminui intensidade enquanto a câmera se aproxima do portal e o personagem toca a alavanca.

## Limites e trade-offs

Muitos canais e bindings frágeis podem quebrar quando o ator muda ou é duplicado na cena.

## Como verificar

Reproduza de início, meio e fim e confira valores efetivos no viewport e no ator durante a sequência.

## Conexões
- [[unreal-sequencer-distinguir-asset-e-actor]] — Unreal Sequencer: distinguir asset e actor.
- [[unreal-sequencer-construir-cortes-de-camera]] — Unreal Sequencer: construir cortes de câmera.

## Fontes
- [Epic Games — Sequencer Overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-sequencer-movie-tool-overview) — Explica Level Sequence, Level Sequence Actor, tracks, keyframes e edição de cinematics. Consulta: 2026-10-04.
- [Epic Games — Movie Render Pipeline](https://dev.epicgames.com/documentation/en-us/unreal-engine/movie-render-pipeline-in-unreal-engine) — Documenta a renderização de cinematics pela Movie Render Queue e Movie Render Graph. Consulta: 2026-10-04.
