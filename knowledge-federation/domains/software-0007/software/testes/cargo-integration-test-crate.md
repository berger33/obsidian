---
id: software.testes.tranche13.000681
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
fontes: ["https://doc.rust-lang.org/book/ch11-03-test-organization.html", "https://doc.rust-lang.org/cargo/commands/cargo-test.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Cargo test: separar testes de integração como crates externos

## Em uma frase
Arquivos no diretório superior `tests/` são compilados individualmente como crates de integração.

## Por que importa
Esse limite exercita a biblioteca do jeito que um consumidor externo a usaria e valida vários módulos juntos pela API pública.

## Como funciona
Importe o crate pelo nome declarado no pacote, divida integrações por fluxo ou fronteira e evite aplicar `cfg(test)` como se cada arquivo fosse módulo interno.

## Exemplo
Um arquivo `tests/persistencia.rs` pode construir repositório público e verificar ciclo de gravação sem acessar campos privados do crate.

## Limites e trade-offs
Cada arquivo compila como crate separado, então helpers comuns precisam ser organizados como módulos auxiliares compatíveis com essa estrutura.

## Como verificar
Rode `cargo test --test persistencia` e confirme que a compilação usa apenas a interface pública do pacote.

## Conexões
- [[cargo-unit-test-module]] — Veja também: Cargo test: manter unit tests perto do módulo.
- [[rustdoc-compile-fail-doctest]] — Veja também: rustdoc: verificar exemplos que devem falhar na compilação.

## Fontes
- [The Rust Book — Test Organization](https://doc.rust-lang.org/book/ch11-03-test-organization.html) — unit modules, privacy and integration-test crates; consultado em 2026-10-02.
- [Cargo — cargo test](https://doc.rust-lang.org/cargo/commands/cargo-test.html) — test target selection, filters, harness flags and doctest runs; consultado em 2026-10-02.
