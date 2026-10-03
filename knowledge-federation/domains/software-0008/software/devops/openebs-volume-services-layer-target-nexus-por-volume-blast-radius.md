---
id: software.devops.tranche18.001702
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
fontes: ["https://openebs.io/docs/concepts/architecture", "https://raw.githubusercontent.com/openebs/openebs/HEAD/README.md", "https://github.com/openebs/openebs"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# OpenEBS: modelo de um controlador (`Target`/`Nexus`) por volume para redução do raio de explosão (*Blast Radius*)

## Em uma frase
Diferentemente de storages tradicionais que concentram o I/O de centenas de volumes em um único controlador monolítico, a *Volume Services Layer* do OpenEBS instancia um controlador de armazenamento independente (*Volume Target* / *Nexus*) para cada volume replicado.

## Por que importa
Se um controlador de armazenamento compartilhado travar ou sofrer contenção de metadados, todos os bancos de dados do cluster perdem acesso a disco ao mesmo tempo; com um controlador dedicado por volume, qualquer falha ou reconstrução (*rebuild*) fica contida a um único `PersistentVolume` e à lista fixa de nós de suas réplicas.

## Como funciona
No modo de armazenamento replicado, a aplicação realiza leituras e escritas através do *Volume Target* (exposto como um *NVMe Target* na rede), que coordena o acesso, replica sincronamente os blocos para os endpoints de rede das *Volume Replicas* nos nós escolhidos e gerencia a reconstrução de réplicas que saíram do estado `Offline` para `Rebuilding` e `Healthy`.

## Exemplo
```bash
kubectl get pvc,pv
kubectl get diskpools -n openebs
```

## Limites e trade-offs
Cada *Volume Replica* no OpenEBS passa por cinco estados bem definidos durante seu ciclo de vida: `Initializing`, `Healthy`, `Offline`, `Rebuilding` e `Terminating`.

## Como verificar
Verifique o estado das réplicas e do Nexus do volume no namespace `openebs` antes e durante um teste de reinicialização de nó.

## Conexões
- [[openebs-arquitetura-container-native-storage-data-engines-control-plane]] — Veja também: OpenEBS: arquitetura Container Native Storage (CNS) com Data Engines e Control Plane no Kubernetes.
- [[openebs-mayastor-replicated-storage-nvme-of-spdk-alta-performance]] — Veja também: OpenEBS `Mayastor`: motor de armazenamento replicado corporativo baseado em NVMe-oF e SPDK.

## Fontes
- [OpenEBS GitHub — README.md (Cloud Native Storage, Local Storage vs Replicated Storage Matrix & Sub-Projects)](https://openebs.io/docs/concepts/architecture) — README oficial do openebs/openebs (CNCF Sandbox) comparando Local Storage e Replicated Storage e detalhando Hostpath, ZFS, LVM, Rawfile e Mayastor; consultado em 2026-10-03.
- [OpenEBS Official Documentation — Architecture v4.6.x (Data Engines, Volume Access/Services/Data/Storage Layers & Control Plane)](https://raw.githubusercontent.com/openebs/openebs/HEAD/README.md) — Documentação oficial de arquitetura do OpenEBS explicando as 4 camadas dos Data Engines, Target/Nexus por volume e estados de Volume Replicas; consultado em 2026-10-03.
- [OpenEBS — Official GitHub Repository](https://github.com/openebs/openebs) — Repositório oficial Apache-2.0 do projeto OpenEBS na CNCF; consultado em 2026-10-03.
