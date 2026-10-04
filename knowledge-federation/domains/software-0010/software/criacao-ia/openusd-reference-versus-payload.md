---
id: software.criacao_ia.tranche03.000253
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
fontes: ["https://openusd.org/release/tut_referencing_layers.html", "https://openusd.org/release/api/class_usd_stage_load_rules.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# OpenUSD: escolher reference ou payload para composição diferida

## Em uma frase
Uma reference incorpora scene description durante composição, enquanto payload é um arc projetado para carregamento diferido controlável pelo stage.

## Por que importa
Asset composition precisa equilibrar acesso imediato, tamanho do working set e capacidade de streaming. Uma referência comum pode tornar conteúdo parte do stage sem política de unload por payload; payload permite que consumidor adie a composição de conteúdo caro até solicitar aquele caminho.

## Como funciona
Use references para compor assets que fazem parte do conjunto carregado por padrão e payloads para subárvores pesadas que podem ser carregadas sob demanda. Combine payload arcs com load rules do stage para definir quais caminhos estão ativos. Avalie também `defaultPrim`, path resolver e strength do arc ao integrar o asset.

## Exemplo
Um veículo compõe chassi e controles como referência essencial, mas usa payload separado para interior de alta resolução. O editor pode navegar no exterior com interior descarregado e carregar esse payload quando a câmera entra ou quando artista abre a tarefa de materiais.

## Limites e trade-offs
Payload não é apenas arquivo menor nem forma de compressão; comportamento de carga depende do stage e do arc. Uma cena pode conter payloads aninhados, resolver contexts e opinions mais fortes que mudam o resultado composto.

## Como verificar
Compare a árvore de prims com payload carregado e descarregado, use UsdStage load rules, verifique referência/defaultPrim e inspecione o prim stack após composição. Teste um asset que tem dependências relativas.

## Conexões
- [[openusd-load-rules-payloads-working-set]] — OpenUSD: tratar load rules como working set de payloads.
- [[openusd-asset-resolver-context-identifiers]] — OpenUSD: resolver context e asset identifiers de pipeline.

## Fontes
- [OpenUSD 26.08 — Referencing Layers](https://openusd.org/release/tut_referencing_layers.html) — explica reference arc, defaultPrim e composição não destrutiva Consulta: 2026-10-04.
- [OpenUSD 26.08 — UsdStageLoadRules API](https://openusd.org/release/api/class_usd_stage_load_rules.html) — documenta load/unload de payloads no working set do stage Consulta: 2026-10-04.
