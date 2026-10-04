---
id: software.seguranca.tranche12.001175
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

# Operação e Automação com **`wg(8)`**, **`wg-quick(8)`**, **`iproute2`** e Roteamento Baseado em Políticas (**`FwMark`** para Full-Tunnel sem Loop)

## Em uma frase
Como funcionam internamente as ferramentas de espaço de usuário do WireGuard (**`wg`** e **`wg-quick`**), e como o WireGuard redireciona 100% do tráfego de internet de uma máquina (`AllowedIPs = 0.0.0.0/0, ::/0`) para dentro de `wg0` **sem que os próprios pacotes UDP criptografados do WireGuard entrem em um loop infinito tentando passar por dentro de `wg0`**?

## Por que importa
A ferramenta de baixo nível **`wg(8)`** configura exclusivamente os parâmetros criptográficos da interface no kernel via Netlink (`listen-port`, `private-key`, `fwmark`, `peer`, `allowed-ips`, `endpoint`, `persistent-keepalive`), enquanto o **`iproute2` (`ip link`, `ip addr`, `ip route`, `ip rule`)** gerencia endereços IP e rotas!

## Como funciona
Já o utilitário **`wg-quick(8)`** (`wg-quick up wg0` / `systemctl enable --now wg-quick@wg0`) automatiza tudo a partir de `/etc/wireguard/wg0.conf` e resolve o problema do *Full-Tunnel (`0.0.0.0/0`)* com uma técnica brilhante de **Policy-Based Routing (`FwMark`)**: ele configura `FwMark = 0xca6c` (`51820`) nos pacotes UDP externos gerados pelo WireGuard, adiciona a rota default `0.0.0.0/0 dev wg0` em uma tabela de roteamento dedicada (`table 51820`) e cria uma regra `ip rule add not fwmark 51820 table 51820` — garantindo que todo o tráfego das aplicações entre no túnel `wg0`, **exceto os próprios pacotes UDP já criptografados pelo WireGuard (que possuem o `fwmark 51820` e saem pela rota física normal)**!

## Exemplo
```bash
# Subir a interface wg0 via systemd/wg-quick e inspecionar as regras de Policy Routing (ip rule / FwMark) criadas automaticamente
sudo systemctl enable --now wg-quick@wg0
ip rule show
sudo wg show wg0 fwmark
```

## Limites e trade-offs
Para adicionar ou remover um novo peer em um servidor WireGuard de produção **em quente (sem derrubar a interface `wg0` e sem desconectar os outros usuários ativos!)**, use **`sudo wg set wg0 peer <PUBKEY> allowed-ips 10.100.0.50/32`** ou use **`SaveConfig = false`** com **`wg syncconf wg0 <(wg-quick strip wg0)`**!

## Como verificar
O comando **`wg syncconf`** aplica apenas o diff exato do arquivo de configuração sobre a interface ativa no kernel sem interromper nenhum túnel existente.

## Conexões
- [[wireguard-furtividade-silencio-udp-cookie-reply-mitigacao-dos]] — Veja também: Furtividade de Rede (*Stealth*) e Mitigação de **DoS (`mac1`, `mac2` e `Cookie Reply`)** no WireGuard: Por Que o WireGuard é Invisível ao Nmap.
- [[wireguard-integracao-firewall-nftables-postup-postdown-killswitch]] — Veja também: Segurança de Tráfego no WireGuard com **`nftables`**: Hooks **`PreUp`/`PostUp`/`PreDown`/`PostDown`**, Isolamento entre Peers e **Kill-Switch**.
- [[wireguard-arquitetura-protocolo-vpn-kernel-noise-ikpsk2-criptografia]] — Referência cruzada direta com wireguard-arquitetura-protocolo-vpn-kernel-noise-ikpsk2-criptografia.
- [[wireguard-cryptokey-routing-allowedips-tabela-roteamento-peers]] — Referência cruzada direta com wireguard-cryptokey-routing-allowedips-tabela-roteamento-peers.

## Fontes
- [WireGuard Official Protocol & Cryptography Specification (`wireguard.com/protocol`)](https://www.wireguard.com/protocol/) — especificação criptográfica oficial do WireGuard detalhando as primitivas fixas (`Noise_IKpsk2_25519_ChaChaPoly_BLAKE2s`), timers de PFS, `PresharedKey` e mitigação de DoS com `mac1`/`mac2` cookies; consultado em 2026-10-03.
- [WireGuard Official Quick Start & CLI Guide (`wireguard.com/quickstart`)](https://www.wireguard.com/quickstart/) — guia oficial de operação com `ip link`, `wg(8)`, `wg-quick(8)`, geração de chaves, `PersistentKeepalive` para travessia de NAT e `dynamic_debug` no kernel Linux; consultado em 2026-10-03.
