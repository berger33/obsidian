---
id: software.devops.tranche07.000614
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

# Grafana Pyroscope v2: caminho de leitura com Query-Frontend, Query-Backend e geração paralela de Flame Graphs

## Em uma frase
O caminho de leitura do Pyroscope v2 utiliza `query-frontend` e `query-backend` stateless para localizar objetos via `metastore` e executar grafos de subconsultas em paralelo para construir flame graphs.

## Por que importa
Renderizar um flame graph na interface gráfica frequentemente exige ler muitos gigabytes de dados brutos de profiling do object storage e aplicar pós-processamento computacionalmente pesado para agregar pilhas de chamadas. De acordo com a documentação da arquitetura v2 do Pyroscope, separar e paralelizar o caminho de leitura permite escalar `query-frontend` e `query-backend` para centenas de instâncias instantaneamente, sem interferir na ingestão e sem exigir discos locais ou camadas complexas de cache.

## Como funciona
Quando o usuário solicita um perfil ou flame graph pela Query API, a requisição chega ao `query-frontend`, que realiza o planejamento preliminar da consulta, consulta o `metastore` para descobrir exatamente quais objetos de dados no object storage contêm os perfis do serviço e intervalo solicitados, e despacha a execução para o serviço `query-backend`. A execução no `query-backend` é modelada como um grafo distribuído onde múltiplas instâncias buscam objetos do object storage em paralelo, processam as subconsultas e combinam os resultados parciais de forma otimizada para minimizar o tráfego de rede antes de devolver o flame graph consolidado ao cliente.

## Exemplo
```bash
# Consulta à API de leitura do Pyroscope na porta 4040 para listar tipos de perfil e labels disponíveis
curl -s "http://localhost:4040/querier.v1.QuerierService/ProfileTypes" \
  -H "Content-Type: application/json" \
  -d '{}'
```

## Limites e trade-offs
Embora `query-frontend` e `query-backend` sejam completamente stateless e escaláveis horizontalmente, consultas que abrangem janelas temporais muito amplas sobre serviços com milhões de símbolos de funções geram alto throughput de leitura contra o object storage (S3/GCS), podendo incorrer em custos de transferência e limites de taxa de `GET` do provedor de nuvem caso a compactação não esteja em dia.

## Como verificar
Execute consultas de flame graph em janelas de tempo variadas e observe nos logs e métricas do `query-frontend` e `query-backend` o fan-out das subconsultas e o tempo de resposta sem impacto na latência do `segment-writer`.

## Conexões
- [[pyroscope-compactacao-compaction-worker-metastore-raft]] — Veja também: Grafana Pyroscope v2: Metastore com consenso Raft e fusão em segundo plano via Compaction-Worker.
- [[pyroscope-coleta-perfis-sdks-grafana-alloy-opentelemetry-ebpf]] — Veja também: Grafana Pyroscope: instrumentação e coleta de perfis via SDKs, Grafana Alloy e OpenTelemetry eBPF Profiler.
- [[pyroscope-continuous-profiling-arquitetura-v2-object-storage]] — Referência cruzada direta com pyroscope-continuous-profiling-arquitetura-v2-object-storage.
- [[pyroscope-grafana-profiles-drilldown-exploracao-queryless]] — Referência cruzada direta com pyroscope-grafana-profiles-drilldown-exploracao-queryless.

## Fontes
- [Grafana Pyroscope GitHub — README.md (Pyroscope 2.0, SDKs, Alloy & Profiles Drilldown)](https://raw.githubusercontent.com/grafana/pyroscope/main/README.md) — README oficial do Grafana Pyroscope 2.0 detalhando casos de uso proativos e reativos, coleta via SDKs/Grafana Alloy/OpenTelemetry eBPF e visualização no Grafana Profiles Drilldown; consultado em 2026-10-03.
- [Grafana Pyroscope Documentation — About the Pyroscope v2 architecture](https://grafana.com/docs/pyroscope/latest/reference-pyroscope-v2-architecture/about-pyroscope-v2-architecture.md) — Documentação oficial da arquitetura Pyroscope v2 com escrita direta em object storage via distributor e segment-writer, consenso Raft no metastore, compaction-workers e query-frontend/query-backend; consultado em 2026-10-03.
- [Grafana Pyroscope — Official GitHub Repository](https://github.com/grafana/pyroscope) — Repositório oficial AGPL-3.0 do Grafana Pyroscope; consultado em 2026-10-03.
