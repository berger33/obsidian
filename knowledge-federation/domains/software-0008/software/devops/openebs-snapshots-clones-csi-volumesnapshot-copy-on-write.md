---
id: software.devops.tranche18.001709
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

# OpenEBS: snapshots e clones instantâneos via CSI `VolumeSnapshot` em LVM, ZFS e Mayastor

## Em uma frase
Os motores CSI do OpenEBS (`Local PV ZFS`, `Local PV LVM` com thin provisioning e `Mayastor`) implementam a API padrão `snapshot.storage.k8s.io/v1` do Kubernetes para criar snapshots pontuais (*point-in-time*) e clones graváveis de `PersistentVolumeClaims`.

## Por que importa
Antes de executar uma migração de schema de banco de dados em produção ou para levantar um ambiente efêmero de homologação com dados reais em segundos, é essencial capturar um snapshot instantâneo e criar um PVC clone sem copiar centenas de gigabytes pela rede.

## Como funciona
O operador define uma `VolumeSnapshotClass` apontando para o driver CSI correspondente (`zfs.csi.openebs.io`, `local.csi.openebs.io` ou `io.openebs.csi-mayastor`) e aplica um recurso `VolumeSnapshot` referenciando o PVC de origem. Para criar um clone, basta criar um novo PVC definindo `spec.dataSource` apontando para o `VolumeSnapshot` criado.

## Exemplo
```yaml
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshot
metadata:
  name: db-pre-migration-snap
spec:
  volumeSnapshotClassName: openebs-zfspv-snapclass
  source:
    persistentVolumeClaimName: db-data-pvc
```

## Limites e trade-offs
No `Local PV ZFS` e no `Local PV LVM`, um PVC clonado a partir de um `VolumeSnapshot` reside obrigatoriamente no mesmo worker node do snapshot original devido à natureza local do pool.

## Como verificar
Execute `kubectl get volumesnapshot` e confirme que `READYTOUSE` atingiu `true` antes de provisionar o PVC clone.

## Conexões
- [[openebs-criterios-escolha-local-storage-vs-replicated-storage]] — Veja também: OpenEBS: matriz de decisão arquitetural entre Local Storage (`LocalPV`) e Replicated Storage (`Mayastor`).
- [[openebs-backup-restore-velero-restic-kopia-protecao-desastres]] — Veja também: OpenEBS: backup externo e recuperação de desastres de volumes locais e replicados com Velero.

## Fontes
- [OpenEBS GitHub — README.md (Cloud Native Storage, Local Storage vs Replicated Storage Matrix & Sub-Projects)](https://raw.githubusercontent.com/openebs/openebs/HEAD/README.md) — README oficial do openebs/openebs (CNCF Sandbox) comparando Local Storage e Replicated Storage e detalhando Hostpath, ZFS, LVM, Rawfile e Mayastor; consultado em 2026-10-03.
- [OpenEBS Official Documentation — Architecture v4.6.x (Data Engines, Volume Access/Services/Data/Storage Layers & Control Plane)](https://openebs.io/docs/concepts/architecture) — Documentação oficial de arquitetura do OpenEBS explicando as 4 camadas dos Data Engines, Target/Nexus por volume e estados de Volume Replicas; consultado em 2026-10-03.
- [OpenEBS — Official GitHub Repository](https://github.com/openebs/openebs) — Repositório oficial Apache-2.0 do projeto OpenEBS na CNCF; consultado em 2026-10-03.
