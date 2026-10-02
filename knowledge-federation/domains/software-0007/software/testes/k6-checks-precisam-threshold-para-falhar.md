---
id: software.testes.tranche10.000410
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
fontes: ["https://grafana.com/docs/k6/latest/using-k6/checks/", "https://grafana.com/docs/k6/latest/using-k6/thresholds/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# k6: combinar checks com thresholds para reprovar a execução

## Em uma frase
Checks registram se uma condição observável passou, mas checks falhados não abortam nem reprovam sozinhos o teste.

## Por que importa
Um teste de carga útil precisa representar o modelo de chegada e transformar métricas em critérios de decisão explícitos. Uma carga pode terminar com falhas de status HTTP e ainda sair com execução considerada aprovada se não houver critério agregado.

## Como funciona
Modele cenários e executors a partir do comportamento esperado, segmente métricas com tags e use thresholds para declarar resultados. Defina threshold sobre a taxa de checks ou métrica relevante para transformar o resultado em pass/fail.

## Exemplo
O script valida status 200 e exige que a taxa de checks bem-sucedidos fique acima do objetivo acordado.

## Limites e trade-offs
Resultados dependem do perfil de workload, ambiente, capacidade geradora e métricas escolhidas; exemplos de thresholds não são SLOs universais. Um check bem-sucedido não é uma métrica de latência e o threshold deve corresponder ao objetivo do teste.

## Como verificar
Force respostas inválidas e confirme que o relatório mostra falhas e o processo retorna resultado de acordo com o threshold.

## Conexões
- [[k6-thresholds-criterios-operacionais-pass-fail]] — Veja também: k6: usar thresholds como critério operacional verificável.

## Fontes
- [Grafana k6 — Checks](https://grafana.com/docs/k6/latest/using-k6/checks/) — checks registram taxas de sucesso e não falham o teste sozinhos; consultado em 2026-10-02.
- [Grafana k6 — Thresholds](https://grafana.com/docs/k6/latest/using-k6/thresholds/) — critérios de pass/fail aplicados a métricas e segmentos; consultado em 2026-10-02.
