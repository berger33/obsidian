---
id: software.devops.tranche18.001737
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

# Piraeus `linstor-affinity-controller`: sincronização dinâmica de `nodeAffinity` de `PersistentVolumes` imutáveis

## Em uma frase
O `linstor-affinity-controller` observa os objetos `PersistentVolume` criados pelo LINSTOR CSI e sincroniza automaticamente suas regras de `nodeAffinity` quando as réplicas do volume são movidas ou reconfiguradas no LINSTOR.

## Por que importa
Quando uma `StorageClass` desabilita o acesso remoto via rede (`allowRemoteVolumeAccess: "false"` para exigir que o Pod rode apenas onde há disco local da réplica), o PV nasce com `nodeAffinity` apontando para os nós A e B. Se mais tarde o operador migrar a réplica do nó B para o nó C no LINSTOR, o campo `nodeAffinity` do PV no Kubernetes é imutável por padrão e impediria o agendamento no nó C.

## Como funciona
Ao detectar a mudança de localização das réplicas no LINSTOR, o `linstor-affinity-controller` remove forçosamente o objeto `PersistentVolume` antigo na API do Kubernetes (com proteção para que o volume físico no LINSTOR nunca seja deletado) e o recria imediatamente com o novo `nodeAffinity` atualizado.

## Exemplo
```bash
kubectl get pods -n piraeus-datastore -l app.kubernetes.io/component=linstor-affinity-controller
kubectl logs -n piraeus-datastore -l app.kubernetes.io/component=linstor-affinity-controller --tail=20
```

## Limites e trade-offs
Na configuração padrão (`allowRemoteVolumeAccess: "true"`), um Pod agendado em um nó sem réplica local ainda consegue acessar o volume via cliente DRBD *diskless* pela rede; a restrição de `nodeAffinity` afeta principalmente volumes com `allowRemoteVolumeAccess` restrito.

## Como verificar
Inspecione `spec.nodeAffinity` de um `PersistentVolume` com acesso local estrito antes e depois de adicionar/mover uma réplica no LINSTOR.

## Conexões
- [[piraeus-linstor-csi-nfs-server-drbd-reactor-readwritemany-rwx]] — Veja também: Piraeus `linstor-csi-nfs-server` e `DRBD Reactor`: suporte a volumes `ReadWriteMany` (`RWX`) altamente disponíveis.
- [[piraeus-ha-controller-failover-rapido-workloads-stateful-drbd-events]] — Veja também: Piraeus `ha-controller`: aceleração de failover de Pods Stateful monitorando eventos de quórum DRBD.

## Fontes
- [Piraeus Operator v2 GitHub — README.md (Managing LINSTOR, DRBD, CSI Driver & High-Availability Controller in Kubernetes)](https://piraeus.io/docs/stable/explanation/components/) — README oficial do piraeusdatastore/piraeus-operator v2 demonstrando deploy server-side e provisionamento declarativo via LinstorCluster; consultado em 2026-10-03.
- [Piraeus Datastore Official Documentation — Understanding Components (Operator, gencert, Controller, Satellite, CSI, NFS Reactor, Affinity & HA Controller)](https://raw.githubusercontent.com/piraeusdatastore/piraeus-operator/v2/README.md) — Documentação oficial de arquitetura dos 9 componentes do Piraeus Datastore, incluindo namespaces UTS/Network dos Satellites, DRBD Reactor RWX e HA failover; consultado em 2026-10-03.
- [Piraeus Operator — Official GitHub Repository](https://github.com/piraeusdatastore/piraeus-operator) — Repositório oficial Apache-2.0 do Piraeus Operator na CNCF; consultado em 2026-10-03.
