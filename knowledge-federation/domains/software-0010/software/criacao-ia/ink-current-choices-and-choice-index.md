---
id: software.criacao_ia.tranche05.000483
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
fontes: ["https://github.com/inkle/ink/blob/master/Documentation/RunningYourInk.md#getting-started-with-the-runtime-api", "https://github.com/inkle/ink/blob/master/ink-engine-runtime/Story.cs"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Ink runtime: apresentar currentChoices e retomar com ChooseChoiceIndex

## Em uma frase
Depois que `canContinue` fica falso, `currentChoices` contém as opções apresentáveis e `ChooseChoiceIndex` seleciona a opção pela posição na lista atual.

## Por que importa
Separar geração de texto e entrada do jogador evita exibir escolhas antigas ou selecionar uma alternativa antes do runtime concluir o trecho.

## Como funciona
Avance a narrativa até `canContinue` ser false, renderize cada `Choice.text` com o índice atual e passe o índice escolhido a `ChooseChoiceIndex`; retome o ciclo de Continue.

## Exemplo
Um painel cria um botão por item de `currentChoices` e seu callback guarda o índice daquele ciclo para chamar `ChooseChoiceIndex(index)` após clique.

## Limites e trade-offs
Choices são geradas durante Continue e algumas escolhas invisíveis não aparecem na lista externa; não persista somente o índice sem identificar estado narrativo associado.

## Como verificar
Teste nenhuma escolha, uma escolha, várias escolhas condicionais e escolha invisível; confirme que índice exibido corresponde ao índice passado ao runtime.

## Conexões
- [[ink-continue-output-granularity]] — Ink runtime: escolher Continue ou ContinueMaximally pela granularidade da interface.
- [[ink-save-complete-story-state-json]] — Ink runtime: salvar o estado narrativo completo com state.ToJson.

## Fontes
- [Ink — Running your ink: runtime API](https://github.com/inkle/ink/blob/master/Documentation/RunningYourInk.md#getting-started-with-the-runtime-api) — Explica obter `currentChoices`, apresentar opções e chamar ChooseChoiceIndex. Consulta: 2026-10-04.
- [Ink — Story currentChoices API](https://github.com/inkle/ink/blob/master/ink-engine-runtime/Story.cs) — Documenta quando a lista é preenchida e o tratamento de escolhas default invisíveis. Consulta: 2026-10-04.
