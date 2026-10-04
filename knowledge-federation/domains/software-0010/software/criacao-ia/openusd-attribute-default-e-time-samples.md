---
id: software.criacao_ia.tranche03.000257
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
fontes: ["https://openusd.org/release/api/class_usd_attribute.html", "https://openusd.org/release/tut_xforms.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# OpenUSD: separar default value de time samples em atributos

## Em uma frase
Um `UsdAttribute` pode armazenar um valor default, valores animados por time samples ou ambos, e a consulta depende do time code solicitado.

## Por que importa
Uma propriedade pode parecer estática quando somente o default foi consultado, ou variar de modo inesperado quando samples e layers se combinam. Em pipelines de animação, separar valor estático e série temporal ajuda a identificar se o dado de fato foi keyframed.

## Como funciona
Use `UsdAttribute.Get()` com `UsdTimeCode.Default()` para consultar default e um time code explícito para consultar animação. Atributos animados podem ser interpolados entre samples segundo a configuração e tipo. Metadados do stage definem faixa de time codes e escala para segundos, que não devem ser confundidos com números de frame sem contexto.

## Exemplo
Uma rotação tem samples nos time codes 1 e 192. O viewer consulta o meio da sequência para obter valor interpolado, enquanto uma ferramenta de exportação também consulta default para verificar se existe valor estático de fallback.

## Limites e trade-offs
Interpolation e disponibilidade dependem de tipo do atributo, samples, blocks e opiniões mais fortes. Time codes são unitless até interpretados com metadados de escala; não presuma que time code 24 significa sempre 1 segundo.

## Como verificar
Liste `GetTimeSamples()`, consulte default e momentos antes, entre e depois dos samples, e inspecione `timeCodesPerSecond`, start/end time code e opiniões por layer.

## Conexões
- [[openusd-opinion-strength-overrides]] — OpenUSD: diagnosticar strength entre local opinions e variants.
- [[openusd-layer-offset-retimar-animacao]] — OpenUSD: retimar animação referenciada com layer offset.

## Fontes
- [OpenUSD 26.08 — UsdAttribute API](https://openusd.org/release/api/class_usd_attribute.html) — define consultas de atributos por default ou time code e presença de time samples Consulta: 2026-10-04.
- [OpenUSD 26.08 — Transformations, Animation, and Layer Offsets](https://openusd.org/release/tut_xforms.html) — demonstra samples de animação e escala de time codes para segundos Consulta: 2026-10-04.
