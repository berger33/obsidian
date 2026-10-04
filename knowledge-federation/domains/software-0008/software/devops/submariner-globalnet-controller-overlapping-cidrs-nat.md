---
id: software.devops.tranche14.001317
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

# Submariner: Interconexão de Clusters com CIDRs Sobrepostos usando Globalnet Controller

## Em uma frase
O **Globalnet Controller** é o componente opcional do Submariner projetado para interconectar clusters Kubernetes cujas faixas de IPs de Pods (`ClusterCIDR`) ou de Services (`ServiceCIDR`) se sobrepõem.

## Por que importa
Na prática corporativa, dezenas de clusters criados com configurações padrão de instaladores (`kubeadm`, EKS, OpenShift ou kind) nascem com o mesmo CIDR `10.244.0.0/16` ou `172.30.0.0/16`, tornando impossível o roteamento IP direto sem tradução de endereços.

## Como funciona
Com o Globalnet habilitado no Broker (`subctl deploy-broker --globalnet`), cada cluster recebe uma fatia exclusiva de uma faixa virtual global (`GlobalCIDR`, padrão `242.0.0.0/8`), e o Globalnet Controller aloca IPs globais únicos para os Services exportados e Pods que precisam de comunicação entre clusters, realizando SNAT/DNAT transparente nos nós Gateway.

## Exemplo
```bash
subctl deploy-broker --globalnet --globalnet-cidr 242.0.0.0/8
subctl show networks
```

## Limites e trade-offs
Ativar o Globalnet quando nenhum dos clusters possui CIDRs sobrepostos adiciona sobrecarga desnecessária de tradução NAT e gerenciamento de IPs virtuais.

## Como verificar
Planeje os CIDRs de novos clusters para não colidirem sempre que possível e ative o Globalnet especificamente quando precisar integrar clusters existentes com CIDRs sobrepostos.

## Conexões
- [[submariner-headless-services-statefulsets-dns-pod-clusterid]] — Veja também: Submariner: Resolução DNS de Headless Services por Pod e cluster-id no ClusterSet.
- [[submariner-operator-implantacao-subctl-vs-helm-charts]] — Veja também: Submariner: Arquitetura Baseada em Operator e Implantação via subctl vs Helm Charts.

## Fontes
- [Submariner Official Documentation — Architecture (Gateway Engine, Route Agent, Broker, Lighthouse Service Discovery & Globalnet)](https://submariner.io/getting-started/architecture/) — Documentação oficial de arquitetura do Submariner detalhando ClusterSet, ServiceExport, ServiceImport, domínio clusterset.local, Headless Services por cluster-id e Globalnet Controller; consultado em 2026-10-03.
- [Submariner GitHub — README.md (Network Path, vx-submariner VXLAN Tunnel, Operator, subctl & Helm Deployment)](https://raw.githubusercontent.com/submariner-io/submariner/devel/README.md) — README oficial do submariner-io/submariner descrevendo o caminho de pacotes entre worker nodes e nós Gateway eleitos, submariner-operator e comandos subctl; consultado em 2026-10-03.
- [Submariner — Official GitHub Repository](https://github.com/submariner-io/submariner) — Repositório oficial CNCF Sandbox do Submariner; consultado em 2026-10-03.
