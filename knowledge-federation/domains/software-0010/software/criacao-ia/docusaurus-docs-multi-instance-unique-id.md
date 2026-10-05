---
id: software.criacao_ia.tranche05.000478
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
fontes: ["https://docusaurus.io/docs/docs-multi-instance", "https://docusaurus.io/docs/api/plugins/@docusaurus/plugin-content-docs#configuration"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Docusaurus: configurar instâncias do plugin docs para catálogos independentes

## Em uma frase
Vários conjuntos de documentação com rotas ou ciclos de release próprios podem ser mantidos por instâncias distintas de `plugin-content-docs`.

## Por que importa
Um produto com documentação Android, iOS ou páginas de comunidade pode exigir navegação e versões que não pertencem ao mesmo catálogo.

## Como funciona
Configure instâncias com `path`, `routeBasePath` e `sidebarPath` distintos e atribua um `id` único a cada instância adicional; configure itens de navbar com `docsPluginId` quando aplicável.

## Exemplo
A instância default atende documentação de produto versionada; uma instância `community` serve `/community` sem versão própria e usa outra sidebar.

## Limites e trade-offs
O preset classic já inclui uma instância docs. Se cada catálogo for muito grande, a documentação aconselha considerar sites Docusaurus separados para evitar rebuild desnecessário.

## Como verificar
Execute CLI para listar comandos de versionamento, gere as duas rotas e confirme que navbar, sidebars e arquivos de versão se referem à instância correta.

## Conexões
- [[docusaurus-version-safe-links-and-imports]] — Docusaurus: manter links e imports válidos quando docs são versionados.
- [[docusaurus-mdx-vs-commonmark-format]] — Docusaurus: escolher formato MDX ou CommonMark conforme a sintaxe dos docs.

## Fontes
- [Docusaurus — Docs multi-instance](https://docusaurus.io/docs/docs-multi-instance) — Mostra IDs, paths, routes e versionamento independentes para cada instância. Consulta: 2026-10-04.
- [Docusaurus — plugin-content-docs configuration](https://docusaurus.io/docs/api/plugins/@docusaurus/plugin-content-docs#configuration) — Lista opções do plugin usadas para configurar instâncias e conteúdo. Consulta: 2026-10-04.
