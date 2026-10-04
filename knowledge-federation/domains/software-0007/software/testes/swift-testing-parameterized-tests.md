---
id: software.testes.tranche15.000923
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://developer.apple.com/documentation/testing/parameterizedtesting", "https://developer.apple.com/documentation/testing"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Swift Testing: parametrizar com arguments

## Em uma frase
A macro `@Test(arguments:)` executa a mesma função para cada argumento, gerando um resultado pai com um filho por valor ou combinação.

## Por que importa
Repetir funções quase idênticas para cada entrada multiplica código e esconde qual dado falhou quando o resultado aparece agregado.

## Como funciona
Passe coleções de argumentos para a macro, use tuplas para múltiplos parâmetros e marque `.serialized` quando a ordem entre casos for necessária.

## Exemplo
`@Test(arguments: [1, 2, 3]) func quadrado(_ v: Int) { #expect(v * v >= v) }` gera três execuções independentes.

## Limites e trade-offs
Várias coleções produzem produto cartesiano, o que pode explodir em quantidade de casos; a parametrização também roda em paralelo por padrão.

## Como verificar
Reduza um caso que falha e confirme que o relatório identifica exatamente o argumento problemático, sem exigir reprodução manual do conjunto inteiro.

## Conexões
- [[swift-testing-suites-and-lifecycle]] — Veja também: Swift Testing: organizar suítes e ciclo de vida.
- [[swift-testing-traits]] — Veja também: Swift Testing: controlar testes com traits.

## Fontes
- [Apple — Parameterized testing](https://developer.apple.com/documentation/testing/parameterizedtesting) — testes parametrizados, coleções de argumentos e combinações; consultado em 2026-10-02.
- [Apple — Swift Testing](https://developer.apple.com/documentation/testing) — macros @Test e @Suite, expectativas #expect e #require e modelo de suítes; consultado em 2026-10-02.
