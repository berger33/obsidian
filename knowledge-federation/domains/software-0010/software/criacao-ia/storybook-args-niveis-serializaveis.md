---
id: software.criacao_ia.tranche05.000462
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
fontes: ["https://storybook.js.org/docs/writing-stories/args", "https://storybook.js.org/docs/essentials/toolbars-and-globals"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Storybook: distribuir args por story e componente sem guardar estado global em props

## Em uma frase
Args são valores serializáveis que configuram a renderização; podem ser definidos por história, componente ou global e alterações atualizam o componente.

## Por que importa
Uma hierarquia explícita reduz duplicação e deixa controles do Storybook editar props sem modificar o componente de produção.

## Como funciona
Coloque valores exclusivos no `args` da história, defaults compartilhados no meta do componente e configurações globais adequadas no preview; prefira `globals` com toolbar para opções realmente globais como tema.

## Exemplo
Stories `Primary` e `Disabled` compartilham label no meta, variam `primary` individualmente e usam um global de tema para trocar contexto visual da biblioteca.

## Limites e trade-offs
O objeto args precisa ser JSON-serializável; callbacks e valores complexos de framework podem exigir mapeamento ou outra solução em vez de controle direto.

## Como verificar
Altere um controle no painel, confirme rerender e valide precedência entre nível global, meta e story; teste que URL e addons continuam serializando os valores necessários.

## Conexões
- [[storybook-csf-default-meta-named-stories]] — Storybook: organizar CSF com meta default e histórias como exports nomeados.
- [[storybook-typescript-meta-storyobj-satisfies]] — Storybook TypeScript: ligar Meta e StoryObj com satisfies para checar args.

## Fontes
- [Storybook — Args](https://storybook.js.org/docs/writing-stories/args) — Define níveis de args, serialização JSON e rerenderização quando seus valores mudam. Consulta: 2026-10-04.
- [Storybook — Toolbars & globals](https://storybook.js.org/docs/essentials/toolbars-and-globals) — Distingue globals de args e mostra controle por toolbar e decorators. Consulta: 2026-10-04.
