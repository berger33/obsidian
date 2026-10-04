---
id: software.seguranca.tranche12.001177
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

# Arquitetura Avançada no Linux — **Isolamento por Network Namespaces (`ip netns`)** com WireGuard: Roteamento Físico Separado do Túnel

## Em uma frase
O módulo do **WireGuard no Kernel Linux** possui uma propriedade arquitetural única e extraordinária para segurança e engenharia de redes: **quando você cria a interface `wg0` no namespace de rede raiz (`init_net` — onde fica sua placa física `eth0`/`wlan0`) e depois move a interface `wg0` para dentro de um Network Namespace isolado (`ip link set wg0 netns seguro`) ou container, a interface `wg0` lembra que o seu socket UDP criptografado pertence ao namespace físico original**!

## Por que importa
O que isso significa na prática? Significa que dentro do namespace `seguro` (ou dentro de um container de aplicação sensível), **a única interface de rede existente é `wg0` (e `lo`)**!

## Como funciona
Mesmo que um processo dentro do namespace `seguro` seja totalmente comprometido por um invasor com `root` naquele namespace, **é fisicamente impossível para o processo vazar um único pacote fora da VPN (*Zero-Leak Guarantee*)** ou descobrir o endereço IP real da placa física `eth0` do host — porque a placa `eth0` nem sequer existe dentro daquele Network Namespace, enquanto o kernel envia os pacotes UDP já criptografados do `wg0` pela `eth0` do namespace pai!

## Exemplo
```bash
# Criar um Network Namespace isolado ('cofre') onde a UNICA rota fisica possivel para qualquer processo e o tunel criptografado wg0
sudo ip netns add cofre
sudo ip link add wg0 type wireguard
sudo wg setconf wg0 /etc/wireguard/wg0-raw.conf
sudo ip link set wg0 netns cofre
sudo ip -n cofre addr add 10.100.0.99/24 dev wg0
sudo ip -n cofre link set lo up
sudo ip -n cofre link set wg0 up
sudo ip -n cofre route add default dev wg0
```

## Limites e trade-offs
Você também pode fazer a operação inversa (chamada de *Physical Interface in Container Namespace*): mover a placa física `eth0` e o `wlan0` para dentro de um namespace `fisico` isolado, e deixar no namespace principal do sistema apenas a interface `wg0` — garantindo que todo o sistema operacional principal só enxergue a rede através do túnel WireGuard!

## Como verificar
Para executar qualquer comando ou serviço dentro do namespace isolado criado acima, basta usar `sudo ip netns exec cofre <comando>` (ou `NetworkNamespacePath=/run/netns/cofre` em uma unit do `systemd`).

## Conexões
- [[wireguard-integracao-firewall-nftables-postup-postdown-killswitch]] — Veja também: Segurança de Tráfego no WireGuard com **`nftables`**: Hooks **`PreUp`/`PostUp`/`PreDown`/`PostDown`**, Isolamento entre Peers e **Kill-Switch**.
- [[wireguard-otimizacao-mtu-mss-clamping-fragmentacao-performance-kernel]] — Veja também: Diagnóstico de Rede e Otimização de **MTU (`1420` Bytes) e TCP MSS Clamping** em Túneis WireGuard IPv4/IPv6.
- [[wireguard-arquitetura-protocolo-vpn-kernel-noise-ikpsk2-criptografia]] — Referência cruzada direta com wireguard-arquitetura-protocolo-vpn-kernel-noise-ikpsk2-criptografia.
- [[wireguard-operacao-cli-wg-wg-quick-iproute2-fwmark-roteamento]] — Referência cruzada direta com wireguard-operacao-cli-wg-wg-quick-iproute2-fwmark-roteamento.

## Fontes
- [WireGuard Official Protocol & Cryptography Specification (`wireguard.com/protocol`)](https://www.wireguard.com/protocol/) — especificação criptográfica oficial do WireGuard detalhando as primitivas fixas (`Noise_IKpsk2_25519_ChaChaPoly_BLAKE2s`), timers de PFS, `PresharedKey` e mitigação de DoS com `mac1`/`mac2` cookies; consultado em 2026-10-03.
- [WireGuard Official Quick Start & CLI Guide (`wireguard.com/quickstart`)](https://www.wireguard.com/quickstart/) — guia oficial de operação com `ip link`, `wg(8)`, `wg-quick(8)`, geração de chaves, `PersistentKeepalive` para travessia de NAT e `dynamic_debug` no kernel Linux; consultado em 2026-10-03.
