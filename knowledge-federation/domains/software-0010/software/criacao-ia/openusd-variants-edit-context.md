---
id: software.criacao_ia.tranche03.000255
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
fontes: ["https://openusd.org/release/tut_authoring_variants.html", "https://openusd.org/release/api/class_usd_variant_set.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# OpenUSD: autorar opiniões no variant edit context correto

## Em uma frase
Para gravar uma propriedade dentro de uma variant, selecione a variant e direcione a edição ao seu `VariantEditContext`.

## Por que importa
Selecionar uma opção de variant altera a composição, mas não redireciona automaticamente todos os comandos de autoria. Sem edit context, uma gravação pode virar opinion local mais forte e mascarar todas as alternativas da variant set.

## Como funciona
Crie ou acesse `UsdVariantSet`, adicione as opções e selecione a que receberá dados. Use `GetVariantEditContext()` para que `UsdAttribute.Set()` escreva no edit target da variant. Inspecione o root layer e as seleções resultantes depois da gravação; strength ordering decide como essa opinion interage com layers mais fortes.

## Exemplo
Uma variant set `shadingVariant` guarda cores red, blue e green. O script escolhe `red`, entra no variant edit context e grava `displayColor`; depois seleciona green e grava seu valor. A cena troca seleção sem substituir a opinião local da prim.

## Limites e trade-offs
Variants selecionadas podem ser afetadas por opiniões e regras mais fortes, e a variante não é uma cópia independente de toda a cena. O edit context controla destino de autoria, não valida se a propriedade escolhida é semanticamente adequada.

## Como verificar
Exporte a layer como USDA, confirme que opinião aparece sob a chave da variante e alterne seleções. Repita sem edit context para observar como uma local opinion pode sobrepor alternativas.

## Conexões
- [[openusd-asset-resolver-context-identifiers]] — OpenUSD: resolver context e asset identifiers de pipeline.
- [[openusd-opinion-strength-overrides]] — OpenUSD: diagnosticar strength entre local opinions e variants.

## Fontes
- [OpenUSD 26.08 — Authoring Variants](https://openusd.org/release/tut_authoring_variants.html) — demonstra seleção de variant, edit context e efeito de local opinion Consulta: 2026-10-04.
- [OpenUSD 26.08 — UsdVariantSet API](https://openusd.org/release/api/class_usd_variant_set.html) — define operações para criar e selecionar variant sets e variants Consulta: 2026-10-04.
