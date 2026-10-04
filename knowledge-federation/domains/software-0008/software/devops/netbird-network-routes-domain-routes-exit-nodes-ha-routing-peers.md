---
id: software.devops.tranche19.001875
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-19.md"
fontes: ["https://raw.githubusercontent.com/netbirdio/netbird/main/README.md", "https://docs.netbird.io/about-netbird/how-netbird-works", "https://github.com/netbirdio/netbird"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# NetBird Network Routes e Exit Nodes: roteamento para sub-redes privadas (CIDR), rotas por domínio DNS e grupos de alta disponibilidade

## Em uma frase
O recurso **Network Routes** do NetBird permite que **Routing Peers** anunciem sub-redes privadas inteiras (CIDR como `10.100.0.0/16`), **rotas baseadas em domínios DNS** (ex.: `*.internal.rds.amazonaws.com` resolvidos dinamicamente) ou atuem como **Exit Nodes** (`0.0.0.0/0`), sem exigir instalar o cliente NetBird em cada recurso de destino.

## Por que importa
Em nuvens públicas onde bancos gerenciados (RDS, Cloud SQL) ou endpoints privados de SaaS mudam de IP ou não aceitam agentes, rotas baseadas em CIDR e em domínios DNS permitem rotear apenas o tráfego necessário pelo túnel.

## Como funciona
Ao configurar a mesma `Network Route` com um **Peer Group** contendo múltiplos *Routing Peers* (em vez de um único peer isolado), o NetBird distribui e faz failover automático da rota em alta disponibilidade entre os roteadores saudáveis.

## Exemplo
```bash
# Listando as rotas de rede recebidas e selecionadas pelo cliente local:
netbird routes list
```

## Limites e trade-offs
A CLI `netbird routes list` (e `netbird routes select` / `deselect`) permite ao usuário inspecionar quais rotas remotas e Exit Nodes estão ativos no seu cliente.

## Como verificar
Execute `netbird routes list` em um peer cliente para verificar as rotas CIDR e de domínio propagadas pelo Management Service.

## Conexões
- [[netbird-controle-acesso-groups-policies-nftables-posture-checks]] — Veja também: NetBird Access Control e Posture Checks: políticas baseadas em grupos aplicadas via `nftables` e verificação de postura.
- [[netbird-private-dns-custom-zones-ebpf-xdp-port-sharing]] — Veja também: NetBird Private DNS: resolução de FQDNs de peers, `Custom DNS Zones` e compartilhamento de porta DNS com XDP/eBPF.

## Fontes
- [NetBird GitHub — README.md (Zero-Trust Peer-to-Peer Private Network, Feature Matrix, Rosenpass PQC, Self-Hosted Quickstart & Internals)](https://raw.githubusercontent.com/netbirdio/netbird/main/README.md) — README oficial do netbirdio/netbird detalhando conectividade Kernel WireGuard, controle de acesso, rotas DNS, resistência quântica Rosenpass e self-hosting; consultado em 2026-10-03.
- [NetBird Official Documentation — How NetBird Works (Management, Client, Signal with NaCl Box E2E Encryption & TURN Relay Architecture)](https://docs.netbird.io/about-netbird/how-netbird-works) — Documentação oficial de arquitetura do NetBird explicando o funcionamento do Management, Client, Signal (Pion ICE + NaCl box) e Relay; consultado em 2026-10-03.
- [NetBird — Official GitHub Repository](https://github.com/netbirdio/netbird) — Repositório oficial BSD-3-Clause do NetBird; consultado em 2026-10-03.
