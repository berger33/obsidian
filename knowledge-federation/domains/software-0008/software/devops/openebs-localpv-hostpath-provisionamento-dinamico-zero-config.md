---
id: software.devops.tranche18.001704
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

# OpenEBS `Local PV Hostpath`: substituto dinâmico zero-configuração para volumes `hostPath` nativos

## Em uma frase
O **Local PV Hostpath** (`openebs/dynamic-localpv-provisioner`) é o provisionador single-node estável do OpenEBS que cria diretórios locais sob demanda nos worker nodes como `PersistentVolumes` sem exigir configuração prévia de discos adicionais nem driver CSI complexo.

## Por que importa
O volume `hostPath` embutido do Kubernetes não possui provisionamento dinâmico via `StorageClass` e exige privilégios administrativos no Pod, enquanto o `local` PV estático requer pré-criar manualmente cada ponto de montagem antes do agendamento.

## Como funciona
Com a `StorageClass` `openebs-hostpath` (configurada com `volumeBindingMode: WaitForFirstConsumer`), o provisionador aguarda o scheduler escolher o nó do Pod, cria automaticamente um subdiretório isolado dentro do caminho base do nó (por padrão `/var/openebs/local`) e vincula o `PersistentVolume` com afinidade de nó (`nodeAffinity`) fixa para aquele host.

## Exemplo
```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: mongo-local-pvc
spec:
  storageClassName: openebs-hostpath
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 20Gi
```

## Limites e trade-offs
Como o `Local PV Hostpath` compartilha o sistema de arquivos subjacente do host, ele não impõe cota rígida de capacidade por diretório nem oferece snapshots nativos; para cotas rígidas e snapshots locais, utilize `Local PV LVM` ou `Local PV ZFS`.

## Como verificar
Aplique o PVC e um Pod consumidor e execute `kubectl get pv -o wide` para confirmar o provisionamento dinâmico e a regra de `nodeAffinity`.

## Conexões
- [[openebs-mayastor-replicated-storage-nvme-of-spdk-alta-performance]] — Veja também: OpenEBS `Mayastor`: motor de armazenamento replicado corporativo baseado em NVMe-oF e SPDK.
- [[openebs-localpv-lvm-csi-snapshots-thin-provisioning-resize]] — Veja também: OpenEBS `Local PV LVM`: provisionamento CSI de volumes lógicos LVM2 com snapshots, clones e expansão online.

## Fontes
- [OpenEBS GitHub — README.md (Cloud Native Storage, Local Storage vs Replicated Storage Matrix & Sub-Projects)](https://raw.githubusercontent.com/openebs/openebs/HEAD/README.md) — README oficial do openebs/openebs (CNCF Sandbox) comparando Local Storage e Replicated Storage e detalhando Hostpath, ZFS, LVM, Rawfile e Mayastor; consultado em 2026-10-03.
- [OpenEBS Official Documentation — Architecture v4.6.x (Data Engines, Volume Access/Services/Data/Storage Layers & Control Plane)](https://openebs.io/docs/concepts/architecture) — Documentação oficial de arquitetura do OpenEBS explicando as 4 camadas dos Data Engines, Target/Nexus por volume e estados de Volume Replicas; consultado em 2026-10-03.
- [OpenEBS — Official GitHub Repository](https://github.com/openebs/openebs) — Repositório oficial Apache-2.0 do projeto OpenEBS na CNCF; consultado em 2026-10-03.
