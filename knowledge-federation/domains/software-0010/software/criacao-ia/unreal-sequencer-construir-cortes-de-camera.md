---
id: software.criacao_ia.tranche01.000073
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

# Unreal Sequencer: construir cortes de câmera

## Em uma frase

Camera Cuts determina qual câmera fornece a visão durante intervalos definidos da sequência.

## Por que importa

Cortes explícitos ajudam a revisar linguagem visual e evitam depender da câmera de edição que estava ativa por acaso.

## Como funciona

Crie cameras, insira bindings na track Camera Cuts e ajuste duração e sobreposição conforme o formato da cena.

## Exemplo

Uma animação mostra plano geral, corte para detalhe do item e volta ao personagem antes do gameplay.

## Limites e trade-offs

Binding de câmera removido ou faixa fora do tempo pode mostrar view inesperada ou tela sem o corte pretendido.

## Como verificar

Reproduza a sequência sem pilotar câmera manualmente e verifique todos os pontos de corte e o frame inicial.

## Conexões
- [[unreal-sequencer-animar-com-tracks-e-keyframes]] — Unreal Sequencer: animar com tracks e keyframes.
- [[unreal-sequencer-organizar-shots-e-sub-sequences]] — Unreal Sequencer: organizar Shots e Sub-Sequences.

## Fontes
- [Epic Games — Sequencer Overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-sequencer-movie-tool-overview) — Explica Level Sequence, Level Sequence Actor, tracks, keyframes e edição de cinematics. Consulta: 2026-10-04.
- [Epic Games — Movie Render Pipeline](https://dev.epicgames.com/documentation/en-us/unreal-engine/movie-render-pipeline-in-unreal-engine) — Documenta a renderização de cinematics pela Movie Render Queue e Movie Render Graph. Consulta: 2026-10-04.
