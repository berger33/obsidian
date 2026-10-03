---
id: software.devops.tranche18.001739
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
fontes: ["https://raw.githubusercontent.com/piraeusdatastore/piraeus-operator/v2/README.md", "https://piraeus.io/docs/stable/explanation/components/", "https://github.com/piraeusdatastore/piraeus-operator"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Piraeus `LinstorSatelliteConfiguration`: provisionamento declarativo de Storage Pools (`LVM`, `LVMThin`, `ZFS`) nos nós

## Em uma frase
O Custom Resource `LinstorSatelliteConfiguration` (`piraeus.io/v1`) permite declarar quais dispositivos de bloco ou pools dos worker nodes devem ser configurados pelo Piraeus Operator como *Storage Pools* LINSTOR (`lvmPool`, `lvmThinPool`, `zfsPool` ou `fileThinPool`), filtrando nós por `nodeSelector`.

## Por que importa
Em um cluster heterogêneo onde 5 nós possuem discos `/dev/nvme0n1` e outros 5 possuem `/dev/sdb`, configurar manualmente Volume Groups LVM e executar comandos `linstor storage-pool create` em cada servidor quebra a automação GitOps.

## Como funciona
O engenheiro cria objetos `LinstorSatelliteConfiguration` especificando `spec.storagePools` e opcionalmente `spec.nodeSelector` e `spec.properties`. O `piraeus-operator` prepara automaticamente os dispositivos físicos nos nós correspondentes e registra os pools no `linstor-controller`.

## Exemplo
```yaml
apiVersion: piraeus.io/v1
kind: LinstorSatelliteConfiguration
metadata:
  name: nvme-thin-pool-config
spec:
  nodeSelector:
    storage-tier: nvme
  storagePools:
    - name: lvm-thin
      lvmThinPool: {}
      source:
        hostDevices:
          - /dev/nvme1n1
```

## Limites e trade-offs
Para suportar snapshots CSI rápidos e clones eficientes sem consumo imediato de espaço bruto, prefira `lvmThinPool` ou `zfsPool` em vez de `lvmPool` espesso.

## Como verificar
Aplique a `LinstorSatelliteConfiguration` e execute `kubectl exec -n piraeus-datastore deploy/linstor-controller -- linstor storage-pool list` para verificar a criação dos pools.

## Conexões
- [[piraeus-ha-controller-failover-rapido-workloads-stateful-drbd-events]] — Veja também: Piraeus `ha-controller`: aceleração de failover de Pods Stateful monitorando eventos de quórum DRBD.
- [[piraeus-carregamento-modulo-kernel-drbd-module-loader-host-networking]] — Veja também: Piraeus: gerenciamento do módulo de kernel DRBD9 e configuração de rede dedicada de replicação.

## Fontes
- [Piraeus Operator v2 GitHub — README.md (Managing LINSTOR, DRBD, CSI Driver & High-Availability Controller in Kubernetes)](https://raw.githubusercontent.com/piraeusdatastore/piraeus-operator/v2/README.md) — README oficial do piraeusdatastore/piraeus-operator v2 demonstrando deploy server-side e provisionamento declarativo via LinstorCluster; consultado em 2026-10-03.
- [Piraeus Datastore Official Documentation — Understanding Components (Operator, gencert, Controller, Satellite, CSI, NFS Reactor, Affinity & HA Controller)](https://piraeus.io/docs/stable/explanation/components/) — Documentação oficial de arquitetura dos 9 componentes do Piraeus Datastore, incluindo namespaces UTS/Network dos Satellites, DRBD Reactor RWX e HA failover; consultado em 2026-10-03.
- [Piraeus Operator — Official GitHub Repository](https://github.com/piraeusdatastore/piraeus-operator) — Repositório oficial Apache-2.0 do Piraeus Operator na CNCF; consultado em 2026-10-03.
