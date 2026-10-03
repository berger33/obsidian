---
id: software.devops.tranche07.000619
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
fontes: ["https://raw.githubusercontent.com/grafana/pyroscope/main/README.md", "https://grafana.com/docs/pyroscope/latest/reference-pyroscope-v2-architecture/", "https://github.com/grafana/pyroscope"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Grafana Pyroscope: migração da arquitetura v1 (ingesters com disco) para v2 (object storage direto)

## Em uma frase
O Pyroscope 2.0 torna a arquitetura v2 o padrão e permite que implantações v1 existentes habilitem a nova arquitetura via flag e migrem para escrita direta em object storage sem perda de dados.

## Por que importa
Na arquitetura v1 do Pyroscope, os perfis precisavam ser mantidos em memória e em discos locais dentro de `ingesters` stateful antes de serem enviados ao armazenamento de longo prazo, o que exigia provisionamento caro de RAM/SSD e tornava rollouts e reescalonamentos demorados. Segundo o anúncio e a documentação oficial do Pyroscope 2.0, a migração para a v2 elimina os ingesters e discos locais mantendo a continuidade dos dados históricos já coletados.

## Como funciona
Ao atualizar para o Pyroscope 2.0 (ou habilitar a arquitetura v2 via flag de configuração/Helm em implantações v1), o tráfego de ingestão deixa de passar por `ingesters` com WAL em disco local e passa a fluir pelo novo caminho de escrita composto por `distributor` e `segment-writer`, que gravam segmentos diretamente no bucket de object storage e registram seus metadados no `metastore`. Durante e após a transição, o sistema preserva o acesso aos perfis armazenados no bucket para que consultas históricas no Grafana Profiles Drilldown não sofram interrupção nem perda de dados.

## Exemplo
```bash
# Verificação da versão do binário Pyroscope antes de iniciar a migração para v2
./pyroscope -version

# Consulta de saúde e métricas de armazenamento após ativar a arquitetura v2
curl -s http://localhost:4040/metrics | grep -E "pyroscope_build_info|metastore|segment_writer"
```

## Limites e trade-offs
Durante o processo de migração de um cluster v1 em Kubernetes via Helm para a arquitetura v2, é necessário descomissionar de forma ordenada os StatefulSets antigos de `ingester` (garantindo o flush final dos blocos pendentes em seus discos locais) e provisionar o novo componente `metastore` com consenso Raft, além de ajustar dashboards e alertas operacionais que monitoravam métricas antigas de `ingester`.

## Como verificar
Após concluir o rollout de migração via Helm, confirme que novos perfis estão sendo gravados por `segment-writers` e compactados por `compaction-workers`, e execute uma consulta no Grafana cobrindo o período anterior à migração para atestar zero perda de dados.

## Conexões
- [[pyroscope-modos-implantacao-monolitico-microsservicos-kubernetes]] — Veja também: Grafana Pyroscope: modos de implantação monolítico e de microsserviços em Kubernetes com Helm.
- [[pyroscope-casos-uso-proativo-reativo-otimizacao-cpu-memoria-io]] — Veja também: Grafana Pyroscope: uso proativo e reativo de continuous profiling para otimizar CPU, memória e I/O.
- [[pyroscope-continuous-profiling-arquitetura-v2-object-storage]] — Referência cruzada direta com pyroscope-continuous-profiling-arquitetura-v2-object-storage.
- [[pyroscope-compactacao-compaction-worker-metastore-raft]] — Referência cruzada direta com pyroscope-compactacao-compaction-worker-metastore-raft.

## Fontes
- [Grafana Pyroscope GitHub — README.md (Pyroscope 2.0, SDKs, Alloy & Profiles Drilldown)](https://raw.githubusercontent.com/grafana/pyroscope/main/README.md) — README oficial do Grafana Pyroscope 2.0 detalhando casos de uso proativos e reativos, coleta via SDKs/Grafana Alloy/OpenTelemetry eBPF e visualização no Grafana Profiles Drilldown; consultado em 2026-10-03.
- [Grafana Pyroscope Documentation — About the Pyroscope v2 architecture](https://grafana.com/docs/pyroscope/latest/reference-pyroscope-v2-architecture/) — Documentação oficial da arquitetura Pyroscope v2 com escrita direta em object storage via distributor e segment-writer, consenso Raft no metastore, compaction-workers e query-frontend/query-backend; consultado em 2026-10-03.
- [Grafana Pyroscope — Official GitHub Repository](https://github.com/grafana/pyroscope) — Repositório oficial AGPL-3.0 do Grafana Pyroscope; consultado em 2026-10-03.
