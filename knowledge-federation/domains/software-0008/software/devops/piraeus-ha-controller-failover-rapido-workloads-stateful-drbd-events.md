---
id: software.devops.tranche18.001738
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

# Piraeus `ha-controller`: aceleração de failover de Pods Stateful monitorando eventos de quórum DRBD

## Em uma frase
O **Piraeus High Availability Controller** (`ha-controller`), implantado como DaemonSet em todos os nós do cluster, escuta eventos do DRBD em tempo real para detectar falhas de armazenamento ou isolamento de nó e evictar rapidamente os Pods afetados para que subam em um nó saudável.

## Por que importa
No comportamento padrão do Kubernetes, quando um worker node trava ou perde rede, um Pod de `StatefulSet` com volume `ReadWriteOnce` pode levar de **6 a 15 minutos** para sofrer failover (aguardando `node-monitor-grace-period`, `pod-eviction-timeout` e o timeout de `VolumeAttachment` CSI).

## Como funciona
Ao escutar diretamente o barramento de eventos e quórum do DRBD9, o `ha-controller` identifica em segundos que um nó perdeu acesso ao armazenamento ou ficou isolado da maioria das réplicas, aplicando taints/deleções seguras nos Pods e liberando os `VolumeAttachments` para reduzir o tempo de failover de minutos para poucos segundos.

## Exemplo
```bash
kubectl get pods -n piraeus-datastore -l app.kubernetes.io/component=ha-controller -o wide
kubectl logs -n piraeus-datastore -l app.kubernetes.io/component=ha-controller --tail=30
```

## Limites e trade-offs
Para que a detecção de isolamento e prevenção de *split-brain* do `ha-controller` e do DRBD9 opere com segurança máxima, configure volumes críticos com quórum DRBD (tipicamente 3 réplicas ou 2 réplicas + 1 tiebreaker diskless).

## Como verificar
Simule a falha de um nó que hospeda um Pod Stateful com volume Piraeus e meça o tempo até o Pod entrar em `Running` no nó substituto com o `ha-controller` ativo.

## Conexões
- [[piraeus-linstor-affinity-controller-sincronizacao-nodeaffinity-pv]] — Veja também: Piraeus `linstor-affinity-controller`: sincronização dinâmica de `nodeAffinity` de `PersistentVolumes` imutáveis.
- [[piraeus-linstorsatelliteconfiguration-storage-pools-lvm-thin-zfs]] — Veja também: Piraeus `LinstorSatelliteConfiguration`: provisionamento declarativo de Storage Pools (`LVM`, `LVMThin`, `ZFS`) nos nós.

## Fontes
- [Piraeus Operator v2 GitHub — README.md (Managing LINSTOR, DRBD, CSI Driver & High-Availability Controller in Kubernetes)](https://piraeus.io/docs/stable/explanation/components/) — README oficial do piraeusdatastore/piraeus-operator v2 demonstrando deploy server-side e provisionamento declarativo via LinstorCluster; consultado em 2026-10-03.
- [Piraeus Datastore Official Documentation — Understanding Components (Operator, gencert, Controller, Satellite, CSI, NFS Reactor, Affinity & HA Controller)](https://raw.githubusercontent.com/piraeusdatastore/piraeus-operator/v2/README.md) — Documentação oficial de arquitetura dos 9 componentes do Piraeus Datastore, incluindo namespaces UTS/Network dos Satellites, DRBD Reactor RWX e HA failover; consultado em 2026-10-03.
- [Piraeus Operator — Official GitHub Repository](https://github.com/piraeusdatastore/piraeus-operator) — Repositório oficial Apache-2.0 do Piraeus Operator na CNCF; consultado em 2026-10-03.
