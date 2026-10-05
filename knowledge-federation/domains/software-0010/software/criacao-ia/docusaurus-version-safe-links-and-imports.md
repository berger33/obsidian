---
id: software.criacao_ia.tranche05.000477
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
fontes: ["https://docusaurus.io/docs/versioning#recommended-practices", "https://docusaurus.io/docs/markdown-features/assets"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Docusaurus: manter links e imports válidos quando docs são versionados

## Em uma frase
Links relativos a outros arquivos `.md` são reescritos para a versão correspondente, enquanto imports compartilhados devem usar alias `@site` em vez de caminhos relativos.

## Por que importa
Ao copiar um arquivo para outra profundidade ou pasta de versão, caminhos relativos a componentes podem quebrar ou resolver para conteúdo da versão errada.

## Como funciona
Ligue documentos por caminho relativo com extensão Markdown e importe código compartilhado com `@site/...`; reserve caminhos relativos para assets que realmente são versionados junto ao documento.

## Exemplo
Uma página linka `../setup/install.md` para preservar o alvo da versão e importa um componente compartilhado com `@site/src/components/Callout`.

## Limites e trade-offs
Assets podem ser específicos da versão ou globais: a escolha determina usar caminho relativo no conteúdo versionado ou recurso em `/static`.

## Como verificar
Gere rotas para duas versões, siga links entre documentos de cada versão, importe componentes e teste imagens e downloads no build final.

## Conexões
- [[docusaurus-current-vs-latest-version]] — Docusaurus: distinguir versão current da versão latest usada no navbar.
- [[docusaurus-docs-multi-instance-unique-id]] — Docusaurus: configurar instâncias do plugin docs para catálogos independentes.

## Fontes
- [Docusaurus — Versioning recommended practices](https://docusaurus.io/docs/versioning#recommended-practices) — Recomenda links relativos `.md` entre docs e alias `@site` para imports compartilhados. Consulta: 2026-10-04.
- [Docusaurus — Markdown assets](https://docusaurus.io/docs/markdown-features/assets) — Explica caminhos relativos para assets collocated e como arquivos são transformados em URLs. Consulta: 2026-10-04.
