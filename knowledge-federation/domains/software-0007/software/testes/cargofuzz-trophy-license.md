---
id: software.testes.tranche23.001709
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-23.md"
fontes: ["https://github.com/rust-fuzz/cargo-fuzz/blob/main/README.md", "https://rust-fuzz.github.io/book/cargo-fuzz/tutorial.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Troféus e licença: MIT mais Apache-2.0, bugs em crates famosos

## Em uma frase
A seção Trophy Case do README oficial mantém a cultura do ecossistema: uma lista de bugs encontrados pelo cargo fuzz (e outros fuzzers) vive no repositório rust-fuzz/trophy-case, com o convite explícito para adicionar o seu; a licença é dupla, "both the MIT license and the Apache License (Version 2.0)", com os textos LICENSE-MIT e LICENSE-APACHE no próprio repo.

## Por que importa
Trophy cases servem de estudo técnico — cada entrada mostra o padrão do harness que achou o quê — e a dupla licença MIT/Apache remove o medo de adotar fuzzing em crates comerciais, sendo o padrão do ecossistema Rust para tooling.

## Como funciona
O repositório de troféus é compartilhado entre ferramentas (o texto diz "and others"), o que o README do cargo-fuzz explicita ao se referir a ele — os troféus listam fuzzers variados, não um hall próprio.

## Exemplo
Antes de justificar fuzzing para a equipe, abra o trophy-case e filtre as entradas de projetos que sua stack usa; a lista é o argumento de valor, e o par de licenças é o argumento jurídico, ambos em páginas oficiais.

## Limites e trade-offs
O trophy case é curado por auto-relato — entradas refletem o que os caçadores reportaram, não um censo de bugs de crates Rust; a própria existência dele não mede a eficácia esperada no seu crate.

## Como verificar
Abra as seções Trophy case e License do README oficial e confirme a descrição da lista, a frase "and others" e o par de licenças com seus arquivos.

## Conexões
- [[cargofuzz-coverage-docs]] — Veja também: cargo fuzz coverage e onde a documentação real mora.

## Fontes
- [cargo-fuzz — README oficial](https://github.com/rust-fuzz/cargo-fuzz/blob/main/README.md) — instalação, plataformas, subcomandos, workspace e licenças; consultado em 2026-10-03.
- [Rust Fuzz Book — tutorial do cargo-fuzz](https://rust-fuzz.github.io/book/cargo-fuzz/tutorial.html) — init, alvo fuzz_target, saída, crash em artifacts e cargo fuzz list; consultado em 2026-10-03.
