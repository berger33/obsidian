---
id: software.devops.tranche07.000602
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

# Grafana Mimir: caminho de escrita com Distributor, Ingester e replicação em quórum

## Em uma frase
O caminho de escrita do Grafana Mimir recebe amostras via remote write no `distributor`, valida limites por tenant e replica cada série em múltiplos `ingesters` (tipicamente fator 3) com confirmação por quórum.

## Por que importa
Perder métricas de produção durante a falha repentina de um nó ou reinicialização de pod compromete alertas críticos de SLO e auditorias de capacidade. De acordo com a documentação do Grafana Mimir, a replicação síncrona de amostras recebidas garante alta disponibilidade na ingestão e permite atualizações ou downgrades contínuos com zero downtime, sem exigir sistemas externos de filas como Apache Kafka no caminho padrão de escrita.

## Como funciona
Quando servidores Prometheus ou agentes Grafana Alloy enviam lotes HTTP POST via protocolo Prometheus Remote Write para o `distributor`, este componente stateless valida a conformidade dos rótulos, aplica limites de taxa e cardinalidade do tenant (`X-Scope-OrgID`) e realiza o sharding das séries usando um hash ring distribuído mantido via protocolo gossip (memberlist) ou armazenamento KV (Consul/etcd). Para cada série temporal, o `distributor` envia as amostras em paralelo via gRPC para `N` `ingesters` distintos (por padrão 3 réplicas em zonas de disponibilidade separadas) e aguarda confirmação de pelo menos um quórum (`floor(N/2) + 1`, ou seja, 2 de 3) antes de retornar sucesso `200 OK` ao cliente.

## Exemplo
```yaml
# Trecho de configuração mimir.yaml para replicação de ingesters com zone awareness
distributor:
  pool:
    health_check_ingesters: true
ingester:
  ring:
    replication_factor: 3
    zone_awareness_enabled: true
    kvstore:
      store: memberlist
```

## Limites e trade-offs
A replicação com fator 3 triplica o consumo de memória RAM e CPU na camada de `ingester` e aumenta o tráfego de rede intra-cluster gRPC entre zonas de disponibilidade. Se `zone_awareness_enabled` estiver ativo mas uma zona inteira ficar sem capacidade ou com número insuficiente de instâncias saudáveis, escritas podem falhar por falta de quórum caso o anel não esteja balanceado simetricamente entre as zonas.

## Como verificar
Inspecione a interface web do anel em `/ingester/ring` para verificar se todos os `ingesters` estão no estado `ACTIVE` com tokens distribuídos entre zonas distintas e monitore a métrica `cortex_distributor_received_samples_total` versus amostras descartadas.

## Conexões
- [[mimir-arquitetura-monolitica-microsservicos-armazenamento-prometheus]] — Veja também: Grafana Mimir: arquitetura monolítica, microsserviços e armazenamento de longo prazo para Prometheus.
- [[mimir-caminho-leitura-query-frontend-scheduler-querier-sharding]] — Veja também: Grafana Mimir: caminho de leitura com Query-Frontend, Query-Scheduler, Querier e Query Sharding.
- [[mimir-hash-ring-memberlist-gossip-descoberta-estado]] — Referência cruzada direta com mimir-hash-ring-memberlist-gossip-descoberta-estado.
- [[mimir-store-gateway-compactor-indice-binario-blocos-tsdb]] — Referência cruzada direta com mimir-store-gateway-compactor-indice-binario-blocos-tsdb.

## Fontes
- [Grafana Mimir GitHub — README.md (Scalability, Multi-tenancy & Object Storage)](https://raw.githubusercontent.com/grafana/mimir/main/README.md) — README oficial do Grafana Mimir (AGPL-3.0-only) sobre escalabilidade até 1 bilhão de séries ativas, alta disponibilidade e armazenamento de longo prazo para Prometheus; consultado em 2026-10-03.
- [Grafana Mimir Documentation — Architecture & Components](https://grafana.com/docs/mimir/latest/references/architecture/components.md) — Documentação oficial de arquitetura avançada e componentes do Grafana Mimir (Distributor, Ingester, Querier, Query-frontend, Query-scheduler, Store-gateway, Compactor, Ruler e Alertmanager); consultado em 2026-10-03.
- [Grafana Mimir — Official GitHub Repository](https://github.com/grafana/mimir) — Repositório oficial do Grafana Mimir mantido pela Grafana Labs; consultado em 2026-10-03.
