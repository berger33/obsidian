---
id: software.testes.tranche13.000687
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
fontes: ["https://doc.rust-lang.org/book/ch11-02-running-tests.html", "https://doc.rust-lang.org/cargo/commands/cargo-test.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Rust test harness: controlar concorrência com test-threads

## Em uma frase
Testes do harness podem rodar em múltiplas threads, e `--test-threads` limita a concorrência desse executável.

## Por que importa
Estado global, diretório fixo ou porta reservada pode fazer casos interferirem quando a execução padrão ocorre em paralelo.

## Como funciona
Passe a opção ao harness após `--`, prefira fixtures isoladas por teste e use uma thread apenas como ferramenta de diagnóstico ou quando a dependência não puder ser removida.

## Exemplo
Um teste de configuração global pode rodar com `cargo test -- --test-threads=1` para reproduzir colisão enquanto os casos independentes mantêm paralelismo normal.

## Limites e trade-offs
Serializar esconde a corrida entre testes e aumenta duração; não prova que o código sob teste está thread-safe.

## Como verificar
Rode serial e paralelo em repetição, registre diferença e substitua estado compartilhado por nomes temporários exclusivos.

## Conexões
- [[cargo-no-fail-fast-scope]] — Veja também: Cargo test: entender o escopo de no-fail-fast.
- [[cargo-target-selection]] — Veja também: Cargo test: limitar execução por pacote e target.

## Fontes
- [The Rust Book — Running Tests](https://doc.rust-lang.org/book/ch11-02-running-tests.html) — filters, test threads, output and ignored tests; consultado em 2026-10-02.
- [Cargo — cargo test](https://doc.rust-lang.org/cargo/commands/cargo-test.html) — test target selection, filters, harness flags and doctest runs; consultado em 2026-10-02.
