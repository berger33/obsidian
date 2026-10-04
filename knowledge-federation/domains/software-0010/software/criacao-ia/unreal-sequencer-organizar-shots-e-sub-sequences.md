---
id: software.criacao_ia.tranche01.000074
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

# Unreal Sequencer: organizar Shots e Sub-Sequences

## Em uma frase

Subsequências e shots dividem uma cinematic em unidades menores que podem ser montadas e revisadas na sequência principal.

## Por que importa

Segmentação facilita regravar uma tomada e controlar timing sem reconstruir toda a timeline.

## Como funciona

Defina sequência raiz, sub-sequências, duração e bindings; mantenha nomenclatura e contagem de shots consistentes.

## Exemplo

Uma cutscene de boss mantém introdução, reação e transição para gameplay como três shots editáveis.

## Limites e trade-offs

Subsequência pode herdar tempo e bindings de forma diferente do asset raiz, e alterações globais podem afetar muitas tomadas.

## Como verificar

Renderize cada shot e a montagem completa e confira continuidade, duração, câmera e referências após uma revisão local.

## Conexões
- [[unreal-sequencer-construir-cortes-de-camera]] — Unreal Sequencer: construir cortes de câmera.
- [[unreal-capturar-takes-com-take-recorder]] — Unreal: capturar Takes com Take Recorder.

## Fontes
- [Epic Games — Sequencer Overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-sequencer-movie-tool-overview) — Explica Level Sequence, Level Sequence Actor, tracks, keyframes e edição de cinematics. Consulta: 2026-10-04.
- [Epic Games — Movie Render Pipeline](https://dev.epicgames.com/documentation/en-us/unreal-engine/movie-render-pipeline-in-unreal-engine) — Documenta a renderização de cinematics pela Movie Render Queue e Movie Render Graph. Consulta: 2026-10-04.
