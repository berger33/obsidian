---
id: software.criacao_ia.tranche03.000237
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

# Unreal PCG runtime: dimensionar pool de Partition Actors

## Em uma frase
O pool de Partition Actors reduz alocações repetidas, mas, quando se esgota, pode dobrar e realizar uma operação custosa durante jogo.

## Por que importa
A expansão inesperada do pool pode coincidir com frame hitch justamente quando novas células entram no raio. Pré-dimensionar a reserva com dados de percurso evita interpretar todo pico como custo inevitável do grafo.

## Como funciona
A geração runtime usa pooling de atores particionados; o overlay mostra `PA Pool`, e `pcg.RuntimeGeneration.BasePoolSize` define o tamanho inicial documentado. Meça pico de células e resultados ativos em rotas representativas antes de ajustar o valor. Compare memory footprint com custo de expansão e mantenha a cvar de debug separada da política de build.

## Exemplo
Um nível aberto registra uso máximo de 140 PAs numa corrida com múltiplos jogadores. A equipe repete a captura com pool inicial ampliado e confirma se o pico deixa de dobrar em gameplay, verificando também que a memória não ficou reservada em excesso para níveis menores.

## Limites e trade-offs
O pool não elimina custo de gerar graph ou alocar todos os recursos de conteúdo. Valores muito altos desperdiçam memória e a demanda muda com densidade, quantidade de sources e número de células simultâneas.

## Como verificar
Observe o campo `PA Pool` frame a frame e a cvar `BasePoolSize`; force entradas e saídas repetidas de raio e compare hitches, memória e contagem de atores. Repita na configuração de multiplayer esperada.

## Conexões
- [[ue-pcg-overlay-runtime-generation]] — Unreal PCG: interpretar overlay de geração em runtime.
- [[ue-pcg-cache-runtime-editor-budget]] — Unreal PCG: entender cache CPU e orçamento de memória.

## Fontes
- [Unreal Engine 5.8 — PCG runtime debugging](https://dev.epicgames.com/documentation/unreal-engine/pcg-runtime-generation-debugging-in-unreal-engine?application_version=5.8) — descreve o pool, seu crescimento por dobra e a cvar BasePoolSize Consulta: 2026-10-04.
- [Unreal Engine 5.8 — PCG generation modes](https://dev.epicgames.com/documentation/unreal-engine/using-pcg-generation-modes-in-unreal-engine?application_version=5.8) — documenta pooling e limites de componentes no scheduler runtime Consulta: 2026-10-04.
