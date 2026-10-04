---
id: software.testes.tranche15.000924
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

# Swift Testing: controlar testes com traits

## Em uma frase
Traits são valores aplicados a testes e suítes para desabilitar, condicionar, limitar tempo, marcar tags e registrar referências de defeito.

## Por que importa
Configuração declarativa no ponto do teste evita listas externas de exclusão e deixa visível por que um caso está fora da execução comum.

## Como funciona
Aplique `.disabled()` com motivo para casos bloqueados, `.enabled(if:)` para condições de ambiente e `.timeLimit()` para operações com prazo conhecido.

## Exemplo
`@Test(.disabled(\"aguardando correção\"), .timeLimit(.minutes(1))) func fluxoLongo() async throws { ... }` documenta restrições no próprio caso.

## Limites e trade-offs
Traits não corrigem teste instável nem substituem tempo limite do processo; a condição avaliada no momento da coleta precisa ser estável para não tornar a execução imprevisível.

## Como verificar
Rode a suíte com a condição satisfeita e não satisfeita e confirme que o caso entra e sai da execução conforme o trait aplicado.

## Conexões
- [[swift-testing-parameterized-tests]] — Veja também: Swift Testing: parametrizar com arguments.
- [[swift-testing-tags]] — Veja também: Swift Testing: agrupar e filtrar por tags.

## Fontes
- [Apple — Swift Testing](https://developer.apple.com/documentation/testing) — macros @Test e @Suite, expectativas #expect e #require e modelo de suítes; consultado em 2026-10-02.
- [Apple — Meet Swift Testing (WWDC24)](https://developer.apple.com/videos/play/wwdc2024/10179/) — apresentação das macros, suítes, paralelismo e diferenças do XCTest; consultado em 2026-10-02.
