---
id: software.devops.tranche18.001708
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
fontes: ["https://raw.githubusercontent.com/openebs/openebs/HEAD/README.md", "https://openebs.io/docs/concepts/architecture", "https://github.com/openebs/openebs"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# OpenEBS: matriz de decisão arquitetural entre Local Storage (`LocalPV`) e Replicated Storage (`Mayastor`)

## Em uma frase
A documentação oficial do OpenEBS estabelece uma matriz de engenharia clara entre **Local Storage** (`Hostpath`, `LVM`, `ZFS`) e **Replicated Storage** (`Mayastor`) com base na capacidade da aplicação gerenciar ou não sua própria replicação e alta disponibilidade.

## Por que importa
Usar armazenamento replicado por rede (3 cópias no storage) embaixo de um banco de dados que já faz 3 cópias via Raft/Paxos multiplica o consumo de escrita por 9x (*write amplification* 3x3) e adiciona latência de rede desnecessária.

## Como funciona
A regra canônica do OpenEBS é: 1) escolha **Local Storage** quando a aplicação distribui e replica dados por conta própria (MongoDB ReplicaSet, Cassandra, Kafka, Elasticsearch, TiKV), obtendo latência próxima ao disco físico sem overhead de rede; 2) escolha **Replicated Storage (Mayastor)** para cargas stateful que exigem replicação e failover na camada de bloco (PostgreSQL/MySQL standalone, Percona, GitLab, Prometheus single-instance), permitindo que o Pod seja reagendado em outro nó caso o host falhe.

## Exemplo
```bash
# Listando StorageClasses locais e replicadas instaladas pelo OpenEBS:
kubectl get storageclasses | grep openebs
```

## Limites e trade-offs
Em volumes **Local Storage**, o `PersistentVolume` fica fisicamente preso ao nó onde foi provisionado: se aquele nó desligar permanentemente, o Pod vinculado àquele PVC específico não poderá montar aquele mesmo volume em outro nó.

## Como verificar
Revise os `StatefulSets` do cluster e associe `openebs-lvmpv`/`openebs-zfspv` aos clusters distribuídos e `openebs-mayastor` aos serviços single-replica.

## Conexões
- [[openebs-localpv-rawfile-loopback-extent-files-desenvolvimento]] — Veja também: OpenEBS `Local PV Rawfile`: armazenamento em bloco e arquivo baseado em sparse files locais.
- [[openebs-snapshots-clones-csi-volumesnapshot-copy-on-write]] — Veja também: OpenEBS: snapshots e clones instantâneos via CSI `VolumeSnapshot` em LVM, ZFS e Mayastor.

## Fontes
- [OpenEBS GitHub — README.md (Cloud Native Storage, Local Storage vs Replicated Storage Matrix & Sub-Projects)](https://raw.githubusercontent.com/openebs/openebs/HEAD/README.md) — README oficial do openebs/openebs (CNCF Sandbox) comparando Local Storage e Replicated Storage e detalhando Hostpath, ZFS, LVM, Rawfile e Mayastor; consultado em 2026-10-03.
- [OpenEBS Official Documentation — Architecture v4.6.x (Data Engines, Volume Access/Services/Data/Storage Layers & Control Plane)](https://openebs.io/docs/concepts/architecture) — Documentação oficial de arquitetura do OpenEBS explicando as 4 camadas dos Data Engines, Target/Nexus por volume e estados de Volume Replicas; consultado em 2026-10-03.
- [OpenEBS — Official GitHub Repository](https://github.com/openebs/openebs) — Repositório oficial Apache-2.0 do projeto OpenEBS na CNCF; consultado em 2026-10-03.
