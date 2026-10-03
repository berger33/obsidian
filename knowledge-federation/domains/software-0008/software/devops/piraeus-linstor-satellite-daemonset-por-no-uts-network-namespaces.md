---
id: software.devops.tranche18.001734
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

# Piraeus `linstor-satellite`: arquitetura de um DaemonSet por nó e isolamento de namespaces Linux (`UTS` e `Network`)

## Em uma frase
O `linstor-satellite` roda em cada nó de armazenamento como um agente local stateless que recebe instruções do `linstor-controller` para configurar volumes lógicos (LVM/ZFS) e dispositivos DRBD no sistema operacional host.

## Por que importa
Diferentes worker nodes de um cluster frequentemente possuem discos diferentes ou exigem configurações personalizadas (como carregar imagens de cabeçalhos de kernel específicos para compilar o módulo DRBD), o que seria inflexível com um único DaemonSet global rígido.

## Como funciona
Por isso, o Piraeus Operator implanta **um DaemonSet dedicado por nó** para o `linstor-satellite` (permitindo customização por nó via `LinstorSatelliteConfiguration`). Além disso, o satélite gerencia dois detalhes críticos de namespaces Linux: 1) é iniciado em um **UTS namespace separado** para garantir que as ferramentas `drbdadm` vejam sempre o nome do nó Kubernetes como hostname; e 2) os dispositivos DRBD herdam o **network namespace** do Pod satélite.

## Exemplo
```bash
kubectl exec -n piraeus-datastore ds/linstor-satellite.<node-name> -- drbdadm status
```

## Limites e trade-offs
Como os dispositivos DRBD herdam o network namespace do Pod `linstor-satellite` por padrão, se os satélites não estiverem configurados para usar *host networking*, a replicação DRBD requer que o Pod satélite esteja em execução; usar host networking evita essa dependência durante reinícios do Pod.

## Como verificar
Acesse um Pod satélite com `kubectl exec` e execute `drbdadm status` para verificar que o comando funciona transparentemente dentro do UTS namespace configurado.

## Conexões
- [[piraeus-linstor-controller-estado-crds-kubernetes-orquestracao]] — Veja também: Piraeus `linstor-controller`: gerenciamento central de posicionamento de volumes persistido em objetos Kubernetes.
- [[piraeus-linstor-csi-controller-node-provisionamento-volumes-snapshots]] — Veja também: Piraeus `linstor-csi-controller` e `linstor-csi-node`: tradução de `StorageClass`, `PVC` e `VolumeSnapshot` para LINSTOR.

## Fontes
- [Piraeus Operator v2 GitHub — README.md (Managing LINSTOR, DRBD, CSI Driver & High-Availability Controller in Kubernetes)](https://piraeus.io/docs/stable/explanation/components/) — README oficial do piraeusdatastore/piraeus-operator v2 demonstrando deploy server-side e provisionamento declarativo via LinstorCluster; consultado em 2026-10-03.
- [Piraeus Datastore Official Documentation — Understanding Components (Operator, gencert, Controller, Satellite, CSI, NFS Reactor, Affinity & HA Controller)](https://raw.githubusercontent.com/piraeusdatastore/piraeus-operator/v2/README.md) — Documentação oficial de arquitetura dos 9 componentes do Piraeus Datastore, incluindo namespaces UTS/Network dos Satellites, DRBD Reactor RWX e HA failover; consultado em 2026-10-03.
- [Piraeus Operator — Official GitHub Repository](https://github.com/piraeusdatastore/piraeus-operator) — Repositório oficial Apache-2.0 do Piraeus Operator na CNCF; consultado em 2026-10-03.
