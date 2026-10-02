---
id: software.testes.tranche13.000692
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
fontes: ["https://bheisler.github.io/criterion.rs/book/user_guide/benchmarking_with_inputs.html", "https://bheisler.github.io/criterion.rs/book/user_guide/advanced_configuration.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Criterion.rs: declarar unidade de throughput por iteração

## Em uma frase
Throughput em bytes ou elementos exige informar quantos deles são processados em cada iteração.

## Por que importa
Tempo por operação não comunica capacidade de processamento quando workloads têm tamanhos distintos, mas unidade errada cria uma taxa igualmente enganosa.

## Como funciona
Use `group.throughput(Throughput::Bytes(n))` para volume de bytes ou `Throughput::Elements(n)` para contagem; atualize valor ao percorrer tamanhos diferentes.

## Exemplo
Um decodificador pode declarar o comprimento real do buffer por input para que o relatório estime MiB por segundo além do tempo por chamada.

## Limites e trade-offs
A API de throughput é oferecida em BenchmarkGroup e não na forma simplificada `bench_function`; não infira taxa sem cardinalidade correta.

## Como verificar
Compare a taxa calculada com tamanho conhecido e confira que variar input altera throughput de forma coerente com o trabalho.

## Conexões
- [[criterion-benchmark-group-parameters]] — Veja também: Criterion.rs: agrupar variações com BenchmarkGroup.
- [[criterion-warmup-measurement-phases]] — Veja também: Criterion.rs: separar warmup de coleta de amostras.

## Fontes
- [Criterion.rs — Benchmarking With Inputs](https://bheisler.github.io/criterion.rs/book/user_guide/benchmarking_with_inputs.html) — bench_with_input, BenchmarkGroup, BenchmarkId and input throughput; consultado em 2026-10-02.
- [Criterion.rs — Advanced Configuration](https://bheisler.github.io/criterion.rs/book/user_guide/advanced_configuration.html) — sample size, significance, throughput and sampling modes; consultado em 2026-10-02.
