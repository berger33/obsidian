---
id: software.seguranca.tranche12.001187
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

# Mitigação de **DDoS em Linha de Velocidade** com `nftables`: Família **`netdev` (`hook ingress`)**, Bypass de Conntrack (**`notrack`**) e **`synproxy`**

## Em uma frase
Quando um servidor Linux sofre um ataque volumétrico de **UDP Flood**, **TCP SYN Flood** com IPs falsificados (*IP Spoofing*) ou pacotes malformados (ex.: pacotes TCP com flags `SYN+FIN` ou `SYN+RST` simultâneas, ou fragmentos IPv4 anômalos), por que bloqueá-los apenas na chain `inet filter input` comum pode não ser suficiente para salvar a CPU?

## Por que importa
Porque antes de um pacote chegar ao hook `input` (`priority 0`), o kernel já alocou uma entrada na tabela de **Connection Tracking (`nf_conntrack`, `priority -200`)**! Sob milhões de pacotes por segundo com IPs de origem falsificados, a tabela `nf_conntrack` enche (`nf_conntrack: table full, dropping packet`) e derruba as conexões dos usuários reais!

## Como funciona
O `nftables` resolve isso com **três defesas de baixíssimo nível**: **(1) Família `netdev` no `hook ingress` (`priority -500`)** — atrelada diretamente ao driver da placa de rede (`device "eth0"`), descarta pacotes malformados, bogons e blocklists logo após o DMA da NIC, **antes mesmo da camada IP e muito antes do `conntrack`**!; **(2) `notrack` no `hook prerouting priority raw (-300)`** para protocolos stateless de altíssimo volume (como servidores DNS autoritativos na porta `53`); e **(3) `synproxy`** para absorver ataques TCP SYN Flood validando SYN Cookies antes de abrir conexão!

## Exemplo
```nft
# Descartar fragmentos IP, pacotes TCP invalidos (XMAS/NULL/SYN+FIN) e IPs banidos diretamente no hook ingress (netdev) antes do conntrack
table netdev ddos_shield {
    chain ingress_eth0 {
        type filter hook ingress device "eth0" priority -500; policy accept;
        ip frag-off & 0x1fff != 0 counter drop
        tcp flags & (fin|syn) == (fin|syn) counter drop
        tcp flags & (syn|rst) == (syn|rst) counter drop
        tcp flags & (fin|syn|rst|psh|ack|urg) == 0x0 counter drop
    }
}
```

## Limites e trade-offs
Processar descartes de DDoS em uma base chain **`table netdev ... hook ingress`** é dezenas de vezes mais rápido do que na chain `input` tradicional, pois o pacote é descartado na porta de entrada da pilha de rede sem alocar memória no `nf_conntrack` nem consultar a tabela de roteamento!

## Como verificar
A partir do kernel Linux 5.5+, uma única chain `netdev` suporta múltiplos dispositivos (`devices = { eth0, eth1 }`).

## Conexões
- [[nftables-nat-masquerade-dnat-snat-redirecionamento-portas]] — Veja também: Configuração de **NAT (`snat`, `masquerade`, `dnat` e `redirect`)** no `nftables` para Gateways VPN, Containers e Honeypots.
- [[nftables-aceleracao-hardware-software-flowtables-fastpath-roteadores]] — Veja também: Aceleração de Fluxos de Rede com **`flowtables` (Fastpath Software e Hardware Offload)** no `nftables` para Gateways de Alta Vazão (10GbE / 40GbE).
- [[nftables-arquitetura-firewall-kernel-linux-netfilter-tabelas-inet]] — Referência cruzada direta com nftables-arquitetura-firewall-kernel-linux-netfilter-tabelas-inet.
- [[nftables-chains-hooks-prioridades-conntrack-stateful-firewall]] — Referência cruzada direta com nftables-chains-hooks-prioridades-conntrack-stateful-firewall.

## Fontes
- [Official nftables Wiki — Quick Reference: nftables in 10 Minutes](https://wiki.nftables.org/wiki-nftables/index.php/Quick_reference-nftables_in_10_minutes) — documentação oficial do projeto Netfilter detalhando tabelas (`ip`, `ip6`, `inet`, `arp`, `bridge`, `netdev`), chains, hooks, prioridades, matches (`ct`, `meta`, `tcp`, `ip`) e scripting atômico; consultado em 2026-10-03.
- [Official nftables Wiki — Generic Set Infrastructure (Anonymous & Named Sets, Intervals, Timeouts & Auto-Merge)](https://wiki.nftables.org/wiki-nftables/index.php/Sets) — documentação oficial das estruturas de dados de alta performance de Sets (`hashtables` e `red-black trees`), `flags interval`, `timeout`, `auto-merge`, `counter` e `typeof`; consultado em 2026-10-03.
