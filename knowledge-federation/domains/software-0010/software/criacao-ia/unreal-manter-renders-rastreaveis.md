---
id: software.criacao_ia.tranche01.000080
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

# Unreal: manter renders rastreáveis

## Em uma frase

Identificadores de cena, versão de projeto e preset permitem saber qual sequência produziu cada arquivo.

## Por que importa

Rastreabilidade acelera correção e impede que preview antigo seja confundido com render aprovado.

## Como funciona

Inclua código ou build, shot, data e versão de preset no nome ou metadados controlados do job.

## Exemplo

Um render registra `build-42/shot-03/preset-final-v2`, com arquivo de log salvo junto à entrega.

## Limites e trade-offs

Nomes sozinhos podem ser editados ou duplicados; metadados precisam acompanhar arquivo em armazenamento partilhado.

## Como verificar

Escolha uma saída aleatória e reconstrua engine, sequence, preset e commit de origem somente com os registros mantidos.

## Conexões
- [[unreal-revisar-sequencia-renderizada-alem-do-viewport]] — Unreal: revisar sequência renderizada além do viewport.
- [[comfyui-ler-um-workflow-como-grafo]] — ComfyUI: ler um workflow como grafo.

## Fontes
- [Epic Games — Sequencer Overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-sequencer-movie-tool-overview) — Explica Level Sequence, Level Sequence Actor, tracks, keyframes e edição de cinematics. Consulta: 2026-10-04.
- [Epic Games — Movie Render Pipeline](https://dev.epicgames.com/documentation/en-us/unreal-engine/movie-render-pipeline-in-unreal-engine) — Documenta a renderização de cinematics pela Movie Render Queue e Movie Render Graph. Consulta: 2026-10-04.
