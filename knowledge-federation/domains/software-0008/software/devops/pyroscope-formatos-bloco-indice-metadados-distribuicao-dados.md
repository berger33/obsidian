---
id: software.devops.tranche07.000617
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

# Grafana Pyroscope v2: formato de blocos, distribuição adaptativa de dados e índice de metadados

## Em uma frase
A arquitetura v2 do Pyroscope organiza os dados em formatos de bloco otimizados no object storage com distribuição adaptativa por serviço e índice de metadados centralizado no `metastore`.

## Por que importa
Uma consulta comum de flame graph na interface gráfica pode abranger horas de execução de um serviço distribuído em centenas de pods; se os perfis desse serviço estivessem espalhados aleatoriamente em milhares de objetos no S3, a leitura exigiria baixar dados irrelevantes de outros serviços. Segundo a documentação oficial da arquitetura v2 do Pyroscope, o posicionamento adaptativo de dados (adaptive data placement) e o índice de metadados minimizam o número de objetos lidos por consulta.

## Como funciona
Durante a ingestão, os `distributors` encaminham os perfis para `segment-writers` específicos de modo a co-localizar perfis da mesma aplicação, garantindo que dados com alta probabilidade de serem consultados juntos sejam armazenados juntos. Cada `segment-writer` grava um único objeto por shard contendo os dados dos serviços daquele shard e registra a localização, o intervalo de tempo e os metadados dos serviços no `metastore`. Posteriormente, os `compaction-workers` fundem esses segmentos em blocos maiores no formato de bloco v2, atualizando o índice de metadados no `metastore` para que o `query-frontend` saiba exatamente quais blocos contêm os dados necessários antes de acionar os `query-backends`.

## Exemplo
```yaml
# Configuração de armazenamento de blocos S3 para o Pyroscope Server
storage:
  backend: s3
  s3:
    endpoint: s3.sa-east-1.amazonaws.com
    bucket_name: pyroscope-v2-blocks
    secret_access_key: ${AWS_SECRET_ACCESS_KEY}
    access_key_id: ${AWS_ACCESS_KEY_ID}
```

## Limites e trade-offs
A co-localização de dados de múltiplos serviços de um tenant dentro de um único objeto por shard reduz drasticamente o custo de chamadas `PUT` no S3 durante a escrita, mas exige que os `compaction-workers` reorganizem e compactem esses dados rapidamente em segundo plano para evitar amplificação de leitura quando um único serviço do shard é consultado em janelas longas.

## Como verificar
Inspecione as métricas de leitura de blocos e de consultas ao `metastore` no endpoint `/metrics` do Pyroscope para confirmar que o número de objetos lidos do object storage por consulta de flame graph permanece baixo após a compactação.

## Conexões
- [[pyroscope-grafana-profiles-drilldown-exploracao-queryless]] — Veja também: Grafana Pyroscope: visualização e análise sem consultas com Grafana Profiles Drilldown.
- [[pyroscope-modos-implantacao-monolitico-microsservicos-kubernetes]] — Veja também: Grafana Pyroscope: modos de implantação monolítico e de microsserviços em Kubernetes com Helm.
- [[pyroscope-continuous-profiling-arquitetura-v2-object-storage]] — Referência cruzada direta com pyroscope-continuous-profiling-arquitetura-v2-object-storage.
- [[pyroscope-caminho-escrita-distributor-segment-writer-metastore]] — Referência cruzada direta com pyroscope-caminho-escrita-distributor-segment-writer-metastore.
- [[pyroscope-compactacao-compaction-worker-metastore-raft]] — Referência cruzada direta com pyroscope-compactacao-compaction-worker-metastore-raft.

## Fontes
- [Grafana Pyroscope GitHub — README.md (Pyroscope 2.0, SDKs, Alloy & Profiles Drilldown)](https://raw.githubusercontent.com/grafana/pyroscope/main/README.md) — README oficial do Grafana Pyroscope 2.0 detalhando casos de uso proativos e reativos, coleta via SDKs/Grafana Alloy/OpenTelemetry eBPF e visualização no Grafana Profiles Drilldown; consultado em 2026-10-03.
- [Grafana Pyroscope Documentation — About the Pyroscope v2 architecture](https://grafana.com/docs/pyroscope/latest/reference-pyroscope-v2-architecture/about-pyroscope-v2-architecture.md) — Documentação oficial da arquitetura Pyroscope v2 com escrita direta em object storage via distributor e segment-writer, consenso Raft no metastore, compaction-workers e query-frontend/query-backend; consultado em 2026-10-03.
- [Grafana Pyroscope — Official GitHub Repository](https://github.com/grafana/pyroscope) — Repositório oficial AGPL-3.0 do Grafana Pyroscope; consultado em 2026-10-03.
