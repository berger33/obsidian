---
id: software.testes.tranche23.001700
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

# cargo fuzz: o subcomando do cargo para libFuzzer

## Em uma frase
O README oficial define o projeto em uma linha: "A cargo subcommand for fuzzing with libFuzzer! Easy to use!" — em vez de montar manualmente os flags do clang com sanitizer, o usuário instala um binário cargo e ganha um fluxo de fuzzing nativo do ecossistema de crates.

## Por que importa
Em Rust, o custo de entrada para fuzzing era a combinação LLVM + sanitizer + corpus; o subcomando embute essa combinação e mantém targets dentro do próprio workspace do crate, versionados junto com o código.

## Como funciona
A instalação declarada é cargo install cargo-fuzz; a partir daí, cada comando roda dentro do diretório do crate-alvo como um comando cargo comum, e o README remete a referência completa de flags para cargo fuzz --help.

## Exemplo
Instale o subcomando, entre em qualquer crate com biblioteca e confirme que cargo fuzz --help lista init, add, run, fmt, tmin, cmin e coverage, exatamente como na seção Usage do README.

## Limites e trade-offs
É um wrapper: a motoridade vem do libFuzzer e das flags instáveis do rustc — isso aparece nas restrições documentadas da próxima nota, que definem o que o pacote pode e não pode fazer por você.

## Como verificar
Abra o topo do README em rust-fuzz/cargo-fuzz e confirme a definição, o comando de instalação e a lista de subcomandos da seção Usage.

## Conexões
- [[cargofuzz-platform-limits]] — Veja também: Restrições de plataforma: sanitizers pedem x86-64/AArch64, Unix e nightly.

## Fontes
- [cargo-fuzz — README oficial](https://github.com/rust-fuzz/cargo-fuzz/blob/main/README.md) — instalação, plataformas, subcomandos, workspace e licenças; consultado em 2026-10-03.
- [Rust Fuzz Book — tutorial do cargo-fuzz](https://rust-fuzz.github.io/book/cargo-fuzz/tutorial.html) — init, alvo fuzz_target, saída, crash em artifacts e cargo fuzz list; consultado em 2026-10-03.
