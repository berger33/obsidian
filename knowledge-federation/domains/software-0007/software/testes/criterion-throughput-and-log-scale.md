---
id: software.testes.tranche13.000698
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
fontes: ["https://bheisler.github.io/criterion.rs/book/user_guide/advanced_configuration.html", "https://bheisler.github.io/criterion.rs/book/user_guide/benchmarking_with_inputs.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Criterion.rs: escolher escala de gráfico para tamanhos crescentes

## Em uma frase
Grupos podem descrever throughput e usar escala logarítmica quando tamanhos de input crescem exponencialmente.

## Por que importa
Uma escala inadequada pode comprimir os pontos pequenos e esconder a forma de tendência que o experimento deveria comparar.

## Como funciona
Defina `PlotConfiguration` no grupo, use eixo log quando justificar a distribuição dos inputs e mantenha IDs ordenados para relacionar ponto e tamanho.

## Exemplo
Medições em 1, 10, 100 e 1.000 itens podem ficar legíveis em escala log, com throughput declarado para cada dimensão.

## Limites e trade-offs
Escala visual não muda cálculo de significância nem compensa amostras ausentes; escolha não deve ser usada para dramatizar uma inclinação.

## Como verificar
Abra plot gerado e confirme que marcadores e rótulos exibem as dimensões reais antes de tirar conclusão.

## Conexões
- [[criterion-flat-sampling-long-workload]] — Veja também: Criterion.rs: reservar Flat sampling para medições longas.
- [[criterion-benchmark-loop-scope]] — Veja também: Criterion.rs: manter trabalho relevante dentro do bencher.

## Fontes
- [Criterion.rs — Advanced Configuration](https://bheisler.github.io/criterion.rs/book/user_guide/advanced_configuration.html) — sample size, significance, throughput and sampling modes; consultado em 2026-10-02.
- [Criterion.rs — Benchmarking With Inputs](https://bheisler.github.io/criterion.rs/book/user_guide/benchmarking_with_inputs.html) — bench_with_input, BenchmarkGroup, BenchmarkId and input throughput; consultado em 2026-10-02.
