---
id: software.testes.tranche15.000922
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

# Swift Testing: organizar suítes e ciclo de vida

## Em uma frase
Qualquer tipo que contenha funções de teste forma uma suíte, e a anotação `@Suite` é necessária apenas para nome, traits ou agrupamento explícito.

## Por que importa
Suítes organizam a execução e definem onde colocar preparação e limpeza, substituindo a hierarquia de classes do XCTest por tipos com valor.

## Como funciona
Prefira `struct` para estado isolado, use `@Suite` quando precisar de nome ou trait e coloque preparação no inicializador da suíte.

## Exemplo
Um `struct` de suíte pode guardar dependências inicializadas no `init`, e uma `class` ou `actor` permite verificação no `deinit` após cada teste.

## Limites e trade-offs
Cada função recebe uma instância nova da suíte por padrão, então estado mutável compartilhado entre casos não é preservado automaticamente.

## Como verificar
Adicione um contador de inicializações e confirme quantas instâncias foram criadas para duas funções de teste, verificando o isolamento.

## Conexões
- [[swift-testing-expect-and-require]] — Veja também: Swift Testing: distinguir expect e require.
- [[swift-testing-parameterized-tests]] — Veja também: Swift Testing: parametrizar com arguments.

## Fontes
- [Apple — Swift Testing](https://developer.apple.com/documentation/testing) — macros @Test e @Suite, expectativas #expect e #require e modelo de suítes; consultado em 2026-10-02.
- [Apple — Meet Swift Testing (WWDC24)](https://developer.apple.com/videos/play/wwdc2024/10179/) — apresentação das macros, suítes, paralelismo e diferenças do XCTest; consultado em 2026-10-02.
