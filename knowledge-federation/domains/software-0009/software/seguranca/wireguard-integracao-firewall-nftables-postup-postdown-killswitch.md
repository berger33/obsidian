---
id: software.seguranca.tranche12.001176
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-12.md"
fontes: ["https://www.wireguard.com/protocol/", "https://www.wireguard.com/quickstart/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Segurança de Tráfego no WireGuard com **`nftables`**: Hooks **`PreUp`/`PostUp`/`PreDown`/`PostDown`**, Isolamento entre Peers e **Kill-Switch**

## Em uma frase
Apenas levantar uma interface `wg0` no servidor concentrador **não define quem pode acessar quais portas na rede interna nem impede que o Cliente A tente atacar diretamente o Cliente B dentro da sub-rede `10.100.0.0/24` da VPN**!

## Por que importa
Para aplicar **Zero Trust / Privilégio Mínimo** sobre os clientes conectados ao seu concentrador WireGuard, você combina a garantia de identidade IP do **Cryptokey Routing (`AllowedIPs /32`)** com regras de filtragem e NAT no **`nftables`** (carregadas automaticamente pelas diretivas **`PostUp`** e **`PostDown`** do `/etc/wireguard/wg0.conf` ou na configuração principal do `/etc/nftables.conf`)!

## Como funciona
Por exemplo, na chain `forward` do `nftables`, você pode: **(1)** Bloquear tráfego cliente-a-cliente (`iifname "wg0" oifname "wg0" drop`); **(2)** Permitir que os IPs do grupo de Engenharia (`@wg_eng`) acessem apenas a sub-rede de homologação na porta `443`/`22`; e **(3)** Em estações clientes que operam em modo *Full-Tunnel*, configurar um **Kill-Switch** no `PreUp`/`PostDown` que bloqueia qualquer pacote de saída que não tenha o `meta mark` (`fwmark`) do próprio WireGuard!

## Exemplo
```ini
# Exemplo de diretivas PostUp e PostDown em /etc/wireguard/wg0.conf aplicando isolamento de clientes e NAT com nftables
[Interface]
Address = 10.100.0.1/24
ListenPort = 51820
PrivateKey = <CHAVE_PRIVADA_DO_SERVIDOR>
PostUp = nft add table inet wg_filter; nft 'add chain inet wg_filter forward { type filter hook forward priority 0; policy accept; }'; nft add rule inet wg_filter forward iifname "wg0" oifname "wg0" drop
PostDown = nft delete table inet wg_filter
```

## Limites e trade-offs
Por que combinar **WireGuard + `nftables`** é tão poderoso para microsegmentação? Porque graças ao **Cryptokey Routing**, quando uma regra do `nftables` vê um pacote vindo da interface `iifname "wg0"` com `ip saddr 10.100.0.2`, o kernel já validou criptograficamente com `ChaCha20-Poly1305` e `Curve25519` que aquele pacote veio da chave privada de Alice!

## Como verificar
Nunca esqueça de habilitar o encaminhamento de pacotes no kernel (`net.ipv4.ip_forward = 1` e `net.ipv6.conf.all.forwarding = 1` em `/etc/sysctl.d/99-wireguard.conf`) quando o host WireGuard atuar como gateway/roteador.

## Conexões
- [[wireguard-operacao-cli-wg-wg-quick-iproute2-fwmark-roteamento]] — Veja também: Operação e Automação com **`wg(8)`**, **`wg-quick(8)`**, **`iproute2`** e Roteamento Baseado em Políticas (**`FwMark`** para Full-Tunnel sem Loop).
- [[wireguard-isolamento-network-namespaces-linux-containerizacao-roteamento]] — Veja também: Arquitetura Avançada no Linux — **Isolamento por Network Namespaces (`ip netns`)** com WireGuard: Roteamento Físico Separado do Túnel.
- [[wireguard-cryptokey-routing-allowedips-tabela-roteamento-peers]] — Referência cruzada direta com wireguard-cryptokey-routing-allowedips-tabela-roteamento-peers.
- [[nftables-arquitetura-firewall-kernel-linux-netfilter-tabelas-inet]] — Referência cruzada direta com nftables-arquitetura-firewall-kernel-linux-netfilter-tabelas-inet.

## Fontes
- [WireGuard Official Protocol & Cryptography Specification (`wireguard.com/protocol`)](https://www.wireguard.com/protocol/) — especificação criptográfica oficial do WireGuard detalhando as primitivas fixas (`Noise_IKpsk2_25519_ChaChaPoly_BLAKE2s`), timers de PFS, `PresharedKey` e mitigação de DoS com `mac1`/`mac2` cookies; consultado em 2026-10-03.
- [WireGuard Official Quick Start & CLI Guide (`wireguard.com/quickstart`)](https://www.wireguard.com/quickstart/) — guia oficial de operação com `ip link`, `wg(8)`, `wg-quick(8)`, geração de chaves, `PersistentKeepalive` para travessia de NAT e `dynamic_debug` no kernel Linux; consultado em 2026-10-03.
