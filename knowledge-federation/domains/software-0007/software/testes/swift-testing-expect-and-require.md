---
id: software.testes.tranche15.000921
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
fontes: ["https://developer.apple.com/documentation/testing", "https://developer.apple.com/documentation/testing/migratingfromxctest"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Swift Testing: distinguir expect e require

## Em uma frase
`#expect` registra uma falha e continua a execução, enquanto `#require` interrompe o teste ao falhar e devolve o valor desembrulhado.

## Por que importa
Verificações independentes devem continuar e reportar todas as falhas, mas pré-condições precisam parar o caso antes que o restante seja executado sobre valor inválido.

## Como funciona
Use `#expect` para as afirmações do comportamento e `#require` para dependências sem as quais o restante do teste não faz sentido.

## Exemplo
`let usuario = try #require(await banco.buscar(id))` interrompe se o valor for nulo, e as expectativas seguintes trabalham com o valor garantido.

## Limites e trade-offs
`#require` lança erro e exige função que possa lançar; usá-lo em toda verificação transforma o teste em sequência que reporta apenas a primeira falha encontrada.

## Como verificar
Provoke uma falha em cada macro e compare o relatório: a expectativa mantém as verificações seguintes, e a exigência encerra o caso no ponto de falha.

## Conexões
- [[swift-testing-test-macro]] — Veja também: Swift Testing: marcar testes com @Test.
- [[swift-testing-suites-and-lifecycle]] — Veja também: Swift Testing: organizar suítes e ciclo de vida.

## Fontes
- [Apple — Swift Testing](https://developer.apple.com/documentation/testing) — macros @Test e @Suite, expectativas #expect e #require e modelo de suítes; consultado em 2026-10-02.
- [Apple — Migrating from XCTest](https://developer.apple.com/documentation/testing/migratingfromxctest) — equivalências de asserções, suítes e ciclo de vida entre frameworks; consultado em 2026-10-02.
