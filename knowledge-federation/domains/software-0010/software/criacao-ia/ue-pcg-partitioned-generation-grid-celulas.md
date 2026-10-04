---
id: software.criacao_ia.tranche03.000231
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
fontes: ["https://dev.epicgames.com/documentation/unreal-engine/using-pcg-generation-modes-in-unreal-engine?application_version=5.8", "https://dev.epicgames.com/documentation/unreal-engine/using-pcg-with-world-partition-in-unreal-engine?application_version=5.8"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Unreal PCG: partitioned generation divide domínio em células

## Em uma frase
Partitioned Generation distribui os resultados do PCG por uma grade definida, em vez de manter todos os meshes no domínio de um único componente.

## Por que importa
Um componente enorme pode gerar grande volume de atores e dificultar streaming e atualização localizada. Dividir o resultado em células dá a outros sistemas como World Partition e Level Instancing unidades menores de organização, carregamento e debug.

## Como funciona
Ative `Is Partitioned` no asset e configure `Partition Grid Size` no `PCGWorldActor`; cada célula recebe componente local. Dimensione a grade considerando escala dos objetos e frequência de atualização, e regenere os assets depois de alterar a grade. Geração hierárquica também depende de componentes particionados.

## Exemplo
Um bioma com árvores espaçadas e vegetação rasteira pode particionar o volume para que conjuntos locais de pontos e atores sejam gerados por célula. O nível pode então carregar conteúdo próximo sem executar novamente a geração de toda a área do bioma.

## Limites e trade-offs
Particionar não é automaticamente sinônimo de melhor desempenho: grades muito pequenas aumentam número de componentes, overhead e fronteiras; grades grandes reduzem granularidade. O resultado também depende do modo de geração e de como os atores gerados são consumidos pelo projeto.

## Como verificar
Inspecione os atores e componentes criados no Outliner, carregue e descarregue células vizinhas e compare tempo e memória com modo não particionado. Depois de alterar o tamanho da grade, use Cleanup e gere novamente.

## Conexões
- [[ue-pcg-higen-cascata-grid-size]] — Unreal PCG: fluxo de dados entre HiGen grid sizes.

## Fontes
- [Unreal Engine 5.8 — PCG generation modes](https://dev.epicgames.com/documentation/unreal-engine/using-pcg-generation-modes-in-unreal-engine?application_version=5.8) — define modos, componentes locais e configuração da grade particionada Consulta: 2026-10-04.
- [Unreal Engine 5.8 — PCG with World Partition](https://dev.epicgames.com/documentation/unreal-engine/using-pcg-with-world-partition-in-unreal-engine?application_version=5.8) — mostra integração dos resultados PCG com células, Data Layers e HLOD Consulta: 2026-10-04.
