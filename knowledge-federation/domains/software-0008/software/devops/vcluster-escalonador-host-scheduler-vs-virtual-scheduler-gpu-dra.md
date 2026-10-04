---
id: software.devops.tranche10.000976
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

# vCluster: Host Scheduler vs Virtual Scheduler e agendamento de GPUs com Dynamic Resource Allocation (DRA)

## Em uma frase
Por padrão, o vCluster reutiliza o **scheduler do Control Plane Cluster** para economizar recursos, mas permite habilitar o **Virtual Scheduler** interno quando o tenant precisa de node labels, taints/tolerations, operações de `drain` ou agendamento avançado de GPUs com **Dynamic Resource Allocation (DRA)**.

## Por que importa
Em um cluster compartilhado de forma densa, rodar um binário `kube-scheduler` separado para cada um dos 100 Tenant Clusters consumiria memória desnecessária; contudo, em cargas de IA/ML ou quando o administrador do Tenant Cluster quer aplicar `kubectl cordon`/`kubectl drain` ou usar taints nos nós visíveis dentro do vCluster, a decisão de agendamento precisa acontecer dentro do próprio vCluster.

## Como funciona
Conforme explica a seção `Control plane` em `vcluster.com/docs/vcluster/introduction/architecture/`: (1) **Host Scheduler (padrão)**: o vCluster não inicia um scheduler próprio; o syncer cria o `Pod` no namespace hospedeiro sem `nodeName` atribuído, deixando o scheduler global do Control Plane Cluster decidir em qual nó colocá-lo; (2) **Virtual Scheduler (`controlPlane.advanced.virtualScheduler.enabled: true`)**: o vCluster executa um scheduler próprio que toma as decisões de posicionamento dentro do Tenant Cluster (respeitando taints, afinidades e `drain` virtuais) e já sincroniza o `Pod` com o `nodeName` definido; e (3) **GPU-aware scheduling (`v0.32+`)**: suporta **Dynamic Resource Allocation (DRA)** com `ResourceClaim`, `ResourceClaimTemplate` e `DeviceClass`, além de redimensionamento de pods in-place (*in-place pod resizing*).

## Exemplo
```yaml
# Habilitar o Virtual Scheduler no vcluster.yaml para suportar taints, node labels e drain dentro do Tenant Cluster
controlPlane:
  advanced:
    virtualScheduler:
      enabled: true
```

## Limites e trade-offs
Para que o **Virtual Scheduler** consiga tomar decisões precisas de agendamento dentro do Tenant Cluster no modo de nós compartilhados/dedicados, o vCluster precisa sincronizar informações reais dos nós a partir do cluster hospedeiro (`sync.fromHost.nodes.enabled: true`); sem visibilidade da capacidade real dos nós, o scheduler virtual não saberia quais nós possuem recursos livres.

## Como verificar
Com o Virtual Scheduler habilitado, execute `kubectl get events` dentro do vCluster ao criar um pod e confirme que os eventos de `Scheduled` são emitidos pelo scheduler do próprio vCluster.

## Conexões
- [[vcluster-armazenamento-estado-sqlite-etcd-postgres-mysql-ha]] — Veja também: vCluster: opções de Backing Store (SQLite embarcado, etcd embarcado/externo, PostgreSQL e MySQL) e Alta Disponibilidade.
- [[vcluster-sleep-mode-pause-resume-economia-custos]] — Veja também: vCluster: redução de custos de infraestrutura com Sleep Mode, vcluster pause/resume e anotações de hibernação.
- [[vcluster-clusters-kubernetes-virtuais-multitenancy-arquitetura]] — Referência cruzada direta com vcluster-clusters-kubernetes-virtuais-multitenancy-arquitetura.
- [[vcluster-modos-nos-shared-dedicated-private-nodes-standalone]] — Referência cruzada direta com vcluster-modos-nos-shared-dedicated-private-nodes-standalone.
- [[vcluster-auto-nodes-karpenter-gpu-ai-factories-slurm-ray]] — Referência cruzada direta com vcluster-auto-nodes-karpenter-gpu-ai-factories-slurm-ray.

## Fontes
- [vCluster GitHub — README.md (CNCF Certified Kubernetes & AI Conformant, Architecture Comparison, vind, Auto Nodes, Snapshots & Sleep Mode)](https://raw.githubusercontent.com/loft-sh/vcluster/main/README.md) — README oficial do loft-sh/vcluster detalhando Tenant Clusters, comparação entre Shared/Dedicated/Private Nodes/Standalone, driver Docker vind, Auto Nodes (Karpenter), Node VPN, Snapshots e Sleep Mode; consultado em 2026-10-03.
- [vCluster Official Documentation — Architecture (v0.37 Control Plane, API Server, Data Store, Syncer, Virtual Scheduler & vind vs KinD)](https://www.vcluster.com/docs/vcluster/introduction/architecture/) — Documentação oficial de arquitetura do vCluster (v0.37) explicando o processo unificado do control plane (API server, controller manager, datastore SQLite/etcd/SQL, syncer), virtual scheduler e tabela comparativa vind vs KinD; consultado em 2026-10-03.
- [Loft Labs vCluster — Official GitHub Repository](https://github.com/loft-sh/vcluster) — Repositório oficial do vCluster; consultado em 2026-10-03.
