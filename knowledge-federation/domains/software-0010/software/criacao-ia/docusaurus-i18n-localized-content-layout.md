---
id: software.criacao_ia.tranche05.000480
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
fontes: ["https://docusaurus.io/docs/i18n/introduction", "https://docusaurus.io/docs/api/docusaurus-config#i18n"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Docusaurus i18n: localizar conteúdo por locale sem supor detecção automática

## Em uma frase
O fluxo i18n configura locales, coloca traduções em diretórios específicos e faz build/deploy por locale, mas não detecta automaticamente a língua do visitante.

## Por que importa
Roteamento por idioma, traduções de interface e Markdown são responsabilidades diferentes; presumir redirecionamento automático pode frustrar usuários e indexação.

## Como funciona
Declare `defaultLocale` e `locales`, traduza docs completos em `i18n/<locale>/docusaurus-plugin-content-docs/...` e textos de componentes em arquivos `code.json`; decida estratégia de domínio e seleção no host/site.

## Exemplo
Um site com `en` e `fr` mantém tradução francesa do guia no diretório docs do plugin e strings de navbar no `i18n/fr/code.json` ou arquivos de tema relevantes.

## Limites e trade-offs
O sistema não fornece detecção automática de locale nem tradução de slugs; localização de arquivos para plugin multi-instância inclui seu plugin ID.

## Como verificar
Construa locale default e secundário, verifique links/labels traduzidos e `hreflang`, e teste separadamente a política de seleção ou redirecionamento no host.

## Conexões
- [[docusaurus-mdx-vs-commonmark-format]] — Docusaurus: escolher formato MDX ou CommonMark conforme a sintaxe dos docs.

## Fontes
- [Docusaurus — i18n introduction](https://docusaurus.io/docs/i18n/introduction) — Expõe metas e não-metas de i18n, estrutura de arquivos e ausência de detecção automática. Consulta: 2026-10-04.
- [Docusaurus — i18n configuration](https://docusaurus.io/docs/api/docusaurus-config#i18n) — Define a configuração de locale padrão e alternativas no arquivo do site. Consulta: 2026-10-04.
