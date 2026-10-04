---
id: software.devops.tranche07.000603
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
fontes: ["https://raw.githubusercontent.com/grafana/mimir/main/README.md", "https://grafana.com/docs/mimir/latest/references/architecture/components.md", "https://github.com/grafana/mimir"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Grafana Mimir: caminho de leitura com Query-Frontend, Query-Scheduler, Querier e Query Sharding

## Em uma frase
O caminho de leitura do Grafana Mimir paraleliza consultas PromQL dividindo intervalos de tempo e fragmentando séries (query sharding) através do `query-frontend`, `query-scheduler` e múltiplos `queriers`.

## Por que importa
Consultas PromQL de alta cardinalidade ou que abrangem semanas de dados históricos facilmente esgotam a memória e a CPU de um único avaliador sequencial. Segundo a documentação oficial do Grafana Mimir, o motor de consulta paraleliza extensivamente a execução para que agregações globais sobre múltiplas instâncias do Prometheus completem em baixa latência mesmo sob alta concorrência de painéis Grafana.

## Como funciona
Quando uma consulta PromQL chega ao `query-frontend`, ele aplica políticas de QoS por tenant, divide consultas de longo alcance em fatias de tempo menores (por exemplo, janelas de 24 horas), decompõe expressões agregáveis em múltiplas subconsultas paralelas via query sharding e verifica o cache de resultados. As subconsultas são enfileiradas no `query-scheduler` (componente opcional que desacopla o gerenciamento de filas do escalonamento do frontend), de onde trabalhadores stateless `querier` puxam tarefas para execução. Cada `querier` busca dados recentes diretamente dos `ingesters` (via gRPC) e dados históricos de blocos TSDB através dos `store-gateways` (ou diretamente do object storage), fundindo e deduplicando as amostras antes de devolver o resultado parcial ao `query-frontend`.

## Exemplo
```bash
# Consulta PromQL enviada ao endpoint compatível com Prometheus no Query-Frontend do Mimir
curl -G -s http://localhost:8080/prometheus/api/v1/query_range \
  -H "X-Scope-OrgID: tenant-producao" \
  --data-urlencode 'query=sum by (cluster) (rate(http_requests_total[5m]))' \
  --data-urlencode 'start=2026-10-01T00:00:00Z' \
  --data-urlencode 'end=2026-10-02T00:00:00Z' \
  --data-urlencode 'step=60s'
```

## Limites e trade-offs
Ativar o query sharding acelera drasticamente agregações pesadas (`sum`, `count`, `avg`), mas multiplica o número de subconsultas internas processadas pelos `queriers` e `store-gateways`; se a fila do `query-scheduler` e a concorrência máxima por `querier` (`-querier.max-concurrent`) não forem dimensionadas proporcionalmente, consultas simples e curtas podem sofrer contenção atrás de dezenas de fragmentos de uma única consulta analítica.

## Como verificar
Analise as métricas `cortex_query_frontend_queries_total` e `cortex_query_scheduler_queue_duration_seconds` para confirmar que o particionamento temporal e o query sharding estão distribuindo subconsultas entre múltiplos `queriers` sem acúmulo de fila.

## Conexões
- [[mimir-caminho-escrita-distributor-ingester-replicacao-quorum]] — Veja também: Grafana Mimir: caminho de escrita com Distributor, Ingester e replicação em quórum.
- [[mimir-store-gateway-compactor-indice-binario-blocos-tsdb]] — Veja também: Grafana Mimir: Store-Gateway, Compactor, binary index-header e bucket index em blocos TSDB.
- [[mimir-arquitetura-monolitica-microsservicos-armazenamento-prometheus]] — Referência cruzada direta com mimir-arquitetura-monolitica-microsservicos-armazenamento-prometheus.
- [[mimir-motor-consulta-promql-otimizacoes-memoria]] — Referência cruzada direta com mimir-motor-consulta-promql-otimizacoes-memoria.

## Fontes
- [Grafana Mimir GitHub — README.md (Scalability, Multi-tenancy & Object Storage)](https://raw.githubusercontent.com/grafana/mimir/main/README.md) — README oficial do Grafana Mimir (AGPL-3.0-only) sobre escalabilidade até 1 bilhão de séries ativas, alta disponibilidade e armazenamento de longo prazo para Prometheus; consultado em 2026-10-03.
- [Grafana Mimir Documentation — Architecture & Components](https://grafana.com/docs/mimir/latest/references/architecture/components.md) — Documentação oficial de arquitetura avançada e componentes do Grafana Mimir (Distributor, Ingester, Querier, Query-frontend, Query-scheduler, Store-gateway, Compactor, Ruler e Alertmanager); consultado em 2026-10-03.
- [Grafana Mimir — Official GitHub Repository](https://github.com/grafana/mimir) — Repositório oficial do Grafana Mimir mantido pela Grafana Labs; consultado em 2026-10-03.
