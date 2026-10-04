---
id: software.devops.tranche07.000605
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

# Grafana Mimir: Hash Rings e protocolo gossip Memberlist para coordenação distribuída

## Em uma frase
O Grafana Mimir utiliza estruturas de Hash Ring distribuídas sincronizadas via protocolo gossip Memberlist (ou KV stores como Consul e etcd) para sharding, replicação e descoberta de componentes stateful e stateless.

## Por que importa
Em um sistema distribuído que processa até 1 bilhão de séries ativas, rotear cada série consistente para os mesmos `ingesters` ou dividir blocos e regras entre `store-gateways`, `compactors`, `rulers` e `alertmanagers` exige um mecanismo de consenso leve que não se torne gargalo nem dependa obrigatoriamente de bancos de dados externos. Segundo a documentação de arquitetura do Mimir, os hash rings e o Memberlist resolvem esse problema mantendo uma topologia convergente entre todos os nós do cluster.

## Como funciona
Cada componente participante gera um conjunto de números aleatórios de 32 bits chamados tokens e os registra na estrutura de dados do anel correspondente (`ingester`, `store-gateway`, `compactor`, `ruler`, `alertmanager`). Para determinar qual instância é responsável por uma série ou bloco, o Mimir calcula o hash da chave (por exemplo, os rótulos da métrica ou o ID do bloco) e localiza o próximo token maior no anel. Quando configurado com `store: memberlist`, os nós formam um cluster gossip sobre TCP/UDP (tipicamente na porta `7946`), propagando deltas de estado (`JOINING`, `ACTIVE`, `LEAVING`, `UNHEALTHY`) e batimentos cardíacos periódicos sem precisar manter um cluster Consul ou etcd dedicado.

## Exemplo
```yaml
# Configuração de memberlist e hash ring no Grafana Mimir
memberlist:
  bind_port: 7946
  join_members:
    - dns+mimir-gossip-ring.mimir.svc.cluster.local:7946
ingester:
  ring:
    kvstore:
      store: memberlist
    heartbeat_period: 15s
    heartbeat_timeout: 1m
```

## Limites e trade-offs
O protocolo gossip Memberlist é eventualmente consistente: durante partições de rede transitórias ou inicializações simultâneas de dezenas de pods, visões ligeiramente divergentes do anel podem causar breves períodos de escrita em réplicas extras ou falhas temporárias de quórum. Para que o Memberlist funcione corretamente no Kubernetes, o serviço headless (`clusterIP: None`) usado em `join_members` precisa resolver os IPs individuais de todos os pods participantes (incluindo `publishNotReadyAddresses: true`).

## Como verificar
Acesse as páginas `/memberlist` e `/ingester/ring` na interface HTTP administrativa do Mimir para inspecionar a saúde dos membros do cluster gossip, o número de mensagens trocadas e a ausência de tokens órfãos em estado `UNHEALTHY`.

## Conexões
- [[mimir-store-gateway-compactor-indice-binario-blocos-tsdb]] — Veja também: Grafana Mimir: Store-Gateway, Compactor, binary index-header e bucket index em blocos TSDB.
- [[mimir-multi-tenancy-isolamento-limites-overrides-exporter]] — Veja também: Grafana Mimir: multi-tenancy nativo, isolamento por X-Scope-OrgID, limites de QoS e Overrides-Exporter.
- [[mimir-caminho-escrita-distributor-ingester-replicacao-quorum]] — Referência cruzada direta com mimir-caminho-escrita-distributor-ingester-replicacao-quorum.

## Fontes
- [Grafana Mimir GitHub — README.md (Scalability, Multi-tenancy & Object Storage)](https://raw.githubusercontent.com/grafana/mimir/main/README.md) — README oficial do Grafana Mimir (AGPL-3.0-only) sobre escalabilidade até 1 bilhão de séries ativas, alta disponibilidade e armazenamento de longo prazo para Prometheus; consultado em 2026-10-03.
- [Grafana Mimir Documentation — Architecture & Components](https://grafana.com/docs/mimir/latest/references/architecture/) — Documentação oficial de arquitetura avançada e componentes do Grafana Mimir (Distributor, Ingester, Querier, Query-frontend, Query-scheduler, Store-gateway, Compactor, Ruler e Alertmanager); consultado em 2026-10-03.
- [Grafana Mimir — Official GitHub Repository](https://github.com/grafana/mimir) — Repositório oficial do Grafana Mimir mantido pela Grafana Labs; consultado em 2026-10-03.
