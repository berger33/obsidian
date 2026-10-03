---
id: software.devops.tranche07.000608
tipo: tecnica
dominio: software
subdominio: devops
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-07.md"
fontes: ["https://raw.githubusercontent.com/grafana/mimir/main/README.md", "https://grafana.com/docs/mimir/latest/references/architecture/", "https://github.com/grafana/mimir"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Grafana Mimir: motor de consulta PromQL do Mimir (MQE) e redução de consumo de memória

## Em uma frase
O Mimir Query Engine (MQE) estende e otimiza a avaliação de PromQL evitando buscas caras no índice invertido TSDB e processando fluxos de séries com menor alocação de memória nos `queriers` e `store-gateways`.

## Por que importa
No motor PromQL tradicional do Prometheus, consultas que agregam centenas de milhares de séries temporais materializam grandes estruturas em memória e realizam buscas repetitivas no índice invertido do TSDB, frequentemente causando erros de Out-Of-Memory (OOM) nos `queriers`. Conforme a documentação de arquitetura avançada do Grafana Mimir, o Mimir Query Engine e as otimizações de busca em `store-gateway` reduzem o consumo de memória em até 64% e aceleram consultas de alta cardinalidade.

## Como funciona
O Mimir Query Engine opera como um avaliador compatível com PromQL projetado especificamente para cargas distribuídas e multi-tenant. Ele implementa streaming e decodificação otimizada de blocos e chunks entre `store-gateways`, `ingesters` e `queriers`, além de contornar buscas desnecessárias no índice invertido quando os seletores de rótulos permitem varreduras diretas mais eficientes no cabeçalho binário (`binary index-header`). Combinado ao query sharding do `query-frontend`, o MQE consegue agregar subconjuntos disjuntos de séries em paralelo sem precisar manter todas as séries descomprimidas simultaneamente na memória heap de um único processo Go.

## Exemplo
```bash
# Consulta PromQL de alta cardinalidade executada pelo motor de consulta do Mimir
curl -G -s http://localhost:8080/prometheus/api/v1/query \
  -H "X-Scope-OrgID: tenant-global" \
  --data-urlencode 'query=topk(10, sum by (pod, namespace) (rate(container_cpu_usage_seconds_total[5m])))' \
  --data-urlencode 'stats=all'
```

## Limites e trade-offs
Embora o motor de consulta do Mimir reduza substancialmente o footprint de memória por consulta, expressões com seletores regex não ancorados (como `{pod=~".*api.*"}`) sobre milhões de séries ainda exigem varredura extensa de postagens no índice; nesses casos, configurar limites defensivos como `max_fetched_series_per_query` e `max_fetched_chunk_bytes_per_query` continua essencial para proteger a estabilidade dos `queriers`.

## Como verificar
Adicione o parâmetro `stats=all` nas requisições HTTP à API de consulta do Mimir e monitore o perfil de memória (`go_memstats_heap_inuse_bytes`) e a latência `cortex_querier_request_duration_seconds` nos pods `querier` e `store-gateway`.

## Conexões
- [[mimir-ruler-alertmanager-avaliacao-regras-multi-tenant]] — Veja também: Grafana Mimir: Ruler e Alertmanager opcionais para avaliação de regras e alertas multi-tenant.
- [[mimir-migracao-prometheus-thanos-cortex-blocos-tsdb]] — Veja também: Grafana Mimir: migração a partir de Prometheus, Thanos ou Cortex com compatibilidade de blocos TSDB.
- [[mimir-caminho-leitura-query-frontend-scheduler-querier-sharding]] — Referência cruzada direta com mimir-caminho-leitura-query-frontend-scheduler-querier-sharding.
- [[mimir-store-gateway-compactor-indice-binario-blocos-tsdb]] — Referência cruzada direta com mimir-store-gateway-compactor-indice-binario-blocos-tsdb.

## Fontes
- [Grafana Mimir GitHub — README.md (Scalability, Multi-tenancy & Object Storage)](https://raw.githubusercontent.com/grafana/mimir/main/README.md) — README oficial do Grafana Mimir (AGPL-3.0-only) sobre escalabilidade até 1 bilhão de séries ativas, alta disponibilidade e armazenamento de longo prazo para Prometheus; consultado em 2026-10-03.
- [Grafana Mimir Documentation — Architecture & Components](https://grafana.com/docs/mimir/latest/references/architecture/) — Documentação oficial de arquitetura avançada e componentes do Grafana Mimir (Distributor, Ingester, Querier, Query-frontend, Query-scheduler, Store-gateway, Compactor, Ruler e Alertmanager); consultado em 2026-10-03.
- [Grafana Mimir — Official GitHub Repository](https://github.com/grafana/mimir) — Repositório oficial do Grafana Mimir mantido pela Grafana Labs; consultado em 2026-10-03.
