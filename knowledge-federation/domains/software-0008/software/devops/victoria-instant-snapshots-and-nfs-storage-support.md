---
id: software.devops.tranche05.000415
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

# Backups com snapshots instantâneos (hard links) e suporte a armazenamento NFS (EFS e Filestore)

## Em uma frase
Na seção de recursos proeminentes, o README oficial destaca dois diferenciais de armazenamento do VictoriaMetrics: (1) backup e restauração com **snapshots instantâneos (instant snapshots)** para bases de múltiplos terabytes, que criam pontos de consistência imediatos na estrutura de arquivos sem interromper a ingestão; e (2) suporte oficial para armazenar dados em **sistemas de arquivos baseados em NFS**, como **Amazon EFS** e **Google Filestore**, além de excelente desempenho sobre discos de alta latência de I/O e baixo IOPS (como HDDs e volumes de rede em AWS, GCP e Azure).

## Por que importa
Bancos de dados de séries temporais baseados em `mmap` frequentemente corrompem dados ou sofrem quedas severas de performance quando montados sobre sistemas de arquivos de rede (NFS/EFS) ou discos com latência de I/O variável. A engine de armazenamento do VictoriaMetrics evita essas armadilhas e cria snapshots de terabytes em milissegundos usando hard links.

## Como funciona
Acione o endpoint de criação de snapshot instantâneo (`/snapshot/create`) antes de copiar backups para object storage externo (por exemplo com `vmbackup`) e utilize volumes de rede ou blocos padrão de nuvem com segurança.

## Exemplo
Para realizar backup diário de um banco de séries temporais de 4 TB sem pausar a escrita de métricas, a automação cria um snapshot instantâneo no VictoriaMetrics em menos de um segundo, transfere os blocos imutáveis do snapshot para um bucket S3 e remove o snapshot local ao final.

## Limites e trade-offs
Após concluir a cópia do backup externo a partir de um snapshot local, lembre-se sempre de deletar o snapshot local (`/snapshot/delete`) para que os blocos antigos compactados possam ter seu espaço em disco liberado pelo sistema de arquivos.

## Como verificar
Crie um snapshot via API `/snapshot/create`, liste-o em `/snapshot/list` e remova-o com `/snapshot/delete` verificando a execução instantânea.

## Conexões
- [[victoria-multi-protocol-ingestion-prometheus-influx-graphite-otel]] — Veja também: Ingestão multi-protocolo: Prometheus, InfluxDB, Graphite, OpenTSDB, DataDog, NewRelic e OpenTelemetry.
- [[victoria-ram-footprint-and-compression-benchmarks]] — Veja também: Eficiência de memória RAM, compressão de dados (7x a 70x) e controle de alta cardinalidade.

## Fontes
- [VictoriaMetrics GitHub — README.md (Single-Node & Cluster, MetricsQL, Protocols, Snapshots & Benchmarks)](https://raw.githubusercontent.com/VictoriaMetrics/VictoriaMetrics/master/README.md) — README oficial do VictoriaMetrics detalhando versões Single-node e Cluster sob licença Apache-2.0, armazenamento de longo prazo para Prometheus, linguagens PromQL e MetricsQL, snapshots instantâneos, 11 protocolos de ingestão, suporte a NFS (EFS/Filestore), recursos Enterprise/LTS e benchmarks de RAM e compressão.; consultado em 2026-10-03.
- [VictoriaMetrics Documentation — Key Concepts & Quick Start](https://docs.victoriametrics.com/victoriametrics/keyconcepts/) — Documentação oficial de conceitos fundamentais e início rápido do VictoriaMetrics.; consultado em 2026-10-03.
- [VictoriaMetrics — Official GitHub Repository](https://github.com/VictoriaMetrics/VictoriaMetrics) — Repositório principal Apache-2.0 do VictoriaMetrics com binários para single-node, cluster e vmutils.; consultado em 2026-10-03.
