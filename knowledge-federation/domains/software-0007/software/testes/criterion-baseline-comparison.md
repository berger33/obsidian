---
id: software.testes.tranche13.000696
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

# Criterion.rs: tratar comparação automática como hipótese

## Em uma frase
Criterion compara estatísticas atuais com dados previamente salvos e estima se a diferença pode ser atribuída a variação.

## Por que importa
Uma comparação repetível acelera revisão de desempenho, desde que baseline tenha sido obtido de código e ambiente comparáveis.

## Como funciona
Salve resultados por revisão, use mesmo grupo e inputs, examine intervalo de mudança e p-value apresentados e confirme ganhos importantes com novo run controlado.

## Exemplo
Um job compara branch de feature ao artefato de referência, mantendo CPU, perfil de build e dataset equivalentes.

## Limites e trade-offs
Ruído de sistema ou mudança de ambiente pode produzir aparente melhora pequena; comparação automática não identifica qual alteração causalmente mudou o tempo.

## Como verificar
Rode versão de referência duas vezes e meça a dispersão antes de interpretar sinal de regressão da branch.

## Conexões
- [[criterion-outlier-interpretation]] — Veja também: Criterion.rs: interpretar outliers sem descartá-los.
- [[criterion-flat-sampling-long-workload]] — Veja também: Criterion.rs: reservar Flat sampling para medições longas.

## Fontes
- [Criterion.rs — Analysis Process](https://bheisler.github.io/criterion.rs/book/analysis.html) — warmup, measurement, outliers, bootstrap analysis and comparison; consultado em 2026-10-02.
- [Criterion.rs — Command-Line Output](https://bheisler.github.io/criterion.rs/book/user_guide/command_line_output.html) — confidence intervals, change summaries and outlier reporting; consultado em 2026-10-02.
