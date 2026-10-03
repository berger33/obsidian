---
id: software.devops.tranche18.001701
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

# OpenEBS: arquitetura Container Native Storage (CNS) com Data Engines e Control Plane no Kubernetes

## Em uma frase
O OpenEBS (projeto CNCF Sandbox licenciado sob Apache 2.0) implementa o padrão *Container Native Storage* (CNS) fornecendo armazenamento persistente para cargas de trabalho Kubernetes por meio de motores de dados conteinerizados divididos em duas abordagens principais: **Local Storage** e **Replicated Storage**.

## Por que importa
Aplicações distribuídas modernas (como Cassandra, MongoDB ou Kafka) já replicam dados na própria camada de aplicação e precisam apenas de desempenho bruto de disco local (`LocalPV`), enquanto bancos standalone ou sistemas legados exigem replicação síncrona no nível do volume de bloco (`Mayastor`) com failover entre nós.

## Como funciona
A arquitetura do OpenEBS divide-se no **Control Plane** (provisionadores dinâmicos CSI, gerenciamento de snapshots/clones, expansão de volume e métricas Prometheus) e nos **Data Engines**, que por sua vez são decompostos em quatro camadas: *Volume Access Layer* (montagem Ext4/XFS ou bloco raw pelo `kubelet`/CSI), *Volume Services Layer* (Target/Nexus dedicado por volume), *Volume Data Layer* (Volume Replicas nos nós) e *Storage Layer* (dispositivos físicos NVMe/SAS/SSD).

## Exemplo
```bash
helm repo add openebs https://openebs.github.io/openebs
helm repo update
helm install openebs --namespace openebs openebs/openebs --create-namespace
kubectl get pods -n openebs
```

## Limites e trade-offs
Ao instalar o chart guarda-chuva `openebs/openebs`, você pode habilitar ou desabilitar motores específicos (`lvm-localpv`, `zfs-localpv`, `mayastor`) conforme a necessidade do cluster para economizar recursos nos worker nodes.

## Como verificar
Execute `kubectl get sc` e `kubectl get pods -n openebs` para verificar as `StorageClasses` e os controladores provisionados.

## Conexões
- [[openebs-volume-services-layer-target-nexus-por-volume-blast-radius]] — Veja também: OpenEBS: modelo de um controlador (`Target`/`Nexus`) por volume para redução do raio de explosão (*Blast Radius*).

## Fontes
- [OpenEBS GitHub — README.md (Cloud Native Storage, Local Storage vs Replicated Storage Matrix & Sub-Projects)](https://raw.githubusercontent.com/openebs/openebs/HEAD/README.md) — README oficial do openebs/openebs (CNCF Sandbox) comparando Local Storage e Replicated Storage e detalhando Hostpath, ZFS, LVM, Rawfile e Mayastor; consultado em 2026-10-03.
- [OpenEBS Official Documentation — Architecture v4.6.x (Data Engines, Volume Access/Services/Data/Storage Layers & Control Plane)](https://openebs.io/docs/concepts/architecture) — Documentação oficial de arquitetura do OpenEBS explicando as 4 camadas dos Data Engines, Target/Nexus por volume e estados de Volume Replicas; consultado em 2026-10-03.
- [OpenEBS — Official GitHub Repository](https://github.com/openebs/openebs) — Repositório oficial Apache-2.0 do projeto OpenEBS na CNCF; consultado em 2026-10-03.
