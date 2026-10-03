---
id: software.devops.tranche18.001703
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

# OpenEBS `Mayastor`: motor de armazenamento replicado corporativo baseado em NVMe-oF e SPDK

## Em uma frase
O **Mayastor** é o motor de armazenamento replicado multi-nó de classe corporativa do OpenEBS, projetado do zero sobre semântica **NVMe-oF** (*NVMe over Fabrics* / RDMA / TCP) para entregar baixa latência, snapshots, clones e alta disponibilidade em SSDs NVMe modernos.

## Por que importa
Motores de armazenamento em espaço de kernel ou baseados em iSCSI legado introduzem trocas de contexto e overhead de CPU que impedem aproveitar os milhões de IOPS de discos NVMe PCIe Gen4/Gen5.

## Como funciona
No Mayastor, cada nó de armazenamento gerencia *DiskPools* sobre dispositivos de bloco dedicados e executa um plano de dados de alta performance. Quando um `PersistentVolumeClaim` é criado com uma `StorageClass` Mayastor (`repl: "3"`), o CSI provisiona um Nexus NVMe-oF que replica cada gravação de forma síncrona para 3 nós distintos.

## Exemplo
```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: openebs-mayastor-3repl
provisioner: io.openebs.csi-mayastor
parameters:
  protocol: nvmf
  repl: "3"
  fsType: ext4
volumeBindingMode: WaitForFirstConsumer
```

## Limites e trade-offs
O Mayastor exige recursos dedicados nos worker nodes (incluindo páginas de memória *HugePages* de 2 MiB habilitadas no kernel Linux, núcleos de CPU reservados para o io-engine e módulos `nvme-tcp` carregados).

## Como verificar
Confirme a alocação de HugePages nos nós (`grep HugePages_ /proc/meminfo`) e verifique com `kubectl get dsp -n openebs` se os `DiskPools` estão `Online`.

## Conexões
- [[openebs-volume-services-layer-target-nexus-por-volume-blast-radius]] — Veja também: OpenEBS: modelo de um controlador (`Target`/`Nexus`) por volume para redução do raio de explosão (*Blast Radius*).
- [[openebs-localpv-hostpath-provisionamento-dinamico-zero-config]] — Veja também: OpenEBS `Local PV Hostpath`: substituto dinâmico zero-configuração para volumes `hostPath` nativos.

## Fontes
- [OpenEBS GitHub — README.md (Cloud Native Storage, Local Storage vs Replicated Storage Matrix & Sub-Projects)](https://raw.githubusercontent.com/openebs/openebs/HEAD/README.md) — README oficial do openebs/openebs (CNCF Sandbox) comparando Local Storage e Replicated Storage e detalhando Hostpath, ZFS, LVM, Rawfile e Mayastor; consultado em 2026-10-03.
- [OpenEBS Official Documentation — Architecture v4.6.x (Data Engines, Volume Access/Services/Data/Storage Layers & Control Plane)](https://openebs.io/docs/concepts/architecture) — Documentação oficial de arquitetura do OpenEBS explicando as 4 camadas dos Data Engines, Target/Nexus por volume e estados de Volume Replicas; consultado em 2026-10-03.
- [OpenEBS — Official GitHub Repository](https://github.com/openebs/openebs) — Repositório oficial Apache-2.0 do projeto OpenEBS na CNCF; consultado em 2026-10-03.
