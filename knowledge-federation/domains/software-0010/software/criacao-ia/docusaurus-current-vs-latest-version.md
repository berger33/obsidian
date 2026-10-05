---
id: software.criacao_ia.tranche05.000476
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
fontes: ["https://docusaurus.io/docs/versioning#overview", "https://docusaurus.io/docs/api/plugins/@docusaurus/plugin-content-docs#configuration"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Docusaurus: distinguir versão current da versão latest usada no navbar

## Em uma frase
A versão `current` é definida pelo conteúdo na pasta `docs`, enquanto `latest` é a versão preferida de navegação configurada pelo plugin.

## Por que importa
Em um ciclo de release, docs em desenvolvimento podem ser `current`, mas o navbar deve direcionar usuários à versão lançada e suportada.

## Como funciona
Revise `lastVersion`, `includeCurrentVersion` e metadados `versions` para escolher qual versão atende `/docs`, qual fica em rota própria e se a versão em andamento será publicada.

## Exemplo
O projeto publica docs v1 como latest em `/docs` enquanto mantém docs v2 em desenvolvimento na rota `/docs/next`.

## Limites e trade-offs
A associação default e rotas podem ser customizadas; não deduza status de release apenas pelo nome de pasta ou label visual.

## Como verificar
Confira rotas geradas e dropdown para docs atuais e versionados e confirme o destino usado por links de navbar em cada estado.

## Conexões
- [[docusaurus-versioning-freeze-current-docs]] — Docusaurus: criar versões de documentação como snapshots deliberados.
- [[docusaurus-version-safe-links-and-imports]] — Docusaurus: manter links e imports válidos quando docs são versionados.

## Fontes
- [Docusaurus — Versioning terminology and routes](https://docusaurus.io/docs/versioning#overview) — Define current pela pasta docs e latest pela navegação e mostra URLs padrões. Consulta: 2026-10-04.
- [Docusaurus — plugin-content-docs configuration](https://docusaurus.io/docs/api/plugins/@docusaurus/plugin-content-docs#configuration) — Define `lastVersion`, `includeCurrentVersion` e personalização de versões. Consulta: 2026-10-04.
