---
id: software.devops.tranche07.000613
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

# Grafana Pyroscope v2: Metastore com consenso Raft e fusão em segundo plano via Compaction-Worker

## Em uma frase
O serviço `metastore` (replicado via consenso Raft) mantém o índice de metadados e coordena os `compaction-workers` stateless para fundir pequenos segmentos em blocos maiores em até 15 segundos medianos.

## Por que importa
Em um cluster de grande porte, o número de pequenos segmentos criados no armazenamento de objetos pode chegar a milhões por hora, o que degradaria severamente o desempenho das consultas por amplificação de leitura e sobrecarregaria o índice de metadados. Segundo a documentação oficial da arquitetura v2 do Pyroscope, a compactação contínua em segundo plano mantém o número de objetos e entradas de metadados sob controle sem exigir discos locais nos trabalhadores de compactação.

## Como funciona
O `metastore` é o único componente stateful do Pyroscope v2, utilizando o algoritmo de consenso Raft para replicar o índice de metadados dos blocos e agendar trabalhos de compactação. Assim que novos segmentos são gravados no object storage pelos `segment-writers`, o `metastore` coordena instâncias stateless de `compaction-worker` para buscar esses segmentos pequenos, mesclá-los em blocos maiores e mais eficientes para leitura, gravar os blocos consolidados de volta no object storage e atualizar o índice de metadados. Os `compaction-workers` iniciam a compactação o mais rápido possível após a escrita, mantendo o tempo mediano até a primeira compactação em no máximo 15 segundos.

## Exemplo
```yaml
# Trecho conceitual de implantação distribuída dos papéis metastore e compaction-worker no Pyroscope v2
target: metastore,compaction-worker
storage:
  backend: s3
  s3:
    bucket_name: pyroscope-profiles-prod
    endpoint: s3.amazonaws.com
```

## Limites e trade-offs
Como o `metastore` utiliza consenso Raft e participa tanto do caminho de escrita (registro de novos segmentos e coordenação de compactação) quanto do caminho de leitura (localização de objetos para o `query-frontend`), ele deve ser implantado com número ímpar de réplicas (por exemplo, 3 ou 5) sobre rede e armazenamento de baixa latência; a perda de quórum no Raft interrompe novas confirmações de metadados e agendamentos de compactação.

## Como verificar
Monitore as métricas de saúde do `metastore` e dos `compaction-workers` em `/metrics`, verificando que a latência até a primeira compactação permanece dentro da faixa esperada (~15 segundos) e que não há acúmulo de segmentos não compactados no bucket.

## Conexões
- [[pyroscope-caminho-escrita-distributor-segment-writer-metastore]] — Veja também: Grafana Pyroscope v2: caminho de escrita stateless com Distributor e Segment-Writer.
- [[pyroscope-caminho-leitura-query-frontend-backend-flame-graphs]] — Veja também: Grafana Pyroscope v2: caminho de leitura com Query-Frontend, Query-Backend e geração paralela de Flame Graphs.
- [[pyroscope-continuous-profiling-arquitetura-v2-object-storage]] — Referência cruzada direta com pyroscope-continuous-profiling-arquitetura-v2-object-storage.

## Fontes
- [Grafana Pyroscope GitHub — README.md (Pyroscope 2.0, SDKs, Alloy & Profiles Drilldown)](https://raw.githubusercontent.com/grafana/pyroscope/main/README.md) — README oficial do Grafana Pyroscope 2.0 detalhando casos de uso proativos e reativos, coleta via SDKs/Grafana Alloy/OpenTelemetry eBPF e visualização no Grafana Profiles Drilldown; consultado em 2026-10-03.
- [Grafana Pyroscope Documentation — About the Pyroscope v2 architecture](https://grafana.com/docs/pyroscope/latest/reference-pyroscope-v2-architecture/about-pyroscope-v2-architecture.md) — Documentação oficial da arquitetura Pyroscope v2 com escrita direta em object storage via distributor e segment-writer, consenso Raft no metastore, compaction-workers e query-frontend/query-backend; consultado em 2026-10-03.
- [Grafana Pyroscope — Official GitHub Repository](https://github.com/grafana/pyroscope) — Repositório oficial AGPL-3.0 do Grafana Pyroscope; consultado em 2026-10-03.
