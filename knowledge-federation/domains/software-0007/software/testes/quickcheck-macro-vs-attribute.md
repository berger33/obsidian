---
id: software.testes.tranche25.001941
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-25.md"
fontes: ["https://raw.githubusercontent.com/BurntSushi/quickcheck/master/README.md", "https://docs.rs/quickcheck"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Duas formas de declarar propriedades: a macro quickcheck! e o atributo #[quickcheck]

## Em uma frase
As seções Simple example e The #[quickcheck] attribute mostram as duas sintaxes suportadas: o bloco macro quickcheck! { fn prop(xs: Vec<u32>) -> bool { ... } } (importando use quickcheck::quickcheck; e compatível com versões antigas do Rust) e o atributo procedural #[quickcheck] colocado diretamente sobre uma função de teste (importando use quickcheck_macros::quickcheck;), que converte a função de propriedade em uma função #[test].

## Por que importa
O atributo #[quickcheck] da crate auxiliar quickcheck_macros reduz o nível de indentação e deixa cada propriedade com a aparência exata de um teste unitário comum do Rust, enquanto a macro declarativa quickcheck! funciona apenas com a crate principal sem precisar da dependência de macro procedural.

## Como funciona
Para usar apenas a crate base, adicione quickcheck = "1" em [dev-dependencies] e envolva as funções em quickcheck! { ... }; se preferir anotar funções individuais com #[quickcheck], adicione também quickcheck_macros = "1" em [dev-dependencies].

## Exemplo
Com quickcheck_macros, o exemplo oficial fica simplesmente #[quickcheck] fn double_reversal_is_identity(xs: Vec<isize>) -> bool { xs == reverse(&reverse(&xs)) } dentro do módulo #[cfg(test)] mod tests.

## Limites e trade-offs
Para usar #[quickcheck] é obrigatório importar o macro de quickcheck_macros (use quickcheck_macros::quickcheck;) e manter ambas as crates (quickcheck e quickcheck_macros) nas dependências de desenvolvimento.

## Como verificar
Conferi as seções Simple example, The #[quickcheck] attribute e Installation no README oficial.

## Conexões
- [[quickcheck-what-it-is]] — Veja também: quickcheck em Rust: testes baseados em propriedades e shrinking por busca binária.
- [[quickcheck-logging-and-default-features]] — Veja também: Diagnóstico com RUST_LOG=quickcheck e as features padrão use_logging e regex.

## Fontes
- [quickcheck — README oficial](https://raw.githubusercontent.com/BurntSushi/quickcheck/master/README.md) — README oficial da crate quickcheck com property-based testing, shrinking por busca binária, macro quickcheck! e atributo #[quickcheck], RUST_LOG=quickcheck, política de MSRV 1.85.0, compatibilidade de Arbitrary e trait Testable com TestResult::discard.; consultado em 2026-10-03.
- [Crate quickcheck no docs.rs](https://docs.rs/quickcheck) — Documentação oficial da API da crate quickcheck no docs.rs.; consultado em 2026-10-03.
