---
id: software.testes.tranche10.000413
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
fontes: ["https://grafana.com/docs/k6/latest/using-k6/scenarios/concepts/open-vs-closed/", "https://grafana.com/docs/k6/latest/using-k6/scenarios/executors/", "https://grafana.com/docs/k6/latest/using-k6/metrics/reference/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# k6: escolher modelo de chegada aberto ou fechado

## Em uma frase
Executors baseados em VUs mantêm usuários virtuais que iniciam nova iteração após a anterior; arrival-rate agenda iterações por taxa.

## Por que importa
Um teste de carga útil precisa representar o modelo de chegada e transformar métricas em critérios de decisão explícitos. Com modelo fechado, a taxa de novas iterações pode cair quando o sistema fica lento; isso altera o estímulo recebido.

## Como funciona
Modele cenários e executors a partir do comportamento esperado, segmente métricas com tags e use thresholds para declarar resultados. Selecione modelo de chegada conforme a pergunta do teste e monitore dropped iterations quando a taxa for aberta.

## Exemplo
Uma taxa de chegada constante mede comportamento de fila sob volume oferecido, enquanto usuários fechados representam sessões que pensam entre ações.

## Limites e trade-offs
Resultados dependem do perfil de workload, ambiente, capacidade geradora e métricas escolhidas; exemplos de thresholds não são SLOs universais. Modelos não são intercambiáveis e a escolha inadequada pode produzir conclusões diferentes sobre saturação.

## Como verificar
Compare taxa prevista e taxa efetiva durante atraso artificial e confira dropped iterations e duração das iterações.

## Conexões
- [[k6-scenarios-executors-workload-nomeado]] — Veja também: k6: separar cenários e executors por workload.
- [[k6-dropped-iterations-capacidade-vus]] — Veja também: k6: interpretar dropped iterations junto à capacidade de VUs.

## Fontes
- [Grafana k6 — Open and closed models](https://grafana.com/docs/k6/latest/using-k6/scenarios/concepts/open-vs-closed/) — diferença entre chegada desacoplada e iterações condicionadas à duração do VU; consultado em 2026-10-02.
- [Grafana k6 — Executors](https://grafana.com/docs/k6/latest/using-k6/scenarios/executors/) — modelos de carga baseados em usuários e taxa de chegada; consultado em 2026-10-02.
- [Grafana k6 — Built-in metrics](https://grafana.com/docs/k6/latest/using-k6/metrics/reference/) — tipos, semântica e amostragem de métricas k6; consultado em 2026-10-02.
