---
id: software.testes.tranche10.000416
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-10.md"
fontes: ["https://grafana.com/docs/k6/latest/using-k6/tags-and-groups/", "https://grafana.com/docs/k6/latest/using-k6/thresholds/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# k6: usar tags para segmentar métricas de forma controlada

## Em uma frase
Tags categorizam requests, checks, thresholds e métricas customizadas para filtragem e comparação.

## Por que importa
Um teste de carga útil precisa representar o modelo de chegada e transformar métricas em critérios de decisão explícitos. Sem segmentação, dados de endpoints distintos se misturam; tags com valores únicos podem aumentar cardinalidade e custo do backend.

## Como funciona
Modele cenários e executors a partir do comportamento esperado, segmente métricas com tags e use thresholds para declarar resultados. Use valores estáveis como operação, tipo de fluxo e cenário, evitando identificadores por usuário ou request.

## Exemplo
Uma tag `operation:checkout` permite threshold por endpoint lógico sem criar uma série para cada pedido.

## Limites e trade-offs
Resultados dependem do perfil de workload, ambiente, capacidade geradora e métricas escolhidas; exemplos de thresholds não são SLOs universais. Nem toda saída ou backend trata tags da mesma forma; valide o formato e a cardinalidade no destino real.

## Como verificar
Examine séries emitidas e confirme que valores de tags são limitados e não carregam dados sensíveis.

## Conexões
- [[k6-setup-teardown-dados-compartilhados]] — Veja também: k6: manter setup e teardown como lifecycle explícito.
- [[k6-threshold-por-tag-e-escopo-de-metrica]] — Veja também: k6: limitar threshold a segmentos etiquetados.

## Fontes
- [Grafana k6 — Tags and groups](https://grafana.com/docs/k6/latest/using-k6/tags-and-groups/) — tags em métricas, checks, grupos e filtros; consultado em 2026-10-02.
- [Grafana k6 — Thresholds](https://grafana.com/docs/k6/latest/using-k6/thresholds/) — critérios de pass/fail aplicados a métricas e segmentos; consultado em 2026-10-02.
