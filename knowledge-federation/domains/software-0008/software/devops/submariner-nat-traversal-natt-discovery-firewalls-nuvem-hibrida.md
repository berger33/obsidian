---
id: software.devops.tranche14.001320
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

# Submariner: NAT Traversal (NAT-T), Descoberta de IP Público e Portas de Firewall em Nuvem Híbrida

## Em uma frase
Quando clusters Kubernetes estão atrás de dispositivos NAT (como AWS NAT Gateways, roteadores corporativos ou VPCs privadas), o Submariner utiliza **NAT Traversal (NAT-T)** e descoberta automática de endpoints públicos/privados para estabelecer o túnel entre os nós Gateway.

## Por que importa
Protocolos de túnel IPsec puros (ESP protocolo 50) frequentemente são bloqueados ou corrompidos por dispositivos NAT intermediários se os pacotes não forem encapsulados em UDP.

## Como funciona
O Submariner encapsula o tráfego IPsec em UDP (porta padrão `4500/UDP`) e utiliza uma porta adicional de descoberta de NAT (`4490/UDP`) para que os Gateways negociem automaticamente se devem se conectar pelo IP privado direto (quando na mesma VPC/LAN) ou pelo IP público traduzido pelo NAT.

## Exemplo
```bash
subctl diagnose firewall inter-cluster ~/.kube/config-cluster-a ~/.kube/config-cluster-b
subctl show endpoints
```

## Limites e trade-offs
Esquecer de liberar nos firewalls de borda tanto a porta do túnel (`4500/UDP`) quanto a porta de NAT discovery (`4490/UDP`) entre os IPs públicos dos nós Gateway impede a negociação automática do túnel.

## Como verificar
Valide a abertura das portas UDP entre os clusters com `subctl diagnose firewall inter-cluster` antes de liberar o tráfego de produção.

## Conexões
- [[submariner-diagnostico-automatizado-subctl-diagnose-verify-gather]] — Veja também: Submariner: Diagnóstico Automatizado, Testes E2E e Coleta de Logs (subctl diagnose, verify e gather).

## Fontes
- [Submariner Official Documentation — Architecture (Gateway Engine, Route Agent, Broker, Lighthouse Service Discovery & Globalnet)](https://raw.githubusercontent.com/submariner-io/submariner/devel/README.md) — Documentação oficial de arquitetura do Submariner detalhando ClusterSet, ServiceExport, ServiceImport, domínio clusterset.local, Headless Services por cluster-id e Globalnet Controller; consultado em 2026-10-03.
- [Submariner GitHub — README.md (Network Path, vx-submariner VXLAN Tunnel, Operator, subctl & Helm Deployment)](https://submariner.io/getting-started/architecture/) — README oficial do submariner-io/submariner descrevendo o caminho de pacotes entre worker nodes e nós Gateway eleitos, submariner-operator e comandos subctl; consultado em 2026-10-03.
- [Submariner — Official GitHub Repository](https://github.com/submariner-io/submariner) — Repositório oficial CNCF Sandbox do Submariner; consultado em 2026-10-03.
