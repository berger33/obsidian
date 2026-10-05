---
id: software.criacao_ia.tranche05.000482
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

# Ink runtime: escolher Continue ou ContinueMaximally pela granularidade da interface

## Em uma frase
`Continue()` devolve uma unidade de texto por passo, enquanto `ContinueMaximally()` consome conteúdo disponível em uma única chamada.

## Por que importa
Um diálogo que anima uma linha ou aplica efeitos de UI entre linhas não deve avançar a história além do ponto em que a interface consegue apresentar estado.

## Como funciona
Repita `Continue()` enquanto `canContinue` para exibir e processar linha a linha; use `ContinueMaximally()` quando a aplicação realmente quiser concatenar todo o conteúdo antes de apresentar escolhas.

## Exemplo
Uma visual novel chama `Continue()` uma vez por clique, lê `currentText` e `currentTags`, e pede nova interação antes de continuar; uma ferramenta de transcript pode usar ContinueMaximally.

## Limites e trade-offs
A sequência de interação do jogo pode não coincidir com os passos internos do Ink; variáveis ou tags intermediárias podem precisar ser aplicadas no momento correto.

## Como verificar
Crie uma cena com várias linhas e efeitos entre elas, confirme que a UI não consome conteúdo cedo demais e compare com modo de transcrição completa.

## Conexões
- [[ink-compile-json-story-runtime]] — Ink: compilar arquivos .ink para JSON e carregar uma instância Story.
- [[ink-current-choices-and-choice-index]] — Ink runtime: apresentar currentChoices e retomar com ChooseChoiceIndex.

## Fontes
- [Ink — Running your ink: runtime API](https://github.com/inkle/ink/blob/master/Documentation/RunningYourInk.md#getting-started-with-the-runtime-api) — Descreve loop `canContinue`, ContinueMaximally e escolha de pausar por linha. Consulta: 2026-10-04.
- [Ink — Story runtime source](https://github.com/inkle/ink/blob/master/ink-engine-runtime/Story.cs) — Define estado atual de texto e escolhas gerados durante a execução de Continue. Consulta: 2026-10-04.
