---
id: software.criacao_ia.tranche05.000474
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-05.md"
fontes: ["https://docusaurus.io/docs/sidebar/multiple-sidebars", "https://docusaurus.io/docs/api/plugins/@docusaurus/plugin-content-docs#markdown-front-matter"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Docusaurus: fixar associação de múltiplas sidebars com displayed_sidebar

## Em uma frase
Quando um documento aparece em mais de um sidebar, sua sidebar exibida não é garantida sem front matter `displayed_sidebar`.

## Por que importa
A sidebar ativa também dirige links anterior e próximo; associação ambígua pode mostrar navegação incompatível com a seção em que o leitor está.

## Como funciona
Configure `displayed_sidebar` com o ID do sidebar que deve ser mostrado. Para apenas criar um link adicional sem alterar associação ou paginação, use um item `ref` na sidebar secundária.

## Exemplo
Uma referência compartilhada fica como `doc` na sidebar principal de API e como `ref` no tutorial; seu front matter fixa a sidebar de API e a sequência local.

## Limites e trade-offs
`displayed_sidebar: null` remove sidebar e paginação; uma sidebar forçada que não contém o doc também não gera paginação para ele.

## Como verificar
Abra o mesmo doc a partir de cada seção e confira sidebar, links anterior/próximo e efeito de itens `ref` na navegação.

## Conexões
- [[docusaurus-sidebar-position-frontmatter]] — Docusaurus: controlar ordem de sidebar automática com sidebar_position.
- [[docusaurus-versioning-freeze-current-docs]] — Docusaurus: criar versões de documentação como snapshots deliberados.

## Fontes
- [Docusaurus — Using multiple sidebars](https://docusaurus.io/docs/sidebar/multiple-sidebars) — Explica associação indeterminada, override por displayed_sidebar, paginação e tipo ref. Consulta: 2026-10-04.
- [Docusaurus — plugin-content-docs front matter](https://docusaurus.io/docs/api/plugins/@docusaurus/plugin-content-docs#markdown-front-matter) — Define campos `displayed_sidebar`, `pagination_next` e `pagination_prev`. Consulta: 2026-10-04.
