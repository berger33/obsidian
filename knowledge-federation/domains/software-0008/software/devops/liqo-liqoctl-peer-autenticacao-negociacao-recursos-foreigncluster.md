---
id: software.devops.tranche17.001622
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

# Liqo: estabelecimento de peering entre clusters com `liqoctl peer` e representação `ForeignCluster`

## Em uma frase
O comando `liqoctl peer` automatiza o emparelhamento entre um cluster consumidor local (ex.: `rome`) e um cluster provedor remoto (ex.: `milan`), negociando identidades criptográficas, endpoints de rede do gateway e fatias de recursos (`ResourceSlice`) representadas pelo CRD `ForeignCluster`.

## Por que importa
Configurar manualmente túneis VPN site-to-site, autoridades certificadoras cruzadas, ServiceAccounts com escopo mínimo e nós virtuais entre dois clusters de nuvens diferentes (como GKE e EKS) envolve dezenas de passos manuais sujeitos a falha.

## Como funciona
Ao executar `liqoctl peer --remote-kubeconfig "$KUBECONFIG_MILAN"` a partir do cluster consumidor, o Liqo troca credenciais temporárias de autenticação, estabelece o túnel seguro do gateway (via `LoadBalancer` ou `--gw-server-service-type NodePort`), negocia os recursos ofertados pelo provedor e cria no cluster consumidor um nó virtual `liqo-milan` pronto para receber Pods.

## Exemplo
```bash
export KUBECONFIG="$PWD/liqo_kubeconf_rome"
export KUBECONFIG_MILAN="$PWD/liqo_kubeconf_milan"
liqoctl peer --remote-kubeconfig "$KUBECONFIG_MILAN" --gw-server-service-type NodePort
kubectl get foreignclusters
kubectl get nodes
```

## Limites e trade-offs
Em ambientes onde o operador do cluster consumidor não possui o `kubeconfig` administrativo do cluster provedor, o peering pode ser estabelecido de forma desacoplada gerando um comando/token de peering no provedor e consumindo-o no consumidor.

## Como verificar
Execute `liqoctl info` e `kubectl get nodes` no cluster consumidor (`rome`) e confirme que o nó virtual representando o cluster remoto (`milan`) aparece com status `Ready`.

## Conexões
- [[liqo-arquitetura-peering-dinamico-virtual-kubelet-multi-cluster]] — Veja também: Liqo: arquitetura de peering dinâmico P2P e abstração de cluster remoto como nó virtual (`Virtual Kubelet`).
- [[liqo-namespace-offloading-twin-namespaces-politicas-posicionamento]] — Veja também: Liqo: *Namespace Offloading* (`liqoctl offload namespace`), namespaces gêmeos e estratégias de mapeamento.

## Fontes
- [Liqo GitHub — README.md (Dynamic and Seamless Kubernetes Multi-Cluster Topologies, Peering, Offloading, Network & Storage Fabric)](https://docs.liqo.io/en/stable/examples/quick-start.html) — README oficial do liqotech/liqo detalhando peering P2P, Virtual Nodes via Virtual Kubelet, Network Fabric com NATless/NATting IPAM, reflexão de Services e Storage Fabric; consultado em 2026-10-03.
- [Liqo Official Documentation — Quick Start & Examples (liqoctl peer, liqoctl offload namespace, Virtual Node Scheduling & Service Exposure)](https://raw.githubusercontent.com/liqotech/liqo/master/README.md) — Guia oficial Quick Start do Liqo demonstrando peering entre clusters, extensão de namespaces com liqoctl offload e agendamento transparente de Pods remotos; consultado em 2026-10-03.
- [Liqo — Official GitHub Repository](https://github.com/liqotech/liqo) — Repositório oficial Apache-2.0 do Liqo; consultado em 2026-10-03.
