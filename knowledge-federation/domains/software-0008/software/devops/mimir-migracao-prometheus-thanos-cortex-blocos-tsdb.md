---
id: software.devops.tranche07.000609
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

# Grafana Mimir: migração a partir de Prometheus, Thanos ou Cortex com compatibilidade de blocos TSDB

## Em uma frase
O Grafana Mimir suporta migração direta a partir de Prometheus, Thanos ou Cortex graças à compatibilidade com o protocolo Remote Write, APIs HTTP do Prometheus e formato de blocos TSDB em object storage.

## Por que importa
Organizações que já acumularam meses ou anos de métricas históricas em buckets S3/GCS usando Thanos ou Cortex, ou em discos locais do Prometheus, não podem descartar seu histórico de observabilidade nem reescrever centenas de dashboards Grafana e regras de alerta ao adotar o Mimir. A documentação oficial do Grafana Mimir fornece caminhos diretos de migração para preservar tanto o fluxo em tempo real quanto os blocos históricos.

## Como funciona
Para ingestão em tempo real, basta apontar a seção `remote_write` dos servidores Prometheus existentes (ou agentes Grafana Alloy) para o endpoint `/api/v1/push` do `distributor` do Mimir, informando o cabeçalho `X-Scope-OrgID` se multi-tenancy estiver ativo. Para migrar dados históricos do Prometheus ou do Thanos, os blocos TSDB de 2 horas (ou blocos já compactados pelo Thanos sem downsampling incompatível) são copiados para a pasta do tenant no bucket de objetos do Mimir (`<bucket>/<tenant-id>/`), onde o `compactor` e o `store-gateway` passam a indexá-los no `bucket-index` e servi-los junto às novas métricas; na migração a partir do Cortex com armazenamento em blocos, a estrutura de diretórios e APIs já é diretamente compatível.

## Exemplo
```yaml
# Configuração no prometheus.yml para enviar métricas via remote_write ao Grafana Mimir
remote_write:
  - url: http://mimir-distributor.mimir.svc.cluster.local:8080/api/v1/push
    headers:
      X-Scope-OrgID: cluster-prod-br
    queue_config:
      capacity: 10000
      max_shards: 50
      max_samples_per_send: 2000
```

## Limites e trade-offs
Ao importar blocos históricos gerados pelo Thanos para o bucket do Mimir, blocos que sofreram downsampling específico do Thanos (resoluções de 5m e 1h) não são utilizados pelo motor de leitura padrão do Mimir, devendo-se manter apenas os blocos TSDB de resolução bruta (raw) para evitar desperdício de armazenamento e inconsistências de compactação. Além disso, durante a transição com escrita dupla (dual-writing), o tráfego de rede de saída dos servidores Prometheus dobra.

## Como verificar
Após apontar o `remote_write` e sincronizar os blocos históricos no bucket, execute uma consulta `query_range` no Mimir cobrindo o período anterior e posterior ao corte para validar que não há lacunas temporais nem duplicação de séries nos gráficos do Grafana.

## Conexões
- [[mimir-motor-consulta-promql-otimizacoes-memoria]] — Veja também: Grafana Mimir: motor de consulta PromQL do Mimir (MQE) e redução de consumo de memória.
- [[mimir-operacao-producao-dashboards-alertas-runbooks-mixins]] — Veja também: Grafana Mimir: operação em produção com Mixins, dashboards, alertas e runbooks empacotados.
- [[mimir-arquitetura-monolitica-microsservicos-armazenamento-prometheus]] — Referência cruzada direta com mimir-arquitetura-monolitica-microsservicos-armazenamento-prometheus.
- [[mimir-store-gateway-compactor-indice-binario-blocos-tsdb]] — Referência cruzada direta com mimir-store-gateway-compactor-indice-binario-blocos-tsdb.

## Fontes
- [Grafana Mimir GitHub — README.md (Scalability, Multi-tenancy & Object Storage)](https://raw.githubusercontent.com/grafana/mimir/main/README.md) — README oficial do Grafana Mimir (AGPL-3.0-only) sobre escalabilidade até 1 bilhão de séries ativas, alta disponibilidade e armazenamento de longo prazo para Prometheus; consultado em 2026-10-03.
- [Grafana Mimir Documentation — Architecture & Components](https://grafana.com/docs/mimir/latest/references/architecture/) — Documentação oficial de arquitetura avançada e componentes do Grafana Mimir (Distributor, Ingester, Querier, Query-frontend, Query-scheduler, Store-gateway, Compactor, Ruler e Alertmanager); consultado em 2026-10-03.
- [Grafana Mimir — Official GitHub Repository](https://github.com/grafana/mimir) — Repositório oficial do Grafana Mimir mantido pela Grafana Labs; consultado em 2026-10-03.
