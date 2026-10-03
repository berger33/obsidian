---
id: software.devops.tranche02.000122
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-02.md"
fontes: ["https://raw.githubusercontent.com/cilium/cilium/main/README.rst", "https://docs.cilium.io/en/stable/overview/component-overview/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Modos de operação CNI: overlay (VXLAN/Geneve), roteamento nativo e BGP/L2

## Em uma frase
A seção `CNI (Container Network Interface)` do `README.rst` detalha três opções de implantação do Cilium como plugin CNI: **Overlay networking** (rede virtual baseada em encapsulamento VXLAN e Geneve que exige apenas conectividade IP entre hosts), **Native routing mode** (uso da tabela de roteamento regular do host Linux, integrando-se com roteadores de nuvem, daemons de roteamento e infraestrutura IPv6 nativa) e **Flexible routing options** (descoberta de vizinhos L2 ou BGP através de fronteiras L3).

## Por que importa
Cada topologia de datacenter ou nuvem pública impõe restrições diferentes: o modo overlay funciona imediatamente sobre qualquer rede IP, enquanto o roteamento nativo com BGP ou integração de nuvem elimina o overhead de encapsulamento.

## Como funciona
Escolha entre encapsulamento (`VXLAN`/`Geneve`) para portabilidade imediata ou `Native routing` com anúncio BGP/L2 quando a rede subjacente puder rotear diretamente os IPs dos pods.

## Exemplo
Em um datacenter bare-metal, a equipe configura o Cilium em modo de roteamento nativo com BGP para anunciar prefixos de pods diretamente aos switches Top-of-Rack.

## Limites e trade-offs
Alterar o modo de roteamento (de overlay para nativo) em um cluster em produção impacta o tráfego ativo; planeje e teste a topologia antes de entrar em produção.

## Como verificar
Conferi a subseção CNI (Container Network Interface) em `README.rst` de `cilium/cilium`.

## Conexões
- [[cilium-ebpf-dataplane-networking-security-observability]] — Veja também: Dataplane baseado em eBPF para rede, observabilidade e segurança graduado na CNCF.
- [[cilium-ebpf-load-balancing-kube-proxy-replacement]] — Veja também: Balanceamento de carga eBPF L4, substituição do kube-proxy, XDP, DSR e Maglev.

## Fontes
- [Cilium — GitHub README.rst](https://raw.githubusercontent.com/cilium/cilium/main/README.rst) — Visão geral do Cilium (dataplane eBPF, CNI overlay/native/BGP, substituição do kube-proxy, Cluster Mesh, Network Policy L3-L7/DNS, Service Mesh, Hubble, releases estáveis, SBOM SPDX e licenças).; consultado em 2026-10-03.
- [Cilium Documentation — Architecture and Component Overview](https://docs.cilium.io/en/stable/overview/component-overview/) — Documentação oficial de arquitetura, requisitos de sistema e operação do Cilium referenciada no README.; consultado em 2026-10-03.
