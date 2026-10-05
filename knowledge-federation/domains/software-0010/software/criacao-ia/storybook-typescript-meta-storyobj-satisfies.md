---
id: software.criacao_ia.tranche05.000463
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
fontes: ["https://storybook.js.org/docs/writing-stories/typescript", "https://storybook.js.org/docs/writing-stories"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Storybook TypeScript: ligar Meta e StoryObj com satisfies para checar args

## Em uma frase
Os tipos `Meta` e `StoryObj` conectam propriedades do componente às stories, e `satisfies` preserva inferência enquanto verifica compatibilidade.

## Por que importa
Erros de propriedades ausentes ou inválidas aparecem no editor e no build em vez de só surgir quando a story é aberta.

## Como funciona
Tipifique metadata como `satisfies Meta<typeof Component>`, derive `StoryObj<typeof meta>` e aplique `satisfies Story` aos exports de story; use tipo de interseção quando houver args customizados.

## Exemplo
Uma story `Button` deriva o tipo de `meta`, e `Primary` recebe `args` com `primary` e `label` validados contra as props do componente.

## Limites e trade-offs
O recurso de inferência via `satisfies` requer TypeScript 4.9 ou superior; CSF Next está indicado como preview nas docs consultadas, não como API estável universal.

## Como verificar
Rode typecheck com prop obrigatória omitida, valor inválido e arg customizado; confirme que a conexão entre Meta e StoryObj sinaliza os três casos.

## Conexões
- [[storybook-args-niveis-serializaveis]] — Storybook: distribuir args por story e componente sem guardar estado global em props.
- [[storybook-globals-toolbar-decorator-theme]] — Storybook: usar globals e toolbar para variar contexto compartilhado como tema.

## Fontes
- [Storybook — Writing stories in TypeScript](https://storybook.js.org/docs/writing-stories/typescript) — Documenta `Meta`, `StoryObj`, `satisfies` e inferência de args. Consulta: 2026-10-04.
- [Storybook — How to write stories](https://storybook.js.org/docs/writing-stories) — Mostra padrão de meta tipado e story com args em CSF. Consulta: 2026-10-04.
