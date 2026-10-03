---
id: software.devops.tranche19.001872
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

# NetBird Negociação P2P: descoberta de candidatos via Pion ICE (STUN) e sinalização criptografada fim-a-fim no Signal

## Em uma frase
Para estabelecer túneis WireGuard ponto-a-ponto diretos através de firewalls e NATs sem expor metadados de endereços internos em texto claro no servidor de sinalização, o cliente NetBird combina a biblioteca **Pion ICE (WebRTC)** com criptografia ponta-a-ponto **NaCl `box`** sobre o **Signal Service**.

## Por que importa
Se o servidor de sinalização visse em texto claro todos os endereços IP privados e portas locais de cada máquina durante a negociação ICE, um comprometimento do servidor Signal vazaria a topologia interna das sub-redes dos clientes.

## Como funciona
Conforme detalhado na documentação oficial de arquitetura do NetBird: cada cliente descobre seus candidatos de conexão (`IP:port` via STUN) e os envia ao par remoto através do Signal; porém, o corpo da mensagem é criptografado ponta-a-ponto com uma chave compartilhada derivada da chave privada local e da chave pública do par remoto (NaCl `box`: `Curve25519`, `XSalsa20`, `Poly1305`). O Signal vê apenas as duas chaves públicas para rotear a mensagem e sai de cena assim que o túnel WireGuard direto é estabelecido.

## Exemplo
```bash
# Verificando o tipo de conexão (P2P direto vs Relay) e o par de candidatos ICE:
netbird status --detail | grep -E "Peer|Connection type|ICE candidate"
```

## Limites e trade-offs
Quando o firewall de ambos os lados bloqueia UDP direto (ex.: NAT simétrico estrito nos dois lados), o Pion ICE seleciona automaticamente o candidato do **Relay Service** (TURN), mantendo o tráfego inteiramente criptografado pelo WireGuard dentro do túnel.

## Como verificar
Inspecione os candidatos ICE local e remoto negociados em uma sessão ativa com `netbird status --detail`.

## Conexões
- [[netbird-arquitetura-zero-trust-mesh-wireguard-management-signal-relay]] — Veja também: NetBird: arquitetura Zero-Trust P2P sobre Kernel WireGuard com `Client`, `Management`, `Signal` e `Relay` (Coturn).
- [[netbird-setup-keys-provisionamento-automatizado-servidores-containers-ephemeral]] — Veja também: NetBird `Setup Keys`: registro automatizado de servidores, containers e nós efêmeros em massa.

## Fontes
- [NetBird GitHub — README.md (Zero-Trust Peer-to-Peer Private Network, Feature Matrix, Rosenpass PQC, Self-Hosted Quickstart & Internals)](https://docs.netbird.io/about-netbird/how-netbird-works) — README oficial do netbirdio/netbird detalhando conectividade Kernel WireGuard, controle de acesso, rotas DNS, resistência quântica Rosenpass e self-hosting; consultado em 2026-10-03.
- [NetBird Official Documentation — How NetBird Works (Management, Client, Signal with NaCl Box E2E Encryption & TURN Relay Architecture)](https://raw.githubusercontent.com/netbirdio/netbird/main/README.md) — Documentação oficial de arquitetura do NetBird explicando o funcionamento do Management, Client, Signal (Pion ICE + NaCl box) e Relay; consultado em 2026-10-03.
- [NetBird — Official GitHub Repository](https://github.com/netbirdio/netbird) — Repositório oficial BSD-3-Clause do NetBird; consultado em 2026-10-03.
