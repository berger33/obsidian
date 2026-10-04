---
id: software.testes.tranche13.000699
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

# Criterion.rs: manter trabalho relevante dentro do bencher

## Em uma frase
A closure de benchmark precisa repetir o trabalho que se deseja medir e evitar que preparação não representativa domine a duração.

## Por que importa
Benchmark pode parecer mais rápido que a operação real quando a entrada já está aquecida, estado residual cresce ou resultado é totalmente eliminado pelo otimizador.

## Como funciona
Use a forma de iteração adequada ao custo de preparar valores, estabilize dataset fora ou dentro do ciclo conforme a pergunta e proteja input/output com `black_box` quando apropriado.

## Exemplo
Um parser pode medir apenas parse do buffer imutável se preparação não faz parte da pergunta, mas outro benchmark separado inclui leitura do disco quando essa etapa importa.

## Limites e trade-offs
Trocar ponto de preparação muda a unidade experimental; não compare esses resultados como se medissem exatamente a mesma operação.

## Como verificar
Revise código do callback, perfil de build e custos incluídos; valide duração do benchmark em ordem de grandeza compatível com a operação descrita.

## Conexões
- [[criterion-throughput-and-log-scale]] — Veja também: Criterion.rs: escolher escala de gráfico para tamanhos crescentes.

## Fontes
- [Criterion.rs — Benchmarking With Inputs](https://bheisler.github.io/criterion.rs/book/user_guide/benchmarking_with_inputs.html) — bench_with_input, BenchmarkGroup, BenchmarkId and input throughput; consultado em 2026-10-02.
- [Criterion.rs — Analysis Process](https://bheisler.github.io/criterion.rs/book/analysis.html) — warmup, measurement, outliers, bootstrap analysis and comparison; consultado em 2026-10-02.
