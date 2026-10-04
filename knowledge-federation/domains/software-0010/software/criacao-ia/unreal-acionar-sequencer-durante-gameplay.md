---
id: software.criacao_ia.tranche01.000076
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

# Unreal: acionar Sequencer durante gameplay

## Em uma frase

Blueprints e componentes podem iniciar, pausar ou controlar sequência em resposta a eventos do jogo.

## Por que importa

Conectar cinematic ao estado da partida permite sincronizar animação, câmera e fluxo sem uma renderização offline.

## Como funciona

Use evento de gameplay para controlar sequência, defina política de pausa e restauração de estado e trate interrupção.

## Exemplo

Ao entrar numa sala, o Blueprint reproduz entrada curta e devolve controle ao jogador no frame previsto.

## Limites e trade-offs

Uma sequência pode bloquear input, mudar câmera ou deixar ator em estado final se interrupção não for tratada.

## Como verificar

Teste início, pause, fim natural, troca de level e cancelamento, verificando input e estado de cada ator.

## Conexões
- [[unreal-capturar-takes-com-take-recorder]] — Unreal: capturar Takes com Take Recorder.
- [[unreal-montar-uma-fila-de-renderizacao]] — Unreal: montar uma fila de renderização.

## Fontes
- [Epic Games — Sequencer Overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-sequencer-movie-tool-overview) — Explica Level Sequence, Level Sequence Actor, tracks, keyframes e edição de cinematics. Consulta: 2026-10-04.
- [Epic Games — Movie Render Pipeline](https://dev.epicgames.com/documentation/en-us/unreal-engine/movie-render-pipeline-in-unreal-engine) — Documenta a renderização de cinematics pela Movie Render Queue e Movie Render Graph. Consulta: 2026-10-04.
