---
id: software.testes.tranche10.000411
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
fontes: ["https://grafana.com/docs/k6/latest/using-k6/thresholds/", "https://grafana.com/docs/k6/latest/using-k6/metrics/reference/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# k6: usar thresholds como critério operacional verificável

## Em uma frase
Thresholds expressam condições de aprovação sobre métricas e podem afetar o resultado final de uma execução.

## Por que importa
Um teste de carga útil precisa representar o modelo de chegada e transformar métricas em critérios de decisão explícitos. Sem limite declarado, números de latência ou erro ficam sujeitos a interpretação posterior e não controlam CI.

## Como funciona
Modele cenários e executors a partir do comportamento esperado, segmente métricas com tags e use thresholds para declarar resultados. Associe cada threshold a um objetivo, agregação e métrica nomeados, e versione o critério com o script.

## Exemplo
O job exige p95 de duração inferior ao limite acordado e taxa de falha abaixo do máximo permitido.

## Limites e trade-offs
Resultados dependem do perfil de workload, ambiente, capacidade geradora e métricas escolhidas; exemplos de thresholds não são SLOs universais. Threshold é tão útil quanto o workload e o ambiente que o alimentam; não copie valores de exemplo como padrão universal.

## Como verificar
Execute um cenário de controle que viole cada limite e confirme o status de saída do runner.

## Conexões
- [[k6-checks-precisam-threshold-para-falhar]] — Veja também: k6: combinar checks com thresholds para reprovar a execução.
- [[k6-scenarios-executors-workload-nomeado]] — Veja também: k6: separar cenários e executors por workload.

## Fontes
- [Grafana k6 — Thresholds](https://grafana.com/docs/k6/latest/using-k6/thresholds/) — critérios de pass/fail aplicados a métricas e segmentos; consultado em 2026-10-02.
- [Grafana k6 — Built-in metrics](https://grafana.com/docs/k6/latest/using-k6/metrics/reference/) — tipos, semântica e amostragem de métricas k6; consultado em 2026-10-02.
