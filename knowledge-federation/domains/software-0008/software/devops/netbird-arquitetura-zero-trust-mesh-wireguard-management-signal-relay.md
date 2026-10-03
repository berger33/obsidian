---
id: software.devops.tranche19.001871
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

# NetBird: arquitetura Zero-Trust P2P sobre Kernel WireGuard com `Client`, `Management`, `Signal` e `Relay` (Coturn)

## Em uma frase
O **NetBird** (licenciado sob BSD-3-Clause) combina uma rede overlay peer-to-peer sem configuração baseada em **Kernel WireGuard**, **Pion ICE (WebRTC)** e **Coturn** com um sistema centralizado de controle de acesso Zero-Trust, composto por quatro elementos: **Client Application**, **Management Service**, **Signal Service** e **Relay Service**.

## Por que importa
Construir uma malha WireGuard corporativa com SSO/MFA, verificações de postura de dispositivo, DNS privado e NAT traversal exige orquestrar a distribuição de chaves, negociação de candidatos ICE e regras de firewall (`nftables`/`iptables`) em dezenas de sistemas operacionais.

## Como funciona
No NetBird: 1) o **Management Service** mantém o mapa da rede, atribui IPs CGNAT (`100.64.0.0/10` e dual-stack IPv6) e distribui chaves públicas WireGuard e políticas; 2) o **Signal Service** permite que dois pares troquem candidatos de conexão (`IP:port`) com mensagens criptografadas ponta-a-ponto via NaCl `box` (`Curve25519`, `XSalsa20`, `Poly1305`) sem nunca ler o conteúdo; 3) o **Relay Service** (TURN/Coturn) atua como fallback criptografado quando o NAT simétrico impede conexão direta; e 4) o **Client** gerencia o túnel WireGuard, firewall e DNS local (onde a chave privada jamais sai da máquina).

## Exemplo
```bash
netbird up
netbird status -d
```

## Limites e trade-offs
O comando `netbird status -d` (`--detail`) exibe para cada peer conectado se a conexão atual é direta P2P (`Relayed: false`), os candidatos ICE locais/remotos selecionados, a latência e se a resistência pós-quântica (Rosenpass) está ativa.

## Como verificar
Execute `netbird status -d` em um nó registrado para auditar o estado da conexão com o Management, Signal, Relays e Peers.

## Conexões
- [[netbird-protocolo-negociacao-p2p-pion-ice-signal-nacl-box-encryption]] — Veja também: NetBird Negociação P2P: descoberta de candidatos via Pion ICE (STUN) e sinalização criptografada fim-a-fim no Signal.

## Fontes
- [NetBird GitHub — README.md (Zero-Trust Peer-to-Peer Private Network, Feature Matrix, Rosenpass PQC, Self-Hosted Quickstart & Internals)](https://raw.githubusercontent.com/netbirdio/netbird/main/README.md) — README oficial do netbirdio/netbird detalhando conectividade Kernel WireGuard, controle de acesso, rotas DNS, resistência quântica Rosenpass e self-hosting; consultado em 2026-10-03.
- [NetBird Official Documentation — How NetBird Works (Management, Client, Signal with NaCl Box E2E Encryption & TURN Relay Architecture)](https://docs.netbird.io/about-netbird/how-netbird-works) — Documentação oficial de arquitetura do NetBird explicando o funcionamento do Management, Client, Signal (Pion ICE + NaCl box) e Relay; consultado em 2026-10-03.
- [NetBird — Official GitHub Repository](https://github.com/netbirdio/netbird) — Repositório oficial BSD-3-Clause do NetBird; consultado em 2026-10-03.
