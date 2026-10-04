---
id: software.testes.tranche23.001703
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
fontes: ["https://rust-fuzz.github.io/book/cargo-fuzz/tutorial.html", "https://github.com/rust-fuzz/cargo-fuzz/blob/main/README.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Anatomia de um fuzz target: no_main, macro e fatia de bytes

## Em uma frase
O tutorial oficial constrói o target canônico: o arquivo em fuzz/fuzz_targets começa com #![no_main] e extern crate libfuzzer_sys, importa a crate sob teste e registra o alvo com a macro fuzz_target! recebendo um closure cujo parâmetro é uma fatia &[u8] de bytes pseudoaleatórios.

## Por que importa
Essa assinatura é o contrato do motor — libFuzzer chama repetidamente o corpo do closure com dados gerados — e o trabalho do autor é traduzir bytes para a entrada que o parser do crate recebe, como o exemplo faz convertendo com from_utf8 antes de chamar Url::parse.

## Como funciona
O book explica o critério de parada: a execução vai até o programa "hits an error condition (segfault, panic, etc)"; o snippet do tutorial tem o if let Ok para descartar silenciosamente inputs que nem sequer são UTF-8 válido, mantendo o fuzzing focado no que o parser aceita.

## Exemplo
Copie o fuzz_target do exemplo do tutorial para um parser seu, aceitando &[u8], convertendo para &str e chamando a função pública; um panic é o oráculo que o motor procura.

## Limites e trade-offs
O exemplo é didático e descarta erros de parse silenciosamente; targets reais precisam decidir o que ignorar com cuidado — descartar cedo demais é o modo como fuzzers não chegam a caminhos profundos, como a doc do AFL++ para harnesses ecoa (nota do grupo AFL++).

## Como verificar
Abra o bloco de código do target no tutorial do Rust Fuzz Book e a explicação do parágrafo seguinte ("libFuzzer is going to repeatedly call the body..."), no material oficial.

## Conexões
- [[cargofuzz-init-workspace]] — Veja também: cargo fuzz init: o diretório fuzz dentro (ou fora) do workspace.
- [[cargofuzz-run-crash]] — Veja também: cargo fuzz run: lendo a saída do libFuzzer até o crash.

## Fontes
- [Rust Fuzz Book — tutorial do cargo-fuzz](https://rust-fuzz.github.io/book/cargo-fuzz/tutorial.html) — init, alvo fuzz_target, saída, crash em artifacts e cargo fuzz list; consultado em 2026-10-03.
- [cargo-fuzz — README oficial](https://github.com/rust-fuzz/cargo-fuzz/blob/main/README.md) — instalação, plataformas, subcomandos, workspace e licenças; consultado em 2026-10-03.
