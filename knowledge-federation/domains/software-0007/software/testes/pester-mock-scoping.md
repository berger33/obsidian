---
id: software.testes.tranche22.001577
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-22.md"
fontes: ["https://pester.dev/docs/usage/mocking", "https://pester.dev/docs/quick-start"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Pester: o mock vale onde foi declarado

## Em uma frase
Desde a reescrita do v5, mocks não são mais válidos no Describe inteiro: eles valem apenas no bloco onde foram colocados, o que torna o It que os declara autossuficiente e o teste vizinho imune.

## Por que importa
O escopo global do v4 obrigava equipes a centralizar mocks em BeforeAll com contaminação difícil de rastrear; escopo por bloco restaura a independência entre casos do mesmo arquivo.

## Como funciona
Declare Mock f { "mock" } dentro de um It e veja o It seguinte receber a função real, como demonstra o exemplo oficial com function f () { "real" } no BeforeAll do Describe.

## Exemplo
It "i" { Mock f { "mock" }; f | Should-Be "mock" } It "j" { f | Should-Be "real" } — duas visões do mesmo comando num mesmo Describe.

## Limites e trade-offs
Mockar comandos chamados dentro de um Script Module exige código adicional, alertado na página com link para a seção de unit testing em módulos.

## Como verificar
Crie dois Its com expectativas opostas sobre o mesmo comando e confirme que a ordem de execução não altera nenhum dos dois resultados.

## Conexões
- [[pester-mock-verification]] — Veja também: Pester: Should-Invoke, -Times e -Verifiable.
- [[pester-mock-advanced]] — Veja também: Pester: natives, $PesterBoundParameters e classes.

## Fontes
- [Pester — Mocking](https://pester.dev/docs/usage/mocking) — Mock, Should-Invoke, escopo, natives e classes; consultado em 2026-10-03.
- [Pester — Quick start](https://pester.dev/docs/quick-start) — mini-DSL, convenção de nomes e primeira execução; consultado em 2026-10-03.
