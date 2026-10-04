---
id: software.testes.tranche13.000690
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
fontes: ["https://bheisler.github.io/criterion.rs/book/user_guide/benchmarking_with_inputs.html", "https://bheisler.github.io/criterion.rs/book/analysis.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Criterion.rs: nomear benchmark com input explícito

## Em uma frase
`bench_with_input()` associa um valor de entrada e um identificador ao benchmark e passa o input por `black_box`.

## Por que importa
Nomear tamanho de workload deixa resultados comparáveis e reduz risco de uma otimização remover cálculo que não produz efeito observável.

## Como funciona
Use `BenchmarkId` para identificar o caso, forneça a entrada como dado separado e mantenha a operação medida dentro do callback do bencher.

## Exemplo
Um parser pode comparar payloads de 1, 8 e 64 kilobytes com rótulos que aparecem no relatório, sem duplicar três funções de benchmark.

## Limites e trade-offs
`black_box` não corrige benchmark que mede setup por engano nem representa uma garantia de segurança contra toda otimização do compilador.

## Como verificar
Rode cada input e confirme que relatório distingue os IDs; revise o trecho medido para garantir que trabalho relevante continua observável.

## Conexões
- [[criterion-benchmark-group-parameters]] — Veja também: Criterion.rs: agrupar variações com BenchmarkGroup.

## Fontes
- [Criterion.rs — Benchmarking With Inputs](https://bheisler.github.io/criterion.rs/book/user_guide/benchmarking_with_inputs.html) — bench_with_input, BenchmarkGroup, BenchmarkId and input throughput; consultado em 2026-10-02.
- [Criterion.rs — Analysis Process](https://bheisler.github.io/criterion.rs/book/analysis.html) — warmup, measurement, outliers, bootstrap analysis and comparison; consultado em 2026-10-02.
