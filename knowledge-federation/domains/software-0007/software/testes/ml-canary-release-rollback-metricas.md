---
id: software.testes.tranche08.000219
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
fontes: ["https://developers.google.com/machine-learning/crash-course/production-ml-systems/deployment-testing", "https://developers.google.com/machine-learning/crash-course/production-ml-systems/monitoring"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# ML: liberar modelo por canário e critério de rollback

## Em uma frase
Defina métricas e guardrails antes de expor uma versão de modelo a uma fração de tráfego.

## Por que importa
Canário reduz blast radius, mas sem baseline e condição de rollback a equipe pode ampliar exposição durante regressão silenciosa.

## Como funciona
Compare versões em tráfego compatível, monitore latência, erro, qualidade disponível e segmentos de risco, e mantenha artefato anterior pronto para retorno.

## Exemplo
Uma versão começa em pequena população; aumento de erro de serving ou indicador de dano acima do limite pausa promoção automaticamente.

## Limites e trade-offs
Métricas de qualidade com rótulo tardio não são imediatas; guardrails técnicos não substituem auditoria de impacto ou análise de subgrupos.

## Como verificar
Simule falha de qualidade e infraestrutura, confirme congelamento de rollout e rollback para versão conhecida com rastreabilidade.

## Conexões
- [[ml-calibracao-limiares-decisao]] — Veja também: ML: testar calibração e limiares de decisão.
- [[ml-monitoring-drift-feature-label]] — Veja também: ML: monitorar drift sem confundir com queda de qualidade.

## Fontes
- [Google ML — Deployment testing](https://developers.google.com/machine-learning/crash-course/production-ml-systems/deployment-testing) — reprodutibilidade, integração e validação de releases de modelos; consultado em 2026-10-02.
- [Google ML — Monitoring pipelines](https://developers.google.com/machine-learning/crash-course/production-ml-systems/monitoring) — schema, training-serving skew, leakage e métricas de produção; consultado em 2026-10-02.
