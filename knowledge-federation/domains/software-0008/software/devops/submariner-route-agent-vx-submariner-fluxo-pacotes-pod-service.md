---
id: software.devops.tranche14.001313
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-14.md"
fontes: ["https://raw.githubusercontent.com/submariner-io/submariner/devel/README.md", "https://submariner.io/getting-started/architecture/", "https://github.com/submariner-io/submariner"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Submariner: Route Agent, Túnel Interno vx-submariner e Caminho de Rede entre Worker Nodes e Gateways

## Em uma frase
O **Route Agent** roda como um DaemonSet em todos os nós do cluster e programa as tabelas de roteamento e regras iptables/nftables locais para encaminhar o tráfego destinado a clusters remotos através do túnel VXLAN interno (`vx-submariner`) até o nó Gateway líder local.

## Por que importa
Quando um Pod de origem está em um worker node que **não** é o nó Gateway eleito, o pacote precisa atravessar a rede interna do cluster até chegar ao nó Gateway sem ser descartado pelo CNI local.

## Como funciona
O pacote sai do Pod no worker node, entra na interface de túnel VXLAN `vx-submariner` até o nó Gateway ativo do cluster local, atravessa o túnel WAN criptografado até o nó Gateway do cluster de destino e lá é entregue de duas maneiras conforme o CIDR de destino: via rede programada pelo CNI (se o destino for um IP de Pod) ou via `kube-proxy` do nó Gateway de destino (se o destino for um IP de `Service`).

## Exemplo
```bash
subctl show endpoints
kubectl -n submariner-operator get daemonset submariner-routeagent
```

## Limites e trade-offs
Bloquear a porta UDP do túnel VXLAN interno (`vx-submariner`, tipicamente porta 4800/UDP) nos Security Groups internos entre os worker nodes e os nós Gateway do mesmo cluster impede que Pods fora do nó Gateway alcancem o cluster remoto.

## Como verificar
Execute `subctl verify` (ou `subctl diagnose firewall intra-cluster`) para validar que o túnel `vx-submariner` entre worker nodes e nós Gateway está desbloqueado.

## Conexões
- [[submariner-gateway-engine-leader-election-cable-drivers-ipsec-wireguard]] — Veja também: Submariner: Gateway Engine, Eleição de Líder e Cable Drivers (Libreswan IPsec, WireGuard e VXLAN).
- [[submariner-broker-sincronizacao-crds-endpoint-clusterset]] — Veja também: Submariner: O Papel do Broker na Troca de Metadados (Endpoints e ServiceImports) entre Clusters.

## Fontes
- [Submariner Official Documentation — Architecture (Gateway Engine, Route Agent, Broker, Lighthouse Service Discovery & Globalnet)](https://raw.githubusercontent.com/submariner-io/submariner/devel/README.md) — Documentação oficial de arquitetura do Submariner detalhando ClusterSet, ServiceExport, ServiceImport, domínio clusterset.local, Headless Services por cluster-id e Globalnet Controller; consultado em 2026-10-03.
- [Submariner GitHub — README.md (Network Path, vx-submariner VXLAN Tunnel, Operator, subctl & Helm Deployment)](https://submariner.io/getting-started/architecture/) — README oficial do submariner-io/submariner descrevendo o caminho de pacotes entre worker nodes e nós Gateway eleitos, submariner-operator e comandos subctl; consultado em 2026-10-03.
- [Submariner — Official GitHub Repository](https://github.com/submariner-io/submariner) — Repositório oficial CNCF Sandbox do Submariner; consultado em 2026-10-03.
