---
id: software.criacao_ia.tranche05.000487
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
fontes: ["https://github.com/inkle/ink/blob/master/Documentation/RunningYourInk.md#external-functions", "https://github.com/inkle/ink/blob/master/Documentation/WritingWithInk.md#7-advanced-game-side-logic"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Ink: classificar funções externas como ações ou operações lookahead-safe

## Em uma frase
Funções externas C# podem provocar efeitos colaterais, e a opção `lookaheadSafe` diferencia essas ações de funções puras durante lookahead do runtime.

## Por que importa
O runtime pode avaliar adiante para juntar conteúdo; reproduzir áudio ou alterar mundo durante essa avaliação antecipada pode executar antes da fala ser apresentada.

## Como funciona
Declare `EXTERNAL` no Ink e faça bind em C#; mantenha `lookaheadSafe` false para ações e use true só se a função for idempotente e não alterar estado de jogo.

## Exemplo
`playSound` continua ação insegura para lookahead, enquanto `distance(a,b)` pode ser pura e segura para avaliação antecipada se apenas calcular e retornar valor.

## Limites e trade-offs
Uma função chamada pura não deve ter efeitos colaterais nem ser problemática se executada mais de uma vez; fallback Ink com mesma assinatura pode habilitar preview sem binding do jogo.

## Como verificar
Teste texto colado por glue, confirme que ação só ocorre no momento de apresentação e que função pura mantém resultado estável mesmo quando chamada durante lookahead.

## Conexões
- [[ink-tags-como-metadados-de-conteudo]] — Ink runtime: transportar tags de linha, knot e escolha como metadados invisíveis.
- [[ink-evaluationfunction-call-from-game]] — Ink runtime: chamar função do roteiro com EvaluationFunction sem consumir diálogo.

## Fontes
- [Ink — Running your ink: external functions](https://github.com/inkle/ink/blob/master/Documentation/RunningYourInk.md#external-functions) — Define binding, tipos e distinção entre ações e funções puras com `lookaheadSafe`. Consulta: 2026-10-04.
- [Ink — Writing with Ink: game-side logic](https://github.com/inkle/ink/blob/master/Documentation/WritingWithInk.md#7-advanced-game-side-logic) — Apresenta alternativas de integração de lógica entre roteiro e código do jogo. Consulta: 2026-10-04.
