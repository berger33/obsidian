---
id: software.devops.tranche10.000977
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-10.md"
fontes: ["https://raw.githubusercontent.com/loft-sh/vcluster/main/README.md", "https://www.vcluster.com/docs/vcluster/introduction/architecture/", "https://github.com/loft-sh/vcluster"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# vCluster: redução de custos de infraestrutura com Sleep Mode, vcluster pause/resume e anotações de hibernação

## Em uma frase
O recurso de **Sleep Mode** (e os comandos CLI `vcluster pause` / `vcluster resume`, enriquecidos com anotações em nível de workload na v0.33+) permite pausar Tenant Clusters inativos de desenvolvimento, preview ou treinamento para liberar 100% da CPU/RAM/GPU dos workloads sem perder o estado do cluster.

## Por que importa
Ambientes de desenvolvimento, homologação e preview de Pull Requests costumam ficar ociosos durante a noite e nos finais de semana (mais de 70% das horas da semana), mas continuam consumindo nós caros de computação na nuvem. Deletar o cluster inteiro exigiria reaprovisionar e reinstalar tudo na manhã seguinte; pausar o vCluster zera os pods mantendo todo o estado salvo no datastore.

## Como funciona
Quando um Tenant Cluster entra em **Sleep Mode** (automaticamente por inatividade na vCluster Platform ou manualmente via **`vcluster pause <nome>`**): (1) os `Pod`s dos workloads sincronizados no namespace hospedeiro são encerrados, liberando imediatamente CPU, memória e GPUs para o cluster/autoscaler reduzir os nós; (2) todas as definições de `Deployment`s, `StatefulSet`s, `ConfigMap`s, `Secret`s, `CRD`s e dados no datastore do vCluster permanecem intactos; e (3) assim que o desenvolvedor executa **`vcluster resume <nome>`** (ou faz uma requisição à API do cluster com instant wake configurado), o control plane e os workloads voltam a rodar em segundos exatamente de onde pararam.

## Exemplo
```bash
# Pausar um Tenant Cluster inativo para liberar recursos de computação e retomá-lo instantaneamente quando necessário
vcluster pause my-vcluster --namespace team-x
vcluster list
vcluster resume my-vcluster --namespace team-x
```

## Limites e trade-offs
Quando um vCluster é pausado (`vcluster pause`), todos os processos em memória dentro dos pods daquele Tenant Cluster são terminados (`SIGTERM`); qualquer estado que a aplicação não tenha gravado em um `PersistentVolumeClaim` (`PVC`) ou banco de dados externo será perdido ao pausar, exatamente como ocorreria em um restart de pod.

## Como verificar
Execute `vcluster pause my-vcluster -n team-x` e verifique com `kubectl get pods -n team-x` no cluster hospedeiro que os pods das aplicações do tenant foram removidos, retornando imediatamente após `vcluster resume`.

## Conexões
- [[vcluster-escalonador-host-scheduler-vs-virtual-scheduler-gpu-dra]] — Veja também: vCluster: Host Scheduler vs Virtual Scheduler e agendamento de GPUs com Dynamic Resource Allocation (DRA).
- [[vcluster-snapshots-backup-restore-s3-oci-azure-local]] — Veja também: vCluster: Snapshot e Restore de Tenant Clusters para S3, registries OCI, Azure Blob e armazenamento local.
- [[vcluster-clusters-kubernetes-virtuais-multitenancy-arquitetura]] — Referência cruzada direta com vcluster-clusters-kubernetes-virtuais-multitenancy-arquitetura.
- [[vcluster-vind-execucao-docker-local-ci-comparacao-kind]] — Referência cruzada direta com vcluster-vind-execucao-docker-local-ci-comparacao-kind.
- [[infracost-estimativa-custos-nuvem-terraform-finops-shift-left]] — Referência cruzada direta com infracost-estimativa-custos-nuvem-terraform-finops-shift-left.

## Fontes
- [vCluster GitHub — README.md (CNCF Certified Kubernetes & AI Conformant, Architecture Comparison, vind, Auto Nodes, Snapshots & Sleep Mode)](https://raw.githubusercontent.com/loft-sh/vcluster/main/README.md) — README oficial do loft-sh/vcluster detalhando Tenant Clusters, comparação entre Shared/Dedicated/Private Nodes/Standalone, driver Docker vind, Auto Nodes (Karpenter), Node VPN, Snapshots e Sleep Mode; consultado em 2026-10-03.
- [vCluster Official Documentation — Architecture (v0.37 Control Plane, API Server, Data Store, Syncer, Virtual Scheduler & vind vs KinD)](https://www.vcluster.com/docs/vcluster/introduction/architecture/) — Documentação oficial de arquitetura do vCluster (v0.37) explicando o processo unificado do control plane (API server, controller manager, datastore SQLite/etcd/SQL, syncer), virtual scheduler e tabela comparativa vind vs KinD; consultado em 2026-10-03.
- [Loft Labs vCluster — Official GitHub Repository](https://github.com/loft-sh/vcluster) — Repositório oficial do vCluster; consultado em 2026-10-03.
