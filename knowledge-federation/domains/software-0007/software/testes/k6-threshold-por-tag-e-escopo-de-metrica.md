---
id: software.testes.tranche10.000417
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
fontes: ["https://grafana.com/docs/k6/latest/using-k6/thresholds/", "https://grafana.com/docs/k6/latest/using-k6/tags-and-groups/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# k6: limitar threshold a segmentos etiquetados

## Em uma frase
Threshold pode selecionar subconjuntos de métricas filtrando tags associadas aos samples.

## Por que importa
Um teste de carga útil precisa representar o modelo de chegada e transformar métricas em critérios de decisão explícitos. Um SLO agregado pode esconder regressão em uma classe de request mais crítica ou incluir tráfego que não pertence ao objetivo.

## Como funciona
Modele cenários e executors a partir do comportamento esperado, segmente métricas com tags e use thresholds para declarar resultados. Aplique tags consistentes à requisição e declare threshold usando o seletor de métrica e tag correspondentes.

## Exemplo
Requests API e conteúdo estático recebem tags diferentes e têm limites p95 próprios na configuração do run.

## Limites e trade-offs
Resultados dependem do perfil de workload, ambiente, capacidade geradora e métricas escolhidas; exemplos de thresholds não são SLOs universais. Tag ausente ou com grafia divergente pode fazer o seletor abranger zero samples ou o segmento errado.

## Como verificar
Inspecione as amostras do resultado e teste cada expressão com dados que incluam e excluam a tag alvo.

## Conexões
- [[k6-tags-segmentar-metricas-sem-alta-cardinalidade]] — Veja também: k6: usar tags para segmentar métricas de forma controlada.
- [[k6-sleep-pacing-representar-think-time]] — Veja também: k6: modelar think time em vez de adicionar pausas arbitrárias.

## Fontes
- [Grafana k6 — Thresholds](https://grafana.com/docs/k6/latest/using-k6/thresholds/) — critérios de pass/fail aplicados a métricas e segmentos; consultado em 2026-10-02.
- [Grafana k6 — Tags and groups](https://grafana.com/docs/k6/latest/using-k6/tags-and-groups/) — tags em métricas, checks, grupos e filtros; consultado em 2026-10-02.
