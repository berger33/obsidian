---
id: software.devops.tranche18.001705
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

# OpenEBS `Local PV LVM`: provisionamento CSI de volumes lógicos LVM2 com snapshots, clones e expansão online

## Em uma frase
O **Local PV LVM** (`openebs/lvm-localpv`) é um driver CSI estável para produção que provisiona dinamicamente volumes lógicos **LVM2** (*Logical Volume Manager*) a partir de *Volume Groups* (VGs) pré-configurados nos nós Kubernetes.

## Por que importa
Em cargas stateful de alta performance que já possuem replicação própria (como clusters PostgreSQL Patroni, TiKV ou Kafka), usar um volume LVM local oferece desempenho quase idêntico ao disco físico com suporte a *thin provisioning*, redimensionamento online, snapshots e proteção RAID do LVM2.

## Como funciona
O agente CSI em cada nó monitora os Volume Groups LVM disponíveis (expondo topologia via CRD `LVMNode`). Quando um PVC solicita armazenamento na `StorageClass` `openebs-lvmpv`, o driver cria um Logical Volume (`lvcreate`) no nó onde o Pod foi agendado, formata-o com `ext4`/`xfs` (ou entrega como bloco bruto) e monta no container.

## Exemplo
```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: openebs-lvmpv
provisioner: local.csi.openebs.io
allowVolumeExpansion: true
volumeBindingMode: WaitForFirstConsumer
parameters:
  storage: "lvm"
  volgroup: "lvmvg"
  thinProvision: "yes"
```

## Limites e trade-offs
Para que os snapshots CSI (`VolumeSnapshot`) funcionem no `Local PV LVM`, o volume precisa ser criado com `thinProvision: "yes"` sobre um * thin pool* LVM2.

## Como verificar
Execute `kubectl get lvmnodes -n openebs` e `kubectl get lvmvolumes -n openebs` para inspecionar os Volume Groups e volumes lógicos provisionados nos nós.

## Conexões
- [[openebs-localpv-hostpath-provisionamento-dinamico-zero-config]] — Veja também: OpenEBS `Local PV Hostpath`: substituto dinâmico zero-configuração para volumes `hostPath` nativos.
- [[openebs-localpv-zfs-datasets-zvols-compressao-raidz-snapshots]] — Veja também: OpenEBS `Local PV ZFS`: provisionamento CSI de datasets e ZVOLs sobre pools ZFS com compressão e RAID-Z.

## Fontes
- [OpenEBS GitHub — README.md (Cloud Native Storage, Local Storage vs Replicated Storage Matrix & Sub-Projects)](https://raw.githubusercontent.com/openebs/openebs/HEAD/README.md) — README oficial do openebs/openebs (CNCF Sandbox) comparando Local Storage e Replicated Storage e detalhando Hostpath, ZFS, LVM, Rawfile e Mayastor; consultado em 2026-10-03.
- [OpenEBS Official Documentation — Architecture v4.6.x (Data Engines, Volume Access/Services/Data/Storage Layers & Control Plane)](https://openebs.io/docs/concepts/architecture) — Documentação oficial de arquitetura do OpenEBS explicando as 4 camadas dos Data Engines, Target/Nexus por volume e estados de Volume Replicas; consultado em 2026-10-03.
- [OpenEBS — Official GitHub Repository](https://github.com/openebs/openebs) — Repositório oficial Apache-2.0 do projeto OpenEBS na CNCF; consultado em 2026-10-03.
