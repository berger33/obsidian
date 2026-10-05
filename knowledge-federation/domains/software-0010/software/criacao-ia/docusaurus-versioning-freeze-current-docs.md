---
id: software.criacao_ia.tranche05.000475
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
fontes: ["https://docusaurus.io/docs/versioning", "https://docusaurus.io/docs/api/plugins/@docusaurus/plugin-content-docs"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Docusaurus: criar versões de documentação como snapshots deliberados

## Em uma frase
O comando `docs:version` copia o conteúdo e sidebar atuais para uma versão marcada, deixando `docs/` livre para evolução posterior.

## Por que importa
Uma versão publicada de produto pode precisar de instruções imutáveis mesmo quando a documentação de desenvolvimento muda para o próximo release.

## Como funciona
Revise `docs/` antes de congelar, rode `docusaurus docs:version <versão>` e inspecione a nova pasta `versioned_docs`, o sidebar versionado e a entrada em `versions.json`.

## Exemplo
Antes de iniciar documentação para v2, marque v1.4.0; os arquivos e sidebar de v1.4.0 passam a ser mantidos no snapshot correspondente.

## Limites e trade-offs
O versionamento aumenta arquivos, build time e custo de contribuição; a documentação recomenda usá-lo quando releases de docs mudam com frequência ou tráfego exige suporte por release.

## Como verificar
Compare conteúdo copiado com a versão em produção, navegue pelo seletor e confirme que edição de docs atuais não altera a página congelada.

## Conexões
- [[docusaurus-sidebar-association-pagination]] — Docusaurus: fixar associação de múltiplas sidebars com displayed_sidebar.
- [[docusaurus-current-vs-latest-version]] — Docusaurus: distinguir versão current da versão latest usada no navbar.

## Fontes
- [Docusaurus — Versioning](https://docusaurus.io/docs/versioning) — Descreve snapshot via CLI e arquivos de docs, sidebars e versions.json criados. Consulta: 2026-10-04.
- [Docusaurus — plugin-content-docs](https://docusaurus.io/docs/api/plugins/@docusaurus/plugin-content-docs) — Lista opções para habilitar, limitar e configurar versões no plugin. Consulta: 2026-10-04.
