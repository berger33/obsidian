---
id: software.testes.tranche13.000680
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

# Cargo test: manter unit tests perto do módulo

## Em uma frase
Unit tests escritos num módulo `#[cfg(test)]` dentro do arquivo podem acessar itens privados do módulo pai.

## Por que importa
Testar unidade próxima do código ajuda a localizar falhas e permite cobrir funções internas sem torná-las API pública artificialmente.

## Como funciona
Crie submódulo de testes sob `cfg(test)`, importe o escopo pai necessário e concentre assertions em comportamento cujo diagnóstico beneficie da visibilidade local.

## Exemplo
Um teste interno pode invocar função privada que normaliza argumento, enquanto um teste de integração valida o resultado público do crate.

## Limites e trade-offs
Visibilidade privada não obriga a testar toda função diretamente; se assertion acompanha implementação interna, pode dificultar refatoração sem proteger contrato externo.

## Como verificar
Rode `cargo test` e depois `cargo build`; confirme que módulo de teste é compilado no primeiro fluxo e não integra o artefato normal.

## Conexões
- [[cargo-integration-test-crate]] — Veja também: Cargo test: separar testes de integração como crates externos.

## Fontes
- [The Rust Book — Test Organization](https://doc.rust-lang.org/book/ch11-03-test-organization.html) — unit modules, privacy and integration-test crates; consultado em 2026-10-02.
- [Cargo — cargo test](https://doc.rust-lang.org/cargo/commands/cargo-test.html) — test target selection, filters, harness flags and doctest runs; consultado em 2026-10-02.
