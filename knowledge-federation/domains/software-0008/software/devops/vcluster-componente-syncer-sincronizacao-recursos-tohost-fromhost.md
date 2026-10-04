---
id: software.devops.tranche10.000972
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

# vCluster: funcionamento do Syncer, recursos puramente virtuais vs sincronizados (toHost e fromHost)

## Em uma frase
No modo de nós compartilhados ou dedicados, o componente **syncer** do vCluster mantém objetos de alto nível (`Deployment`, `StatefulSet`, `CRD`, `RBAC`) exclusivamente dentro do datastore do Tenant Cluster e sincroniza apenas os recursos necessários (`Pod`, `Service`, `PersistentVolumeClaim`, `Ingress`) com o namespace do cluster hospedeiro.

## Por que importa
Se um Tenant Cluster sincronizasse todos os seus `Deployment`s, `Role`s e `CustomResourceDefinition`s para o cluster hospedeiro, haveria colisão de versões de CRDs entre diferentes equipes e sobrecarga no `etcd` do cluster hospedeiro. A página oficial `Architecture` explica como o syncer isola a API mantendo a execução leve.

## Como funciona
Quando um desenvolvedor aplica um `Deployment` de 3 réplicas dentro do seu vCluster: (1) o `Deployment` e o `ReplicaSet` são gravados no datastore do próprio vCluster e reconciliados pelo `controller-manager` interno do vCluster, que cria 3 objetos `Pod` virtuais; (2) o **syncer** detecta esses 3 `Pod`s virtuais e os traduz (`sync.toHost`) criando 3 `Pod`s reais dentro do namespace `team-x` do cluster hospedeiro (reescrevendo nomes para evitar colisões); (3) o scheduler e o `kubelet` do cluster hospedeiro iniciam os containers dos pods; e (4) o syncer atualiza o status/IPs de volta (`sync.fromHost`) no API server do vCluster. Recursos de alto nível nunca saem do vCluster!

## Exemplo
```yaml
# Exemplo de configuração vcluster.yaml habilitando sincronização bidirecional customizada no syncer (toHost / fromHost)
sync:
  toHost:
    ingresses:
      enabled: true
  fromHost:
    nodes:
      enabled: false
```

## Limites e trade-offs
Como explica uma nota de arquitetura no README oficial do vCluster, a pilha de plataforma compartilhada (reutilização de CNI, CSI e Ingress do Control Plane Cluster) e o **Resource syncing** (`toHost`/`fromHost`) aplicam-se apenas aos modos **Shared Nodes** e **Dedicated Nodes**; nos modos **Private Nodes** e **Standalone**, os nós workers se juntam diretamente ao Tenant Cluster e não há sincronização de pods para um cluster hospedeiro.

## Como verificar
Crie um `Deployment` chamado `nginx` dentro do vCluster e execute `kubectl get deployments -n team-x` no cluster hospedeiro: você verá que o `Deployment` `nginx` não existe no cluster hospedeiro, mas os `Pod`s sincronizados estão rodando lá.

## Conexões
- [[vcluster-clusters-kubernetes-virtuais-multitenancy-arquitetura]] — Veja também: vCluster: criação de Tenant Clusters Kubernetes isolados e certificados pela CNCF sobre infraestrutura compartilhada.
- [[vcluster-modos-nos-shared-dedicated-private-nodes-standalone]] — Veja também: vCluster: comparação arquitetural entre Shared Nodes, Dedicated Nodes, Private Nodes e vCluster Standalone.
- [[vcluster-armazenamento-estado-sqlite-etcd-postgres-mysql-ha]] — Referência cruzada direta com vcluster-armazenamento-estado-sqlite-etcd-postgres-mysql-ha.

## Fontes
- [vCluster GitHub — README.md (CNCF Certified Kubernetes & AI Conformant, Architecture Comparison, vind, Auto Nodes, Snapshots & Sleep Mode)](https://raw.githubusercontent.com/loft-sh/vcluster/main/README.md) — README oficial do loft-sh/vcluster detalhando Tenant Clusters, comparação entre Shared/Dedicated/Private Nodes/Standalone, driver Docker vind, Auto Nodes (Karpenter), Node VPN, Snapshots e Sleep Mode; consultado em 2026-10-03.
- [vCluster Official Documentation — Architecture (v0.37 Control Plane, API Server, Data Store, Syncer, Virtual Scheduler & vind vs KinD)](https://www.vcluster.com/docs/vcluster/introduction/architecture/) — Documentação oficial de arquitetura do vCluster (v0.37) explicando o processo unificado do control plane (API server, controller manager, datastore SQLite/etcd/SQL, syncer), virtual scheduler e tabela comparativa vind vs KinD; consultado em 2026-10-03.
- [Loft Labs vCluster — Official GitHub Repository](https://github.com/loft-sh/vcluster) — Repositório oficial do vCluster; consultado em 2026-10-03.
