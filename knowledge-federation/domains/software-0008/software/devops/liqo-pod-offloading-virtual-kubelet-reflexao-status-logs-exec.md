---
id: software.devops.tranche17.001624
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

# Liqo: offloading transparente de Pods via Virtual Kubelet e suporte nativo a `kubectl logs` e `exec`

## Em uma frase
Quando o `kube-scheduler` do cluster consumidor agenda um Pod em um nó virtual do Liqo, o agente *Virtual Kubelet* do Liqo não inicia um container localmente: ele cria um *Twin Pod* correspondente no cluster provedor remoto e sincroniza continuamente seu status, IP e eventos de volta.

## Por que importa
Para que a experiência multi-cluster seja 100% transparente para desenvolvedores e operadores, comandos padrão de observabilidade e depuração (`kubectl get pods -o wide`, `kubectl describe pod`, `kubectl logs`, `kubectl exec`, `kubectl port-forward`) precisam funcionar no cluster consumidor exatamente como em Pods locais.

## Como funciona
O controlador do nó virtual intercepta a atribuição do Pod, traduz referências de `ConfigMaps`, `Secrets` e `ServiceAccounts` refletidos no namespace gêmeo, submete o Pod ao `kube-apiserver` do provedor e atua como proxy para as APIs de Kubelet (`logs`, `exec`, `attach`, métricas para HPA), roteando o tráfego pelo túnel da Network Fabric.

## Exemplo
```bash
kubectl create deployment nginx-multi --image=nginx:1.25 --replicas=4 -n demo-app
kubectl get pods -n demo-app -o wide
kubectl exec -it -n demo-app deploy/nginx-multi -- hostname
```

## Limites e trade-offs
Pods locais normais não são agendados nos nós virtuais do Liqo a menos que seu namespace tenha sido explicitamente habilitado via `liqoctl offload namespace` (que injeta automaticamente a toleration para o taint `virtual-node.liqo.io/not-allowed: NoExecute` do nó virtual).

## Como verificar
Execute `kubectl get pods -n demo-app -o wide` no cluster consumidor e confirme que parte das réplicas roda nos nós físicos locais e parte roda no nó virtual remoto, ambas com status `Running`.

## Conexões
- [[liqo-namespace-offloading-twin-namespaces-politicas-posicionamento]] — Veja também: Liqo: *Namespace Offloading* (`liqoctl offload namespace`), namespaces gêmeos e estratégias de mapeamento.
- [[liqo-network-fabric-wireguard-ipam-nat-remapping-cni-agnostic]] — Veja também: Liqo: *Network Fabric* multi-cluster agnóstica de CNI com túneis seguros e remapeamento IPAM sem colisão de CIDRs.

## Fontes
- [Liqo GitHub — README.md (Dynamic and Seamless Kubernetes Multi-Cluster Topologies, Peering, Offloading, Network & Storage Fabric)](https://docs.liqo.io/en/stable/examples/quick-start.html) — README oficial do liqotech/liqo detalhando peering P2P, Virtual Nodes via Virtual Kubelet, Network Fabric com NATless/NATting IPAM, reflexão de Services e Storage Fabric; consultado em 2026-10-03.
- [Liqo Official Documentation — Quick Start & Examples (liqoctl peer, liqoctl offload namespace, Virtual Node Scheduling & Service Exposure)](https://raw.githubusercontent.com/liqotech/liqo/master/README.md) — Guia oficial Quick Start do Liqo demonstrando peering entre clusters, extensão de namespaces com liqoctl offload e agendamento transparente de Pods remotos; consultado em 2026-10-03.
- [Liqo — Official GitHub Repository](https://github.com/liqotech/liqo) — Repositório oficial Apache-2.0 do Liqo; consultado em 2026-10-03.
