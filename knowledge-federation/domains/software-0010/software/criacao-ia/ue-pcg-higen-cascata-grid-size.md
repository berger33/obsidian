---
id: software.criacao_ia.tranche03.000232
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
fontes: ["https://dev.epicgames.com/documentation/unreal-engine/using-pcg-generation-modes-in-unreal-engine?application_version=5.8", "https://dev.epicgames.com/documentation/unreal-engine/procedural-content-generation-framework-node-reference-in-unreal-engine?application_version=5.8"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Unreal PCG: fluxo de dados entre HiGen grid sizes

## Em uma frase
Na geração hierárquica, dados de uma grade maior podem ser reutilizados ao descer para grade menor, mas o fluxo não sobe de uma grade menor para uma maior.

## Por que importa
Uma graph que ignora a direção dessa cascata pode repetir operações pesadas em cada célula ou replicar os mesmos pontos em muitas células menores. A decisão de grid size é parte do plano de execução e afeta custo e duplicação, não apenas precisão visual.

## Como funciona
Ative Hierarchical Generation em graph com componente particionado. Insira `Grid Size` antes de sampler para controlar o nível de detalhe daquele ramo; nós sem esse ponto usam o default. Quando entradas vêm de vários grid sizes, a saída usa a menor grade. Uma operação compartilhada e cara pode usar nível maior ou Unbounded e então delegar detalhes às grades menores.

## Exemplo
Um ramo gera rochas grandes numa grade ampla e outro grama numa grade pequena. Se os pontos das rochas forem repassados a cada célula fina, use `Cull Points Outside Actor Bounds` para remover pontos fora dos limites locais ou ajuste a sequência para não duplicar o trabalho.

## Limites e trade-offs
Subgraphs herdam grid size de seus dados de entrada ou graph pai e têm seu próprio controle de grid desabilitado. Escolhas impróprias podem aumentar custo ou alterar cobertura. O cache de dados não elimina duplicatas automaticamente.

## Como verificar
Compare quantidade de pontos e chamadas de sampler por célula, examine grid size de cada nó no Debug Object Tree e teste entradas que chegam em níveis diferentes. Valide limites da célula para identificar dados repetidos.

## Conexões
- [[ue-pcg-partitioned-generation-grid-celulas]] — Unreal PCG: partitioned generation divide domínio em células.
- [[ue-pcg-world-partition-data-layers-hlod]] — Unreal PCG: propagar Data Layers e HLOD aos atores gerados.

## Fontes
- [Unreal Engine 5.8 — PCG generation modes](https://dev.epicgames.com/documentation/unreal-engine/using-pcg-generation-modes-in-unreal-engine?application_version=5.8) — define a cascata de HiGen, menor grid size em múltiplas entradas e caso Unbounded Consulta: 2026-10-04.
- [Unreal Engine 5.8 — PCG node reference](https://dev.epicgames.com/documentation/unreal-engine/procedural-content-generation-framework-node-reference-in-unreal-engine?application_version=5.8) — serve de referência para nós de sampler, culling e transformação de pontos Consulta: 2026-10-04.
