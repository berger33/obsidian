---
id: software.testes.tranche10.000412
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
fontes: ["https://grafana.com/docs/k6/latest/using-k6/scenarios/", "https://grafana.com/docs/k6/latest/using-k6/scenarios/executors/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# k6: separar cenários e executors por workload

## Em uma frase
Scenario descreve como executar funções de teste e escolhe executor, duração, usuários ou taxa de iteração.

## Por que importa
Um teste de carga útil precisa representar o modelo de chegada e transformar métricas em critérios de decisão explícitos. Uma única função default pode misturar perfis de uso diferentes e impedir atribuição clara de métricas.

## Como funciona
Modele cenários e executors a partir do comportamento esperado, segmente métricas com tags e use thresholds para declarar resultados. Separe jornadas relevantes em cenários nomeados e selecione executor conforme a forma de chegada e duração esperada.

## Exemplo
Cenários distintos modelam navegação de leitura e submissões de escrita, cada qual com tags próprias no resultado.

## Limites e trade-offs
Resultados dependem do perfil de workload, ambiente, capacidade geradora e métricas escolhidas; exemplos de thresholds não são SLOs universais. Mais cenários aumentam custo e precisam compartilhar dados com cuidado para não distorcer a carga.

## Como verificar
Confirme no sumário que quantidade de VUs e iterações corresponde ao perfil planejado de cada cenário.

## Conexões
- [[k6-thresholds-criterios-operacionais-pass-fail]] — Veja também: k6: usar thresholds como critério operacional verificável.
- [[k6-open-arrival-closed-vus]] — Veja também: k6: escolher modelo de chegada aberto ou fechado.

## Fontes
- [Grafana k6 — Scenarios](https://grafana.com/docs/k6/latest/using-k6/scenarios/) — execução de workloads nomeados com executors e parâmetros; consultado em 2026-10-02.
- [Grafana k6 — Executors](https://grafana.com/docs/k6/latest/using-k6/scenarios/executors/) — modelos de carga baseados em usuários e taxa de chegada; consultado em 2026-10-02.
