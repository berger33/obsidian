---
id: software.devops.tranche14.001311
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

# Submariner: Arquitetura de Rede Multi-Cluster CNI-Agnostic na CNCF

## Em uma frase
O **Submariner** (`submariner-io/submariner`, projeto **CNCF Sandbox**) conecta as redes de overlay de múltiplos clusters Kubernetes (on-premises e em nuvens públicas), permitindo alcançabilidade IP direta entre Pods e Services de clusters diferentes de forma independente do plugin CNI utilizado.

## Por que importa
Expor cada microsserviço interno via Ingress público ou LoadBalancer externo apenas para que um Pod no Cluster A converse com um Pod no Cluster B adiciona latência, custo de balanceadores e complexidade de gerenciamento de certificados e firewalls.

## Como funciona
O Submariner achata a conectividade L3 entre os clusters que compõem um `ClusterSet` por meio de cinco componentes coordenados: **Broker** (troca de metadados CRDs), **Gateway Engine** (túneis criptografados ou não entre clusters), **Route Agent** (roteamento nos worker nodes), **Service Discovery / Lighthouse** (DNS multi-cluster) e **Globalnet Controller** (opcional para CIDRs sobrepostos).

## Exemplo
```bash
subctl version
subctl show all
```

## Limites e trade-offs
Interconectar dois clusters que possuem exatamente a mesma faixa CIDR de Pods ou de Services (como `10.244.0.0/16` padrão) sem habilitar o componente **Globalnet** no momento do join causa conflito de roteamento IP entre os clusters.

## Como verificar
Verifique os CIDRs de cada cluster com `subctl show networks` antes da conexão e habilite o Globalnet caso haja sobreposição de endereços.

## Conexões
- [[submariner-gateway-engine-leader-election-cable-drivers-ipsec-wireguard]] — Veja também: Submariner: Gateway Engine, Eleição de Líder e Cable Drivers (Libreswan IPsec, WireGuard e VXLAN).

## Fontes
- [Submariner Official Documentation — Architecture (Gateway Engine, Route Agent, Broker, Lighthouse Service Discovery & Globalnet)](https://raw.githubusercontent.com/submariner-io/submariner/devel/README.md) — Documentação oficial de arquitetura do Submariner detalhando ClusterSet, ServiceExport, ServiceImport, domínio clusterset.local, Headless Services por cluster-id e Globalnet Controller; consultado em 2026-10-03.
- [Submariner GitHub — README.md (Network Path, vx-submariner VXLAN Tunnel, Operator, subctl & Helm Deployment)](https://submariner.io/getting-started/architecture/) — README oficial do submariner-io/submariner descrevendo o caminho de pacotes entre worker nodes e nós Gateway eleitos, submariner-operator e comandos subctl; consultado em 2026-10-03.
- [Submariner — Official GitHub Repository](https://github.com/submariner-io/submariner) — Repositório oficial CNCF Sandbox do Submariner; consultado em 2026-10-03.
