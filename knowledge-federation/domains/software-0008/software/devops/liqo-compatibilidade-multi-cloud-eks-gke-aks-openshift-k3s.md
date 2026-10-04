---
id: software.devops.tranche17.001629
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

# Liqo: operação multi-cloud heterogênea entre AWS EKS, Google GKE, Azure AKS, OpenShift e K3s

## Em uma frase
O `liqoctl install <provider>` inclui adaptadores nativos de autodeteccão para provedores gerenciados (`eks`, `gke`, `aks`, `openshift`, `k3s`, `kind`, `kubeadm`), extraindo automaticamente CIDRs de Pod/Service, endpoints de API e configurações de CNI específicas de cada nuvem.

## Por que importa
Conectar um cluster Amazon EKS (usando AWS VPC CNI) a um cluster Google GKE (usando Cilium/Dataplane V2) ou a um cluster K3s de borda exige parâmetros de rede e descoberta muito diferentes em cada ponta.

## Como funciona
Ao executar `liqoctl install eks` em um lado e `liqoctl install gke` no outro, a CLI consulta as APIs do provedor e do cluster para configurar automaticamente o `liqo-ipam` e o `liqo-fabric` sem exigir que o operador informe manualmente sub-redes ou interfaces de túnel.

## Exemplo
```bash
liqoctl install eks --eks-cluster-name prod-eks-us --region us-east-1
liqoctl install gke --project-id my-gcp-proj --zone europe-west1-b --cluster-id prod-gke-eu
```

## Limites e trade-offs
Ao emparelhar clusters em nuvens públicas distintas, avalie os custos de tráfego de saída (*egress data transfer*) cobrados pelos provedores de nuvem para o tráfego que atravessa o túnel do gateway do Liqo.

## Como verificar
Execute `liqoctl info` em cada cluster após a instalação específica do provedor e valide os `Cluster labels` (`liqo.io/provider`) e os CIDRs detectados.

## Conexões
- [[liqo-crd-replicator-sincronizacao-estado-out-of-band-in-band]] — Veja também: Liqo: sincronização de Custom Resources entre clusters via `liqo-crd-replicator` e modos de peering.
- [[liqo-unoffload-unpeer-descomissionamento-limpo-topologias]] — Veja também: Liqo: descomissionamento seguro de offloading e encerramento de peering (`liqoctl unoffload` e `unpeer`).

## Fontes
- [Liqo GitHub — README.md (Dynamic and Seamless Kubernetes Multi-Cluster Topologies, Peering, Offloading, Network & Storage Fabric)](https://raw.githubusercontent.com/liqotech/liqo/master/README.md) — README oficial do liqotech/liqo detalhando peering P2P, Virtual Nodes via Virtual Kubelet, Network Fabric com NATless/NATting IPAM, reflexão de Services e Storage Fabric; consultado em 2026-10-03.
- [Liqo Official Documentation — Quick Start & Examples (liqoctl peer, liqoctl offload namespace, Virtual Node Scheduling & Service Exposure)](https://docs.liqo.io/en/stable/examples/quick-start.html) — Guia oficial Quick Start do Liqo demonstrando peering entre clusters, extensão de namespaces com liqoctl offload e agendamento transparente de Pods remotos; consultado em 2026-10-03.
- [Liqo — Official GitHub Repository](https://github.com/liqotech/liqo) — Repositório oficial Apache-2.0 do Liqo; consultado em 2026-10-03.
