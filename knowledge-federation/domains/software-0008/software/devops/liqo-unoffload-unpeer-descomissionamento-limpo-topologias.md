---
id: software.devops.tranche17.001630
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
fontes: ["https://docs.liqo.io/en/stable/examples/quick-start.html", "https://raw.githubusercontent.com/liqotech/liqo/master/README.md", "https://github.com/liqotech/liqo"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Liqo: descomissionamento seguro de offloading e encerramento de peering (`liqoctl unoffload` e `unpeer`)

## Em uma frase
O Liqo provê os comandos `liqoctl unoffload namespace` e `liqoctl unpeer` para drenar workloads remotos, remover namespaces gêmeos e encerrar o emparelhamento entre clusters de forma limpa e reversível.

## Por que importa
Quando um cluster provedor temporário (usado para *cloud bursting* durante um evento sazonal) não é mais necessário, simplesmente desligar o cluster remoto sem drenar os Twin Pods e remover o nó virtual deixaria objetos órfãos e endpoints fantasma no cluster consumidor.

## Como funciona
O operador executa primeiro `liqoctl unoffload namespace <ns>`, que remove a permissão de agendamento remoto, drena os Twin Pods de volta para os nós locais (ou outros clusters) e apaga o namespace gêmeo remoto. Em seguida, `liqoctl unpeer --remote-kubeconfig ...` desfaz o túnel de rede, revoga as credenciais e remove o nó virtual.

## Exemplo
```bash
liqoctl unoffload namespace demo-app
liqoctl unpeer --remote-kubeconfig "$KUBECONFIG_MILAN"
kubectl get nodes
```

## Limites e trade-offs
Antes de executar `liqoctl unpeer`, certifique-se de que os nós físicos locais possuem capacidade suficiente para reabsorver as réplicas que estavam rodando no nó virtual remoto.

## Como verificar
Execute `liqoctl info` e `kubectl get foreignclusters` após o `unpeer` e confirme que nenhum peering ativo ou nó virtual residual permaneceu no cluster.

## Conexões
- [[liqo-compatibilidade-multi-cloud-eks-gke-aks-openshift-k3s]] — Veja também: Liqo: operação multi-cloud heterogênea entre AWS EKS, Google GKE, Azure AKS, OpenShift e K3s.

## Fontes
- [Liqo GitHub — README.md (Dynamic and Seamless Kubernetes Multi-Cluster Topologies, Peering, Offloading, Network & Storage Fabric)](https://docs.liqo.io/en/stable/examples/quick-start.html) — README oficial do liqotech/liqo detalhando peering P2P, Virtual Nodes via Virtual Kubelet, Network Fabric com NATless/NATting IPAM, reflexão de Services e Storage Fabric; consultado em 2026-10-03.
- [Liqo Official Documentation — Quick Start & Examples (liqoctl peer, liqoctl offload namespace, Virtual Node Scheduling & Service Exposure)](https://raw.githubusercontent.com/liqotech/liqo/master/README.md) — Guia oficial Quick Start do Liqo demonstrando peering entre clusters, extensão de namespaces com liqoctl offload e agendamento transparente de Pods remotos; consultado em 2026-10-03.
- [Liqo — Official GitHub Repository](https://github.com/liqotech/liqo) — Repositório oficial Apache-2.0 do Liqo; consultado em 2026-10-03.
