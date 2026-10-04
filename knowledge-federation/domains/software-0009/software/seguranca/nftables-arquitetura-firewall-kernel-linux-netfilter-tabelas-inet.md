---
id: software.seguranca.tranche12.001181
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

# Arquitetura do **`nftables` (`Netfilter Project`)**: Máquina Virtual de Bytecode no Kernel Linux, Família Dual-Stack **`inet`** e Substituição do `iptables`

## Em uma frase
Por que o projeto **Netfilter** do Kernel Linux desenvolveu o **`nftables`** (`nft`) para substituir os antigos `iptables`, `ip6tables`, `arptables` e `ebtables`, e quais problemas graves de segurança e performance da arquitetura antiga ele resolve?

## Por que importa
No antigo `iptables`, você era obrigado a manter **dois arquivos de firewall completamente separados** (um para IPv4 no `iptables` e outro para IPv6 no `ip6tables` — o que frequentemente deixava servidores expostos em IPv6 por esquecimento!), a avaliação de milhares de regras era linear $O(n)$ e cada modificação individual recarregava toda a tabela no kernel!

## Como funciona
O **`nftables`** (padrão no Debian 10+, Ubuntu 20.04+, RHEL 8+, AlmaLinux e Rocky Linux) compila suas regras em espaço de usuário (`nft`) para um **bytecode de máquina virtual (`nf_tables`)** executado no kernel, introduz a família de endereços unificada **`inet` (que filtra IPv4 e IPv6 simultaneamente na mesma tabela e na mesma regra!)**, aplica **atualizações 100% atômicas (`nft -f /etc/nftables.conf`)** e possui estruturas nativas de **Sets e Mapas ($O(1)$ / $O(\log n)$)**!

## Exemplo
```nft
#!/usr/sbin/nft -f
# Exemplo de firewall host-based atomico Dual-Stack (IPv4 + IPv6) usando a familia 'inet' no /etc/nftables.conf
flush ruleset

table inet filter {
    chain input {
        type filter hook input priority filter; policy drop;
        iif "lo" accept
        ct state vmap { established : accept, related : accept, invalid : drop }
        ip protocol icmp accept
        ip6 nexthdr ipv6-icmp accept
        tcp dport { 22, 443 } ct state new accept
    }
}
```

## Limites e trade-offs
Observe a elegância da família **`inet`**: a única regra `tcp dport { 22, 443 } ct state new accept` protege e autoriza simultaneamente conexões TCP sobre **IPv4 e IPv6**, eliminando para sempre o risco de *drift* de segurança entre as duas pilhas de rede!

## Como verificar
Diferente do `iptables` (que criava dezenas de tabelas e chains vazias por padrão no kernel mesmo sem uso), no `nftables` **zero tabelas ou chains existem até que você as declare explicitamente**, economizando ciclos de CPU em cada pacote que atravessa a interface de rede.

## Conexões
- [[nftables-chains-hooks-prioridades-conntrack-stateful-firewall]] — Veja também: Anatomia de **Chains, Hooks (`prerouting`, `input`, `forward`, `output`, `postrouting`, `ingress`), Prioridades** e **Connection Tracking (`ct state`)** no `nftables`.
- [[nftables-conjuntos-sets-anonimos-nomeados-intervalos-timeouts-dinamicos]] — Referência cruzada direta com nftables-conjuntos-sets-anonimos-nomeados-intervalos-timeouts-dinamicos.
- [[wireguard-integracao-firewall-nftables-postup-postdown-killswitch]] — Referência cruzada direta com wireguard-integracao-firewall-nftables-postup-postdown-killswitch.

## Fontes
- [Official nftables Wiki — Quick Reference: nftables in 10 Minutes](https://wiki.nftables.org/wiki-nftables/index.php/Quick_reference-nftables_in_10_minutes) — documentação oficial do projeto Netfilter detalhando tabelas (`ip`, `ip6`, `inet`, `arp`, `bridge`, `netdev`), chains, hooks, prioridades, matches (`ct`, `meta`, `tcp`, `ip`) e scripting atômico; consultado em 2026-10-03.
- [Official nftables Wiki — Generic Set Infrastructure (Anonymous & Named Sets, Intervals, Timeouts & Auto-Merge)](https://wiki.nftables.org/wiki-nftables/index.php/Sets) — documentação oficial das estruturas de dados de alta performance de Sets (`hashtables` e `red-black trees`), `flags interval`, `timeout`, `auto-merge`, `counter` e `typeof`; consultado em 2026-10-03.
