---
id: software.devops.tranche17.001627
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-17.md"
fontes: ["https://raw.githubusercontent.com/liqotech/liqo/master/README.md", "https://docs.liqo.io/en/stable/examples/quick-start.html", "https://github.com/liqotech/liqo"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Liqo: *Storage Fabric* e `StorageClass` virtual (`liqo`) para aplicações stateful com gravidade de dados

## Em uma frase
A *Storage Fabric* do Liqo permite executar cargas de trabalho stateful (`StatefulSet`, bancos de dados replicados) em múltiplos clusters por meio de uma `StorageClass` virtual (`liqo`) que adia o provisionamento real do volume (`WaitForFirstConsumer`) para o cluster onde o Pod for agendado.

## Por que importa
Um `PersistentVolumeClaim` tradicional está preso a um único cluster físico; se um Pod de um `StatefulSet` for agendado em um nó virtual apontando para outro cluster, ele não conseguiria montar um disco EBS/PD criado no cluster de origem.

## Como funciona
Quando um PVC solicita `storageClassName: liqo` (com `volumeBindingMode: WaitForFirstConsumer`), o Liqo aguarda a decisão do scheduler. Se o Pod for agendado no nó virtual `liqo-milan`, a Storage Fabric cria um PVC real no cluster `milan` usando a `StorageClass` padrão de `milan`, vincula o PV virtual no consumidor e adiciona afinidade permanente de nó ao PV para garantir a *gravidade de dados* (reagendamentos futuros daquele Pod irão sempre para o cluster onde o disco reside).

## Exemplo
```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: db-data-pvc
  namespace: demo-app
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: liqo
  resources:
    requests:
      storage: 10Gi
```

## Limites e trade-offs
O Liqo não copia blocos de disco síncronos entre nuvens para um único PVC `ReadWriteOnce`; a alta disponibilidade multi-cluster de bancos de dados é obtida agendando réplicas do `StatefulSet` em clusters diferentes, onde cada réplica usa seu próprio PVC `liqo` local ao seu cluster e replica dados no nível da aplicação (ex.: Raft/PostgreSQL/MySQL).

## Como verificar
Crie um `StatefulSet` usando `storageClassName: liqo` e confirme que os PVCs reais são provisionados nos respectivos clusters onde cada réplica do `StatefulSet` foi alocada.

## Conexões
- [[liqo-service-offloading-endpointslice-reflection-multi-cluster]] — Veja também: Liqo: reflexão de `Services` e `EndpointSlices` para descoberta e balanceamento de carga multi-cluster.
- [[liqo-crd-replicator-sincronizacao-estado-out-of-band-in-band]] — Veja também: Liqo: sincronização de Custom Resources entre clusters via `liqo-crd-replicator` e modos de peering.

## Fontes
- [Liqo GitHub — README.md (Dynamic and Seamless Kubernetes Multi-Cluster Topologies, Peering, Offloading, Network & Storage Fabric)](https://raw.githubusercontent.com/liqotech/liqo/master/README.md) — README oficial do liqotech/liqo detalhando peering P2P, Virtual Nodes via Virtual Kubelet, Network Fabric com NATless/NATting IPAM, reflexão de Services e Storage Fabric; consultado em 2026-10-03.
- [Liqo Official Documentation — Quick Start & Examples (liqoctl peer, liqoctl offload namespace, Virtual Node Scheduling & Service Exposure)](https://docs.liqo.io/en/stable/examples/quick-start.html) — Guia oficial Quick Start do Liqo demonstrando peering entre clusters, extensão de namespaces com liqoctl offload e agendamento transparente de Pods remotos; consultado em 2026-10-03.
- [Liqo — Official GitHub Repository](https://github.com/liqotech/liqo) — Repositório oficial Apache-2.0 do Liqo; consultado em 2026-10-03.
