---
id: software.testes.tranche23.001697
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-23.md"
fontes: ["https://go.dev/doc/security/fuzz/", "https://go.dev/doc/tutorial/fuzz"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# O que conta como falha — inclusive o timeout de um segundo

## Em uma frase
A seção Failing input lista as quatro causas de falha durante o fuzzing: panic no código ou no teste; chamada a t.Fail (inclusive via t.Error/t.Fatal); erro não recuperável como os.Exit ou stack overflow; e o alvo ter demorado demais — o timeout de execução do fuzz target é atualmente 1 segundo, podendo capturar deadlock ou loop infinito, ou comportamento intencional lento.

## Por que importa
A regra dos um segundo é a mais surpreendente e a mais formatadora: ela obriga targets rápidos, como a seção Suggestions recomenda para o motor trabalhar eficiente, e transforma hangs em falhas detectáveis sem wall-clock monitorado.

## Como funciona
A doc amarra as recomendações ao contrato: targets devem ser rápidos e determinísticos para permitir reprodução fácil de novas falhas e cobertura; e como o target roda em paralelo entre workers em ordem não determinística, estado não pode persistir além de cada chamada nem depender de estado global.

## Exemplo
Faça um fuzz target com select que nunca satisfaz, confirme a falha por timeout de 1s no log e repita o input manualmente com t.Log para ver que o problema se reproduz como teste comum.

## Limites e trade-offs
Um bug legítimo em código lento por design conta como timeout, não como crash limpo — a página admite que a lentidão intencional também dispara o caso; para alvos que precisam ser pesados, a doc não oferece knob do timeout do target, só os de minimização e duração.

## Como verificar
Abra a subseção Failing input e a seção Suggestions da página Go Fuzzing e confira as quatro causas, a frase do timeout de 1 segundo e as duas sugestões de determinismo.

## Conexões
- [[gofuzz-output-metrics]] — Veja também: Lendo a saída do motor: execs, new interesting e baseline.
- [[gofuzz-minimization-regression]] — Veja também: Minimização automática e a falha que vira teste permanente.

## Fontes
- [Go — Go Fuzzing (documentação oficial)](https://go.dev/doc/security/fuzz/) — requisitos, modos, saída, falhas, minimização, formato do corpus e glossário; consultado em 2026-10-03.
- [Go — Tutorial: Fuzzing with Go](https://go.dev/doc/tutorial/fuzz) — tutorial profundo indicado na seção Resources da doc oficial; consultado em 2026-10-03.
