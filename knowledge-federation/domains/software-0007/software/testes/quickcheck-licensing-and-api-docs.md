---
id: software.testes.tranche25.001949
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

# Duplo licenciamento MIT / UNLICENSE e documentação completa em docs.rs

## Em uma frase
O cabeçalho e a seção Documentation do README oficial informam que a crate quickcheck é publicada no crates.io, tem CI em GitHub Actions, possui a API inteiramente documentada em https://docs.rs/quickcheck e é distribuída sob dupla licença MIT ou UNLICENSE (https://unlicense.org/).

## Por que importa
O par de licenças MIT ou UNLICENSE (dedicação ao domínio público) é ainda mais permissivo que o padrão MIT/Apache-2.0 do ecossistema Rust, eliminando qualquer atrito de atribuição quando a opção UNLICENSE é escolhida.

## Como funciona
Consulte https://docs.rs/quickcheck para a documentação completa dos tipos Gen, Arbitrary, TestResult e QuickCheck, e registre o licenciamento MIT OR Unlicense nos inventários de conformidade do projeto.

## Exemplo
Ao implementar o trait Arbitrary manualmente para uma struct de domínio, a documentação em docs.rs/quickcheck traz as assinaturas exatas de arbitrary(&mut Gen) e shrink(&self).

## Limites e trade-offs
A nota registra os metadados oficiais de licenciamento e documentação publicados no README do repositório BurntSushi/quickcheck.

## Como verificar
Conferi o cabeçalho de licenciamento e a seção Documentation no README oficial.

## Conexões
- [[quickcheck-vs-proptest-and-fuzzing-alternatives]] — Veja também: Quando escolher quickcheck, quando escolher proptest e quando ir para fuzzing.

## Fontes
- [quickcheck — README oficial](https://raw.githubusercontent.com/BurntSushi/quickcheck/master/README.md) — README oficial da crate quickcheck com property-based testing, shrinking por busca binária, macro quickcheck! e atributo #[quickcheck], RUST_LOG=quickcheck, política de MSRV 1.85.0, compatibilidade de Arbitrary e trait Testable com TestResult::discard.; consultado em 2026-10-03.
- [Crate quickcheck no docs.rs](https://docs.rs/quickcheck) — Documentação oficial da API da crate quickcheck no docs.rs.; consultado em 2026-10-03.
