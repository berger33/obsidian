---
id: software.testes.tranche13.000695
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
fontes: ["https://bheisler.github.io/criterion.rs/book/analysis.html", "https://bheisler.github.io/criterion.rs/book/user_guide/command_line_output.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Criterion.rs: interpretar outliers sem descartá-los

## Em uma frase
Criterion classifica outliers e avisa sobre sua presença, mas a análise subsequente continua usando as amostras coletadas.

## Por que importa
Picos podem sinalizar interferência ou cauda real de latência; descartá-los automaticamente esconderia uma condição relevante do sistema medido.

## Como funciona
Leia contagem e severidade de outliers junto de intervalos e gráficos, investigue carga concorrente e mantenha a mesma política ao comparar baselines.

## Exemplo
Uma regressão com muitos picos pode motivar análise do scheduler, mesmo que a mediana pareça estável no relatório.

## Limites e trade-offs
Um outlier observado não prova sua causa, e a classificação estatística de Criterion não substitui telemetria ou desenho experimental.

## Como verificar
Execute sob carga conhecida e ociosa, compare distribuição e anote condição ambiental antes de declarar mudança de desempenho.

## Conexões
- [[criterion-sample-size-tradeoff]] — Veja também: Criterion.rs: ajustar sample_size conforme precisão.
- [[criterion-baseline-comparison]] — Veja também: Criterion.rs: tratar comparação automática como hipótese.

## Fontes
- [Criterion.rs — Analysis Process](https://bheisler.github.io/criterion.rs/book/analysis.html) — warmup, measurement, outliers, bootstrap analysis and comparison; consultado em 2026-10-02.
- [Criterion.rs — Command-Line Output](https://bheisler.github.io/criterion.rs/book/user_guide/command_line_output.html) — confidence intervals, change summaries and outlier reporting; consultado em 2026-10-02.
