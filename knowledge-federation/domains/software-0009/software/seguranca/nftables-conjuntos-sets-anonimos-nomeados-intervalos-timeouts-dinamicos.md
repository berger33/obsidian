---
id: software.seguranca.tranche12.001183
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

# Conjuntos de Alta Performance (**Sets Anônimos e Nomeados**) no `nftables`: Intervalos CIDR (`flags interval`), `auto-merge`, `timeout` e Blocklists em $O(1)$

## Em uma frase
No antigo `iptables`, se você quisesse bloquear uma lista de 50.000 endereços IP maliciosos de Threat Intelligence sem instalar a extensão externa `ipset`, adicionar 50.000 regras `-A INPUT -s <IP> -j DROP` derrubava a performance de rede do servidor. No **`nftables`**, o subsistema de **Sets (Conjuntos)** é nativo do próprio bytecode e usa **hashtables e árvores rubro-negras (*red-black trees*)** no kernel!

## Por que importa
O `nftables` oferece **Sets Anônimos** (declarados inline entre chaves `{ 22, 80, 443 }`, imutáveis e atrelados à regra) e **Sets Nomeados (`set <nome> { ... }`)**, referenciados nas regras com **`@<nome>`** e atualizáveis em tempo real sem tocar nas regras!

## Como funciona
Ao criar um Set Nomeado para blocklists ou allowlists de redes, você pode habilitar: **`type ipv4_addr`** (ou `typeof ip saddr`), **`flags interval`** (para suportar blocos CIDR como `10.0.0.0/8` e faixas `192.168.1.1-192.168.1.50`), **`auto-merge`** (que funde automaticamente IPs e sub-redes adjacentes/sobrepostas sem dar erro de conflito!), **`flags timeout`** (para que cada IP bloqueado expire sozinho após ex.: `24h`!) e **`counter`** (contador individual de pacotes/bytes por IP dentro do set!)!

## Exemplo
```nft
# Definicao de um Set Nomeado com suporte a CIDR (interval), auto-merge, timeout automatico e contadores por elemento
table inet filter {
    set threat_blocklist_v4 {
        type ipv4_addr
        flags interval, timeout
        auto-merge
        timeout 24h
        counter
        elements = { 198.51.100.0/24, 203.0.113.45 timeout 1h }
    }

    chain input {
        type filter hook input priority -10; policy accept;
        ip saddr @threat_blocklist_v4 drop
    }
}
```

## Limites e trade-offs
Com o set nomeado ativo, adicionar ou remover um endereço IP em tempo real a partir de um script de resposta a incidentes (ou do **CrowdSec** / **Fail2ban**) leva microssegundos: **`sudo nft add element inet filter threat_blocklist_v4 { 192.0.2.99 timeout 6h }`** — e para consultar se um IP específico pertence a um intervalo CIDR dentro do set, basta rodar **`sudo nft get element inet filter threat_blocklist_v4 { 198.51.100.77 }`**!

## Como verificar
O comando `nft get element` é um recurso fantástico de diagnóstico para descobrir qual bloco CIDR dentro de um set de milhares de linhas está casando com um determinado IP.

## Conexões
- [[nftables-chains-hooks-prioridades-conntrack-stateful-firewall]] — Veja também: Anatomia de **Chains, Hooks (`prerouting`, `input`, `forward`, `output`, `postrouting`, `ingress`), Prioridades** e **Connection Tracking (`ct state`)** no `nftables`.
- [[nftables-mapas-vereditos-vmap-concatenacoes-arquitetura-escalavel]] — Veja também: Mapas de Veredito (**`vmap`**) e **Concatenações de Seletores (`.` Tuplas)** no `nftables`: Substituindo Centenas de Regras Lineares por Uma Única Busca em Hash.
- [[nftables-arquitetura-firewall-kernel-linux-netfilter-tabelas-inet]] — Referência cruzada direta com nftables-arquitetura-firewall-kernel-linux-netfilter-tabelas-inet.
- [[nftables-rate-limiting-meters-dynamic-sets-anti-bruteforce-ssh]] — Referência cruzada direta com nftables-rate-limiting-meters-dynamic-sets-anti-bruteforce-ssh.

## Fontes
- [Official nftables Wiki — Quick Reference: nftables in 10 Minutes](https://wiki.nftables.org/wiki-nftables/index.php/Quick_reference-nftables_in_10_minutes) — documentação oficial do projeto Netfilter detalhando tabelas (`ip`, `ip6`, `inet`, `arp`, `bridge`, `netdev`), chains, hooks, prioridades, matches (`ct`, `meta`, `tcp`, `ip`) e scripting atômico; consultado em 2026-10-03.
- [Official nftables Wiki — Generic Set Infrastructure (Anonymous & Named Sets, Intervals, Timeouts & Auto-Merge)](https://wiki.nftables.org/wiki-nftables/index.php/Sets) — documentação oficial das estruturas de dados de alta performance de Sets (`hashtables` e `red-black trees`), `flags interval`, `timeout`, `auto-merge`, `counter` e `typeof`; consultado em 2026-10-03.
