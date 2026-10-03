---
id: software.devops.tranche19.001876
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
fontes: ["https://docs.netbird.io/about-netbird/how-netbird-works", "https://raw.githubusercontent.com/netbirdio/netbird/main/README.md", "https://github.com/netbirdio/netbird"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# NetBird Private DNS: resolução de FQDNs de peers, `Custom DNS Zones` e compartilhamento de porta DNS com XDP/eBPF

## Em uma frase
O cliente NetBird executa um **resolvedor DNS embutido** em cada máquina que resolve os FQDNs automáticos dos pares da rede (ex.: `<peer>.netbird.cloud` ou domínio customizado), **Custom DNS Zones** e servidores upstream por grupo de distribuição, utilizando inclusive técnicas de **XDP/eBPF** no Linux para compartilhar a porta DNS padrão com resolvedores locais.

## Por que importa
Conflitos pela porta UDP `53` com `systemd-resolved`, `dnsmasq` ou `NetworkManager` são uma das maiores fontes de dor de cabeça em clientes VPN para Linux.

## Como funciona
No NetBird, o resolvedor local responde pelos registros `A`/`AAAA` dos peers autorizados e encaminha consultas de *Match Domains* corporativos (como `corp.internal`) para os nameservers privados acessíveis através da malha NetBird.

## Exemplo
```bash
# Verificando a configuração de DNS aplicada pelo agente NetBird:
netbird status --detail | grep -A 10 "DNS"
```

## Limites e trade-offs
Ao configurar *Nameserver Groups* no NetBird, é possível associar servidores DNS internos específicos apenas a determinados grupos de distribuição (ex.: apenas máquinas do grupo `engineering` recebem o DNS da zona `.dev.internal`).

## Como verificar
Execute `dig <peer-name>.netbird.cloud` (ou seu domínio customizado) a partir de um peer conectado e verifique o retorno do IP `100.64.x.y`.

## Conexões
- [[netbird-network-routes-domain-routes-exit-nodes-ha-routing-peers]] — Veja também: NetBird Network Routes e Exit Nodes: roteamento para sub-redes privadas (CIDR), rotas por domínio DNS e grupos de alta disponibilidade.
- [[netbird-rosenpass-post-quantum-cryptography-wireguard-preshared-keys]] — Veja também: NetBird com Rosenpass (`--enable-rosenpass`): resistência pós-quântica (PQC) para túneis WireGuard.

## Fontes
- [NetBird GitHub — README.md (Zero-Trust Peer-to-Peer Private Network, Feature Matrix, Rosenpass PQC, Self-Hosted Quickstart & Internals)](https://docs.netbird.io/about-netbird/how-netbird-works) — README oficial do netbirdio/netbird detalhando conectividade Kernel WireGuard, controle de acesso, rotas DNS, resistência quântica Rosenpass e self-hosting; consultado em 2026-10-03.
- [NetBird Official Documentation — How NetBird Works (Management, Client, Signal with NaCl Box E2E Encryption & TURN Relay Architecture)](https://raw.githubusercontent.com/netbirdio/netbird/main/README.md) — Documentação oficial de arquitetura do NetBird explicando o funcionamento do Management, Client, Signal (Pion ICE + NaCl box) e Relay; consultado em 2026-10-03.
- [NetBird — Official GitHub Repository](https://github.com/netbirdio/netbird) — Repositório oficial BSD-3-Clause do NetBird; consultado em 2026-10-03.
