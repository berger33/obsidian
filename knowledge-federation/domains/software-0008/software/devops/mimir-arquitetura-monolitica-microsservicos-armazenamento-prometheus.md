---
id: software.devops.tranche07.000601
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

# Grafana Mimir: arquitetura monolítica, microsserviços e armazenamento de longo prazo para Prometheus

## Em uma frase
O Grafana Mimir (distribuído sob licença AGPL-3.0-only) fornece armazenamento multi-tenant de longo prazo e escalabilidade horizontal para métricas do Prometheus até 1 bilhão de séries temporais ativas.

## Por que importa
Instâncias isoladas do Prometheus enfrentam limites verticais de memória, disco local e ausência de visão global entre múltiplos clusters. Segundo a documentação oficial do Grafana Mimir, o projeto resolve essa barreira ao desacoplar ingestão, consulta e compactação sobre object storage (AWS S3, GCS, Azure Blob Storage, OpenStack Swift ou S3-compatível), permitindo começar com um único binário sem dependências externas no modo monolítico (`-target=all`) ou escalar cada componente independentemente em modo de microsserviços.

## Como funciona
Conforme a documentação de arquitetura do Grafana Mimir, o sistema divide sua operação em componentes especializados que interagem em cluster: `distributor`, `ingester`, `querier`, `query-frontend`, `query-scheduler`, `store-gateway` e `compactor`, além de componentes opcionais (`alertmanager`, `ruler` e `overrides-exporter`). No modo monolítico, todos esses componentes rodam dentro de um único processo de sistema operacional, ideal para avaliação rápida, desenvolvimento ou implantações de pequeno e médio porte; já no modo de microsserviços, cada papel é implantado em conjuntos separados de pods Kubernetes, permitindo escalar leitura, escrita e compactação de forma isolada.

## Exemplo
```bash
# Execução local do Grafana Mimir em modo monolítico com configuração mínima
mimir -config.file=mimir-monolithic.yaml -target=all

# Verificação de prontidão e estado dos componentes internos via HTTP
curl -s http://localhost:8080/ready
curl -s http://localhost:8080/services
```

## Limites e trade-offs
O modo de microsserviços oferece isolamento de falhas e elasticidade granular para centenas de milhões de séries ativas, porém introduz complexidade operacional significativa em malhas de rede gRPC, balanceamento de carga e dimensionamento de múltiplos Deployments e StatefulSets. Por outro lado, manter o modo monolítico em cargas massivas acopla picos de consultas pesadas ao consumo de memória do caminho de escrita (`ingester`), podendo degradar a ingestão se não houver limites rígidos por tenant.

## Como verificar
Consulte o endpoint `/ready` e a página administrativa `/services` na porta HTTP do Mimir para confirmar que todos os módulos configurados em `-target` atingiram o estado `RUNNING` sem erros de inicialização de armazenamento de objetos.

## Conexões
- [[mimir-caminho-escrita-distributor-ingester-replicacao-quorum]] — Veja também: Grafana Mimir: caminho de escrita com Distributor, Ingester e replicação em quórum.
- [[mimir-store-gateway-compactor-indice-binario-blocos-tsdb]] — Referência cruzada direta com mimir-store-gateway-compactor-indice-binario-blocos-tsdb.

## Fontes
- [Grafana Mimir GitHub — README.md (Scalability, Multi-tenancy & Object Storage)](https://raw.githubusercontent.com/grafana/mimir/main/README.md) — README oficial do Grafana Mimir (AGPL-3.0-only) sobre escalabilidade até 1 bilhão de séries ativas, alta disponibilidade e armazenamento de longo prazo para Prometheus; consultado em 2026-10-03.
- [Grafana Mimir Documentation — Architecture & Components](https://grafana.com/docs/mimir/latest/references/architecture/components.md) — Documentação oficial de arquitetura avançada e componentes do Grafana Mimir (Distributor, Ingester, Querier, Query-frontend, Query-scheduler, Store-gateway, Compactor, Ruler e Alertmanager); consultado em 2026-10-03.
- [Grafana Mimir — Official GitHub Repository](https://github.com/grafana/mimir) — Repositório oficial do Grafana Mimir mantido pela Grafana Labs; consultado em 2026-10-03.
