---
id: software.seguranca.tranche12.001185
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

# Proteção Anti-Brute-Force e **Rate Limiting Dinâmico por IP (`flags dynamic, timeout` / `ct count`)** Nativamente no `nftables`

## Em uma frase
Você sabia que o **`nftables`** consegue detectar e banir automaticamente em nível de kernel qualquer endereço IP que tente fazer força bruta no SSH (porta `22`) ou abrir centenas de conexões simultâneas na porta `443` — **sem precisar de nenhum daemon externo lendo arquivos de log em espaço de usuário**?

## Por que importa
Isso é feito através dos **Dynamic Sets (`flags dynamic, timeout`)** (que substituíram e unificaram a antiga sintaxe `meter`): quando uma nova conexão TCP (`ct state new`) chega na porta `22`, a expressão **`add @ssh_ratelimit { ip saddr limit rate over 4/minute burst 4 packets }`** rastreia a taxa de pacotes **individualmente para cada `ip saddr`**; se aquele IP específico ultrapassar 4 novas conexões por minuto, a condição avalia como verdadeira e você pode **adicioná-lo automaticamente a um segundo set `@ssh_jail` com `timeout 1h`**, bloqueando-o instantaneamente no kernel!

## Como funciona
Além de limitar por taxa temporal (`limit rate over`), você também pode limitar o **número máximo de conexões simultâneas abertas por um mesmo IP de origem** usando **`ct count over 20`**!

## Exemplo
```nft
# Banir automaticamente por 1 hora no kernel qualquer IP que exceder 4 novas conexoes SSH por minuto usando Dynamic Sets
table inet filter {
    set ssh_ratelimit {
        type ipv4_addr
        size 65535
        flags dynamic, timeout
        timeout 1m
    }

    set ssh_jail {
        type ipv4_addr
        size 65535
        flags dynamic, timeout
        timeout 1h
    }

    chain input {
        type filter hook input priority filter; policy accept;
        ip saddr @ssh_jail counter drop
        tcp dport 22 ct state new add @ssh_ratelimit { ip saddr limit rate over 4/minute burst 4 packets } add @ssh_jail { ip saddr } drop
    }
}
```

## Limites e trade-offs
Defina sempre o parâmetro **`size 65535`** (número máximo de entradas na tabela hash) e **`timeout`** em todo set com a flag `dynamic` — isso garante que um ataque distribuído de milhões de IPs falsificados não possa esgotar a memória RAM do kernel!

## Como verificar
Para inspecionar em tempo real quais endereços IP estão atualmente na prisão `@ssh_jail` e quantos segundos faltam para expirarem (`expires`), execute `sudo nft list set inet filter ssh_jail`.

## Conexões
- [[nftables-mapas-vereditos-vmap-concatenacoes-arquitetura-escalavel]] — Veja também: Mapas de Veredito (**`vmap`**) e **Concatenações de Seletores (`.` Tuplas)** no `nftables`: Substituindo Centenas de Regras Lineares por Uma Única Busca em Hash.
- [[nftables-nat-masquerade-dnat-snat-redirecionamento-portas]] — Veja também: Configuração de **NAT (`snat`, `masquerade`, `dnat` e `redirect`)** no `nftables` para Gateways VPN, Containers e Honeypots.
- [[nftables-arquitetura-firewall-kernel-linux-netfilter-tabelas-inet]] — Referência cruzada direta com nftables-arquitetura-firewall-kernel-linux-netfilter-tabelas-inet.
- [[nftables-conjuntos-sets-anonimos-nomeados-intervalos-timeouts-dinamicos]] — Referência cruzada direta com nftables-conjuntos-sets-anonimos-nomeados-intervalos-timeouts-dinamicos.
- [[openssh-hardening-sshd-config-criptografia-autenticacao-restricoes]] — Referência cruzada direta com openssh-hardening-sshd-config-criptografia-autenticacao-restricoes.

## Fontes
- [Official nftables Wiki — Quick Reference: nftables in 10 Minutes](https://wiki.nftables.org/wiki-nftables/index.php/Quick_reference-nftables_in_10_minutes) — documentação oficial do projeto Netfilter detalhando tabelas (`ip`, `ip6`, `inet`, `arp`, `bridge`, `netdev`), chains, hooks, prioridades, matches (`ct`, `meta`, `tcp`, `ip`) e scripting atômico; consultado em 2026-10-03.
- [Official nftables Wiki — Generic Set Infrastructure (Anonymous & Named Sets, Intervals, Timeouts & Auto-Merge)](https://wiki.nftables.org/wiki-nftables/index.php/Sets) — documentação oficial das estruturas de dados de alta performance de Sets (`hashtables` e `red-black trees`), `flags interval`, `timeout`, `auto-merge`, `counter` e `typeof`; consultado em 2026-10-03.
