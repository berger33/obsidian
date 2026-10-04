---
id: software.testes.tranche10.000414
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
fontes: ["https://grafana.com/docs/k6/latest/using-k6/metrics/reference/", "https://grafana.com/docs/k6/latest/using-k6/scenarios/executors/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# k6: interpretar dropped iterations junto à capacidade de VUs

## Em uma frase
Arrival-rate executors podem deixar de iniciar iterações quando não há VUs disponíveis ou o tempo máximo termina.

## Por que importa
Um teste de carga útil precisa representar o modelo de chegada e transformar métricas em critérios de decisão explícitos. Ignorar iterações descartadas pode fazer parecer que a taxa planejada foi alcançada quando o gerador não sustentou o perfil.

## Como funciona
Modele cenários e executors a partir do comportamento esperado, segmente métricas com tags e use thresholds para declarar resultados. Dimensione preAllocatedVUs e maxVUs com cautela e trate dropped iterations como sinal a investigar, não como sucesso silencioso.

## Exemplo
Um teste compara taxa prevista, iterações completadas e dropped iterations antes de avaliar latência da aplicação.

## Limites e trade-offs
Resultados dependem do perfil de workload, ambiente, capacidade geradora e métricas escolhidas; exemplos de thresholds não são SLOs universais. Aumentar VUs pode pressionar o gerador e não corrigir gargalo, rede ou limite do próprio cenário.

## Como verificar
Observe recursos do gerador e efetue um teste de controle para separar saturação do cliente de saturação do serviço.

## Conexões
- [[k6-open-arrival-closed-vus]] — Veja também: k6: escolher modelo de chegada aberto ou fechado.
- [[k6-setup-teardown-dados-compartilhados]] — Veja também: k6: manter setup e teardown como lifecycle explícito.

## Fontes
- [Grafana k6 — Built-in metrics](https://grafana.com/docs/k6/latest/using-k6/metrics/reference/) — tipos, semântica e amostragem de métricas k6; consultado em 2026-10-02.
- [Grafana k6 — Executors](https://grafana.com/docs/k6/latest/using-k6/scenarios/executors/) — modelos de carga baseados em usuários e taxa de chegada; consultado em 2026-10-02.
