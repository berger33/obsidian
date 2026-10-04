---
id: software.criacao_ia.tranche03.000238
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
fontes: ["https://dev.epicgames.com/documentation/unreal-engine/pcg-runtime-generation-debugging-in-unreal-engine?application_version=5.8", "https://dev.epicgames.com/documentation/unreal-engine/procedural-content-generation-framework-node-reference-in-unreal-engine?application_version=5.8"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Unreal PCG: entender cache CPU e orçamento de memória

## Em uma frase
O cache de graph PCG retém resultados de nós CPU para evitar reexecução, com habilitação e budget independentes para worlds de jogo e editor.

## Por que importa
Cache pode reduzir trabalho repetido, mas seus benefícios dependem de reutilização real e podem vir acompanhados de pressão de memória. Projetos que assumem o mesmo estado padrão no editor e runtime podem medir resultados diferentes.

## Como funciona
Inspecione `pcg.Cache.Runtime.Enabled` e `pcg.Cache.Editor.Enabled` na configuração de UE 5.8: runtime está desabilitado por padrão e editor habilitado. Ajuste `pcg.Cache.Runtime.MemoryBudgetMB` ou a contraparte de editor; quando o budget é excedido, entradas antigas são descartadas. Flush ou Force Regen ajudam a distinguir cache hit de node que não executou durante debug.

## Exemplo
Uma graph cara amostra terreno compartilhado por células finas. A equipe mede cache hit em runtime e editor separadamente, sobe o budget apenas se a taxa de reutilização compensa a memória e repete profiling após descarte das entradas mais antigas.

## Limites e trade-offs
Cache guarda dados de saída de nós CPU conforme condições de reutilização, não resultados arbitrários de side effects nem todos os trabalhos GPU. Um cache hit pode impedir um breakpoint de disparar, por isso debug precisa poder forçar regeneração.

## Como verificar
Compare execução com cache habilitado/desabilitado usando mesmos inputs, meça memória e tempo, reduza budget e confirme eviction. Ative `Force Regen` antes de concluir que um breakpoint não funciona.

## Conexões
- [[ue-pcg-runtime-partition-actor-pool]] — Unreal PCG runtime: dimensionar pool de Partition Actors.
- [[ue-pcg-gpu-compute-graph-transferencias]] — Unreal PCG GPU: agrupar nós para reduzir transferências.

## Fontes
- [Unreal Engine 5.8 — PCG runtime debugging](https://dev.epicgames.com/documentation/unreal-engine/pcg-runtime-generation-debugging-in-unreal-engine?application_version=5.8) — define cvars de enable, budgets, eviction e interação de cache com breakpoint Consulta: 2026-10-04.
- [Unreal Engine 5.8 — PCG node reference](https://dev.epicgames.com/documentation/unreal-engine/procedural-content-generation-framework-node-reference-in-unreal-engine?application_version=5.8) — contextualiza nós CPU e comportamento de execução no graph PCG Consulta: 2026-10-04.
