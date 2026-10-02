---
id: software.testes.tranche13.000686
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

# Cargo test: entender o escopo de no-fail-fast

## Em uma frase
`--no-fail-fast` faz Cargo continuar para executáveis de teste posteriores depois de um deles falhar.

## Por que importa
Coletar falhas de vários targets reduz ciclos de CI, mas a flag não muda o comportamento interno do libtest para continuar depois de cada caso.

## Como funciona
Use a opção quando o job precisa de diagnóstico de todos os executáveis e leia os resultados por target; não a trate como justificativa para ignorar exit code não zero.

## Exemplo
Se testes de biblioteca falham, o Cargo ainda pode executar o alvo de integração seguinte e produzir um segundo bloco de resultados no log.

## Limites e trade-offs
Sem a flag Cargo pode encerrar após o primeiro executável falhar, embora aquele executável rode seus casos até concluir.

## Como verificar
Crie dois targets de teste descartáveis, faça um falhar e outro passar e compare sequência e status final com e sem a flag.

## Conexões
- [[cargo-no-run-compilation-check]] — Veja também: Cargo test: compilar alvos sem executá-los.
- [[cargo-test-thread-count-isolation]] — Veja também: Rust test harness: controlar concorrência com test-threads.

## Fontes
- [Cargo — cargo test](https://doc.rust-lang.org/cargo/commands/cargo-test.html) — test target selection, filters, harness flags and doctest runs; consultado em 2026-10-02.
- [The Rust Book — Running Tests](https://doc.rust-lang.org/book/ch11-02-running-tests.html) — filters, test threads, output and ignored tests; consultado em 2026-10-02.
