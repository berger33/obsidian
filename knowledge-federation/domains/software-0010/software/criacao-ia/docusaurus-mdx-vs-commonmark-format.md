---
id: software.criacao_ia.tranche05.000479
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
fontes: ["https://docusaurus.io/docs/markdown-features#mdx-vs-commonmark", "https://docusaurus.io/docs/api/docusaurus-config#markdown"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Docusaurus: escolher formato MDX ou CommonMark conforme a sintaxe dos docs

## Em uma frase
Docusaurus 3 compila Markdown e MDX com o compilador MDX, usando formato MDX por padrão e permitindo opt-in experimental a CommonMark.

## Por que importa
Texto com JSX ou sintaxe ambígua pode compilar de modo diferente entre formatos, então a extensão `.md` sozinha não garante parser CommonMark.

## Como funciona
Use padrão MDX se docs inserem componentes JSX; para CommonMark configure `markdown.format` ou front matter `mdx.format: md`, e avalie `detect` se `.md` e `.mdx` tiverem papéis distintos.

## Exemplo
Uma página `.mdx` importa um componente React interativo; documentação textual `.md` usa CommonMark em configuração `detect` após validar plugins e exemplos.

## Limites e trade-offs
O suporte CommonMark é declarado experimental nas docs v3.10.2 e possui limitações; outros plugins remark/rehype podem alterar parsing e render.

## Como verificar
Compile exemplos representativos de JSX, autolinks, tabelas e directives no formato escolhido e inspecione erros e saída renderizada.

## Conexões
- [[docusaurus-docs-multi-instance-unique-id]] — Docusaurus: configurar instâncias do plugin docs para catálogos independentes.
- [[docusaurus-i18n-localized-content-layout]] — Docusaurus i18n: localizar conteúdo por locale sem supor detecção automática.

## Fontes
- [Docusaurus — Markdown features, MDX vs CommonMark](https://docusaurus.io/docs/markdown-features#mdx-vs-commonmark) — Define formato padrão MDX, opções de CommonMark e o status experimental. Consulta: 2026-10-04.
- [Docusaurus — Markdown configuration](https://docusaurus.io/docs/api/docusaurus-config#markdown) — Documenta `markdown.format` e como configurar formatos para o site. Consulta: 2026-10-04.
