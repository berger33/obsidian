---
id: software.devops.tranche10.000975
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

# vCluster: opções de Backing Store (SQLite embarcado, etcd embarcado/externo, PostgreSQL e MySQL) e Alta Disponibilidade

## Em uma frase
O datastore do plano de controle do vCluster utiliza um banco **SQLite embarcado** por padrão para máxima leveza, mas permite configurar **etcd** (embarcado ou externo em StatefulSet dedicado), **PostgreSQL** ou **MySQL/RDS** com múltiplas réplicas e eleição de líder para Alta Disponibilidade (HA).

## Por que importa
Para ambientes efêmeros de preview ou desenvolvimento, rodar um cluster `etcd` de 3 nós para cada tenant desperdiçaria memória RAM e disco; porém, para Tenant Clusters de produção crítica, um único pod com SQLite em disco local não oferece failover imediato se o nó hospedeiro cair.

## Como funciona
Conforme descreve a seção `Control plane` da página `Architecture` e a tabela `Key features` do README oficial: (1) **SQLite embarcado (padrão)**: roda como parte do processo unificado dentro do pod `vcluster-0` (1 réplica), exigindo mínimo absoluto de CPU/RAM; (2) **Embedded etcd (`v0.35+` com suporte a snapshots etcd v3)** ou **External etcd**: permite escalar o plano de controle com consenso Raft dedicado; e (3) **Bancos relacionais externos (`PostgreSQL`, `MySQL`, Amazon RDS)**: através da camada de tradução Kine, múltiplos Tenant Clusters podem armazenar seu estado em bancos de dados gerenciados de alta disponibilidade na nuvem enquanto o control plane do vCluster roda múltiplas réplicas com **leader election**.

## Exemplo
```yaml
# Exemplo de configuração vcluster.yaml habilitando Alta Disponibilidade (múltiplas réplicas do control plane) com etcd embarcado
controlPlane:
  statefulSet:
    highAvailability:
      replicas: 3
  backingStore:
    etcd:
      embedded:
        enabled: true
```

## Limites e trade-offs
Ao utilizar o datastore padrão **SQLite embarcado**, o plano de controle do vCluster deve rodar com `replicas: 1` (pois o SQLite é um banco em arquivo local que não suporta escritas distribuídas concorrentes entre múltiplos pods); para configurar `replicas: 3` no control plane do vCluster, altere sempre o `backingStore` para `etcd` (embedded/deployed) ou para um banco externo (`database.external` PostgreSQL/MySQL).

## Como verificar
No cluster hospedeiro, execute `kubectl get pods -n <vcluster-namespace>` para verificar a quantidade de réplicas do control plane e se o `etcd` roda embarcado ou em StatefulSet separado.

## Conexões
- [[vcluster-vind-execucao-docker-local-ci-comparacao-kind]] — Veja também: vCluster in Docker (vind): execução de Tenant Clusters diretamente em containers Docker sem Kubernetes prévio.
- [[vcluster-escalonador-host-scheduler-vs-virtual-scheduler-gpu-dra]] — Veja também: vCluster: Host Scheduler vs Virtual Scheduler e agendamento de GPUs com Dynamic Resource Allocation (DRA).
- [[vcluster-clusters-kubernetes-virtuais-multitenancy-arquitetura]] — Referência cruzada direta com vcluster-clusters-kubernetes-virtuais-multitenancy-arquitetura.
- [[vcluster-snapshots-backup-restore-s3-oci-azure-local]] — Referência cruzada direta com vcluster-snapshots-backup-restore-s3-oci-azure-local.
- [[k3s-armazenamento-estado-kine-sqlite-etcd-bancos-relacionais]] — Referência cruzada direta com k3s-armazenamento-estado-kine-sqlite-etcd-bancos-relacionais.

## Fontes
- [vCluster GitHub — README.md (CNCF Certified Kubernetes & AI Conformant, Architecture Comparison, vind, Auto Nodes, Snapshots & Sleep Mode)](https://raw.githubusercontent.com/loft-sh/vcluster/main/README.md) — README oficial do loft-sh/vcluster detalhando Tenant Clusters, comparação entre Shared/Dedicated/Private Nodes/Standalone, driver Docker vind, Auto Nodes (Karpenter), Node VPN, Snapshots e Sleep Mode; consultado em 2026-10-03.
- [vCluster Official Documentation — Architecture (v0.37 Control Plane, API Server, Data Store, Syncer, Virtual Scheduler & vind vs KinD)](https://www.vcluster.com/docs/vcluster/introduction/architecture/) — Documentação oficial de arquitetura do vCluster (v0.37) explicando o processo unificado do control plane (API server, controller manager, datastore SQLite/etcd/SQL, syncer), virtual scheduler e tabela comparativa vind vs KinD; consultado em 2026-10-03.
- [Loft Labs vCluster — Official GitHub Repository](https://github.com/loft-sh/vcluster) — Repositório oficial do vCluster; consultado em 2026-10-03.
