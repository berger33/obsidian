---
id: software.devops.tranche17.001648
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-17.md"
fontes: ["https://raw.githubusercontent.com/openyurtio/openyurt/master/README.md", "https://openyurt.io/docs/core-concepts/architecture/", "https://github.com/openyurtio/openyurt"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# OpenYurt `Node Resource Manager`: gerenciamento de armazenamento local de borda (LVM, QuotaPath e PMEM)

## Em uma frase
O componente auxiliar `node-resource-manager` do ecossistema OpenYurt gerencia recursos de armazenamento local nos nós de borda — incluindo volumes lógicos **LVM**, diretórios com cota de disco (**QuotaPath**) e memória persistente (**Persistent Memory / PMEM**).

## Por que importa
Em gateways e servidores de borda, raramente existe um cluster de armazenamento distribuído dedicado (como Ceph multi-nó); os containers de banco de dados local e cache de vídeo precisam consumir discos locais do próprio host com isolamento estrito de cota de capacidade e IOPS.

## Como funciona
O `node-resource-manager` descobre discos e grupos de volumes nos nós de borda e provisiona dinamicamente volumes locais isolados por LVM ou cota de projeto de filesystem (`QuotaPath`), evitando que um container com vazamento de logs encha 100% da partição raiz do sistema operacional do gateway de borda.

## Exemplo
```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: yurt-local-lvm
provisioner: lvm.csi.openyurt.io
volumeBindingMode: WaitForFirstConsumer
parameters:
  vgName: yurt-vg0
```

## Limites e trade-offs
Sempre utilize `volumeBindingMode: WaitForFirstConsumer` nas `StorageClasses` locais de borda para garantir que o volume LVM ou QuotaPath seja provisionado no mesmo nó físico de borda onde o Pod consumidor foi agendado.

## Como verificar
Crie um PVC com `storageClassName: yurt-local-lvm` consumido por um Pod de borda e verifique a criação do Logical Volume correspondente no grupo `yurt-vg0` do nó.

## Conexões
- [[openyurt-autonomia-no-prevencao-eviccao-pods-desconexao-wan]] — Veja também: OpenYurt: prevenção de evicção indevida de Pods durante desconexão nuvem-borda (`node-autonomy`).
- [[openyurt-yurt-manager-controladores-webhooks-alta-disponibilidade]] — Veja também: OpenYurt `Yurt-Manager`: consolidação de controladores e webhooks cloud-edge em alta disponibilidade.

## Fontes
- [OpenYurt GitHub — README.md (CNCF Incubating Extending Native Kubernetes to Edge, Non-Intrusive Architecture & Edge Autonomy)](https://raw.githubusercontent.com/openyurtio/openyurt/master/README.md) — README oficial do openyurtio/openyurt (CNCF Incubating) apresentando a filosofia não intrusiva, autonomia de borda, NodePool e operação cloud-edge; consultado em 2026-10-03.
- [OpenYurt Official Documentation — Core Concepts: Architecture (YurtHub Local Cache, Yurt-Tunnel Reverse Proxy, Yurt-Manager & Raven)](https://openyurt.io/docs/core-concepts/architecture/) — Documentação oficial de arquitetura do OpenYurt detalhando YurtHub, Yurt-Tunnel-Server/Agent, controladores do Yurt-Manager e topologia por NodePool; consultado em 2026-10-03.
- [OpenYurt — Official GitHub Repository](https://github.com/openyurtio/openyurt) — Repositório oficial Apache-2.0 do OpenYurt na CNCF; consultado em 2026-10-03.
