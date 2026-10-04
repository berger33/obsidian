---
id: software.seguranca.tranche12.001172
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

# O Conceito Central do WireGuard — **Cryptokey Routing (`AllowedIPs`)**: Unificando Tabela de Roteamento IP e Lista de Controle de Acesso Criptográfica

## Em uma frase
Se você entender apenas um conceito do WireGuard, entenda o **Cryptokey Routing (*Roteamento por Chave Criptográfica*)**: em uma interface WireGuard (`wg0`), cada peer remoto é identificado pela sua **Chave Pública Curve25519 (`PublicKey`)** associada a uma lista de prefixos CIDR IPv4/IPv6 chamada **`AllowedIPs`**!

## Por que importa
Essa única diretiva **`AllowedIPs`** cumpre **duas funções críticas e simétricas** no kernel: **(1) Na saída de pacotes (*Outbound Routing*)**, ela funciona como uma **tabela de roteamento interna**: quando a interface `wg0` recebe um pacote IP cujo endereço de destino (`dst_ip`) pertence ao `AllowedIPs` do Peer B, o WireGuard criptografa o pacote com a chave de sessão do Peer B e o envia para o `Endpoint` UDP do Peer B; e **(2) Na chegada de pacotes (*Inbound Source Validation / Anti-Spoofing*)**, ela funciona como um **filtro estrito de origem (*Reverse Path Forwarding criptográfico*)**: após descriptografar e autenticar um pacote vindo do Peer B, se o endereço IP de origem interno (`src_ip`) daquele pacote **NÃO pertencer ao `AllowedIPs` configurado para o Peer B**, o kernel descarta o pacote imediatamente!

## Como funciona
Isso significa que é **matematicamente impossível** para o Peer B (`AllowedIPs = 10.100.0.2/32`) falsificar pacotes em nome do Peer C (`10.100.0.3/32`), pois cada endereço IP dentro da VPN está criptograficamente amarrado à chave pública do seu dono!

## Exemplo
```ini
# Exemplo de configuracao /etc/wireguard/wg0.conf em um servidor concentrador (Hub) com Cryptokey Routing estrito (/32 por cliente)
[Interface]
Address = 10.100.0.1/24
ListenPort = 51820
PrivateKey = <CHAVE_PRIVADA_DO_SERVIDOR>

[Peer]
# Estacao do Engenheiro Alice - so pode enviar/receber pacotes com IP 10.100.0.2
PublicKey = <CHAVE_PUBLICA_ALICE>
PresharedKey = <PSK_ALICE>
AllowedIPs = 10.100.0.2/32

[Peer]
# Gateway da Filial Sao Paulo - autorizado a rotear a sub-rede 10.200.10.0/24
PublicKey = <CHAVE_PUBLICA_GATEWAY_SP>
PresharedKey = <PSK_GATEWAY_SP>
AllowedIPs = 10.100.0.3/32, 10.200.10.0/24
```

## Limites e trade-offs
Regra de ouro ao configurar `AllowedIPs`: **no servidor concentrador (Hub)**, cada cliente road-warrior deve ter `AllowedIPs = 10.100.0.X/32` (apenas o seu próprio IP `/32`!); já **na máquina do cliente**, se você quiser que apenas o tráfego da rede interna passe pela VPN (*Split Tunnel*), configure `AllowedIPs = 10.100.0.0/24, 10.200.0.0/16`; se quiser que **todo o tráfego de internet** passe pela VPN (*Full Tunnel*), configure `AllowedIPs = 0.0.0.0/0, ::/0` no bloco `[Peer]` do servidor!

## Como verificar
Dois peers diferentes na mesma interface `wg0` **nunca podem ter prefixos idênticos em `AllowedIPs`** (pois a árvore de busca *radix trie* do Cryptokey Routing associa cada prefixo a um único peer).

## Conexões
- [[wireguard-arquitetura-protocolo-vpn-kernel-noise-ikpsk2-criptografia]] — Veja também: Arquitetura do **WireGuard**: VPN Criptográfica no Kernel Linux, Handshake **`Noise_IKpsk2`** e Primitivas Fixas (**ChaCha20-Poly1305, Curve25519, BLAKE2s**).
- [[wireguard-handshake-1rtt-pfs-rekeying-timers-presharedkey-pos-quantico]] — Veja também: Handshake **1-RTT (`Noise_IKpsk2`)**, **Perfect Forward Secrecy (PFS)**, Rotação Automática de Chaves a Cada 2 Minutos e **`PresharedKey` Pós-Quântica**.
- [[wireguard-operacao-cli-wg-wg-quick-iproute2-fwmark-roteamento]] — Referência cruzada direta com wireguard-operacao-cli-wg-wg-quick-iproute2-fwmark-roteamento.
- [[nftables-arquitetura-firewall-kernel-linux-netfilter-tabelas-inet]] — Referência cruzada direta com nftables-arquitetura-firewall-kernel-linux-netfilter-tabelas-inet.

## Fontes
- [WireGuard Official Protocol & Cryptography Specification (`wireguard.com/protocol`)](https://www.wireguard.com/protocol/) — especificação criptográfica oficial do WireGuard detalhando as primitivas fixas (`Noise_IKpsk2_25519_ChaChaPoly_BLAKE2s`), timers de PFS, `PresharedKey` e mitigação de DoS com `mac1`/`mac2` cookies; consultado em 2026-10-03.
- [WireGuard Official Quick Start & CLI Guide (`wireguard.com/quickstart`)](https://www.wireguard.com/quickstart/) — guia oficial de operação com `ip link`, `wg(8)`, `wg-quick(8)`, geração de chaves, `PersistentKeepalive` para travessia de NAT e `dynamic_debug` no kernel Linux; consultado em 2026-10-03.
