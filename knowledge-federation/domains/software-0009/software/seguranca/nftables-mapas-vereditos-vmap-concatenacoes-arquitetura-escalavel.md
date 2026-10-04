---
id: software.seguranca.tranche12.001184
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

# Mapas de Veredito (**`vmap`**) e **Concatenações de Seletores (`.` Tuplas)** no `nftables`: Substituindo Centenas de Regras Lineares por Uma Única Busca em Hash

## Em uma frase
Como um engenheiro de segurança sênior projeta um firewall `nftables` em um gateway corporativo que precisa aplicar políticas diferentes para dezenas de interfaces VLAN, protocolos e portas, mantendo o tempo de inspeção de pacotes constante ($O(1)$)? Usando **Verdict Maps (`vmap`)** combinados com **Concatenações (operador `.`)**!

## Por que importa
Um **Verdict Map (`vmap`)** mapeia uma chave (ex.: protocolo de camada 4, interface de entrada, estado `ct state` ou porta) diretamente para uma ação/veredito (`accept`, `drop`, `jump chain_web`, `goto chain_dmz`): em vez de o kernel avaliar 20 regras `if/else` sequenciais, ele faz **uma única busca em tabela hash** e salta diretamente para a chain de destino!

## Como funciona
Melhor ainda: o operador de **Concatenação (`.`)** do `nftables` permite combinar múltiplos campos de cabeçalho em uma única tupla de busca (por exemplo, **`ip saddr . meta l4proto . th dport`** — IP de origem + Protocolo TCP/UDP + Porta de Destino)! Com uma única regra e um único set concatenado, você expressa uma matriz inteira de controle de acesso (ACL) de microsegmentação!

## Exemplo
```nft
# Usar Concatenacao (ip saddr . meta l4proto . th dport) e Verdict Map (vmap) para microsegmentacao em O(1)
table inet microseg {
    set matriz_acesso {
        typeof ip saddr . meta l4proto . th dport
        elements = {
            10.20.1.10 . tcp . 5432,
            10.20.1.11 . tcp . 6379,
            10.20.2.50 . udp . 53
        }
    }

    chain forward {
        type filter hook forward priority 0; policy drop;
        ct state established,related accept
        ct state invalid drop
        ip saddr . meta l4proto . th dport @matriz_acesso accept
    }
}
```

## Limites e trade-offs
Observe a expressão **`meta l4proto . th dport`**: o seletor de cabeçalho de transporte genérico **`th dport`** (*Transport Header destination port*) lê os primeiros bytes da porta de destino tanto para **TCP** quanto para **UDP** (e SCTP/UDPLite) na mesma estrutura!

## Como verificar
Sempre que precisar adicionar uma nova permissão temporária ou permanente na matriz de microsegmentação acima, você nem precisa editar as regras da chain `forward`: basta adicionar a tupla no set `@matriz_acesso` com `nft add element`!

## Conexões
- [[nftables-conjuntos-sets-anonimos-nomeados-intervalos-timeouts-dinamicos]] — Veja também: Conjuntos de Alta Performance (**Sets Anônimos e Nomeados**) no `nftables`: Intervalos CIDR (`flags interval`), `auto-merge`, `timeout` e Blocklists em $O(1)$.
- [[nftables-rate-limiting-meters-dynamic-sets-anti-bruteforce-ssh]] — Veja também: Proteção Anti-Brute-Force e **Rate Limiting Dinâmico por IP (`flags dynamic, timeout` / `ct count`)** Nativamente no `nftables`.
- [[nftables-arquitetura-firewall-kernel-linux-netfilter-tabelas-inet]] — Referência cruzada direta com nftables-arquitetura-firewall-kernel-linux-netfilter-tabelas-inet.
- [[wireguard-integracao-firewall-nftables-postup-postdown-killswitch]] — Referência cruzada direta com wireguard-integracao-firewall-nftables-postup-postdown-killswitch.

## Fontes
- [Official nftables Wiki — Quick Reference: nftables in 10 Minutes](https://wiki.nftables.org/wiki-nftables/index.php/Quick_reference-nftables_in_10_minutes) — documentação oficial do projeto Netfilter detalhando tabelas (`ip`, `ip6`, `inet`, `arp`, `bridge`, `netdev`), chains, hooks, prioridades, matches (`ct`, `meta`, `tcp`, `ip`) e scripting atômico; consultado em 2026-10-03.
- [Official nftables Wiki — Generic Set Infrastructure (Anonymous & Named Sets, Intervals, Timeouts & Auto-Merge)](https://wiki.nftables.org/wiki-nftables/index.php/Sets) — documentação oficial das estruturas de dados de alta performance de Sets (`hashtables` e `red-black trees`), `flags interval`, `timeout`, `auto-merge`, `counter` e `typeof`; consultado em 2026-10-03.
