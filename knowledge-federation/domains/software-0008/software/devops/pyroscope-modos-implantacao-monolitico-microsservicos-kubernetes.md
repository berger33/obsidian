---
id: software.devops.tranche07.000618
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

# Grafana Pyroscope: modos de implantação monolítico e de microsserviços em Kubernetes com Helm

## Em uma frase
O Grafana Pyroscope pode ser implantado como um único binário/container em modo monolítico ou desmembrado em componentes independentes (`distributor`, `segment-writer`, `metastore`, `compaction-worker`, `query-frontend`, `query-backend`) no Kubernetes via Helm.

## Por que importa
Equipes que estão iniciando com continuous profiling precisam de uma instalação simples de nó único para validação rápida, enquanto plataformas de produção que coletam perfis de milhares de containers exigem escalonamento independente entre ingestão e consulta. De acordo com a documentação do Pyroscope v2, ambos os modos compartilham o mesmo binário e a mesma arquitetura orientada a object storage, permitindo evoluir a topologia conforme a demanda cresce.

## Como funciona
No modo monolítico (single-node), um único processo `./pyroscope` (ou container `grafana/pyroscope` na porta `4040`) executa todos os componentes internamente, podendo usar tanto um bucket de object storage quanto o sistema de arquivos local para armazenar os arquivos de bloco. No modo de microsserviços em Kubernetes (implantado via Helm chart oficial), cada papel arquitetural é executado em pods dedicados: `distributor`, `segment-writer`, `compaction-worker`, `query-frontend` e `query-backend` rodam como Deployments stateless sem discos locais, enquanto o `metastore` roda como StatefulSet com consenso Raft, todos apontando para um bucket compartilhado no S3, GCS, Azure Storage ou Swift.

## Exemplo
```bash
# Desempacotar e executar o binário do Pyroscope localmente na porta 4040
tar xvf pyroscope_linux_amd64.tar.gz
./pyroscope

# Verificar os endpoints HTTP expostos na porta 4040
curl -s http://localhost:4040/ready
```

## Limites e trade-offs
O uso de sistema de arquivos local (`filesystem`) como armazenamento de objetos é suportado exclusivamente em implantações de nó único (single-node); tentar escalar múltiplos pods em modo de microsserviços sem configurar um object storage real (S3, GCS, Azure Blob ou Swift) impede que `segment-writers`, `compaction-workers` e `query-backends` compartilhem segmentos e blocos.

## Como verificar
No Kubernetes, verifique com `kubectl get pods` se todos os pods dos componentes do Pyroscope estão `Ready` e consulte `/ready` na porta `4040` para validar a comunicação com o `metastore` e o bucket de objetos.

## Conexões
- [[pyroscope-formatos-bloco-indice-metadados-distribuicao-dados]] — Veja também: Grafana Pyroscope v2: formato de blocos, distribuição adaptativa de dados e índice de metadados.
- [[pyroscope-migracao-v1-para-v2-sem-perda-dados]] — Veja também: Grafana Pyroscope: migração da arquitetura v1 (ingesters com disco) para v2 (object storage direto).
- [[pyroscope-continuous-profiling-arquitetura-v2-object-storage]] — Referência cruzada direta com pyroscope-continuous-profiling-arquitetura-v2-object-storage.
- [[pyroscope-caminho-escrita-distributor-segment-writer-metastore]] — Referência cruzada direta com pyroscope-caminho-escrita-distributor-segment-writer-metastore.

## Fontes
- [Grafana Pyroscope GitHub — README.md (Pyroscope 2.0, SDKs, Alloy & Profiles Drilldown)](https://raw.githubusercontent.com/grafana/pyroscope/main/README.md) — README oficial do Grafana Pyroscope 2.0 detalhando casos de uso proativos e reativos, coleta via SDKs/Grafana Alloy/OpenTelemetry eBPF e visualização no Grafana Profiles Drilldown; consultado em 2026-10-03.
- [Grafana Pyroscope Documentation — About the Pyroscope v2 architecture](https://grafana.com/docs/pyroscope/latest/reference-pyroscope-v2-architecture/about-pyroscope-v2-architecture.md) — Documentação oficial da arquitetura Pyroscope v2 com escrita direta em object storage via distributor e segment-writer, consenso Raft no metastore, compaction-workers e query-frontend/query-backend; consultado em 2026-10-03.
- [Grafana Pyroscope — Official GitHub Repository](https://github.com/grafana/pyroscope) — Repositório oficial AGPL-3.0 do Grafana Pyroscope; consultado em 2026-10-03.
