---
id: software.criacao_ia.tranche05.000486
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
fontes: ["https://github.com/inkle/ink/blob/master/Documentation/RunningYourInk.md#marking-up-your-ink-content-with-tags", "https://github.com/inkle/ink/blob/master/ink-engine-runtime/Story.cs"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Ink runtime: transportar tags de linha, knot e escolha como metadados invisíveis

## Em uma frase
Tags adicionam metadados não destinados ao texto do jogador e podem ser lidas em linhas, knots, escolhas ou no nível global.

## Por que importa
Um roteiro pode referenciar locução, expressão de personagem, local ou diretiva sem codificar esse metadado em texto visível ao jogador.

## Como funciona
Leia `currentTags` depois de `Continue()` para metadados daquela linha, `globalTags` para dados do story e `TagsForContentAtPath` para obter tags de knot antes de entrar nele; tags de escolha ficam no objeto Choice.

## Exemplo
Uma linha `Passepartout: Really, Monsieur. # surly` chega como fala enquanto a UI usa `currentTags` para selecionar retrato surly.

## Limites e trade-offs
Conteúdo de tag também pode ser dinâmico; estabeleça schema e validação no consumidor do jogo em vez de assumir que toda tag é uma string fixa conhecida.

## Como verificar
Adicione tag de linha, escolha, knot e global ao fixture, inspecione cada API no momento apropriado e confirme que tags não são mostradas como fala.

## Conexões
- [[ink-variables-state-and-observers]] — Ink runtime: sincronizar variáveis globais e UI sem polling por frame.
- [[ink-external-functions-lookahead-safe]] — Ink: classificar funções externas como ações ou operações lookahead-safe.

## Fontes
- [Ink — Running your ink: tags](https://github.com/inkle/ink/blob/master/Documentation/RunningYourInk.md#marking-up-your-ink-content-with-tags) — Descreve tags por escopo e APIs `currentTags`, `globalTags` e TagsForContentAtPath. Consulta: 2026-10-04.
- [Ink — Story currentTags API](https://github.com/inkle/ink/blob/master/ink-engine-runtime/Story.cs) — Define currentTags como tags vistas durante a chamada mais recente de Continue. Consulta: 2026-10-04.
