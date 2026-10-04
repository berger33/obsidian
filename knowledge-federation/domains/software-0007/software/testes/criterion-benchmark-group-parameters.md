---
id: software.testes.tranche13.000691
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

# Criterion.rs: agrupar variações com BenchmarkGroup

## Em uma frase
`BenchmarkGroup` relaciona casos que medem a mesma pergunta com parâmetros diferentes e gera sumarização conjunta.

## Por que importa
Resultados de uma família são mais fáceis de comparar quando tamanho, algoritmo ou configuração aparecem como dimensões nomeadas.

## Como funciona
Crie um grupo, percorra valores representativos, atribua `BenchmarkId` estável e finalize com `finish()` após registrar todos os membros.

## Exemplo
Um benchmark de compressão pode iterar tamanhos de entrada e manter um grupo chamado `compress`, permitindo localizar curvas por tamanho.

## Limites e trade-offs
Se variar algoritmo e volume ao mesmo tempo, o efeito observado mistura dimensões e dificulta explicar qual fator mudou a duração.

## Como verificar
Confira se todas as variantes aparecem no relatório, se os IDs não colidem e se o grupo compara trabalhos equivalentes.

## Conexões
- [[criterion-benchmark-input-black-box]] — Veja também: Criterion.rs: nomear benchmark com input explícito.
- [[criterion-throughput-units]] — Veja também: Criterion.rs: declarar unidade de throughput por iteração.

## Fontes
- [Criterion.rs — Benchmarking With Inputs](https://bheisler.github.io/criterion.rs/book/user_guide/benchmarking_with_inputs.html) — bench_with_input, BenchmarkGroup, BenchmarkId and input throughput; consultado em 2026-10-02.
- [Criterion.rs — Advanced Configuration](https://bheisler.github.io/criterion.rs/book/user_guide/advanced_configuration.html) — sample size, significance, throughput and sampling modes; consultado em 2026-10-02.
