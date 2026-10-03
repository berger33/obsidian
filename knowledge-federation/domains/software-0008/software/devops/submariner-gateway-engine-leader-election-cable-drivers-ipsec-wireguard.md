---
id: software.devops.tranche14.001312
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
fontes: ["https://submariner.io/getting-started/architecture/", "https://raw.githubusercontent.com/submariner-io/submariner/devel/README.md", "https://github.com/submariner-io/submariner"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Submariner: Gateway Engine, Eleição de Líder e Cable Drivers (Libreswan IPsec, WireGuard e VXLAN)

## Em uma frase
O **Gateway Engine** do Submariner roda nos nós rotulados como gateways (`submariner.io/gateway=true`), utiliza eleição de líder para manter um gateway ativo por cluster e estabelece os túneis seguros entre os clusters usando **Cable Drivers** plugáveis (como Libreswan IPsec por padrão, WireGuard ou VXLAN sem criptografia).

## Por que importa
Abrir conectividade de rede de todos os worker nodes de um cluster para todos os worker nodes de outro cluster através de firewalls corporativos e WANs é inviável operacionalmente.

## Como funciona
Ao concentrar o tráfego inter-cluster nos nós Gateway eleitos, apenas os IPs dos nós Gateway precisam de conectividade UDP/IPsec entre os datacenters; caso o nó Gateway líder falhe, outro nó Gateway do mesmo cluster assume a liderança e restabelece os túneis automaticamente.

## Exemplo
```bash
# Rotular um no como Gateway do Submariner e verificar status dos tuneis:
subctl cloud prepare generic
subctl show connections
subctl show gateways
```

## Limites e trade-offs
Implantar apenas um único nó rotulado como `submariner.io/gateway=true` em produção cria um ponto único de falha para toda a comunicação multi-cluster caso aquele host sofra manutenção ou reboot.

## Como verificar
Configure pelo menos dois nós Gateway por cluster e monitore a saúde dos túneis com `subctl show connections` e `subctl show gateways`.

## Conexões
- [[submariner-arquitetura-rede-multicluster-cni-agnostic-cncf]] — Veja também: Submariner: Arquitetura de Rede Multi-Cluster CNI-Agnostic na CNCF.
- [[submariner-route-agent-vx-submariner-fluxo-pacotes-pod-service]] — Veja também: Submariner: Route Agent, Túnel Interno vx-submariner e Caminho de Rede entre Worker Nodes e Gateways.

## Fontes
- [Submariner Official Documentation — Architecture (Gateway Engine, Route Agent, Broker, Lighthouse Service Discovery & Globalnet)](https://submariner.io/getting-started/architecture/) — Documentação oficial de arquitetura do Submariner detalhando ClusterSet, ServiceExport, ServiceImport, domínio clusterset.local, Headless Services por cluster-id e Globalnet Controller; consultado em 2026-10-03.
- [Submariner GitHub — README.md (Network Path, vx-submariner VXLAN Tunnel, Operator, subctl & Helm Deployment)](https://raw.githubusercontent.com/submariner-io/submariner/devel/README.md) — README oficial do submariner-io/submariner descrevendo o caminho de pacotes entre worker nodes e nós Gateway eleitos, submariner-operator e comandos subctl; consultado em 2026-10-03.
- [Submariner — Official GitHub Repository](https://github.com/submariner-io/submariner) — Repositório oficial CNCF Sandbox do Submariner; consultado em 2026-10-03.
