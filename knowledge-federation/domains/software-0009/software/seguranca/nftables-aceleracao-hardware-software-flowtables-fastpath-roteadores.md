---
id: software.seguranca.tranche12.001188
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

# Aceleração de Fluxos de Rede com **`flowtables` (Fastpath Software e Hardware Offload)** no `nftables` para Gateways de Alta Vazão (10GbE / 40GbE)

## Em uma frase
Em um gateway de borda ou firewall roteador Linux de 10 Gbps / 40 Gbps, avaliar toda a pilha clássica de roteamento e chains de `forward` para cada um dos milhões de pacotes pertencentes a um fluxo TCP/UDP já estabelecido e autorizado (por exemplo, um backup grande ou streaming de vídeo) consome CPU desnecessariamente.

## Por que importa
A partir do Kernel Linux 4.16+, o `nftables` introduziu as **`flowtables` (`flowtable`)**: um mecanismo de **Fastpath (Software e Hardware Offload na NIC)** onde, assim que os primeiros pacotes de uma conexão passam pela inspeção de segurança e entram no estado estabelecido, a regra **`flow add @minha_flowtable`** transfere o fluxo para uma tabela de encaminhamento direto na recepção (`ingress`)!

## Como funciona
Todos os pacotes subsequentes daquela conexão dão **bypass completo no caminho lento de roteamento e filtragem (`forward`)**, sendo encaminhados diretamente da interface de entrada para a interface de saída (ou processados diretamente no ASIC da placa de rede quando `flags offload;` é suportado pelo driver)!

## Exemplo
```nft
# Configurar uma Flowtable no nftables para acelerar fluxos TCP/UDP ja estabelecidos entre eth0 e eth1
table inet filter {
    flowtable fastpath {
        hook ingress priority filter
        devices = { eth0, eth1 }
    }

    chain forward {
        type filter hook forward priority 10; policy drop;
        ip protocol { tcp, udp } flow add @fastpath
        ct state { established, related } counter accept
        iifname "eth1" oifname "eth0" accept
    }
}
```

## Limites e trade-offs
O ganho de throughput de uma **`flowtable`** em software já multiplica em até 3x–5x a capacidade de pacotes por segundo (pps) de um roteador Linux em fluxos estabelecidos, mantendo 100% da política de segurança na abertura de cada nova conexão (`ct state new`).

## Como verificar
Se um pacote TCP `FIN` ou `RST` chegar (ou o fluxo ficar ocioso), o kernel remove ou devolve o fluxo automaticamente para o caminho normal do `conntrack`.

## Conexões
- [[nftables-protecao-ddos-familia-netdev-ingress-synproxy-raw-notrack]] — Veja também: Mitigação de **DDoS em Linha de Velocidade** com `nftables`: Família **`netdev` (`hook ingress`)**, Bypass de Conntrack (**`notrack`**) e **`synproxy`**.
- [[nftables-logging-estruturado-ulogd2-nflog-rastreamento-nftrace-debug]] — Veja também: Depuração em Tempo Real (**`meta nftrace set 1` / `nft monitor trace`**) e Logging Estruturado JSON (**`nflog` + `ulogd2`**) no `nftables`.
- [[nftables-arquitetura-firewall-kernel-linux-netfilter-tabelas-inet]] — Referência cruzada direta com nftables-arquitetura-firewall-kernel-linux-netfilter-tabelas-inet.
- [[nftables-chains-hooks-prioridades-conntrack-stateful-firewall]] — Referência cruzada direta com nftables-chains-hooks-prioridades-conntrack-stateful-firewall.

## Fontes
- [Official nftables Wiki — Quick Reference: nftables in 10 Minutes](https://wiki.nftables.org/wiki-nftables/index.php/Quick_reference-nftables_in_10_minutes) — documentação oficial do projeto Netfilter detalhando tabelas (`ip`, `ip6`, `inet`, `arp`, `bridge`, `netdev`), chains, hooks, prioridades, matches (`ct`, `meta`, `tcp`, `ip`) e scripting atômico; consultado em 2026-10-03.
- [Official nftables Wiki — Generic Set Infrastructure (Anonymous & Named Sets, Intervals, Timeouts & Auto-Merge)](https://wiki.nftables.org/wiki-nftables/index.php/Sets) — documentação oficial das estruturas de dados de alta performance de Sets (`hashtables` e `red-black trees`), `flags interval`, `timeout`, `auto-merge`, `counter` e `typeof`; consultado em 2026-10-03.
