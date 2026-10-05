---
id: software.criacao_ia.tranche05.000488
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
fontes: ["https://github.com/inkle/ink/blob/master/Documentation/RunningYourInk.md#running-functions", "https://github.com/inkle/ink/blob/master/ink-engine-runtime/Story.cs"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Ink runtime: chamar função do roteiro com EvaluationFunction sem consumir diálogo

## Em uma frase
`EvaluationFunction` executa diretamente uma função Ink chamada pelo jogo e retorna valor sem exigir `Continue()` para percorrer linhas da função.

## Por que importa
Cálculos de regras narrativas podem permanecer no roteiro enquanto o jogo solicita um resultado pontual sem alterar a sequência de diálogo exibida.

## Como funciona
Chame `EvaluationFunction` com nome e argumentos e capture `textOutput` se a função produzir conteúdo; defina funções no Ink com responsabilidade clara de retorno.

## Exemplo
Um sistema pergunta `calculateEndingScore` ao completar capítulo e usa retorno numérico para determinar rank sem inserir texto auxiliar no diálogo.

## Limites e trade-offs
Texto emitido durante a execução é devolvido em `textOutput` em vez de passar pela interface normal; não trate essa chamada como avanço de conteúdo para o jogador.

## Como verificar
Crie função com argumentos, retorno e linha de texto, chame pela API e confira valor retornado, textOutput e que a próxima linha pública permaneça correta.

## Conexões
- [[ink-external-functions-lookahead-safe]] — Ink: classificar funções externas como ações ou operações lookahead-safe.
- [[ink-precompile-include-filehandler]] — Ink: preferir compilação prévia e configurar includes no fluxo de compilação C#.

## Fontes
- [Ink — Running your ink: running functions](https://github.com/inkle/ink/blob/master/Documentation/RunningYourInk.md#running-functions) — Documenta EvaluationFunction, argumentos, retorno e output de texto. Consulta: 2026-10-04.
- [Ink — Story runtime source](https://github.com/inkle/ink/blob/master/ink-engine-runtime/Story.cs) — Implementa API de Story para avaliação de funções e estado de execução. Consulta: 2026-10-04.
