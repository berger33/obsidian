---
id: software.devops.tranche10.000979
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

# vCluster: Auto Nodes (Karpenter-powered), Node VPN e clusters especializados para IA (Inference, Ray, Run:ai e Slurm)

## Em uma frase
O vCluster suporta provisionamento dinâmico de nós privados baseado em **Karpenter** (**Auto Nodes** `v0.28+` com *node profiles* `v0.36+`), **Node VPN** (`v0.30+`) e serve de fundação certificada (*Kubernetes AI Conformant*) para **Inference Clusters**, **Ray Clusters**, **Run:ai** e **Slurm Clusters**.

## Por que importa
Provedores de nuvem de IA (*AI clouds*), fábricas de IA (*AI factories* on-premises) e plataformas internas que operam milhares de GPUs precisam entregar ambientes isolados onde cada cliente ou execução de treinamento receba seu próprio cluster Kubernetes, Ray ou Slurm com escalonamento automático de nós GPU em nuvem híbrida ou bare metal. O README oficial do vCluster detalha esses casos de uso.

## Como funciona
(1) **Auto Nodes (`autoNodes.enabled: true`)**: utiliza tecnologia baseada no **Karpenter** para provisionar e desprovisionar automaticamente nós privados sob demanda conforme os pods do Tenant Cluster solicitam CPU/GPU, funcionando em nuvem pública, nuvem privada, híbrida e bare metal com perfis por pool (`node profiles` na v0.36+); (2) **Node VPN (`v0.30+`)**: permite que nós privados em diferentes datacenters, redes ou nuvens se juntem ao mesmo Tenant Cluster sobre um overlay VPN criptografado; e (3) **Clusters especializados de IA**: sobre o motor open-source do vCluster, a plataforma entrega clusters dedicados para pilhas de inferência (Dynamo, `llm-d`), **Ray**, **Run:ai** e **Slurm** (*Beta*).

## Exemplo
```yaml
# Exemplo oficial do README habilitando Auto Nodes (autoscaling dinâmico baseado em Karpenter) sobre Private Nodes
autoNodes:
  enabled: true
  nodeProvider: aws
privateNodes:
  enabled: true
```

## Limites e trade-offs
Conforme esclarece a seção `Every kind of cluster` do README oficial, enquanto os **Kubernetes Clusters** e **Nested Clusters** (incluindo Shared/Dedicated/Private Nodes, Standalone e `vind`) fazem parte diretamente do motor open-source no repositório `loft-sh/vcluster`, a entrega gerenciada turnkey de clusters **Slurm**, **Ray**, **Run:ai**, **Inference** e **Node VPN** utiliza a camada **vCluster Platform** (que possui tier gratuito até 64 CPUs e 32 GPUs).

## Como verificar
Consulte a conformidade oficial de IA do vCluster no repositório `cncf/k8s-ai-conformance` referenciado no README e verifique a configuração de `autoNodes` com `vcluster create --help`.

## Conexões
- [[vcluster-snapshots-backup-restore-s3-oci-azure-local]] — Veja também: vCluster: Snapshot e Restore de Tenant Clusters para S3, registries OCI, Azure Blob e armazenamento local.
- [[vcluster-integracoes-nativas-cert-manager-eso-istio-gateway-api]] — Veja também: vCluster: integrações nativas com a pilha do cluster hospedeiro (cert-manager, External Secrets, Istio, KubeVirt e Gateway API).
- [[vcluster-clusters-kubernetes-virtuais-multitenancy-arquitetura]] — Referência cruzada direta com vcluster-clusters-kubernetes-virtuais-multitenancy-arquitetura.
- [[vcluster-modos-nos-shared-dedicated-private-nodes-standalone]] — Referência cruzada direta com vcluster-modos-nos-shared-dedicated-private-nodes-standalone.
- [[vcluster-escalonador-host-scheduler-vs-virtual-scheduler-gpu-dra]] — Referência cruzada direta com vcluster-escalonador-host-scheduler-vs-virtual-scheduler-gpu-dra.

## Fontes
- [vCluster GitHub — README.md (CNCF Certified Kubernetes & AI Conformant, Architecture Comparison, vind, Auto Nodes, Snapshots & Sleep Mode)](https://raw.githubusercontent.com/loft-sh/vcluster/main/README.md) — README oficial do loft-sh/vcluster detalhando Tenant Clusters, comparação entre Shared/Dedicated/Private Nodes/Standalone, driver Docker vind, Auto Nodes (Karpenter), Node VPN, Snapshots e Sleep Mode; consultado em 2026-10-03.
- [vCluster Official Documentation — Architecture (v0.37 Control Plane, API Server, Data Store, Syncer, Virtual Scheduler & vind vs KinD)](https://www.vcluster.com/docs/vcluster/introduction/architecture/) — Documentação oficial de arquitetura do vCluster (v0.37) explicando o processo unificado do control plane (API server, controller manager, datastore SQLite/etcd/SQL, syncer), virtual scheduler e tabela comparativa vind vs KinD; consultado em 2026-10-03.
- [Loft Labs vCluster — Official GitHub Repository](https://github.com/loft-sh/vcluster) — Repositório oficial do vCluster; consultado em 2026-10-03.
