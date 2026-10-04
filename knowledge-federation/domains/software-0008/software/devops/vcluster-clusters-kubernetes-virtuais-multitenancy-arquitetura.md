---
id: software.devops.tranche10.000971
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

# vCluster: criação de Tenant Clusters Kubernetes isolados e certificados pela CNCF sobre infraestrutura compartilhada

## Em uma frase
O **vCluster** (`loft-sh/vcluster`, distribuição Kubernetes certificada pela CNCF e Kubernetes AI Conformant) provisiona **Tenant Clusters** totalmente isolados — cada um com seu próprio API server, controller manager, armazenamento de dados, CRDs e RBAC — rodando dentro de namespaces de um cluster hospedeiro, em Docker ou em bare metal.

## Por que importa
Compartilhar um único cluster Kubernetes entre dezenas de equipes ou clientes apenas por meio de `Namespace`s e `NetworkPolicy` esbarra em um limite arquitetural: CRDs, `ClusterRole`s, webhooks de admissão e versões de API são globais para todo o cluster, impedindo que um tenant seja `cluster-admin` ou instale seus próprios operadores. Por outro lado, criar 200 clusters EKS/GKE separados multiplica o custo de planos de controle e subutiliza GPUs/CPUs. O README oficial e o guia `Architecture` (`vcluster.com/docs/vcluster/introduction/architecture/`) explicam como o vCluster resolve esse dilema.

## Como funciona
Cada Tenant Cluster criado com **`vcluster create my-vcluster --namespace team-x`** executa um plano de controle dedicado dentro de um único container de um pod `StatefulSet` (`vcluster-0`, acompanhado de um pod `vcluster-coredns`) no namespace `team-x` do **Control Plane Cluster**: (1) **Kubernetes API server** dedicado; (2) **controller manager**; (3) **data store** (por padrão SQLite embarcado, ou `etcd`, MySQL, PostgreSQL); (4) **syncer**, que sincroniza recursos de baixo nível (como `Pod`s e `Service`s) com o namespace subjacente; e (5) **scheduler** (reutilizando o scheduler do cluster hospedeiro por padrão ou ativando o virtual scheduler). Para o usuário, tudo funciona como um cluster Kubernetes upstream independente (`kubectl`, Helm, Argo CD, Crossplane e CRDs).

## Exemplo
```bash
# Instalar a CLI do vCluster, criar um Tenant Cluster isolado no namespace team-x e interagir com ele via kubectl
brew install loft-sh/tap/vcluster
vcluster create my-vcluster --namespace team-x
kubectl get namespaces
```

## Limites e trade-offs
Como todos os recursos sincronizados para o namespace do Control Plane Cluster carregam `ownerReferences` apontando para o pod/recurso do Tenant Cluster, conforme destaca a documentação de arquitetura, **deletar o Tenant Cluster — ou deletar o seu namespace no cluster hospedeiro — remove automaticamente todos os recursos associados** sem deixar recursos órfãos; portanto, proteja os namespaces hospedeiros no Control Plane Cluster com RBAC restrito aos operadores de plataforma.

## Como verificar
Dentro de um Tenant Cluster conectado, instale um CRD qualquer como `cluster-admin` e verifique no cluster hospedeiro (ou em um segundo vCluster `team-y`) que aquele CRD não existe fora do seu Tenant Cluster.

## Conexões
- [[vcluster-componente-syncer-sincronizacao-recursos-tohost-fromhost]] — Veja também: vCluster: funcionamento do Syncer, recursos puramente virtuais vs sincronizados (toHost e fromHost).
- [[vcluster-modos-nos-shared-dedicated-private-nodes-standalone]] — Referência cruzada direta com vcluster-modos-nos-shared-dedicated-private-nodes-standalone.
- [[kind-clusters-kubernetes-locais-containers-docker-arquitetura]] — Referência cruzada direta com kind-clusters-kubernetes-locais-containers-docker-arquitetura.

## Fontes
- [vCluster GitHub — README.md (CNCF Certified Kubernetes & AI Conformant, Architecture Comparison, vind, Auto Nodes, Snapshots & Sleep Mode)](https://raw.githubusercontent.com/loft-sh/vcluster/main/README.md) — README oficial do loft-sh/vcluster detalhando Tenant Clusters, comparação entre Shared/Dedicated/Private Nodes/Standalone, driver Docker vind, Auto Nodes (Karpenter), Node VPN, Snapshots e Sleep Mode; consultado em 2026-10-03.
- [vCluster Official Documentation — Architecture (v0.37 Control Plane, API Server, Data Store, Syncer, Virtual Scheduler & vind vs KinD)](https://www.vcluster.com/docs/vcluster/introduction/architecture/) — Documentação oficial de arquitetura do vCluster (v0.37) explicando o processo unificado do control plane (API server, controller manager, datastore SQLite/etcd/SQL, syncer), virtual scheduler e tabela comparativa vind vs KinD; consultado em 2026-10-03.
- [Loft Labs vCluster — Official GitHub Repository](https://github.com/loft-sh/vcluster) — Repositório oficial do vCluster; consultado em 2026-10-03.
