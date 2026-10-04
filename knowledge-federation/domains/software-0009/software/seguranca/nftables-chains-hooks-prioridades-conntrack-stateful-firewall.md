---
id: software.seguranca.tranche12.001182
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

# Anatomia de **Chains, Hooks (`prerouting`, `input`, `forward`, `output`, `postrouting`, `ingress`), Prioridades** e **Connection Tracking (`ct state`)** no `nftables`

## Em uma frase
No **`nftables`**, uma **Tabela (`table`)** é um container lógico de **Chains (`chain`)**, e existem dois tipos de chains: **Base Chains** (que se conectam diretamente a um *hook* da pilha de rede do kernel Linux com um `type`, `hook`, `priority` e `policy`) e **Regular Chains** (sem hook, usadas para organizar e modularizar regras via `jump` ou `goto`)!

## Por que importa
Para as famílias `ip`, `ip6` e `inet`, os cinco hooks clássicos do Netfilter são: **`prerouting`** (antes da decisão de roteamento — ideal para DNAT e raw/notrack), **`input`** (pacotes destinados ao próprio host local), **`forward`** (pacotes roteados através do host para outra máquina/container), **`output`** (pacotes gerados por processos locais) e **`postrouting`** (após o roteamento — ideal para SNAT/Masquerade)!

## Como funciona
Dentro de uma base chain `input` ou `forward` com política padrão restritiva (**`policy drop;`**), a primeira regra após liberar o loopback (`iif "lo" accept`) deve sempre consultar o motor stateful de **Connection Tracking (`ct state`)** para aprovar pacotes `established, related` e descartar pacotes `invalid` antes de avaliar qualquer abertura de porta!

## Exemplo
```bash
# Inspecionar todas as tabelas, base chains, hooks, prioridades e handles (-a) ativos no kernel Linux
sudo nft -a list ruleset
```

## Limites e trade-offs
Por que descartar explicitamente **`ct state invalid drop`** logo no topo da chain `input` e `forward`? Porque pacotes classificados como `invalid` pelo `nf_conntrack` incluem pacotes TCP `ACK`/`FIN`/`RST` órfãos que não pertencem a nenhuma conexão estabelecida (típicos de scans furtivos `nmap -sA` / `-sF` / `-sX`) ou pacotes com checksums/estados corrompidos!

## Como verificar
Use sempre `sudo nft -c -f /etc/nftables.conf` (`-c, --check`) para validar a sintaxe e a semântica de todo o arquivo de regras em modo *dry-run* antes de aplicá-lo em produção.

## Conexões
- [[nftables-arquitetura-firewall-kernel-linux-netfilter-tabelas-inet]] — Veja também: Arquitetura do **`nftables` (`Netfilter Project`)**: Máquina Virtual de Bytecode no Kernel Linux, Família Dual-Stack **`inet`** e Substituição do `iptables`.
- [[nftables-conjuntos-sets-anonimos-nomeados-intervalos-timeouts-dinamicos]] — Veja também: Conjuntos de Alta Performance (**Sets Anônimos e Nomeados**) no `nftables`: Intervalos CIDR (`flags interval`), `auto-merge`, `timeout` e Blocklists em $O(1)$.
- [[nftables-protecao-ddos-familia-netdev-ingress-synproxy-raw-notrack]] — Referência cruzada direta com nftables-protecao-ddos-familia-netdev-ingress-synproxy-raw-notrack.

## Fontes
- [Official nftables Wiki — Quick Reference: nftables in 10 Minutes](https://wiki.nftables.org/wiki-nftables/index.php/Quick_reference-nftables_in_10_minutes) — documentação oficial do projeto Netfilter detalhando tabelas (`ip`, `ip6`, `inet`, `arp`, `bridge`, `netdev`), chains, hooks, prioridades, matches (`ct`, `meta`, `tcp`, `ip`) e scripting atômico; consultado em 2026-10-03.
- [Official nftables Wiki — Generic Set Infrastructure (Anonymous & Named Sets, Intervals, Timeouts & Auto-Merge)](https://wiki.nftables.org/wiki-nftables/index.php/Sets) — documentação oficial das estruturas de dados de alta performance de Sets (`hashtables` e `red-black trees`), `flags interval`, `timeout`, `auto-merge`, `counter` e `typeof`; consultado em 2026-10-03.
