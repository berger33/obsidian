---
id: software.criacao_ia.tranche05.000485
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
fontes: ["https://github.com/inkle/ink/blob/master/Documentation/RunningYourInk.md#settinggetting-ink-variables", "https://github.com/inkle/ink/blob/master/ink-engine-runtime/VariablesState.cs"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Ink runtime: sincronizar variáveis globais e UI sem polling por frame

## Em uma frase
`variablesState` permite ler e definir globals declaradas em Ink, e observadores podem notificar o jogo quando um valor muda.

## Por que importa
Atualizar HUD reativamente reduz consultas repetidas e mantém valores usados por narrativa e gameplay conectados a um estado autoritativo.

## Como funciona
Acesse `story.variablesState[name]` para getter/setter compatível e registre `ObserveVariable` uma vez no ciclo de configuração; atualize a UI a partir do callback.

## Exemplo
O wrapper observa `health` na criação de Story e modifica o contador visual quando Ink atribui uma nova vida após uma escolha.

## Limites e trade-offs
Atribuição só é aceita para variável global declarada no story; tipos seguem tipos Ink e casts para C# precisam corresponder ao valor recebido.

## Como verificar
Teste variável declarada, valor inicial, alteração por Ink e escrita pelo jogo; confirme que callback acontece na mudança e que o UI não registra observador a cada frame.

## Conexões
- [[ink-save-complete-story-state-json]] — Ink runtime: salvar o estado narrativo completo com state.ToJson.
- [[ink-tags-como-metadados-de-conteudo]] — Ink runtime: transportar tags de linha, knot e escolha como metadados invisíveis.

## Fontes
- [Ink — Running your ink: variables and observers](https://github.com/inkle/ink/blob/master/Documentation/RunningYourInk.md#settinggetting-ink-variables) — Documenta acesso de leitura e escrita por `variablesState`. Consulta: 2026-10-04.
- [Ink — VariablesState runtime source](https://github.com/inkle/ink/blob/master/ink-engine-runtime/VariablesState.cs) — Define indexador de globais e evento de mudança em estado de variáveis. Consulta: 2026-10-04.
