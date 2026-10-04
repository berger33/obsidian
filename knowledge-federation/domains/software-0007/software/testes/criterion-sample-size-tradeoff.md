---
id: software.testes.tranche13.000694
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

# Criterion.rs: ajustar sample_size conforme precisão

## Em uma frase
A quantidade de amostras afeta duração da execução e capacidade de estimar diferenças pequenas com a análise estatística configurada.

## Por que importa
Aumentar amostras pode reduzir incerteza, mas multiplica custo de benchmarks lentos e não neutraliza ruído sistemático do ambiente.

## Como funciona
Comece com padrão, altere `sample_size` quando uma decisão exigir sensibilidade diferente e registre significance e tempo junto da configuração adotada.

## Exemplo
Uma comparação de algoritmo executada frequentemente pode reservar amostras moderadas, enquanto investigação de ganho pequeno usa amostra maior em máquina controlada.

## Limites e trade-offs
Aumentar confiança não transforma medição enviesada em evidência correta nem garante que o resultado será reproduzível em outra máquina.

## Como verificar
Compare intervalos, duração e variabilidade ao mudar amostras e repita a mesma alteração sob controle de carga.

## Conexões
- [[criterion-warmup-measurement-phases]] — Veja também: Criterion.rs: separar warmup de coleta de amostras.
- [[criterion-outlier-interpretation]] — Veja também: Criterion.rs: interpretar outliers sem descartá-los.

## Fontes
- [Criterion.rs — Advanced Configuration](https://bheisler.github.io/criterion.rs/book/user_guide/advanced_configuration.html) — sample size, significance, throughput and sampling modes; consultado em 2026-10-02.
- [Criterion.rs — Analysis Process](https://bheisler.github.io/criterion.rs/book/analysis.html) — warmup, measurement, outliers, bootstrap analysis and comparison; consultado em 2026-10-02.
