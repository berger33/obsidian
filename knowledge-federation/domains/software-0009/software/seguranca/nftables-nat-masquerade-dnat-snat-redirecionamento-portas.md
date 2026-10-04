---
id: software.seguranca.tranche12.001186
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
fontes: ["https://wiki.nftables.org/wiki-nftables/index.php/Quick_reference-nftables_in_10_minutes", "https://wiki.nftables.org/wiki-nftables/index.php/Sets"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Configuração de **NAT (`snat`, `masquerade`, `dnat` e `redirect`)** no `nftables` para Gateways VPN, Containers e Honeypots

## Em uma frase
Como configurar tradução de endereços de rede (**Source NAT / Masquerade** para saída de sub-redes WireGuard/Containers e **Destination NAT / Port Redirect** para publicação de serviços ou redirecionamento de portas de honeypots como o Cowrie) usando a família `inet` (suportada para NAT desde o kernel Linux 5.2+ e `nftables` 0.9.1+)?

## Por que importa
No `nftables`, as operações de NAT ocorrem em base chains do **`type nat`**: **(1) `hook prerouting priority dstnat`** (avaliado quando o primeiro pacote da conexão chega, usado para **`dnat to <ip>:<porta>`** que encaminha para outro host ou **`redirect to :<porta>`** que redireciona para uma porta local da própria máquina); e **(2) `hook postrouting priority srcnat`** (avaliado quando o pacote está saindo pela interface externa, usado para **`snat to <ip_fixo>`** quando o gateway tem IP público estático ou **`masquerade`** quando o IP da interface de saída é dinâmico)!

## Como funciona
Como o subsistema de NAT depende do `conntrack`, apenas o primeiro pacote (`ct state new`) atravessa a chain `type nat` — todos os pacotes subsequentes daquela sessão são traduzidos automaticamente em alta velocidade pela tabela de estado do `nf_conntrack`!

## Exemplo
```nft
# Configuracao de NAT Dual-Stack na familia inet: Redirect local (22->2222) no prerouting e Masquerade da VPN wg0 no postrouting
table inet nat {
    chain prerouting {
        type nat hook prerouting priority dstnat; policy accept;
        iifname "eth0" tcp dport 22 redirect to :2222
    }

    chain postrouting {
        type nat hook postrouting priority srcnat; policy accept;
        iifname "wg0" oifname "eth0" masquerade
    }
}
```

## Limites e trade-offs
Lembre-se de um detalhe importante da chain `filter forward` ao usar **`dnat to <ip_interno>`**: quando o pacote chega na chain `forward`, o `prerouting` já ocorreu, portanto o endereço de destino do pacote (`ip daddr`) já é o IP interno traduzido; você também pode liberar de forma elegante todos os pacotes que sofreram DNAT legítimo usando a condição **`ct status dnat accept`** na chain `forward`!

## Como verificar
Se o seu gateway de borda possui um endereço IPv4 público estático fixo, prefira **`snat ip to <IP_PUBLICO>`** em vez de `masquerade`, pois o `snat` é computacionalmente mais leve e não precisa consultar o endereço da interface a cada evento de link.

## Conexões
- [[nftables-rate-limiting-meters-dynamic-sets-anti-bruteforce-ssh]] — Veja também: Proteção Anti-Brute-Force e **Rate Limiting Dinâmico por IP (`flags dynamic, timeout` / `ct count`)** Nativamente no `nftables`.
- [[nftables-protecao-ddos-familia-netdev-ingress-synproxy-raw-notrack]] — Veja também: Mitigação de **DDoS em Linha de Velocidade** com `nftables`: Família **`netdev` (`hook ingress`)**, Bypass de Conntrack (**`notrack`**) e **`synproxy`**.
- [[nftables-arquitetura-firewall-kernel-linux-netfilter-tabelas-inet]] — Referência cruzada direta com nftables-arquitetura-firewall-kernel-linux-netfilter-tabelas-inet.
- [[nftables-chains-hooks-prioridades-conntrack-stateful-firewall]] — Referência cruzada direta com nftables-chains-hooks-prioridades-conntrack-stateful-firewall.
- [[cowrie-isolamento-seguranca-redirecionamento-portas-nftables-docker]] — Referência cruzada direta com cowrie-isolamento-seguranca-redirecionamento-portas-nftables-docker.

## Fontes
- [Official nftables Wiki — Quick Reference: nftables in 10 Minutes](https://wiki.nftables.org/wiki-nftables/index.php/Quick_reference-nftables_in_10_minutes) — documentação oficial do projeto Netfilter detalhando tabelas (`ip`, `ip6`, `inet`, `arp`, `bridge`, `netdev`), chains, hooks, prioridades, matches (`ct`, `meta`, `tcp`, `ip`) e scripting atômico; consultado em 2026-10-03.
- [Official nftables Wiki — Generic Set Infrastructure (Anonymous & Named Sets, Intervals, Timeouts & Auto-Merge)](https://wiki.nftables.org/wiki-nftables/index.php/Sets) — documentação oficial das estruturas de dados de alta performance de Sets (`hashtables` e `red-black trees`), `flags interval`, `timeout`, `auto-merge`, `counter` e `typeof`; consultado em 2026-10-03.
