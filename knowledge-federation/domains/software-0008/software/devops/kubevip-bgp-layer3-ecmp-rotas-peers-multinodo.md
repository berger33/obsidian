---
id: software.devops.tranche13.001283
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-13.md"
fontes: ["https://raw.githubusercontent.com/kube-vip/kube-vip/main/README.md", "https://kube-vip.io/docs/about/architecture/", "https://github.com/kube-vip/kube-vip"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# kube-vip: Modo BGP (Layer 3) para Anúncio Multi-Nó de VIPs e Balanceamento ECMP

## Em uma frase
No modo **BGP (Layer 3)**, em vez de apenas um líder deter o VIP por vez (como no modo ARP), múltiplos nós executando o `kube-vip` estabelecem sessões BGP com os roteadores Top-of-Rack (ToR) e anunciam simultaneamente o endereço VIP (`bgpConfig.routerID`, `bgpConfig.peers`), permitindo balanceamento de carga **ECMP (Equal-Cost Multi-Path)** na malha de rede.

## Por que importa
No modo ARP com eleição de líder sem BGP, todo o tráfego de entrada para um IP de LoadBalancer entra inicialmente pela placa de rede de um único nó líder antes de ser distribuído pelo `kube-proxy`/IPVS.

## Como funciona
Com BGP habilitado, cada nó do cluster anuncia a rota `/32` (IPv4) ou `/128` (IPv6) do VIP para os peers BGP configurados; se um nó falhar, a sessão BGP cai e o roteador ToR retira aquele next-hop da tabela ECMP instantaneamente.

## Exemplo
```yaml
# Exemplo de configuracao estruturada para BGP no arquivo de runtime do kube-vip:
enableBGP: true
bgpConfig:
  routerID: "10.0.10.11"
  localAS: 65000
  peers:
    - address: "10.0.10.1"
      as: 65001
```

## Limites e trade-offs
Usar a chave geradora antiga `bgpPeers` em vez de `bgpConfig.peers` em arquivos de configuração de runtime (`--config-file`) causa rejeição imediata, pois o parser de runtime do `kube-vip` rejeita chaves exclusivas de gerador.

## Como verificar
Em arquivos passados via `--config-file`, utilize sempre a estrutura documentada `bgpConfig.peers` (ou `bgpPeerConfig`).

## Conexões
- [[kubevip-arp-layer2-leader-election-gratuitous-arp-failover]] — Veja também: kube-vip: Modo ARP (Layer 2), Eleição de Líder e Failover Rápido com Gratuitous ARP.
- [[kubevip-control-plane-ipvs-load-balancing-selinux-modprobe]] — Veja também: kube-vip: Balanceamento do Control Plane com IPVS (lb_enable) e Pré-Carregamento de Módulos com SELinux.

## Fontes
- [kube-vip GitHub — README.md (Runtime Config File Precedence, Gateway API without Endpoints & SELinux IPVS Kernel Modules)](https://raw.githubusercontent.com/kube-vip/kube-vip/main/README.md) — README oficial do kube-vip/kube-vip documentando a ordem de precedência de --config-file, anotação kube-vip.io/allow-reconcile-without-endpoints e pré-carregamento de ip_vs/ip_vs_rr com SELinux; consultado em 2026-10-03.
- [kube-vip Official Documentation — Architecture (Cluster VIP, ARP Leader Election, BGP Peering, IPVS Load Balancing & Service Watcher)](https://kube-vip.io/docs/about/architecture/) — Documentação oficial de arquitetura do kube-vip explicando eleição de líder, Gratuitous ARP, BGP multi-nó, balanceamento IPVS do control plane e integração com kube-vip-cloud-provider; consultado em 2026-10-03.
- [kube-vip — Official GitHub Repository](https://github.com/kube-vip/kube-vip) — Repositório oficial Apache-2.0 do kube-vip; consultado em 2026-10-03.
