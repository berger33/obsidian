---
id: software.testes.tranche08.000214
tipo: tecnica
dominio: software
subdominio: testes
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-08.md"
fontes: ["https://developers.google.com/machine-learning/crash-course/production-ml-systems/monitoring", "https://developers.google.com/machine-learning/crash-course/production-ml-systems/deployment-testing"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# ML: testar calibração e limiares de decisão

## Em uma frase
Avalie separadamente ranking, calibração e decisão por threshold, pois uma métrica agregada não valida todas as consequências.

## Por que importa
Mudanças de distribuição ou calibração podem alterar a taxa de falso positivo mesmo com ranking aparentemente estável.

## Como funciona
Defina métricas por classe e população, teste thresholds na validação apropriada e compare custos de erro conforme requisito do produto.

## Exemplo
Um modelo mantém AUC, mas a probabilidade de fraude fica superestimada; teste de calibração e threshold aciona revisão antes de alterar bloqueios.

## Limites e trade-offs
Métricas dependem de população, prevalência e custo de decisão; resultados históricos não garantem desempenho futuro nem justiça entre subgrupos.

## Como verificar
Calcule métricas em conjunto de avaliação separado, revise matriz de confusão por faixa e verifique threshold contra política aprovada.

## Conexões
- [[ml-monitoring-drift-feature-label]] — Veja também: ML: monitorar drift sem confundir com queda de qualidade.
- [[ml-canary-release-rollback-metricas]] — Veja também: ML: liberar modelo por canário e critério de rollback.

## Fontes
- [Google ML — Monitoring pipelines](https://developers.google.com/machine-learning/crash-course/production-ml-systems/monitoring) — schema, training-serving skew, leakage e métricas de produção; consultado em 2026-10-02.
- [Google ML — Deployment testing](https://developers.google.com/machine-learning/crash-course/production-ml-systems/deployment-testing) — reprodutibilidade, integração e validação de releases de modelos; consultado em 2026-10-02.
