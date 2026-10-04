---
id: software.devops.tranche05.000412
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-05.md"
fontes: ["https://raw.githubusercontent.com/VictoriaMetrics/VictoriaMetrics/master/README.md", "https://docs.victoriametrics.com/victoriametrics/keyconcepts/", "https://github.com/VictoriaMetrics/VictoriaMetrics"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Armazenamento de longo prazo para Prometheus e visão global de consulta no VictoriaMetrics

## Em uma frase
Entre os recursos proeminentes listados no README oficial, o VictoriaMetrics atua como **armazenamento de longo prazo (long-term storage) para o Prometheus** ou como **substituto direto (drop-in replacement) para Prometheus e Graphite no Grafana**. Múltiplas instâncias do Prometheus (ou quaisquer outras fontes de métricas) podem ingerir dados simultaneamente no mesmo VictoriaMetrics via `remote_write` ou scraping direto, sendo consultadas de forma unificada por meio de uma **visão global de consulta (Global query view)** em uma única query.

## Por que importa
Instâncias individuais de Prometheus são projetadas para operação local por cluster ou data center e não oferecem visão agregada multi-cluster nativa sem componentes adicionais pesados. Ao receber `remote_write` de todos os Prometheus da frota, o VictoriaMetrics fornece visão global instantânea nos painéis do Grafana.

## Como funciona
Configure `remote_write` nos servidores Prometheus (ou use `vmagent`) apontando para o endpoint de ingestão do VictoriaMetrics e aponte o data source Prometheus do Grafana diretamente para a URL de leitura do VictoriaMetrics.

## Exemplo
Três clusters Kubernetes regionais enviam suas métricas via Prometheus `remote_write` para um VictoriaMetrics central; a equipe de SRE usa um único data source no Grafana para consultar a saúde agregada global das três regiões.

## Limites e trade-offs
Adicione rótulos externos identificadores de origem (`external_labels`, como `cluster` e `region`) em cada instância Prometheus antes de enviar via `remote_write`, evitando colisão de séries temporais idênticas vindas de clusters diferentes.

## Como verificar
Envie métricas de duas instâncias Prometheus distintas para o VictoriaMetrics e execute uma consulta PromQL no Grafana agregando por `cluster` para validar a visão global unificada.

## Conexões
- [[victoria-single-node-and-cluster-tsdb-apache2]] — Veja também: VictoriaMetrics nas versões Single-node e Cluster sob licença Apache-2.0.
- [[victoria-promql-and-metricsql-query-languages]] — Veja também: Compatibilidade com PromQL e extensões de performance e usabilidade do MetricsQL.

## Fontes
- [VictoriaMetrics GitHub — README.md (Single-Node & Cluster, MetricsQL, Protocols, Snapshots & Benchmarks)](https://raw.githubusercontent.com/VictoriaMetrics/VictoriaMetrics/master/README.md) — README oficial do VictoriaMetrics detalhando versões Single-node e Cluster sob licença Apache-2.0, armazenamento de longo prazo para Prometheus, linguagens PromQL e MetricsQL, snapshots instantâneos, 11 protocolos de ingestão, suporte a NFS (EFS/Filestore), recursos Enterprise/LTS e benchmarks de RAM e compressão.; consultado em 2026-10-03.
- [VictoriaMetrics Documentation — Key Concepts & Quick Start](https://docs.victoriametrics.com/victoriametrics/keyconcepts/) — Documentação oficial de conceitos fundamentais e início rápido do VictoriaMetrics.; consultado em 2026-10-03.
- [VictoriaMetrics — Official GitHub Repository](https://github.com/VictoriaMetrics/VictoriaMetrics) — Repositório principal Apache-2.0 do VictoriaMetrics com binários para single-node, cluster e vmutils.; consultado em 2026-10-03.
