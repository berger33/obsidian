---
id: software.testes.tranche08.000215
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

# ML: monitorar drift sem confundir com queda de qualidade

## Em uma frase
Separe mudança na distribuição de entradas de mudança no resultado real do modelo, que pode exigir rótulo tardio.

## Por que importa
Drift em feature é sinal de investigação, não prova isolada de que predição está errada; rótulos e métricas podem chegar depois.

## Como funciona
Acompanhe estatísticas de entrada, disponibilidade de feature, cobertura e métricas supervisionadas quando labels se tornam confiáveis. Defina janela e segmentos relevantes.

## Exemplo
Mudança de canal eleva proporção de valores ausentes; alerta de dados dispara enquanto equipe aguarda rótulo para avaliar impacto preditivo.

## Limites e trade-offs
Limiares estatísticos geram alarmes falsos e podem não captar mudança de relação entre feature e target; combine evidências.

## Como verificar
Simule drift conhecido, missingness e atraso de label; confirme métricas, alerta e decisão de rollback conforme severidade.

## Conexões
- [[ml-calibracao-limiares-decisao]] — Veja também: ML: testar calibração e limiares de decisão.
- [[ml-canary-release-rollback-metricas]] — Veja também: ML: liberar modelo por canário e critério de rollback.

## Fontes
- [Google ML — Monitoring pipelines](https://developers.google.com/machine-learning/crash-course/production-ml-systems/monitoring) — schema, training-serving skew, leakage e métricas de produção; consultado em 2026-10-02.
- [Google ML — Deployment testing](https://developers.google.com/machine-learning/crash-course/production-ml-systems/deployment-testing) — reprodutibilidade, integração e validação de releases de modelos; consultado em 2026-10-02.
