---
id: software.criacao_ia.tranche05.000461
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
fontes: ["https://storybook.js.org/docs/writing-stories", "https://storybook.js.org/docs/api/csf"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Storybook: organizar CSF com meta default e histórias como exports nomeados

## Em uma frase
Component Story Format representa a configuração do componente no export default e cada estado exibível como um export nomeado do módulo.

## Por que importa
A estrutura baseada em módulos é portátil entre ferramentas, fácil de revisar e oferece entradas consistentes para addons, documentação e testes.

## Como funciona
Crie um arquivo `.stories` próximo ao componente, exporte `meta` por default e descreva estados como `Primary`, `Loading` ou `Empty` em exports nomeados; derive título de `component` ou mantenha título legível estaticamente.

## Exemplo
`Button.stories.ts` exporta `meta` com `component: Button` e estados `Primary` e `Disabled`, cada um com seus próprios args.

## Limites e trade-offs
Arquivos de história são desenvolvimento-only segundo o guia; exports e metadados precisam respeitar regras de análise estática do builder.

## Como verificar
Inicie Storybook, confirme agrupamento e nomes no sidebar e verifique que cada export aparece no catálogo sem ser incluído no bundle de produção.

## Conexões
- [[storybook-args-niveis-serializaveis]] — Storybook: distribuir args por story e componente sem guardar estado global em props.

## Fontes
- [Storybook — How to write stories](https://storybook.js.org/docs/writing-stories) — Define CSF, metadados default, exports nomeados e localização dos arquivos de história. Consulta: 2026-10-04.
- [Storybook — Component Story Format](https://storybook.js.org/docs/api/csf) — Apresenta a especificação modular que padroniza meta e definições de story. Consulta: 2026-10-04.
