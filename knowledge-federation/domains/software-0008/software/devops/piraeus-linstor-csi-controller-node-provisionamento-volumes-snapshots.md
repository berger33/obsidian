---
id: software.devops.tranche18.001735
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-18.md"
fontes: ["https://piraeus.io/docs/stable/explanation/components/", "https://raw.githubusercontent.com/piraeusdatastore/piraeus-operator/v2/README.md", "https://github.com/piraeusdatastore/piraeus-operator"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Piraeus `linstor-csi-controller` e `linstor-csi-node`: tradução de `StorageClass`, `PVC` e `VolumeSnapshot` para LINSTOR

## Em uma frase
Os componentes `linstor-csi-controller` (Deployment) e `linstor-csi-node` (DaemonSet em cada nó) implementam a especificação Container Storage Interface traduzindo objetos `StorageClass`, `PersistentVolumeClaim` e `VolumeSnapshot` do Kubernetes em recursos LINSTOR e montando os dispositivos `/dev/drbdX` nos Pods.

## Por que importa
O Kubernetes não conhece nativamente comandos de `linstor resource-group` ou `drbdadm`; ele conversa exclusivamente via gRPC CSI para criar, expandir, tirar snapshot, anexar (`NodeStageVolume`) e montar (`NodePublishVolume`) volumes.

## Como funciona
Quando um PVC é criado, o `linstor-csi-controller` instrui o `linstor-controller` a alocar as réplicas nos storage pools dos nós segundo os parâmetros da `StorageClass` (`placementCount`, `storagePool`). Quando um Pod consumidor é agendado em um nó, o `kubelet` aciona o `linstor-csi-node` local para promover o dispositivo DRBD e montá-lo no container.

## Exemplo
```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: piraeus-storage-replicated
provisioner: linstor.csi.linbit.com
allowVolumeExpansion: true
volumeBindingMode: WaitForFirstConsumer
parameters:
  linstor.csi.linbit.com/storagePool: lvm-thin
  linstor.csi.linbit.com/placementCount: "2"
```

## Limites e trade-offs
Para que um Pod `linstor-csi-node` consiga montar volumes Piraeus em um nó do cluster, é obrigatório que exista um Pod `linstor-satellite` em execução naquele mesmo nó.

## Como verificar
Crie um PVC usando `provisioner: linstor.csi.linbit.com` e confirme com `kubectl get pvc,pv` a vinculação imediata do volume replicado.

## Conexões
- [[piraeus-linstor-satellite-daemonset-por-no-uts-network-namespaces]] — Veja também: Piraeus `linstor-satellite`: arquitetura de um DaemonSet por nó e isolamento de namespaces Linux (`UTS` e `Network`).
- [[piraeus-linstor-csi-nfs-server-drbd-reactor-readwritemany-rwx]] — Veja também: Piraeus `linstor-csi-nfs-server` e `DRBD Reactor`: suporte a volumes `ReadWriteMany` (`RWX`) altamente disponíveis.

## Fontes
- [Piraeus Operator v2 GitHub — README.md (Managing LINSTOR, DRBD, CSI Driver & High-Availability Controller in Kubernetes)](https://piraeus.io/docs/stable/explanation/components/) — README oficial do piraeusdatastore/piraeus-operator v2 demonstrando deploy server-side e provisionamento declarativo via LinstorCluster; consultado em 2026-10-03.
- [Piraeus Datastore Official Documentation — Understanding Components (Operator, gencert, Controller, Satellite, CSI, NFS Reactor, Affinity & HA Controller)](https://raw.githubusercontent.com/piraeusdatastore/piraeus-operator/v2/README.md) — Documentação oficial de arquitetura dos 9 componentes do Piraeus Datastore, incluindo namespaces UTS/Network dos Satellites, DRBD Reactor RWX e HA failover; consultado em 2026-10-03.
- [Piraeus Operator — Official GitHub Repository](https://github.com/piraeusdatastore/piraeus-operator) — Repositório oficial Apache-2.0 do Piraeus Operator na CNCF; consultado em 2026-10-03.
