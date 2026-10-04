---
id: software.testes.tranche13.000685
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

# Cargo test: compilar alvos sem executá-los

## Em uma frase
A opção `--no-run` compila executáveis de teste sem iniciar o harness.

## Por que importa
Esse passo separa erros de compilação de falhas comportamentais e serve para preparar artefatos antes de debug ou execução numa etapa posterior.

## Como funciona
Rode `cargo test --no-run` para validar compilação; selecione pacote ou target se a intenção for limitar o trabalho e não declare resultado dos testes como aprovado.

## Exemplo
Uma pipeline pode compilar todos os testes em um job de build e executar subset em outro job com os binários gerados.

## Limites e trade-offs
Sucesso de compilação não confirma setup, assertions ou integração em runtime; o executável ainda precisa rodar em alguma etapa de validação.

## Como verificar
Depois da compilação, execute o alvo em ambiente controlado e mantenha status de build e status de testes como indicadores separados.

## Conexões
- [[cargo-test-filter-argument-boundary]] — Veja também: Cargo test: separar argumentos do Cargo e do harness.
- [[cargo-no-fail-fast-scope]] — Veja também: Cargo test: entender o escopo de no-fail-fast.

## Fontes
- [Cargo — cargo test](https://doc.rust-lang.org/cargo/commands/cargo-test.html) — test target selection, filters, harness flags and doctest runs; consultado em 2026-10-02.
- [Cargo — Target Configuration](https://doc.rust-lang.org/cargo/reference/cargo-targets.html) — test and doctest target manifest options; consultado em 2026-10-02.
