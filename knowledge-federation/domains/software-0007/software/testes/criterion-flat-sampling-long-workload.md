---
id: software.testes.tranche13.000697
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
fontes: ["https://bheisler.github.io/criterion.rs/book/user_guide/advanced_configuration.html", "https://bheisler.github.io/criterion.rs/book/analysis.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Criterion.rs: reservar Flat sampling para medições longas

## Em uma frase
Criterion oferece modos de amostragem `Auto`, `Linear` e `Flat`, sendo o último destinado a benchmarks de longa duração.

## Por que importa
Reduzir amostras para encurtar teste lento pode empobrecer análise; modo de amostragem apropriado é decisão explícita sobre custo e tratamento estatístico.

## Como funciona
Experimente modo automático primeiro, selecione Flat apenas quando rotina longa exigir e documente que gráficos e análise podem diferir do modo linear padrão.

## Exemplo
Uma migração de banco que leva dezenas de segundos por amostra pode usar modo de longa duração em job noturno separado do smoke performance.

## Limites e trade-offs
Flat muda parte da análise e dos gráficos, por isso resultados de modos diferentes não devem ser misturados sem registrar configuração.

## Como verificar
Compare execução com modos distintos em dataset fixo e verifique tempo real total, cobertura das amostras e relatório produzido.

## Conexões
- [[criterion-baseline-comparison]] — Veja também: Criterion.rs: tratar comparação automática como hipótese.
- [[criterion-throughput-and-log-scale]] — Veja também: Criterion.rs: escolher escala de gráfico para tamanhos crescentes.

## Fontes
- [Criterion.rs — Advanced Configuration](https://bheisler.github.io/criterion.rs/book/user_guide/advanced_configuration.html) — sample size, significance, throughput and sampling modes; consultado em 2026-10-02.
- [Criterion.rs — Analysis Process](https://bheisler.github.io/criterion.rs/book/analysis.html) — warmup, measurement, outliers, bootstrap analysis and comparison; consultado em 2026-10-02.
