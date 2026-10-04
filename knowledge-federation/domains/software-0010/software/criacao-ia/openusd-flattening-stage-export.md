---
id: software.criacao_ia.tranche03.000259
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
fontes: ["https://openusd.org/release/tut_authoring_variants.html", "https://openusd.org/release/api/class_usd_stage.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# OpenUSD: flattening exporta resultado composto, não estrutura editável

## Em uma frase
Exportar um stage flattenado materializa a descrição de cena composta depois de avaliar operators como variants, em vez de preservar esses operators.

## Por que importa
Flattening é útil para entregar uma cena consolidada, mas perde a estrutura que permitia trocar variantes, inspecionar referências e separar autoria por layers. Tratar o resultado como backup equivalente da composição torna uma pipeline difícil de editar e reconciliar.

## Como funciona
Mantenha arquivos de layers e arcs como fonte editável. Use exportação flattenada quando o consumidor precisar do resultado resolvido e documente que composition operators foram avaliados. Se a saída deve conservar variants ou references para edição posterior, exporte as layers relevantes e não substitua o projeto pela representação plana.

## Exemplo
Uma entrega para preview cria um USDA flattenado da seleção de variante atual. O arquivo fonte preserva variant sets e reference arcs; a equipe salva ambos e usa o flatten apenas como snapshot de render, com metadata que identifica a revisão e seleção usada.

## Limites e trade-offs
Flattening não implica automaticamente converter todos os tipos de dados a outro formato nem elimina a necessidade de resolver assets. O conteúdo final ainda depende de load state, selections, resolver context e configuração do stage usada no momento da exportação.

## Como verificar
Compare arquivos antes e depois, procure `variantSet`, `references` e outros arcs na saída, reabra stage e alterne uma variante. Confirme que snapshot reproduz o valor composto esperado para o conjunto carregado.

## Conexões
- [[openusd-layer-offset-retimar-animacao]] — OpenUSD: retimar animação referenciada com layer offset.
- [[openusd-stage-units-up-axis-metadata]] — OpenUSD: harmonizar upAxis, metersPerUnit e timeCodesPerSecond.

## Fontes
- [OpenUSD 26.08 — Authoring Variants](https://openusd.org/release/tut_authoring_variants.html) — mostra `UsdStage.ExportToString` flattenando variants avaliadas Consulta: 2026-10-04.
- [OpenUSD 26.08 — UsdStage API](https://openusd.org/release/api/class_usd_stage.html) — documenta operações de exportação e flattening do stage Consulta: 2026-10-04.
