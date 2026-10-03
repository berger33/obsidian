---
id: software.devops.tranche18.001706
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

# OpenEBS `Local PV ZFS`: provisionamento CSI de datasets e ZVOLs sobre pools ZFS com compressão e RAID-Z

## Em uma frase
O **Local PV ZFS** (`openebs/zfs-localpv`) é um driver CSI estável do OpenEBS que provisiona dinamicamente *datasets* ZFS (para `volumeMode: Filesystem`) ou *ZVOLs* (para `volumeMode: Block` ou sistemas de arquivos `ext4`/`xfs`) sobre *zpools* existentes nos nós Kubernetes.

## Por que importa
O sistema de arquivos ZFS oferece verificação de integridade *copy-on-write* contra corrupção silenciosa (*bit rot*), compressão transparente (`lz4`/`zstd`), cache ARC em RAM, proteção RAID-Z no host e snapshots/clones instantâneos sem custo de cópia.

## Como funciona
Na `StorageClass` (`provisioner: zfs.csi.openebs.io`), o administrador declara o nome do pool ZFS (`poolname`), propriedades nativas ZFS (`compression: "lz4"`, `dedup: "off"`, `recordsize: "128k"`, `thinprovision: "yes"`) e `fstype: "zfs"`. O controlador e o DaemonSet CSI criam o recurso `ZFSVolume` e aplicam exatamente essas propriedades no `zpool` do nó selecionado.

## Exemplo
```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: openebs-zfspv
provisioner: zfs.csi.openebs.io
allowVolumeExpansion: true
volumeBindingMode: WaitForFirstConsumer
parameters:
  poolname: "zfspv-pool"
  fstype: "zfs"
  compression: "lz4"
  thinprovision: "yes"
```

## Limites e trade-offs
Para usar o `Local PV ZFS`, os módulos de kernel do OpenZFS (`zfs.ko`) e o utilitário `zfs` devem estar instalados nos worker nodes e o `zpool` especificado em `poolname` deve estar criado antes do provisionamento.

## Como verificar
Execute `kubectl get zfsvolumes -n openebs` e no nó host `zfs list` para confirmar a criação do dataset ZFS com compressão `lz4`.

## Conexões
- [[openebs-localpv-lvm-csi-snapshots-thin-provisioning-resize]] — Veja também: OpenEBS `Local PV LVM`: provisionamento CSI de volumes lógicos LVM2 com snapshots, clones e expansão online.
- [[openebs-localpv-rawfile-loopback-extent-files-desenvolvimento]] — Veja também: OpenEBS `Local PV Rawfile`: armazenamento em bloco e arquivo baseado em sparse files locais.

## Fontes
- [OpenEBS GitHub — README.md (Cloud Native Storage, Local Storage vs Replicated Storage Matrix & Sub-Projects)](https://raw.githubusercontent.com/openebs/openebs/HEAD/README.md) — README oficial do openebs/openebs (CNCF Sandbox) comparando Local Storage e Replicated Storage e detalhando Hostpath, ZFS, LVM, Rawfile e Mayastor; consultado em 2026-10-03.
- [OpenEBS Official Documentation — Architecture v4.6.x (Data Engines, Volume Access/Services/Data/Storage Layers & Control Plane)](https://openebs.io/docs/concepts/architecture) — Documentação oficial de arquitetura do OpenEBS explicando as 4 camadas dos Data Engines, Target/Nexus por volume e estados de Volume Replicas; consultado em 2026-10-03.
- [OpenEBS — Official GitHub Repository](https://github.com/openebs/openebs) — Repositório oficial Apache-2.0 do projeto OpenEBS na CNCF; consultado em 2026-10-03.
