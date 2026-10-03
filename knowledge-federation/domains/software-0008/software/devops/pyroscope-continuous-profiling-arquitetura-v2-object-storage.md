---
id: software.devops.tranche07.000611
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
fontes: ["https://raw.githubusercontent.com/grafana/pyroscope/main/README.md", "https://grafana.com/docs/pyroscope/latest/reference-pyroscope-v2-architecture/about-pyroscope-v2-architecture.md", "https://github.com/grafana/pyroscope"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Grafana Pyroscope 2.0: plataforma de continuous profiling e arquitetura v2 nativa em Object Storage

## Em uma frase
O Grafana Pyroscope 2.0 (AGPL-3.0) é uma plataforma de continuous profiling cuja arquitetura v2 padrão grava perfis diretamente em object storage, eliminando ingesters em memória e discos locais.

## Por que importa
Identificar gargalos de CPU, alocações de memória, contenção de locks e operações de I/O em produção exige visibilidade em nível de linha de código ao longo do tempo, tanto de forma proativa (redução de custos de nuvem e latência) quanto reativa (resolução rápida de incidentes). Segundo a documentação oficial do Pyroscope 2.0, o redesenho arquitetural v2 remove a necessidade de discos locais e ingesters stateful da v1, reduzindo drasticamente o consumo de recursos e a sobrecarga operacional em larga escala, além de desacoplar totalmente os caminhos de escrita e leitura.

## Como funciona
Na arquitetura v2 do Grafana Pyroscope, a maioria dos componentes é stateless e não requer persistência local entre reinicializações: o caminho de escrita utiliza `distributor` e `segment-writer` para enviar blocos pequenos (segments) direto para o object storage (Amazon S3, Google Cloud Storage, Azure Storage, OpenStack Swift ou sistema de arquivos local em nó único); o `metastore` (único componente stateful, replicado via consenso Raft) mantém o índice de metadados e coordena os `compaction-workers`; e o caminho de leitura escala horizontalmente com `query-frontend` e `query-backend`. Implantações v1 existentes podem habilitar a arquitetura v2 via flag e migrar sem perda de dados.

## Exemplo
```bash
# Execução rápida do servidor Grafana Pyroscope localmente via Docker na porta 4040
docker run -it --rm -p 4040:4040 grafana/pyroscope:latest

# Verificação de prontidão da instância Pyroscope na porta padrão 4040
curl -s http://localhost:4040/ready
```

## Limites e trade-offs
Embora a arquitetura v2 elimine a gestão de volumes persistentes (PVCs) nos serviços de escrita e leitura, ela torna a disponibilidade e a latência de escrita diretamente dependentes do armazenamento de objetos e da saúde do cluster Raft do `metastore`; em modo de microsserviços, o uso de filesystem local não é suportado, exigindo obrigatoriamente um backend de object storage compatível.

## Como verificar
Inicie o servidor Pyroscope, consulte `http://localhost:4040/ready` e verifique nos logs de inicialização que os módulos da arquitetura v2 e o armazenamento de blocos estão ativos e respondendo na porta `4040`.

## Conexões
- [[pyroscope-caminho-escrita-distributor-segment-writer-metastore]] — Veja também: Grafana Pyroscope v2: caminho de escrita stateless com Distributor e Segment-Writer.
- [[pyroscope-compactacao-compaction-worker-metastore-raft]] — Referência cruzada direta com pyroscope-compactacao-compaction-worker-metastore-raft.
- [[pyroscope-caminho-leitura-query-frontend-backend-flame-graphs]] — Referência cruzada direta com pyroscope-caminho-leitura-query-frontend-backend-flame-graphs.

## Fontes
- [Grafana Pyroscope GitHub — README.md (Pyroscope 2.0, SDKs, Alloy & Profiles Drilldown)](https://raw.githubusercontent.com/grafana/pyroscope/main/README.md) — README oficial do Grafana Pyroscope 2.0 detalhando casos de uso proativos e reativos, coleta via SDKs/Grafana Alloy/OpenTelemetry eBPF e visualização no Grafana Profiles Drilldown; consultado em 2026-10-03.
- [Grafana Pyroscope Documentation — About the Pyroscope v2 architecture](https://grafana.com/docs/pyroscope/latest/reference-pyroscope-v2-architecture/about-pyroscope-v2-architecture.md) — Documentação oficial da arquitetura Pyroscope v2 com escrita direta em object storage via distributor e segment-writer, consenso Raft no metastore, compaction-workers e query-frontend/query-backend; consultado em 2026-10-03.
- [Grafana Pyroscope — Official GitHub Repository](https://github.com/grafana/pyroscope) — Repositório oficial AGPL-3.0 do Grafana Pyroscope; consultado em 2026-10-03.
