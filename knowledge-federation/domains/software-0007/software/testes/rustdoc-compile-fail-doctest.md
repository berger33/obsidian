---
id: software.testes.tranche13.000682
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-13.md"
fontes: ["https://doc.rust-lang.org/cargo/commands/cargo-test.html", "https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# rustdoc: verificar exemplos que devem falhar na compilação

## Em uma frase
A cerca `compile_fail` marca um bloco de documentação que rustdoc compila negativamente e aprova quando o trecho não compila.

## Por que importa
Esse caso expressa uma fronteira de API: além de provar usos válidos, a documentação pode proteger contra uma chamada que o tipo ou a interface deve rejeitar.

## Como funciona
Coloque o exemplo inválido junto da API, mantenha o trecho pequeno e isolado e rode `cargo test --doc`; prefira doctest normal para demonstrar caminhos válidos.

## Exemplo
Uma API pode publicar exemplo com argumento que viola restrição de tipo e manter um bloco `compile_fail` para garantir que ele não passe a ser aceito por acidente.

## Limites e trade-offs
O teste valida que houve erro de compilação, não a redação exata do diagnóstico; um typo ou import ausente também pode fazê-lo passar.

## Como verificar
Remova a restrição que tornava o exemplo inválido e confirme que o doctest negativo falha porque o trecho passou a compilar.

## Conexões
- [[cargo-integration-test-crate]] — Veja também: Cargo test: separar testes de integração como crates externos.
- [[cargo-doctest-hidden-setup]] — Veja também: rustdoc: esconder preparação sem retirá-la do doctest.

## Fontes
- [Cargo — cargo test](https://doc.rust-lang.org/cargo/commands/cargo-test.html) — test target selection, filters, harness flags and doctest runs; consultado em 2026-10-02.
- [rustdoc — Documentation Tests](https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html) — code extraction, hidden lines, assertions and execution; consultado em 2026-10-02.
