---
id: software.devops.tranche05.000411
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

# VictoriaMetrics nas versões Single-node e Cluster sob licença Apache-2.0

## Em uma frase
O VictoriaMetrics é uma solução rápida, econômica e escalável para monitoramento e gerenciamento de dados de séries temporais (time series data), otimizada inclusive para cenários de alta rotatividade (high churn rate) em que séries antigas são constantemente substituídas por novas. Conforme destaca explicitamente o README oficial (`Yes, we open-source both the single-node VictoriaMetrics and the cluster version`), tanto a **versão Single-node** (`single-server-victoriametrics`) quanto a **versão Cluster** (`cluster-victoriametrics`) são de código aberto sob **Apache License 2.0**, distribuídas em binários no GitHub Releases e imagens no Docker Hub e Quay.

## Por que importa
Muitos bancos de dados de séries temporais mantêm a versão de nó único aberta mas restringem o clustering horizontal a edições proprietárias, ou exigem arquiteturas distribuídas complexas mesmo para cargas médias. O VictoriaMetrics oferece ambas as topologias sob Apache-2.0 e demonstra em seus benchmarks que uma única instância Single-node escalada verticalmente pode substituir clusters inteiros de tamanho médio de soluções concorrentes.

## Como funciona
Comece com a versão **Single-node** do VictoriaMetrics (um único executável pequeno, sem dependências externas, configurado por flags de linha de comando) para a maioria das cargas de monitoramento e adote a versão **Cluster** quando o volume de ingestão ou requisitos de isolamento multi-tenant ultrapassarem a capacidade vertical de um servidor.

## Exemplo
Uma plataforma SaaS consolida métricas de dezenas de clusters Kubernetes em uma instância Single-node do VictoriaMetrics em uma VM com múltiplos núcleos e SSD, migrando posteriormente para a topologia Cluster apenas quando a ingestão supera milhões de amostras por segundo.

## Limites e trade-offs
Evite implantar a versão Cluster distribuída complexa para volumes pequenos ou médios de métricas onde o binário Single-node opera com menor sobrecarga operacional e uso mínimo de memória.

## Como verificar
Inicie o binário do VictoriaMetrics e consulte os endpoints de saúde e métricas internas (`/metrics`) confirmando a operação estável sem dependências externas.

## Conexões
- [[victoria-prometheus-long-term-storage-and-global-query-view]] — Veja também: Armazenamento de longo prazo para Prometheus e visão global de consulta no VictoriaMetrics.

## Fontes
- [VictoriaMetrics GitHub — README.md (Single-Node & Cluster, MetricsQL, Protocols, Snapshots & Benchmarks)](https://raw.githubusercontent.com/VictoriaMetrics/VictoriaMetrics/master/README.md) — README oficial do VictoriaMetrics detalhando versões Single-node e Cluster sob licença Apache-2.0, armazenamento de longo prazo para Prometheus, linguagens PromQL e MetricsQL, snapshots instantâneos, 11 protocolos de ingestão, suporte a NFS (EFS/Filestore), recursos Enterprise/LTS e benchmarks de RAM e compressão.; consultado em 2026-10-03.
- [VictoriaMetrics Documentation — Key Concepts & Quick Start](https://docs.victoriametrics.com/victoriametrics/keyconcepts/) — Documentação oficial de conceitos fundamentais e início rápido do VictoriaMetrics.; consultado em 2026-10-03.
- [VictoriaMetrics — Official GitHub Repository](https://github.com/VictoriaMetrics/VictoriaMetrics) — Repositório principal Apache-2.0 do VictoriaMetrics com binários para single-node, cluster e vmutils.; consultado em 2026-10-03.
