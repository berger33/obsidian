---
id: software.testes.tranche22.001576
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

# Pester: Should-Invoke, -Times e -Verifiable

## Em uma frase
A verificação de comportamento fica no Should-Invoke: ele checa se um comando mockado foi chamado, quantas vezes e com quais parâmetros, e a variante -Verifiable cobra ao final todos os mocks marcados como verificáveis.

## Por que importa
Testes de infraestrutura raramente ligam para o valor de retorno — o que importa é que a chamada certa aconteceu com o argumento certo; verificação de comportamento é o que falta para esse caso.

## Como funciona
Marque Mock Build {} -Verifiable -ParameterFilter {$version -eq 1.2} e feche o cenário com Should-Invoke -Verifiable; para a ausência, escreva Should-Invoke -CommandName Build -Times 0 -ParameterFilter {$version -eq 1.1}.

## Exemplo
O Context 'When there are no Changes' afirma exatamente que Build não foi chamado com 1.1 — uma asserção negativa documentada no exemplo oficial.

## Limites e trade-offs
ParameterFilter usa outro contexto de variáveis; esquecer de nomear corretamente o parâmetro faz o filtro nunca casar e a contagem -Times 0 passar por falso positivo.

## Como verificar
Troque o filtro para um valor inexistente e confirme que o -Verifiable passa a reclamar do mock não invocado.

## Conexões
- [[pester-mock-basics]] — Veja também: Pester: Mock substitui qualquer comando.
- [[pester-mock-scoping]] — Veja também: Pester: o mock vale onde foi declarado.

## Fontes
- [Pester — Mocking](https://pester.dev/docs/usage/mocking) — Mock, Should-Invoke, escopo, natives e classes; consultado em 2026-10-03.
- [Pester — Quick start](https://pester.dev/docs/quick-start) — mini-DSL, convenção de nomes e primeira execução; consultado em 2026-10-03.
