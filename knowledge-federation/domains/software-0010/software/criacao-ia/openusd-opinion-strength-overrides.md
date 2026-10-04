---
id: software.criacao_ia.tranche03.000256
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
fontes: ["https://openusd.org/release/tut_authoring_variants.html", "https://openusd.org/release/tut_referencing_layers.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# OpenUSD: diagnosticar strength entre local opinions e variants

## Em uma frase
O valor composto de uma propriedade é escolhido pela força relativa das opinions, e uma opinion local mais forte pode prevalecer sobre uma opinion de variant.

## Por que importa
Alternar variant sem mudança visível nem sempre indica erro de UI; um override local ou de outra layer pode continuar vencendo. Entender a ordem de composição evita apagar dados de uma variante quando basta localizar e limpar a opinion dominante.

## Como funciona
Inspecione prim stack, edit target e composition arcs para identificar a origem do valor. A documentação usa o exemplo de uma cor local azul mais forte que valores authorados dentro de variants; `Clear()` remove a opinion local no contexto da layer de autoria, permitindo que variant contribua novamente. Referências e ordenação LIVERPS também influenciam o resultado.

## Exemplo
Um material permanece azul ao escolher a variant vermelha. Inspecionar o stack mostra uma opinion local de `displayColor`; limpá-la no layer correto faz a cor da variant voltar a ser visível sem reescrever dados das opções.

## Limites e trade-offs
A força total depende de tipos de arc, ordem de layers, session layer e detalhes do caminho. Não remova uma opinion sem saber qual layer e edit target serão alterados, especialmente em arquivo compartilhado.

## Como verificar
Compare o valor composto antes e depois de `Clear()`, exporte layers relevantes e revise LIVERPS. Teste com session layer ativa e sem ela para evitar atribuir uma opinion temporária ao asset base.

## Conexões
- [[openusd-variants-edit-context]] — OpenUSD: autorar opiniões no variant edit context correto.
- [[openusd-attribute-default-e-time-samples]] — OpenUSD: separar default value de time samples em atributos.

## Fontes
- [OpenUSD 26.08 — Authoring Variants](https://openusd.org/release/tut_authoring_variants.html) — demonstra override local mais forte que variantes e limpeza da opinion Consulta: 2026-10-04.
- [OpenUSD 26.08 — Referencing Layers](https://openusd.org/release/tut_referencing_layers.html) — explica opinions não destrutivas de over e strength ao compor referências Consulta: 2026-10-04.
