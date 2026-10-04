---
id: software.testes.tranche15.000929
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
fontes: ["https://developer.apple.com/documentation/testing", "https://developer.apple.com/documentation/testing/addingtags"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Swift Testing: executar pela ferramenta de linha de comando

## Em uma frase
O comando `swift test` do SwiftPM descobre e executa os testes do pacote, incluindo os escritos com Swift Testing em toolchains compatíveis.

## Por que importa
A execução local precisa reproduzir o que o pipeline fará, e a linha de comando é o contrato comum entre máquina de desenvolvimento e integração contínua.

## Como funciona
Rode a suíte completa no pacote, use filtro por nome para reduzir o conjunto durante o diagnóstico e preserve a saída para investigar falhas fora da máquina local.

## Exemplo
`swift test --filter PagamentosTests` restringe a execução aos casos que casam com o filtro, acelerando a verificação local.

## Limites e trade-offs
Filtro por nome não seleciona por tag e a execução pode variar conforme o alvo e a plataforma; o resultado considerado válido é o da suíte completa no mesmo ambiente do pipeline.

## Como verificar
Compare a contagem de casos da execução filtrada com a completa e confirme que nenhum alvo do pacote ficou fora da descoberta.

## Conexões
- [[swift-testing-migration-from-xctest]] — Veja também: Swift Testing: migrar casos do XCTest.

## Fontes
- [Apple — Swift Testing](https://developer.apple.com/documentation/testing) — macros @Test e @Suite, expectativas #expect e #require e modelo de suítes; consultado em 2026-10-02.
- [Apple — Adding tags](https://developer.apple.com/documentation/testing/addingtags) — tags para organizar, filtrar e agrupar testes; consultado em 2026-10-02.
