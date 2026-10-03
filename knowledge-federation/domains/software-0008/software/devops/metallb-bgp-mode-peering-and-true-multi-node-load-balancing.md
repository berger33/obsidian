---
id: software.devops.tranche05.000445
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-05.md"
fontes: ["https://raw.githubusercontent.com/metallb/metallb/main/README.md", "https://metallb.io/concepts/", "https://github.com/metallb/metallb"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Modo BGP do MetalLB: sessões de peering com roteadores e balanceamento de carga real entre múltiplos nós

## Em uma frase
No **modo BGP (`BGPAdvertisement` / `BGPPeer`)**, documentado em `metallb.io/concepts/`, todas as máquinas do cluster estabelecem sessões de peering **BGP (Border Gateway Protocol)** com os roteadores próximos controlados pela organização e anunciam a esses roteadores como encaminhar o tráfego para os IPs dos serviços. Ao contrário do modo Layer 2, o uso de BGP permite **balanceamento de carga real através de múltiplos nós simultaneamente** (via ECMP — Equal-Cost Multi-Path nos roteadores) e controle refinado de tráfego graças aos mecanismos de política do protocolo BGP.

## Por que importa
Em clusters bare-metal de produção de alto tráfego ou distribuídos entre múltiplos racks/sub-redes L3, concentrar todo o tráfego de entrada de um IP em um único nó via ARP cria gargalo de banda e failover mais lento. Com BGP + ECMP, o próprio roteador de topo de rack divide os fluxos entre todos os nós saudáveis e remove um nó caído em sub-segundos (especialmente com BFD).

## Como funciona
Em data centers onde a equipe de infraestrutura controla os roteadores Top-of-Rack (ToR) ou roteadores de borda, prefira o modo BGP configurando recursos `BGPPeer` e `BGPAdvertisement` no MetalLB para anunciar os prefixos dos serviços aos roteadores.

## Exemplo
Quatro nós trabalhadores bare-metal fecham sessão BGP com os switches ToR do rack; quando o `Service` do Ingress recebe o IP `198.51.100.10`, os quatro nós anunciam a rota `/32` via BGP e o switch distribui as conexões de entrada igualmente entre os quatro servidores via ECMP.

## Limites e trade-offs
Coopere sempre com a equipe de engenharia de redes ao configurar ASNs (Autonomous System Numbers), filtros de prefixo e limites de rotas nos roteadores BGP para evitar anunciar sub-redes incorretas na malha corporativa.

## Como verificar
Verifique nos logs dos pods `speaker` do MetalLB e na tabela de roteamento do roteador BGP (`show ip bgp` / `ip route`) que a sessão BGP está `Established` e que as rotas `/32` (ou `/128`) dos serviços apresentam múltiplos next-hops ativos.

## Conexões
- [[metallb-layer-2-mode-arp-ipv4-and-ndp-ipv6-announcement]] — Veja também: Modo Layer 2 do MetalLB: anúncio externo via ARP (IPv4) e NDP (IPv6) na rede local.
- [[metallb-controller-and-speaker-pods-architecture]] — Veja também: Arquitetura de componentes do MetalLB: Deployment controller (alocação) e DaemonSet speaker (anúncio).

## Fontes
- [MetalLB GitHub — README.md (Bare-Metal LoadBalancer, Stable Branch Warning & Security Reporting)](https://raw.githubusercontent.com/metallb/metallb/main/README.md) — README oficial do MetalLB descrevendo implementação de balanceador de carga para clusters Kubernetes bare-metal usando protocolos padrão de roteamento, alerta expresso contra consumo de manifestos da branch main de desenvolvimento em favor de branches estáveis e política de reporte de vulnerabilidades com meta de resposta inicial em 48 horas.; consultado em 2026-10-03.
- [MetalLB Official Documentation — Concepts (Address Allocation, IPAddressPool, Layer 2 ARP/NDP & BGP Mode)](https://metallb.io/concepts/) — Documentação oficial de conceitos do MetalLB detalhando alocação de endereços via IPAddressPool (ranges públicos alugados ou privados RFC1918), anúncio externo em modo Layer 2 (ARP para IPv4 e NDP para IPv6) e modo BGP com roteadores para balanceamento real multi-nó.; consultado em 2026-10-03.
- [MetalLB — Official GitHub Repository](https://github.com/metallb/metallb) — Repositório oficial Apache-2.0 do MetalLB na CNCF.; consultado em 2026-10-03.
