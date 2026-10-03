---
id: software.devops.tranche17.001626
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

# Liqo: reflexão de `Services` e `EndpointSlices` para descoberta e balanceamento de carga multi-cluster

## Em uma frase
Quando um `Service` Kubernetes é criado em um namespace com offloading ativo no Liqo, o mecanismo de *Resource Reflection* replica automaticamente o `Service` e sincroniza os `EndpointSlices` bidirecionalmente entre o cluster consumidor e os clusters provedores.

## Por que importa
Se um microsserviço `frontend` tiver Pods espalhados entre o cluster `rome` e o cluster `milan`, e um serviço `backend` também estiver distribuído entre os dois clusters, o DNS padrão (`http://backend.demo-app.svc.cluster.local`) precisa resolver e balancear tráfego tanto para os Pods locais quanto para os Pods remotos.

## Como funciona
O Liqo sincroniza os objetos `Service`, `ConfigMap` e `Secret` para o namespace gêmeo no cluster provedor e traduz os endereços IP dos `EndpointSlices` (aplicando o remapeamento do `liqo-ipam` quando necessário). Dessa forma, um cliente em `rome` acessando o `ClusterIP` local do Service tem seu tráfego balanceado entre os endpoints locais e os endpoints remotos em `milan` (e vice-versa).

## Exemplo
```bash
kubectl expose deployment nginx-multi --port=80 --name=nginx-svc -n demo-app
kubectl get endpointslices -n demo-app
kubectl get svc,endpointslices -n demo-app --kubeconfig "$KUBECONFIG_MILAN"
```

## Limites e trade-offs
Para restringir o tráfego prioritariamente aos endpoints no mesmo cluster e só transbordar para o cluster remoto se os Pods locais falharem, pode-se combinar a reflexão de `EndpointSlices` do Liqo com dicas de topologia (`Topology Aware Routing` / `trafficDistribution`) do Kubernetes.

## Como verificar
Inspecione `kubectl get endpointslices -n demo-app` em ambos os clusters e confirme que os endereços IP de todas as réplicas (locais e remotas) constam nos slices sincronizados.

## Conexões
- [[liqo-network-fabric-wireguard-ipam-nat-remapping-cni-agnostic]] — Veja também: Liqo: *Network Fabric* multi-cluster agnóstica de CNI com túneis seguros e remapeamento IPAM sem colisão de CIDRs.
- [[liqo-storage-fabric-virtual-storageclass-data-gravity-stateful]] — Veja também: Liqo: *Storage Fabric* e `StorageClass` virtual (`liqo`) para aplicações stateful com gravidade de dados.

## Fontes
- [Liqo GitHub — README.md (Dynamic and Seamless Kubernetes Multi-Cluster Topologies, Peering, Offloading, Network & Storage Fabric)](https://raw.githubusercontent.com/liqotech/liqo/master/README.md) — README oficial do liqotech/liqo detalhando peering P2P, Virtual Nodes via Virtual Kubelet, Network Fabric com NATless/NATting IPAM, reflexão de Services e Storage Fabric; consultado em 2026-10-03.
- [Liqo Official Documentation — Quick Start & Examples (liqoctl peer, liqoctl offload namespace, Virtual Node Scheduling & Service Exposure)](https://docs.liqo.io/en/stable/examples/quick-start.html) — Guia oficial Quick Start do Liqo demonstrando peering entre clusters, extensão de namespaces com liqoctl offload e agendamento transparente de Pods remotos; consultado em 2026-10-03.
- [Liqo — Official GitHub Repository](https://github.com/liqotech/liqo) — Repositório oficial Apache-2.0 do Liqo; consultado em 2026-10-03.
