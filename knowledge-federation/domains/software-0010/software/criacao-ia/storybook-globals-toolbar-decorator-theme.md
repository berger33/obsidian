---
id: software.criacao_ia.tranche05.000464
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
fontes: ["https://storybook.js.org/docs/essentials/toolbars-and-globals", "https://storybook.js.org/docs/writing-stories/args"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Storybook: usar globals e toolbar para variar contexto compartilhado como tema

## Em uma frase
Globals representam entradas de renderização não específicas de uma story e costumam ser consumidos por decorators, separados do objeto args.

## Por que importa
Tema, locale ou viewport podem mudar o contexto de várias histórias; armazenar isso em props individuais mistura estado ambiental com API do componente.

## Como funciona
Declare `globalTypes` e `initialGlobals` no preview, exponha as opções por toolbar e leia `context.globals` no decorator para envolver stories em providers apropriados.

## Exemplo
Uma toolbar alterna `light` e `dark`; um decorator lê o global `theme` e fornece o tema correspondente sem adicionar prop artificial a cada componente.

## Limites e trade-offs
Um `globals` definido em story ou meta fixa o valor e desativa aquele controle da toolbar para a story; use override apenas quando o cenário exige valor constante.

## Como verificar
Alterne a toolbar em várias stories, confirme rerender e verifique que valores definidos por story ficam travados como previsto.

## Conexões
- [[storybook-typescript-meta-storyobj-satisfies]] — Storybook TypeScript: ligar Meta e StoryObj com satisfies para checar args.
- [[storybook-loaders-before-render-loaded-context]] — Storybook: usar loaders assíncronos como escape hatch para dados externos.

## Fontes
- [Storybook — Toolbars & globals](https://storybook.js.org/docs/essentials/toolbars-and-globals) — Define globals, configuração de toolbar, acesso por context e uso em decorator. Consulta: 2026-10-04.
- [Storybook — Args](https://storybook.js.org/docs/writing-stories/args) — Explica por que globals são preferíveis a args para algumas configurações compartilhadas. Consulta: 2026-10-04.
