---
id: software.criacao_ia.tranche03.000233
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
fontes: ["https://dev.epicgames.com/documentation/unreal-engine/using-pcg-with-world-partition-in-unreal-engine?application_version=5.8", "https://dev.epicgames.com/documentation/unreal-engine/procedural-content-generation-framework-node-reference-in-unreal-engine?application_version=5.8"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Unreal PCG: propagar Data Layers e HLOD aos atores gerados

## Em uma frase
Atores criados por graph PCG podem herdar Data Layers e HLOD do componente de origem, ou receber referências explícitas por configurações de nó.

## Por que importa
Um resultado procedural útil precisa obedecer ao mesmo particionamento, ciclo de vida e organização de streaming do restante do mundo. Sem propagação deliberada, objetos visualmente presentes podem acabar na layer ou HLOD errada e escapar dos controles de carregamento previstos.

## Como funciona
No `Spawn Actor` ou `Create Target Actor`, escolha `Data Layer Source Type` como `Self` para copiar as layers do componente de origem ou `Data Layer References` para usar atributo de referência de dados. Configure filtros incluídos/excluídos ou layers adicionais conforme o caso. Atribuições de HLOD seguem a configuração equivalente do graph e do nó.

## Exemplo
Volumes distintos geram rochas e árvores em Data Layers próprias. Com `Self`, árvores geradas acompanham a layer do volume de árvores; com dados por atributo, um graph que recebe pontos de atores diferentes pode agrupar cada saída pela referência de Data Layer antes de criar atores.

## Limites e trade-offs
Herança não resolve conflitos de política nem escolhe a layer correta quando os dados agregam múltiplas origens. Atribuição para HLOD e comportamento de nodes podem depender da configuração do projeto, e a integração de streaming precisa ser testada no mapa real.

## Como verificar
Selecione atores gerados na janela Data Layers e HLOD Outliner, valide layer e classe de origem, alterne layers em execução e confirme que dados incluídos/excluídos são os esperados. Teste pontos que referenciam mais de uma layer.

## Conexões
- [[ue-pcg-higen-cascata-grid-size]] — Unreal PCG: fluxo de dados entre HiGen grid sizes.
- [[ue-pcg-runtime-generation-sources-radii]] — Unreal PCG runtime: fontes, raios de geração e limpeza.

## Fontes
- [Unreal Engine 5.8 — PCG with World Partition](https://dev.epicgames.com/documentation/unreal-engine/using-pcg-with-world-partition-in-unreal-engine?application_version=5.8) — detalha propagação de Data Layers, HLOD e settings de Spawn Actor/Create Target Actor Consulta: 2026-10-04.
- [Unreal Engine 5.8 — PCG node reference](https://dev.epicgames.com/documentation/unreal-engine/procedural-content-generation-framework-node-reference-in-unreal-engine?application_version=5.8) — documenta nós de criação e spawn usados para materializar dados como atores Consulta: 2026-10-04.
