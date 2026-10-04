---
id: software.criacao_ia.tranche03.000236
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-03.md"
fontes: ["https://dev.epicgames.com/documentation/unreal-engine/pcg-runtime-generation-debugging-in-unreal-engine?application_version=5.8", "https://dev.epicgames.com/documentation/unreal-engine/using-pcg-generation-modes-in-unreal-engine?application_version=5.8"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Unreal PCG: interpretar overlay de geração em runtime

## Em uma frase
O overlay PCG registra custo de tick, chamadas de geração e cleanup, componentes ativos e uso do pool por frame.

## Por que importa
A geração acontece em rajadas quando células cruzam um raio, então médias de frame escondem atrasos e crescimento de pool. O overlay ajuda a relacionar stutter, componentes pendentes e distância de aparecimento do conteúdo.

## Como funciona
Habilite `pcg.RuntimeGeneration.EnableDebugOverlay 1` em Editor ou Development. Observe `Tick time`, `Generate Calls`, `Cleanup Calls`, `Num Generating Components` e `PA Pool`; grave vídeo e pause em frames relevantes para capturar comportamento transitório. Use `pcg.GraphExecution.DebugDrawGeneratedCells` para visualizar sources e células em geração.

## Exemplo
Durante um percurso de referência, a equipe registra overlay e câmera. Um pico de `Tick time` coincide com várias células recém-entradas; `PA Pool` dobrando no mesmo frame indica esgotamento da reserva, então o tamanho inicial é reavaliado e o teste é repetido.

## Limites e trade-offs
Overlay não está habilitado por padrão em Test ou Shipping builds e seus valores são por frame, não uma série histórica agregada. Um perfil de Editor não reproduz necessariamente custo de runtime final ou uso do hardware do jogador.

## Como verificar
Capture um trace no Unreal Insights e correlacione cvars e overlays com frame time e pop visual. Teste a mesma rota em Development e build alvo com instrumentação de produção adequada.

## Conexões
- [[ue-pcg-scheduler-num-generating-components]] — Unreal PCG runtime: equilibrar scheduler e células concorrentes.
- [[ue-pcg-runtime-partition-actor-pool]] — Unreal PCG runtime: dimensionar pool de Partition Actors.

## Fontes
- [Unreal Engine 5.8 — PCG runtime debugging](https://dev.epicgames.com/documentation/unreal-engine/pcg-runtime-generation-debugging-in-unreal-engine?application_version=5.8) — lista métricas de overlay, cvars para cells e restrição de build Consulta: 2026-10-04.
- [Unreal Engine 5.8 — PCG generation modes](https://dev.epicgames.com/documentation/unreal-engine/using-pcg-generation-modes-in-unreal-engine?application_version=5.8) — explica fontes, scheduler, raio de geração e cvars de runtime Consulta: 2026-10-04.
