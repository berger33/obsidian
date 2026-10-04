---
id: software.testes.tranche13.000688
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
fontes: ["https://doc.rust-lang.org/cargo/commands/cargo-test.html", "https://doc.rust-lang.org/cargo/reference/cargo-targets.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Cargo test: limitar execução por pacote e target

## Em uma frase
Cargo consegue selecionar workspace, pacote, biblioteca, binário, exemplo ou alvo de integração em vez de compilar tudo.

## Por que importa
Seleção focada acelera desenvolvimento e faz cada job declarar quais camadas cobre, evitando que um filtro de nome seja confundido com escolha de target.

## Como funciona
Use `--workspace` ou `-p` para pacotes e `--lib`, `--bin` ou `--test` para targets; confira flags do manifest que mudam quais alvos entram no padrão.

## Exemplo
Um job rápido pode testar só `--lib`, deixando execução dos arquivos em `tests/` para etapa de integração explicitamente nomeada.

## Limites e trade-offs
Selecionar um target pode ainda compilar dependências exigidas ou testar binário como suporte a integração; a lista implícita não é sempre uma única compilação.

## Como verificar
Inspecione log de Cargo e saída de cada executável quando mudar seleção, comparando targets realmente rodados com o escopo esperado pelo job.

## Conexões
- [[cargo-test-thread-count-isolation]] — Veja também: Rust test harness: controlar concorrência com test-threads.
- [[cargo-harness-false-boundary]] — Veja também: Cargo test: desativar harness somente para executor próprio.

## Fontes
- [Cargo — cargo test](https://doc.rust-lang.org/cargo/commands/cargo-test.html) — test target selection, filters, harness flags and doctest runs; consultado em 2026-10-02.
- [Cargo — Target Configuration](https://doc.rust-lang.org/cargo/reference/cargo-targets.html) — test and doctest target manifest options; consultado em 2026-10-02.
