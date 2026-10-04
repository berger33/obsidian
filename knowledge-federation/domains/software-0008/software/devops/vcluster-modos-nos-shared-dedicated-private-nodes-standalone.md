---
id: software.devops.tranche10.000973
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

# vCluster: comparação arquitetural entre Shared Nodes, Dedicated Nodes, Private Nodes e vCluster Standalone

## Em uma frase
Conforme a matriz `Architecture comparison` do README oficial e do guia `Architecture` (v0.37), o vCluster oferece quatro arquiteturas progressivas de isolamento: **Shared Nodes**, **Dedicated Nodes**, **Private Nodes** (`v0.27+`) e **vCluster Standalone** (`v0.29+`).

## Por que importa
Um ambiente de desenvolvimento/CI prioriza máxima densidade e custo mínimo (**Shared Nodes**), enquanto um provedor de GPU Cloud ou ambiente regulado exige isolamento total de nós, CNI e CSI sem visibilidade cruzada entre tenants (**Private Nodes** ou **Standalone** em bare metal).

## Como funciona
As quatro arquiteturas combinam onde roda o control plane e como os worker nodes são alocados: (1) **Shared Nodes**: o control plane e os pods do tenant compartilham os mesmos nós do Control Plane Cluster usando pseudo-nodes (`sync.fromHost.nodes.enabled: false`), oferecendo máxima densidade; (2) **Dedicated Nodes**: os pods do tenant são isolados em um node pool rotulado (`sync.fromHost.nodes.selector.labels`), mas ainda gerenciados pelo Control Plane Cluster; (3) **Private Nodes (`privateNodes.enabled: true`)**: nós externos (VMs, bare metal ou nuvens remotas via VPN overlay) juntam-se diretamente ao Tenant Cluster via token com sua própria pilha **CNI, CSI e rede isolada**; e (4) **Standalone (`controlPlane.standalone.enabled: true`)**: o control plane roda como um binário autocontido diretamente em bare metal ou VMs sem precisar de nenhum Control Plane Cluster prévio (resolvendo o problema do *"cluster one"*).

## Exemplo
```yaml
# Exemplo oficial de configuração vcluster.yaml para Dedicated Nodes (selecionando um node pool específico por label)
sync:
  fromHost:
    nodes:
      enabled: true
      selector:
        labels:
          tenant: my-tenant
```

## Limites e trade-offs
Enquanto **Shared Nodes** e **Dedicated Nodes** já herdam prontos o CNI (rede), CSI (armazenamento) e controladores de Ingress do Control Plane Cluster sem precisar reinstalá-los em cada vCluster, ao escolher **Private Nodes** ou **vCluster Standalone** você obtém isolamento completo de rede/armazenamento (`CNI/CSI isolation: YES`), mas cada Tenant Cluster passa a gerenciar seus próprios nós workers, CNI e CSI.

## Como verificar
Consulte `kubectl get nodes` de dentro do vCluster para verificar se ele está exibindo pseudo-nodes (Shared Nodes) ou os nós dedicados/privados reais associados ao tenant.

## Conexões
- [[vcluster-componente-syncer-sincronizacao-recursos-tohost-fromhost]] — Veja também: vCluster: funcionamento do Syncer, recursos puramente virtuais vs sincronizados (toHost e fromHost).
- [[vcluster-vind-execucao-docker-local-ci-comparacao-kind]] — Veja também: vCluster in Docker (vind): execução de Tenant Clusters diretamente em containers Docker sem Kubernetes prévio.
- [[vcluster-clusters-kubernetes-virtuais-multitenancy-arquitetura]] — Referência cruzada direta com vcluster-clusters-kubernetes-virtuais-multitenancy-arquitetura.

## Fontes
- [vCluster GitHub — README.md (CNCF Certified Kubernetes & AI Conformant, Architecture Comparison, vind, Auto Nodes, Snapshots & Sleep Mode)](https://raw.githubusercontent.com/loft-sh/vcluster/main/README.md) — README oficial do loft-sh/vcluster detalhando Tenant Clusters, comparação entre Shared/Dedicated/Private Nodes/Standalone, driver Docker vind, Auto Nodes (Karpenter), Node VPN, Snapshots e Sleep Mode; consultado em 2026-10-03.
- [vCluster Official Documentation — Architecture (v0.37 Control Plane, API Server, Data Store, Syncer, Virtual Scheduler & vind vs KinD)](https://www.vcluster.com/docs/vcluster/introduction/architecture/) — Documentação oficial de arquitetura do vCluster (v0.37) explicando o processo unificado do control plane (API server, controller manager, datastore SQLite/etcd/SQL, syncer), virtual scheduler e tabela comparativa vind vs KinD; consultado em 2026-10-03.
- [Loft Labs vCluster — Official GitHub Repository](https://github.com/loft-sh/vcluster) — Repositório oficial do vCluster; consultado em 2026-10-03.
