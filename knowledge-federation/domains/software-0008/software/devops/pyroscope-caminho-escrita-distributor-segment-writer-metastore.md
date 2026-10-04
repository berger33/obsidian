---
id: software.devops.tranche07.000612
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

# Grafana Pyroscope v2: caminho de escrita stateless com Distributor e Segment-Writer

## Em uma frase
No caminho de escrita do Pyroscope v2, os componentes stateless e sem disco `distributor` e `segment-writer` agrupam perfis da mesma aplicação em pequenos segmentos gravados sincronamente no object storage.

## Por que importa
Em sistemas de profiling contínuo que recebem milhares de amostras de pilha por segundo de centenas de microsserviços, gravar cada perfil individualmente no S3 ou GCS geraria custos proibitivos de requisições `PUT` e alta amplificação de leitura posterior. De acordo com a documentação da arquitetura v2 do Pyroscope, o agrupamento inteligente por serviço no `segment-writer` minimiza o número de operações de escrita no object storage e co-localiza perfis que serão consultados juntos.

## Como funciona
Os perfis chegam ao `distributor` através da API Push RPC ou do endpoint HTTP `/ingest`. O `distributor` roteia as requisições para instâncias de `segment-writer` de forma a concentrar perfis da mesma aplicação no mesmo escritor. O `segment-writer` acumula os perfis recebidos em pequenos blocos chamados segmentos (segments), produzindo um único objeto por shard que contém os dados de todos os serviços do tenant naquele shard, grava o segmento diretamente no object storage e atualiza o índice de blocos no serviço `metastore`. Por padrão, a ingestão é síncrona: os clientes permanecem bloqueados até que o objeto esteja duravelmente salvo no object storage e registrado no índice de metadados, com latência mediana esperada inferior a 500 ms.

## Exemplo
```bash
# Verificação de métricas do caminho de escrita (distributor e segment-writer) no Pyroscope
curl -s http://localhost:4040/metrics | grep -E "pyroscope_(distributor|segment_writer|ingest)"
```

## Limites e trade-offs
Como a ingestão padrão aguarda a confirmação de escrita no object storage e de registro no `metastore` (latência mediana < 500 ms), os clientes de envio (SDKs, Grafana Alloy ou coletores OTel) precisam configurar timeouts de requisição adequados e buffers de retentativa para absorver oscilações momentâneas de latência na API do provedor de armazenamento em nuvem.

## Como verificar
Envie perfis de teste para o endpoint de ingestão do Pyroscope e confirme que objetos de segmentos estão sendo criados no bucket configurado e registrados no índice do `metastore` sem erros HTTP 5xx no `distributor`.

## Conexões
- [[pyroscope-continuous-profiling-arquitetura-v2-object-storage]] — Veja também: Grafana Pyroscope 2.0: plataforma de continuous profiling e arquitetura v2 nativa em Object Storage.
- [[pyroscope-compactacao-compaction-worker-metastore-raft]] — Veja também: Grafana Pyroscope v2: Metastore com consenso Raft e fusão em segundo plano via Compaction-Worker.
- [[pyroscope-coleta-perfis-sdks-grafana-alloy-opentelemetry-ebpf]] — Referência cruzada direta com pyroscope-coleta-perfis-sdks-grafana-alloy-opentelemetry-ebpf.

## Fontes
- [Grafana Pyroscope GitHub — README.md (Pyroscope 2.0, SDKs, Alloy & Profiles Drilldown)](https://raw.githubusercontent.com/grafana/pyroscope/main/README.md) — README oficial do Grafana Pyroscope 2.0 detalhando casos de uso proativos e reativos, coleta via SDKs/Grafana Alloy/OpenTelemetry eBPF e visualização no Grafana Profiles Drilldown; consultado em 2026-10-03.
- [Grafana Pyroscope Documentation — About the Pyroscope v2 architecture](https://grafana.com/docs/pyroscope/latest/reference-pyroscope-v2-architecture/about-pyroscope-v2-architecture.md) — Documentação oficial da arquitetura Pyroscope v2 com escrita direta em object storage via distributor e segment-writer, consenso Raft no metastore, compaction-workers e query-frontend/query-backend; consultado em 2026-10-03.
- [Grafana Pyroscope — Official GitHub Repository](https://github.com/grafana/pyroscope) — Repositório oficial AGPL-3.0 do Grafana Pyroscope; consultado em 2026-10-03.
