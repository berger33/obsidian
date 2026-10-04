---
id: software.testes.tranche15.000920
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
fontes: ["https://developer.apple.com/documentation/testing", "https://developer.apple.com/videos/play/wwdc2024/10179/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Swift Testing: marcar testes com @Test

## Em uma frase
A macro `@Test` identifica uma função de teste, dispensando herança de classe e o prefixo `test` no nome do método.

## Por que importa
A descoberta explícita elimina ambiguidade: só funções marcadas executam, e o nome pode descrever o comportamento verificado.

## Como funciona
Importe o módulo de testes, marque a função com `@Test` e use `#expect` para expressar a condição que deve ser verdadeira.

## Exemplo
`@Test func somaDuasParcelas() { #expect(2 + 2 == 4) }` é um teste completo, sem classe base nem método com nome reservado.

## Limites e trade-offs
A macro exige o compilador e a versão de ferramenta compatíveis; projetos presos a toolchains antigas continuam dependendo do XCTest.

## Como verificar
Compile e execute a suíte, confirme a descoberta da função e renomeie-a para verificar que o resultado não depende de convenção de nome.

## Conexões
- [[swift-testing-expect-and-require]] — Veja também: Swift Testing: distinguir expect e require.

## Fontes
- [Apple — Swift Testing](https://developer.apple.com/documentation/testing) — macros @Test e @Suite, expectativas #expect e #require e modelo de suítes; consultado em 2026-10-02.
- [Apple — Meet Swift Testing (WWDC24)](https://developer.apple.com/videos/play/wwdc2024/10179/) — apresentação das macros, suítes, paralelismo e diferenças do XCTest; consultado em 2026-10-02.
