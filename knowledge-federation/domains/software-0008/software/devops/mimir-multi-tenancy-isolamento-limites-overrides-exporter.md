---
id: software.devops.tranche07.000606
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

# Grafana Mimir: multi-tenancy nativo, isolamento por X-Scope-OrgID, limites de QoS e Overrides-Exporter

## Em uma frase
O Grafana Mimir isola métricas e consultas de múltiplas equipes por meio do cabeçalho HTTP `X-Scope-OrgID`, aplicando limites globais ou por tenant e expondo essas cotas via componente `overrides-exporter`.

## Por que importa
Compartilhar um único cluster de armazenamento de métricas entre dezenas de unidades de negócio reduz drasticamente custos de infraestrutura, mas introduz o risco de "vizinho barulhento" (noisy neighbor), onde um serviço com explosão de cardinalidade derruba a ingestão ou as consultas de toda a empresa. De acordo com a documentação do Grafana Mimir, o suporte nativo a multi-tenancy e controles avançados de QoS garantem que a capacidade do cluster seja dividida de forma justa e segura entre tenants independentes.

## Como funciona
Quando `multitenancy_enabled: true` é definido, todas as requisições de escrita (Remote Write) e leitura (PromQL, regras, alertas) devem informar o identificador do tenant no cabeçalho `X-Scope-OrgID` (podendo especificar múltiplos tenants separados por `|` em consultas federadas de leitura). No armazenamento de objetos, os blocos TSDB e os índices de cada tenant são gravados em prefixos de diretório estritamente separados. O administrador define limites padrão (`limits`) e pode sobrescrever cotas específicas por tenant em um arquivo de `runtime_config` recarregado dinamicamente sem reiniciar processos; o componente opcional `overrides-exporter` lê esse arquivo e expõe os limites vigentes como métricas Prometheus para uso em dashboards de capacidade e alertas preventivos.

## Exemplo
```yaml
# Exemplo de runtime-config.yaml com overrides de limites por tenant no Mimir
overrides:
  tenant-pagamentos:
    ingestion_rate: 100000
    max_global_series_per_user: 5000000
    max_fetched_series_per_query: 250000
  tenant-homologacao:
    ingestion_rate: 10000
    max_global_series_per_user: 200000
```

## Limites e trade-offs
O Grafana Mimir confia no valor do cabeçalho `X-Scope-OrgID` que recebe, não implementando autenticação de usuários ou validação criptográfica de credenciais por conta própria; por isso, em ambientes de produção multi-tenant, é obrigatório posicionar um proxy reverso autenticador (como NGINX, Envoy ou Grafana Enterprise Metrics gateway) na frente do Mimir para injetar `X-Scope-OrgID` a partir de tokens verificados.

## Como verificar
Consulte o endpoint `/runtime_config?mode=diff` no Mimir para confirmar que as sobrescritas por tenant foram carregadas em tempo de execução e verifique as métricas `cortex_limits_overrides` geradas pelo `overrides-exporter`.

## Conexões
- [[mimir-hash-ring-memberlist-gossip-descoberta-estado]] — Veja também: Grafana Mimir: Hash Rings e protocolo gossip Memberlist para coordenação distribuída.
- [[mimir-ruler-alertmanager-avaliacao-regras-multi-tenant]] — Veja também: Grafana Mimir: Ruler e Alertmanager opcionais para avaliação de regras e alertas multi-tenant.
- [[mimir-arquitetura-monolitica-microsservicos-armazenamento-prometheus]] — Referência cruzada direta com mimir-arquitetura-monolitica-microsservicos-armazenamento-prometheus.
- [[mimir-caminho-escrita-distributor-ingester-replicacao-quorum]] — Referência cruzada direta com mimir-caminho-escrita-distributor-ingester-replicacao-quorum.

## Fontes
- [Grafana Mimir GitHub — README.md (Scalability, Multi-tenancy & Object Storage)](https://raw.githubusercontent.com/grafana/mimir/main/README.md) — README oficial do Grafana Mimir (AGPL-3.0-only) sobre escalabilidade até 1 bilhão de séries ativas, alta disponibilidade e armazenamento de longo prazo para Prometheus; consultado em 2026-10-03.
- [Grafana Mimir Documentation — Architecture & Components](https://grafana.com/docs/mimir/latest/references/architecture/components.md) — Documentação oficial de arquitetura avançada e componentes do Grafana Mimir (Distributor, Ingester, Querier, Query-frontend, Query-scheduler, Store-gateway, Compactor, Ruler e Alertmanager); consultado em 2026-10-03.
- [Grafana Mimir — Official GitHub Repository](https://github.com/grafana/mimir) — Repositório oficial do Grafana Mimir mantido pela Grafana Labs; consultado em 2026-10-03.
