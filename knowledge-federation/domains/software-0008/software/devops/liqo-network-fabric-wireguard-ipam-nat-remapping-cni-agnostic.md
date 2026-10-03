---
id: software.devops.tranche17.001625
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

# Liqo: *Network Fabric* multi-cluster agnóstica de CNI com túneis seguros e remapeamento IPAM sem colisão de CIDRs

## Em uma frase
A *Network Fabric* do Liqo (`liqo-fabric`, `liqo-ipam`, `liqo-gateway` e `liqo-proxy`) provê conectividade direta Pod-a-Pod e Pod-a-Service entre todos os clusters emparelhados através de túneis criptografados (como WireGuard), independentemente do plugin CNI de cada cluster e mesmo quando ambos os clusters usam exatamente o mesmo Pod CIDR (`10.244.0.0/16`).

## Por que importa
Em ambientes brownfield ou clusters criados com configurações padrão (como dois clusters `kind` ou `kubeadm` usando `10.244.0.0/16`), soluções multi-cluster que exigem CIDRs de Pod globalmente únicos obrigam a destruir e recriar clusters inteiros.

## Como funciona
O componente `liqo-ipam` detecta automaticamente sobreposições de faixa de IP (*overlapping CIDRs*) durante o peering, aloca um CIDR externo livre de conflito para representar o cluster par e configura regras de tradução de endereços (NAT stateless) nos gateways do `liqo-fabric`. Assim, qualquer Pod local comunica-se diretamente por IP com qualquer Pod offloaded no cluster remoto de forma transparente.

## Exemplo
```bash
kubectl get pods -n demo-app -o wide
POD_REMOTE_IP=$(kubectl get pods -n demo-app -o wide | grep liqo- | head -n1 | awk '{print $6}')
kubectl run tester -n demo-app --rm -it --image=curlimages/curl -- curl -sI "http://${POD_REMOTE_IP}"
```

## Limites e trade-offs
O tráfego entre clusters atravessa os Pods de gateway do Liqo; portanto, políticas de firewall de infraestrutura entre os clusters precisam liberar a porta UDP/TCP configurada para o serviço do gateway (`LoadBalancer` ou `NodePort`).

## Como verificar
Execute o teste de `curl` a partir de um Pod agendado no nó físico local diretamente para o endereço IP de um Pod agendado no nó virtual do Liqo e confirme a resposta `HTTP/1.1 200 OK`.

## Conexões
- [[liqo-pod-offloading-virtual-kubelet-reflexao-status-logs-exec]] — Veja também: Liqo: offloading transparente de Pods via Virtual Kubelet e suporte nativo a `kubectl logs` e `exec`.
- [[liqo-service-offloading-endpointslice-reflection-multi-cluster]] — Veja também: Liqo: reflexão de `Services` e `EndpointSlices` para descoberta e balanceamento de carga multi-cluster.

## Fontes
- [Liqo GitHub — README.md (Dynamic and Seamless Kubernetes Multi-Cluster Topologies, Peering, Offloading, Network & Storage Fabric)](https://raw.githubusercontent.com/liqotech/liqo/master/README.md) — README oficial do liqotech/liqo detalhando peering P2P, Virtual Nodes via Virtual Kubelet, Network Fabric com NATless/NATting IPAM, reflexão de Services e Storage Fabric; consultado em 2026-10-03.
- [Liqo Official Documentation — Quick Start & Examples (liqoctl peer, liqoctl offload namespace, Virtual Node Scheduling & Service Exposure)](https://docs.liqo.io/en/stable/examples/quick-start.html) — Guia oficial Quick Start do Liqo demonstrando peering entre clusters, extensão de namespaces com liqoctl offload e agendamento transparente de Pods remotos; consultado em 2026-10-03.
- [Liqo — Official GitHub Repository](https://github.com/liqotech/liqo) — Repositório oficial Apache-2.0 do Liqo; consultado em 2026-10-03.
