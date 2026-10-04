---
id: software.devops.tranche10.000978
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

# vCluster: Snapshot e Restore de Tenant Clusters para S3, registries OCI, Azure Blob e armazenamento local

## Em uma frase
Conforme destacado nas tabelas `Key features` e `What's new` (`v0.31` a `v0.35`) do README oficial, o vCluster permite capturar **Snapshots** completos de um Tenant Cluster (incluindo SQLite, etcd embarcado ou Standalone) para buckets **S3**, registries **OCI**, **Azure Blob Storage** ou disco local e restaurá-los em qualquer lugar.

## Por que importa
Fazer backup e migrar um cluster Kubernetes tradicional entre regiões ou provedores de nuvem exige ferramentas complexas que exportam centenas de manifestos YAML avulsos. Como todo o estado de controle de um Tenant Cluster está encapsulado no seu datastore, o vCluster consegue empacotar e restaurar um cluster inteiro como uma imagem OCI ou objeto S3.

## Como funciona
Quando o operador executa **`vcluster snapshot create <nome-vcluster> <uri-destino>`** (por exemplo, `oci://ghcr.io/minha-org/snapshots/cluster-a:v1`, `s3://meu-bucket/snap.tar.gz`, `azblob://...` ou `container:///caminho/local.tar.gz`), o vCluster cria um snapshot consistente do datastore do Tenant Cluster (SQLite, etcd v3 embarcado com suporte aprimorado na `v0.35` ou banco externo) e faz upload para o destino escolhido. Para restaurar o estado ou clonar o Tenant Cluster para outro ambiente/cluster hospedeiro, usa-se **`vcluster restore <nome-vcluster> <uri-destino>`** (ou `vcluster create ... --restore <uri>`).

## Exemplo
```bash
# Criar um snapshot de um Tenant Cluster diretamente em um registry OCI e restaurá-lo
vcluster snapshot create my-vcluster oci://ghcr.io/minha-org/vcluster-snaps:prod-backup -n team-x
vcluster snapshot get my-vcluster oci://ghcr.io/minha-org/vcluster-snaps:prod-backup -n team-x
```

## Limites e trade-offs
O snapshot nativo do vCluster captura o estado completo do **plano de controle e recursos da API do Kubernetes** (Deployments, Secrets, ConfigMaps, CRDs, PVCs); se os seus pods dentro do vCluster gravam dados de bancos de dados em discos físicos (`PersistentVolumes`), combine o snapshot do vCluster com snapshots de volumes CSI (ou armazene dados persistentes em serviços de banco externos/S3).

## Como verificar
Liste os snapshots gerados com `vcluster snapshot get` e teste a criação de um cluster clone em outro namespace usando `vcluster create clone-vcluster -n team-clone --restore <uri>`.

## Conexões
- [[vcluster-sleep-mode-pause-resume-economia-custos]] — Veja também: vCluster: redução de custos de infraestrutura com Sleep Mode, vcluster pause/resume e anotações de hibernação.
- [[vcluster-auto-nodes-karpenter-gpu-ai-factories-slurm-ray]] — Veja também: vCluster: Auto Nodes (Karpenter-powered), Node VPN e clusters especializados para IA (Inference, Ray, Run:ai e Slurm).
- [[vcluster-clusters-kubernetes-virtuais-multitenancy-arquitetura]] — Referência cruzada direta com vcluster-clusters-kubernetes-virtuais-multitenancy-arquitetura.
- [[vcluster-armazenamento-estado-sqlite-etcd-postgres-mysql-ha]] — Referência cruzada direta com vcluster-armazenamento-estado-sqlite-etcd-postgres-mysql-ha.
- [[talos-bootstrap-etcd-gerenciamento-control-plane-ha]] — Referência cruzada direta com talos-bootstrap-etcd-gerenciamento-control-plane-ha.

## Fontes
- [vCluster GitHub — README.md (CNCF Certified Kubernetes & AI Conformant, Architecture Comparison, vind, Auto Nodes, Snapshots & Sleep Mode)](https://raw.githubusercontent.com/loft-sh/vcluster/main/README.md) — README oficial do loft-sh/vcluster detalhando Tenant Clusters, comparação entre Shared/Dedicated/Private Nodes/Standalone, driver Docker vind, Auto Nodes (Karpenter), Node VPN, Snapshots e Sleep Mode; consultado em 2026-10-03.
- [vCluster Official Documentation — Architecture (v0.37 Control Plane, API Server, Data Store, Syncer, Virtual Scheduler & vind vs KinD)](https://www.vcluster.com/docs/vcluster/introduction/architecture/) — Documentação oficial de arquitetura do vCluster (v0.37) explicando o processo unificado do control plane (API server, controller manager, datastore SQLite/etcd/SQL, syncer), virtual scheduler e tabela comparativa vind vs KinD; consultado em 2026-10-03.
- [Loft Labs vCluster — Official GitHub Repository](https://github.com/loft-sh/vcluster) — Repositório oficial do vCluster; consultado em 2026-10-03.
