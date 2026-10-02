---
id: software.testes.tranche13.000689
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
fontes: ["https://doc.rust-lang.org/cargo/reference/cargo-targets.html", "https://doc.rust-lang.org/cargo/commands/cargo-test.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Cargo test: desativar harness somente para executor próprio

## Em uma frase
Alvos com `harness = false` deixam de receber o harness automático e precisam fornecer seu próprio `main` para executar testes.

## Por que importa
O ajuste permite integração com runner especial, mas transfere ao projeto responsabilidade por descoberta, resultado e exit code.

## Como funciona
Mantenha harness automático para testes comuns; use modo customizado somente quando o executor alternativo for parte explícita do desenho e estiver coberto por job próprio.

## Exemplo
Um exemplo executável pode ser habilitado como test e, se não quiser substituição do `main`, ser executado pelo próprio programa com harness desligado.

## Limites e trade-offs
Desativar harness não cria por si só suporte a attributes ou relatórios; a semântica depende do main implementado pelo autor.

## Como verificar
Compile e execute o target customizado em CI e force uma falha para confirmar que o processo retorna sinal de falha reconhecido pelo pipeline.

## Conexões
- [[cargo-target-selection]] — Veja também: Cargo test: limitar execução por pacote e target.

## Fontes
- [Cargo — Target Configuration](https://doc.rust-lang.org/cargo/reference/cargo-targets.html) — test and doctest target manifest options; consultado em 2026-10-02.
- [Cargo — cargo test](https://doc.rust-lang.org/cargo/commands/cargo-test.html) — test target selection, filters, harness flags and doctest runs; consultado em 2026-10-02.
