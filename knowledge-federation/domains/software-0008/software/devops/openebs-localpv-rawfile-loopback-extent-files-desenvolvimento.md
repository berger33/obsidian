---
id: software.devops.tranche18.001707
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

# OpenEBS `Local PV Rawfile`: armazenamento em bloco e arquivo baseado em sparse files locais

## Em uma frase
O subprojeto **Local PV Rawfile** (`openebs/rawfile-localpv`) é um motor CSI do OpenEBS que provisiona volumes persistentes (tanto em modo `Filesystem` quanto em modo `Block`) a partir de arquivos de imagem (*extent/sparse files*) montados via dispositivos loopback sobre qualquer diretório local do nó.

## Por que importa
Em ambientes de desenvolvimento, CI/CD ou servidores em nuvem onde não há discos brutos livres nem partições separadas para criar um Volume Group LVM ou um zpool ZFS, o `Rawfile` oferece cotas rígidas de tamanho e suporte a `volumeMode: Block` usando apenas o disco raiz do nó.

## Como funciona
Quando um PVC é criado, o driver CSI cria um arquivo esparso (`.img`) do tamanho solicitado no diretório configurado do nó, associa um dispositivo de bloco loopback (`/dev/loopX`) quando necessário e formata-o com o sistema de arquivos escolhido, garantindo que um Pod nunca consuma espaço além do limite declarado no PVC.

## Exemplo
```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: openebs-rawfile-localpv
provisioner: rawfile.csi.openebs.io
allowVolumeExpansion: true
volumeBindingMode: WaitForFirstConsumer
```

## Limites e trade-offs
Conforme documentado na matriz oficial do OpenEBS, o `Local PV Rawfile` encontra-se em estágio Beta/Experimental voltado a desenvolvedores e avaliação, enquanto `Local PV Hostpath`, `Local PV LVM`, `Local PV ZFS` e `Mayastor` têm status estável para produção.

## Como verificar
Crie um PVC com `volumeMode: Block` usando a classe `openebs-rawfile-localpv` e verifique o dispositivo de bloco entregue dentro do container.

## Conexões
- [[openebs-localpv-zfs-datasets-zvols-compressao-raidz-snapshots]] — Veja também: OpenEBS `Local PV ZFS`: provisionamento CSI de datasets e ZVOLs sobre pools ZFS com compressão e RAID-Z.
- [[openebs-criterios-escolha-local-storage-vs-replicated-storage]] — Veja também: OpenEBS: matriz de decisão arquitetural entre Local Storage (`LocalPV`) e Replicated Storage (`Mayastor`).

## Fontes
- [OpenEBS GitHub — README.md (Cloud Native Storage, Local Storage vs Replicated Storage Matrix & Sub-Projects)](https://raw.githubusercontent.com/openebs/openebs/HEAD/README.md) — README oficial do openebs/openebs (CNCF Sandbox) comparando Local Storage e Replicated Storage e detalhando Hostpath, ZFS, LVM, Rawfile e Mayastor; consultado em 2026-10-03.
- [OpenEBS Official Documentation — Architecture v4.6.x (Data Engines, Volume Access/Services/Data/Storage Layers & Control Plane)](https://openebs.io/docs/concepts/architecture) — Documentação oficial de arquitetura do OpenEBS explicando as 4 camadas dos Data Engines, Target/Nexus por volume e estados de Volume Replicas; consultado em 2026-10-03.
- [OpenEBS — Official GitHub Repository](https://github.com/openebs/openebs) — Repositório oficial Apache-2.0 do projeto OpenEBS na CNCF; consultado em 2026-10-03.
