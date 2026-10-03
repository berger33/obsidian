---
id: software.devops.tranche17.001621
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
fontes: ["https://raw.githubusercontent.com/liqotech/liqo/master/README.md", "https://docs.liqo.io/en/stable/examples/quick-start.html", "https://github.com/liqotech/liqo"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Liqo: arquitetura de peering dinâmico P2P e abstração de cluster remoto como nó virtual (`Virtual Kubelet`)

## Em uma frase
O Liqo (iniciado no Politecnico di Torino, licenciado sob Apache 2.0) é uma plataforma open-source que habilita topologias multi-cluster dinâmicas e transparentes no Kubernetes, colapsando um cluster remoto inteiro em um nó virtual (`Virtual Node`) compatível com a API e o scheduler padrão do Kubernetes.

## Por que importa
Enquanto sistemas baseados em federação exigem um plano de controle central separado e políticas específicas de propagação, o Liqo permite que um cluster consumidor (*consumer*) enxergue a capacidade negociada com um cluster provedor (*provider*) simplesmente como mais um `Node` local em `kubectl get nodes`.

## Como funciona
A arquitetura do Liqo combina quatro subsistemas: **Peering** (negociação P2P automática de autenticação e cotas de recursos entre clusters independentes), **Offloading** (baseado no *Virtual Kubelet*, que reflete Pods agendados no nó virtual como Twin Pods reais no cluster provedor), **Network Fabric** (túnel seguro multi-cluster com tradução IPAM para conectividade Pod-a-Pod e Pod-a-Service independente da CNI) e **Storage Fabric** (suporte a workloads stateful com gravidade de dados).

## Exemplo
```bash
liqoctl install kind --cluster-id rome
kubectl get pods -n liqo
liqoctl info
```

## Limites e trade-offs
Certifique-se de instalar a mesma versão do Liqo em todos os clusters que estabelecerão peering entre si, garantindo compatibilidade dos CRDs replicados pelo `liqo-crd-replicator`.

## Como verificar
Execute `liqoctl info` após a instalação e confirme que todos os componentes (`liqo-controller-manager`, `liqo-crd-replicator`, `liqo-fabric`, `liqo-ipam`, `liqo-proxy`, `liqo-webhook`) reportam `Liqo is healthy`.

## Conexões
- [[liqo-liqoctl-peer-autenticacao-negociacao-recursos-foreigncluster]] — Veja também: Liqo: estabelecimento de peering entre clusters com `liqoctl peer` e representação `ForeignCluster`.

## Fontes
- [Liqo GitHub — README.md (Dynamic and Seamless Kubernetes Multi-Cluster Topologies, Peering, Offloading, Network & Storage Fabric)](https://raw.githubusercontent.com/liqotech/liqo/master/README.md) — README oficial do liqotech/liqo detalhando peering P2P, Virtual Nodes via Virtual Kubelet, Network Fabric com NATless/NATting IPAM, reflexão de Services e Storage Fabric; consultado em 2026-10-03.
- [Liqo Official Documentation — Quick Start & Examples (liqoctl peer, liqoctl offload namespace, Virtual Node Scheduling & Service Exposure)](https://docs.liqo.io/en/stable/examples/quick-start.html) — Guia oficial Quick Start do Liqo demonstrando peering entre clusters, extensão de namespaces com liqoctl offload e agendamento transparente de Pods remotos; consultado em 2026-10-03.
- [Liqo — Official GitHub Repository](https://github.com/liqotech/liqo) — Repositório oficial Apache-2.0 do Liqo; consultado em 2026-10-03.
