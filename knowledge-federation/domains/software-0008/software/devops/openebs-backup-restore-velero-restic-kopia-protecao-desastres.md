---
id: software.devops.tranche18.001710
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

# OpenEBS: backup externo e recuperação de desastres de volumes locais e replicados com Velero

## Em uma frase
Tanto os motores de **Local Storage** quanto os de **Replicated Storage** do OpenEBS integram-se com o **Velero** (utilizando plugins CSI de snapshot ou backup em nível de sistema de arquivos como Restic/Kopia) para enviar cópias de segurança para Object Storage externo (S3/MinIO/GCS).

## Por que importa
Mesmo a replicação síncrona em 3 nós (`Mayastor`) ou o RAID-Z local (`Local PV ZFS`) não protegem contra exclusão acidental de tabelas por erro humano, ransomware ou perda total da sala de servidores: backups off-cluster são indispensáveis.

## Como funciona
Para volumes locais (`Hostpath`, `LVM`, `ZFS`) e replicados, o Velero faz snapshot dos manifestos Kubernetes e envia os blocos/arquivos do volume montado para um `BackupStorageLocation` em S3, permitindo restaurar a aplicação inteira (inclusive migrando de um motor local para outro cluster em nuvem) com `velero restore create`.

## Exemplo
```bash
velero backup create prod-stateful-backup \
  --include-namespaces prod-db \
  --default-volumes-to-fs-backup \
  --wait
velero backup describe prod-stateful-backup --details
```

## Limites e trade-offs
Para garantir consistência transacional ao fazer backup de bancos de dados via sistema de arquivos, configure *backup hooks* (`pre.hook.backup.velero.io/command`) no Pod para executar `fsfreeze` ou `CHECKPOINT`/`FLUSH TABLES WITH READ LOCK` durante o snapshot.

## Como verificar
Execute `velero backup get` e teste a restauração do PVC em um namespace isolado de teste para validar o RPO/RTO.

## Conexões
- [[openebs-snapshots-clones-csi-volumesnapshot-copy-on-write]] — Veja também: OpenEBS: snapshots e clones instantâneos via CSI `VolumeSnapshot` em LVM, ZFS e Mayastor.

## Fontes
- [OpenEBS GitHub — README.md (Cloud Native Storage, Local Storage vs Replicated Storage Matrix & Sub-Projects)](https://raw.githubusercontent.com/openebs/openebs/HEAD/README.md) — README oficial do openebs/openebs (CNCF Sandbox) comparando Local Storage e Replicated Storage e detalhando Hostpath, ZFS, LVM, Rawfile e Mayastor; consultado em 2026-10-03.
- [OpenEBS Official Documentation — Architecture v4.6.x (Data Engines, Volume Access/Services/Data/Storage Layers & Control Plane)](https://openebs.io/docs/concepts/architecture) — Documentação oficial de arquitetura do OpenEBS explicando as 4 camadas dos Data Engines, Target/Nexus por volume e estados de Volume Replicas; consultado em 2026-10-03.
- [OpenEBS — Official GitHub Repository](https://github.com/openebs/openebs) — Repositório oficial Apache-2.0 do projeto OpenEBS na CNCF; consultado em 2026-10-03.
