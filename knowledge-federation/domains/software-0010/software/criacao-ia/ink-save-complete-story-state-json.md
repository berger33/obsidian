---
id: software.criacao_ia.tranche05.000484
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
fontes: ["https://github.com/inkle/ink/blob/master/Documentation/RunningYourInk.md#saving-and-loading", "https://github.com/inkle/ink/blob/master/ink-engine-runtime/StoryState.cs"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Ink runtime: salvar o estado narrativo completo com state.ToJson

## Em uma frase
`Story.state.ToJson()` serializa estado narrativo além das variáveis globais, incluindo ponto de execução, contagens e estruturas de chamada.

## Por que importa
Salvar só flags de gameplay não restaura em qual trecho o leitor estava, que escolhas foram vistas nem os contadores usados por lógica da narrativa.

## Como funciona
Armazene o JSON produzido por `story.state.ToJson()` e recarregue na instância apropriada com `story.state.LoadJson(savedJson)`; mantenha junto a identificação do jogo e da versão do conteúdo.

## Exemplo
Ao salvar partida, a aplicação grava estado Ink em um campo separado do inventário e ao carregar constrói Story com o JSON do conteúdo antes de restaurar o estado salvo.

## Limites e trade-offs
Formato de save é versionado internamente e evolui; a documentação não define política de migração do arquivo de save da aplicação ou compatibilidade com alterações semânticas do roteiro.

## Como verificar
Salve após uma escolha e variável, recrie Story, carregue JSON e confirme a próxima linha, escolhas, globals e visit counts esperados.

## Conexões
- [[ink-current-choices-and-choice-index]] — Ink runtime: apresentar currentChoices e retomar com ChooseChoiceIndex.
- [[ink-variables-state-and-observers]] — Ink runtime: sincronizar variáveis globais e UI sem polling por frame.

## Fontes
- [Ink — Running your ink: saving and loading](https://github.com/inkle/ink/blob/master/Documentation/RunningYourInk.md#saving-and-loading) — Dá as chamadas públicas ToJson e LoadJson para salvar e restaurar estado. Consulta: 2026-10-04.
- [Ink — StoryState source](https://github.com/inkle/ink/blob/master/ink-engine-runtime/StoryState.cs) — Descreve o estado completo serializado e mantém versão interna do formato JSON. Consulta: 2026-10-04.
