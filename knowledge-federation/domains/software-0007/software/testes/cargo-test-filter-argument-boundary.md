---
id: software.testes.tranche13.000684
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
fontes: ["https://doc.rust-lang.org/cargo/commands/cargo-test.html", "https://doc.rust-lang.org/book/ch11-02-running-tests.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Cargo test: separar argumentos do Cargo e do harness

## Em uma frase
O argumento de filtro e os parâmetros depois de `--` são encaminhados ao executável de teste, enquanto opções antes do separador pertencem ao Cargo.

## Por que importa
Separar essas camadas evita interpretar `--test-threads` como opção do gerenciador de pacotes ou selecionar alvo de forma equivocada.

## Como funciona
Coloque package, target e build options antes de `--`; depois dele, informe filtro, quantidade de threads ou flags do libtest.

## Exemplo
`cargo test nome_do_modulo -- --test-threads=2` pede ao Cargo um filtro e ao harness um limite de threads.

## Limites e trade-offs
Um filtro pode coincidir com mais casos que o nome aparenta, pois nomes completos incluem módulos e alvos diferentes.

## Como verificar
Ative saída detalhada e confirme na invocação qual alvo o Cargo construiu e quais argumentos chegaram ao harness.

## Conexões
- [[cargo-doctest-hidden-setup]] — Veja também: rustdoc: esconder preparação sem retirá-la do doctest.
- [[cargo-no-run-compilation-check]] — Veja também: Cargo test: compilar alvos sem executá-los.

## Fontes
- [Cargo — cargo test](https://doc.rust-lang.org/cargo/commands/cargo-test.html) — test target selection, filters, harness flags and doctest runs; consultado em 2026-10-02.
- [The Rust Book — Running Tests](https://doc.rust-lang.org/book/ch11-02-running-tests.html) — filters, test threads, output and ignored tests; consultado em 2026-10-02.
