---
id: software.devops.tranche18.001736
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

# Piraeus `linstor-csi-nfs-server` e `DRBD Reactor`: suporte a volumes `ReadWriteMany` (`RWX`) altamente disponíveis

## Em uma frase
O componente `linstor-csi-nfs-server` (implantado como DaemonSet em cada nó do cluster) exporta volumes LINSTOR via NFS gerenciados pelo **DRBD Reactor**, habilitando o modo de acesso `ReadWriteMany` (`RWX`) com failover automático entre nós.

## Por que importa
Um dispositivo de bloco replicado por DRBD é nativamente `ReadWriteOnce` (montado em um único nó por vez para não corromper sistemas de arquivos locais como `ext4`/`xfs`); porém muitas aplicações web e pipelines exigem que vários Pods em nós diferentes montem o mesmo volume simultaneamente (`RWX`).

## Como funciona
Quando um PVC solicita `accessModes: [ReadWriteMany]`, o Piraeus cria um volume replicado DRBD entre os nós e o `linstor-csi-nfs-server` utiliza o **DRBD Reactor** para iniciar um servidor NFS exatamente no nó que detém a réplica primária do volume. Se esse nó falhar, o DRBD Reactor promove automaticamente outra réplica em outro nó e sobe o export NFS mantendo a disponibilidade do volume RWX.

## Exemplo
```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: shared-assets-rwx
spec:
  storageClassName: piraeus-storage-replicated
  accessModes:
    - ReadWriteMany
  resources:
    requests:
      storage: 10Gi
```

## Limites e trade-offs
Os exports NFS gerenciados pelo `linstor-csi-nfs-server` podem rodar e sofrer failover em qualquer nó do cluster que possua uma réplica local com disco daquele volume LINSTOR.

## Como verificar
Verifique os Pods `linstor-csi-nfs-server` no namespace `piraeus-datastore` e teste a montagem concorrente de um PVC `ReadWriteMany` em dois Pods agendados em nós diferentes.

## Conexões
- [[piraeus-linstor-csi-controller-node-provisionamento-volumes-snapshots]] — Veja também: Piraeus `linstor-csi-controller` e `linstor-csi-node`: tradução de `StorageClass`, `PVC` e `VolumeSnapshot` para LINSTOR.
- [[piraeus-linstor-affinity-controller-sincronizacao-nodeaffinity-pv]] — Veja também: Piraeus `linstor-affinity-controller`: sincronização dinâmica de `nodeAffinity` de `PersistentVolumes` imutáveis.

## Fontes
- [Piraeus Operator v2 GitHub — README.md (Managing LINSTOR, DRBD, CSI Driver & High-Availability Controller in Kubernetes)](https://piraeus.io/docs/stable/explanation/components/) — README oficial do piraeusdatastore/piraeus-operator v2 demonstrando deploy server-side e provisionamento declarativo via LinstorCluster; consultado em 2026-10-03.
- [Piraeus Datastore Official Documentation — Understanding Components (Operator, gencert, Controller, Satellite, CSI, NFS Reactor, Affinity & HA Controller)](https://raw.githubusercontent.com/piraeusdatastore/piraeus-operator/v2/README.md) — Documentação oficial de arquitetura dos 9 componentes do Piraeus Datastore, incluindo namespaces UTS/Network dos Satellites, DRBD Reactor RWX e HA failover; consultado em 2026-10-03.
- [Piraeus Operator — Official GitHub Repository](https://github.com/piraeusdatastore/piraeus-operator) — Repositório oficial Apache-2.0 do Piraeus Operator na CNCF; consultado em 2026-10-03.
