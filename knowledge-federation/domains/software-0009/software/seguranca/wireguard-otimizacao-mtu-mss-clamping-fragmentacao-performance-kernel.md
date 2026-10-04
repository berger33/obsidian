---
id: software.seguranca.tranche12.001178
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

# Diagnóstico de Rede e Otimização de **MTU (`1420` Bytes) e TCP MSS Clamping** em Túneis WireGuard IPv4/IPv6

## Em uma frase
Um problema clássico em qualquer túnel VPN que deixa administradores intrigados é quando **`ping 10.200.1.10` e conexões SSH curtas funcionam perfeitamente pelo túnel WireGuard, mas páginas HTTPS, chamadas de API grandes ou comandos `git clone` travam misteriosamente no meio do handshake TLS**!

## Por que importa
A causa raiz quase sempre é **Path MTU Discovery Blackhole (PMTUD) / Fragmentação de Pacotes**: em uma rede Ethernet padrão com MTU de `1500` bytes, o encapsulamento do WireGuard adiciona **60 bytes de cabeçalho no IPv4** (`20` bytes IPv4 + `8` bytes UDP + `4` bytes tipo/reserved + `4` bytes key index + `8` bytes nonce + `16` bytes Poly1305 authentication tag) ou **80 bytes de cabeçalho no IPv6** (`40` bytes IPv6 + `40` bytes WireGuard/UDP), resultando no **MTU padrão do `wg-quick` de `1420` bytes** (`1500 - 80`)!

## Como funciona
Se o link subjacente do cliente (ex.: PPPoE `1492`, 4G/5G LTE `1400`, ou uma VPC de nuvem com encapsulamento GENEVE/VXLAN) tiver um MTU menor que `1500` ou bloquear pacotes ICMP `Fragmentation Needed`, pacotes TCP grandes são descartados no caminho! A solução definitiva é dupla: ajustar `MTU = 1380` (ou `1280` em links móveis problemáticos) no `wg0.conf` e ativar **TCP MSS Clamping (`maxseg size set rt mtu`)** no `nftables` do gateway!

## Exemplo
```nft
# Regra de TCP MSS Clamping no nftables do gateway WireGuard para ajustar automaticamente o MSS do handshake TCP SYN ao MTU da rota
table inet wg_mss {
    chain forward {
        type filter hook forward priority mangle; policy accept;
        tcp flags syn tcp option maxseg size set rt mtu
    }
}
```

## Limites e trade-offs
A única linha **`tcp flags syn tcp option maxseg size set rt mtu`** no `nftables` inspeciona os pacotes `TCP SYN` que atravessam o gateway WireGuard e reduz automaticamente o campo `Maximum Segment Size (MSS)` para caber com folga dentro do MTU da interface de saída, eliminando 100% dos travamentos de conexões TLS e SSH sobre VPN!

## Como verificar
Use `ping -M do -s 1392 <ip_interno_vpn>` no Linux para testar empiricamente o maior payload sem fragmentação suportado pelo caminho do seu túnel.

## Conexões
- [[wireguard-isolamento-network-namespaces-linux-containerizacao-roteamento]] — Veja também: Arquitetura Avançada no Linux — **Isolamento por Network Namespaces (`ip netns`)** com WireGuard: Roteamento Físico Separado do Túnel.
- [[wireguard-monitoramento-auditoria-healthcheck-rotacao-chaves-gerencia]] — Veja também: Monitoramento Operacional, **Dynamic Debugging** no Kernel e Gestão de Ciclo de Vida de Chaves WireGuard em Ambientes Corporativos.
- [[wireguard-operacao-cli-wg-wg-quick-iproute2-fwmark-roteamento]] — Referência cruzada direta com wireguard-operacao-cli-wg-wg-quick-iproute2-fwmark-roteamento.
- [[wireguard-integracao-firewall-nftables-postup-postdown-killswitch]] — Referência cruzada direta com wireguard-integracao-firewall-nftables-postup-postdown-killswitch.
- [[nftables-chains-hooks-prioridades-conntrack-stateful-firewall]] — Referência cruzada direta com nftables-chains-hooks-prioridades-conntrack-stateful-firewall.

## Fontes
- [WireGuard Official Protocol & Cryptography Specification (`wireguard.com/protocol`)](https://www.wireguard.com/protocol/) — especificação criptográfica oficial do WireGuard detalhando as primitivas fixas (`Noise_IKpsk2_25519_ChaChaPoly_BLAKE2s`), timers de PFS, `PresharedKey` e mitigação de DoS com `mac1`/`mac2` cookies; consultado em 2026-10-03.
- [WireGuard Official Quick Start & CLI Guide (`wireguard.com/quickstart`)](https://www.wireguard.com/quickstart/) — guia oficial de operação com `ip link`, `wg(8)`, `wg-quick(8)`, geração de chaves, `PersistentKeepalive` para travessia de NAT e `dynamic_debug` no kernel Linux; consultado em 2026-10-03.
