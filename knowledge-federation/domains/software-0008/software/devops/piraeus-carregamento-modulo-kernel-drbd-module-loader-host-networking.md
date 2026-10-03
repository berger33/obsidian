---
id: software.devops.tranche18.001740
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

# Piraeus: gerenciamento do módulo de kernel DRBD9 e configuração de rede dedicada de replicação

## Em uma frase
O Piraeus Operator gerencia automaticamente a inserção ou compilação sob demanda do módulo de kernel **DRBD9** nos worker nodes e permite configurar o uso de *host networking* ou interfaces de rede de alta velocidade dedicadas para o tráfego de replicação dos `linstor-satellites`.

## Por que importa
Distros Linux padrão geralmente vêm com o módulo antigo DRBD 8.4 no kernel (que suporta apenas 2 nós e não possui quórum automático nem malha multi-réplica do DRBD 9), exigindo carregar o módulo DRBD 9 compatível com o kernel exato do host.

## Como funciona
Através de `LinstorSatelliteConfiguration`, o Piraeus Operator configura o container de inicialização de carregamento do módulo DRBD9 e permite ajustar `podTemplate` (por exemplo ativando `hostNetwork: true` para que os dispositivos DRBD não dependam do network namespace efêmero do Pod satélite durante atualizações do operador).

## Exemplo
```yaml
apiVersion: piraeus.io/v1
kind: LinstorSatelliteConfiguration
metadata:
  name: satellite-host-network
spec:
  podTemplate:
    spec:
      hostNetwork: true
      dnsPolicy: ClusterFirstWithHostNet
```

## Limites e trade-offs
Sempre que `hostNetwork: true` é habilitado no `podTemplate` de um `LinstorSatelliteConfiguration`, defina também `dnsPolicy: ClusterFirstWithHostNet` para que o satélite continue resolvendo nomes de serviços internos do Kubernetes.

## Como verificar
Verifique nos worker nodes com `cat /proc/drbd` ou `kubectl exec -n piraeus-datastore ds/linstor-satellite.<node> -- drbdadm --version` que o módulo DRBD 9.x está carregado no kernel.

## Conexões
- [[piraeus-linstorsatelliteconfiguration-storage-pools-lvm-thin-zfs]] — Veja também: Piraeus `LinstorSatelliteConfiguration`: provisionamento declarativo de Storage Pools (`LVM`, `LVMThin`, `ZFS`) nos nós.

## Fontes
- [Piraeus Operator v2 GitHub — README.md (Managing LINSTOR, DRBD, CSI Driver & High-Availability Controller in Kubernetes)](https://piraeus.io/docs/stable/explanation/components/) — README oficial do piraeusdatastore/piraeus-operator v2 demonstrando deploy server-side e provisionamento declarativo via LinstorCluster; consultado em 2026-10-03.
- [Piraeus Datastore Official Documentation — Understanding Components (Operator, gencert, Controller, Satellite, CSI, NFS Reactor, Affinity & HA Controller)](https://raw.githubusercontent.com/piraeusdatastore/piraeus-operator/v2/README.md) — Documentação oficial de arquitetura dos 9 componentes do Piraeus Datastore, incluindo namespaces UTS/Network dos Satellites, DRBD Reactor RWX e HA failover; consultado em 2026-10-03.
- [Piraeus Operator — Official GitHub Repository](https://github.com/piraeusdatastore/piraeus-operator) — Repositório oficial Apache-2.0 do Piraeus Operator na CNCF; consultado em 2026-10-03.
