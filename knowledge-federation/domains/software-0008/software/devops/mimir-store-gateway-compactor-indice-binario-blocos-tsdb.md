---
id: software.devops.tranche07.000604
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

# Grafana Mimir: Store-Gateway, Compactor, binary index-header e bucket index em blocos TSDB

## Em uma frase
O `compactor` do Grafana Mimir mescla e deduplica blocos TSDB no object storage gerando um `bucket-index`, enquanto o `store-gateway` mantém cabeçalhos binários de índice (`index-header`) para acelerar leituras históricas.

## Por que importa
Como cada réplica de `ingester` envia blocos TSDB de 2 horas para o armazenamento de objetos, um cluster com 3 réplicas e dezenas de ingesters produziria milhares de pequenos blocos redundantes por dia, tornando consultas de longo prazo lentas e caras em chamadas de API S3/GCS. A documentação de arquitetura do Mimir detalha como o `compactor` e o `store-gateway` trabalham em conjunto com índices otimizados para reduzir drasticamente o uso de memória e a latência de leitura.

## Como funciona
Periodicamente, o `compactor` consolida múltiplos blocos de 2 horas do mesmo tenant em blocos maiores e deduplicados, removendo amostras repetidas enviadas pelas réplicas de `ingester`, e atualiza o arquivo de metadados `bucket-index.json.gz` por tenant para evitar listagens custosas de buckets (`LIST` no S3). Já o `store-gateway`, organizado em um hash ring com replicação configurável, descobre os blocos pelo `bucket-index`, baixa apenas um subconjunto compacto do índice TSDB chamado binary `index-header` para o disco local e serve fatias de séries e chunks sob demanda aos `queriers`, além de aproveitar caches em memória (memcached/redis) para páginas de índice e chunks.

## Exemplo
```yaml
# Configuração do blocks_storage, compactor e store_gateway no Grafana Mimir
blocks_storage:
  backend: s3
  s3:
    bucket_name: mimir-tsdb-prod
  bucket_store:
    sync_dir: /data/tsdb-sync
    index_header_lazy_loading_enabled: true
compactor:
  data_dir: /data/compactor
  sharding_ring:
    kvstore:
      store: memberlist
store_gateway:
  sharding_ring:
    replication_factor: 3
```

## Limites e trade-offs
O carregamento preguiçoso (`index_header_lazy_loading_enabled`) economiza tempo de inicialização e memória nos `store-gateways`, mas a primeira consulta a um bloco frio sofre latência adicional enquanto o `index-header` é mapeado via `mmap`. Além disso, falhas prolongadas no `compactor` deixam blocos pequenos e duplicados acumularem no bucket, elevando o consumo de RAM dos `store-gateways` e degradando o tempo de resposta das consultas históricas.

## Como verificar
Verifique o endpoint `/store-gateway/ring` e `/compactor/ring`, e monitore a métrica `cortex_compactor_runs_failed_total` (deve permanecer em `0`) e `cortex_bucket_store_blocks_loaded` para assegurar que os blocos estão sendo compactados e carregados corretamente.

## Conexões
- [[mimir-caminho-leitura-query-frontend-scheduler-querier-sharding]] — Veja também: Grafana Mimir: caminho de leitura com Query-Frontend, Query-Scheduler, Querier e Query Sharding.
- [[mimir-hash-ring-memberlist-gossip-descoberta-estado]] — Veja também: Grafana Mimir: Hash Rings e protocolo gossip Memberlist para coordenação distribuída.
- [[mimir-arquitetura-monolitica-microsservicos-armazenamento-prometheus]] — Referência cruzada direta com mimir-arquitetura-monolitica-microsservicos-armazenamento-prometheus.

## Fontes
- [Grafana Mimir GitHub — README.md (Scalability, Multi-tenancy & Object Storage)](https://raw.githubusercontent.com/grafana/mimir/main/README.md) — README oficial do Grafana Mimir (AGPL-3.0-only) sobre escalabilidade até 1 bilhão de séries ativas, alta disponibilidade e armazenamento de longo prazo para Prometheus; consultado em 2026-10-03.
- [Grafana Mimir Documentation — Architecture & Components](https://grafana.com/docs/mimir/latest/references/architecture/components.md) — Documentação oficial de arquitetura avançada e componentes do Grafana Mimir (Distributor, Ingester, Querier, Query-frontend, Query-scheduler, Store-gateway, Compactor, Ruler e Alertmanager); consultado em 2026-10-03.
- [Grafana Mimir — Official GitHub Repository](https://github.com/grafana/mimir) — Repositório oficial do Grafana Mimir mantido pela Grafana Labs; consultado em 2026-10-03.
