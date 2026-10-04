---
id: software.testes.tranche13.000693
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
fontes: ["https://bheisler.github.io/criterion.rs/book/analysis.html", "https://bheisler.github.io/criterion.rs/book/user_guide/advanced_configuration.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Criterion.rs: separar warmup de coleta de amostras

## Em uma frase
Execução de benchmark passa por warmup, medição, análise e comparação com resultados salvos.

## Por que importa
A fase de aquecimento reduz influência de cache frio ou compilação JIT no conjunto medido, mas o período escolhido ainda precisa refletir o comportamento do workload.

## Como funciona
Configure `warm_up_time` para permitir adaptação inicial e `measurement_time` para coletar duração suficiente; interprete cada número como amostra de uma execução ambientalmente condicionada.

## Exemplo
Uma rotina que abre cache em sua primeira chamada pode aquecer antes da coleta e depois medir operações reutilizando esse cache.

## Limites e trade-offs
Warmup não remove variação externa nem corrige operação que muda estado a cada iteração; medir uma carga artificial altera a pergunta.

## Como verificar
Observe saída de warmup e measurement, repita em máquina ociosa e mantenha setup consistente ao comparar versões.

## Conexões
- [[criterion-throughput-units]] — Veja também: Criterion.rs: declarar unidade de throughput por iteração.
- [[criterion-sample-size-tradeoff]] — Veja também: Criterion.rs: ajustar sample_size conforme precisão.

## Fontes
- [Criterion.rs — Analysis Process](https://bheisler.github.io/criterion.rs/book/analysis.html) — warmup, measurement, outliers, bootstrap analysis and comparison; consultado em 2026-10-02.
- [Criterion.rs — Advanced Configuration](https://bheisler.github.io/criterion.rs/book/user_guide/advanced_configuration.html) — sample size, significance, throughput and sampling modes; consultado em 2026-10-02.
