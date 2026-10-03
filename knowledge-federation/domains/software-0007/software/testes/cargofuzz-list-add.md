---
id: software.testes.tranche23.001705
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

# cargo fuzz list e add: múltiplos alvos por crate

## Em uma frase
Os dois subcomandos de gestão declarados no README oficial completam o ciclo de autor: cargo fuzz add <target> cria um novo alvo de fuzzing no projeto já inicializado, e cargo fuzz list exibe a lista de todos os alvos existentes — o tutorial do book o usa logo após o init para confirmar o target gerado.

## Por que importa
Crates com várias superfícies públicas (parser, deserializador, formatador) se beneficiam de um alvo por função de entrada; a listagem é o inventário que o CI itera quando se quer rodar todos os fuzzers em sequência.

## Como funciona
O fluxo oficial é init → edita fuzz/fuzz_targets → run; add e list funcionam como o scaffold e o registro desse conjunto de arquivos em fuzz/fuzz_targets, um .rs por alvo.

## Exemplo
Rode cargo fuzz list antes e depois de um cargo fuzz add parser_header e confira que o nome novo aparece na listagem e que um arquivo correspondente existia em fuzz/fuzz_targets — a mesma checagem que o tutorial demonstra com o target inicial.

## Limites e trade-offs
O README não detalha templates do add (o que o arquivo gerado contém em cada versão); o contrato está no --help do subcomando e no book, que o README referencia como documentação principal.

## Como verificar
Abra as seções add e list do README oficial e o uso do list logo após o init no tutorial do Rust Fuzz Book.

## Conexões
- [[cargofuzz-run-crash]] — Veja também: cargo fuzz run: lendo a saída do libFuzzer até o crash.
- [[cargofuzz-fmt-arbitrary]] — Veja também: cargo fuzz fmt: o que aquele input arbitrário realmente é.

## Fontes
- [cargo-fuzz — README oficial](https://github.com/rust-fuzz/cargo-fuzz/blob/main/README.md) — instalação, plataformas, subcomandos, workspace e licenças; consultado em 2026-10-03.
- [Rust Fuzz Book — tutorial do cargo-fuzz](https://rust-fuzz.github.io/book/cargo-fuzz/tutorial.html) — init, alvo fuzz_target, saída, crash em artifacts e cargo fuzz list; consultado em 2026-10-03.
