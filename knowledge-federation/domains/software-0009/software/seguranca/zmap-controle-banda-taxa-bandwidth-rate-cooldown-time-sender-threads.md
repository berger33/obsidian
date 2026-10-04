---
id: software.seguranca.tranche08.000793
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-08.md"
fontes: ["https://raw.githubusercontent.com/zmap/zmap/main/README.md", "https://raw.githubusercontent.com/zmap/zgrab2/master/README.md", "https://github.com/zmap/zmap/wiki"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# ZMap: Controle de Largura de Banda (**`-B 10M` / `--bandwidth`**) vs Taxa de Pacotes (**`-r` / `--rate`**), `--sender-threads` e `--cooldown-time`

## Em uma frase
Diferente da maioria das ferramentas que só aceitam taxa em pacotes por segundo, o ZMap oferece uma opção muito intuitiva para engenheiros de rede: limitar a transmissão diretamente em **bits/bytes por segundo com `-B` / `--bandwidth`** (suportando sufixos `G`, `M` e `K`, como **`-B 10M`** para 10 Mbps ou `-B 100M` para 100 Mbps), ou em pacotes por segundo com **`-r` / `--rate`**!

## Por que importa
Se você não especificar `-B` nem `-r`, **o ZMap por padrão tentará transmitir na velocidade máxima suportada pela placa de rede e pela CPU** — o que em um servidor de 1 Gbps ou 10 Gbps pode saturar imediatamente o link do roteador se não for limitado!

## Como funciona
Por isso, a regra de ouro operacional do ZMap é **sempre especificar explicitamente `-B` (ex.: `-B 10M` em redes corporativas) ou `-r` (ex.: `-r 5000`)**, além de respeitar o **`--cooldown-time`** (padrão `8` segundos que o ZMap aguarda após enviar o último pacote para receber as respostas em trânsito).

## Exemplo
```bash
# Varrer a porta 443/TCP na sub-rede 10.20.0.0/16 limitando estritamente a largura de banda a 10 Mbps (-B 10M)
sudo zmap -p 443 \
  -B 10M \
  --cooldown-time=8 \
  10.20.0.0/16 \
  -o /cases/easm/zmap_443_hosts.txt
```

## Limites e trade-offs
Para testes rápidos de amostragem estatística (por exemplo, descobrir 100 servidores web aleatórios dentro de uma grande rede sem varrer a rede inteira), o ZMap suporta **`-n` (`--max-targets`, número ou porcentagem como `-n 1%`)**, **`--max-results <N>`** (para assim que encontrar $N$ hosts abertos!) e **`--max-runtime <segundos>`**!

## Como verificar
Monitore na saída de status em tempo real (`stderr`) a taxa de envio (`send rate`), taxa de recepção (`recv rate`), porcentagem concluída e `pcap drop rate` (que deve ser `0%`; se houver drops no pcap, reduza `-B` ou `-r`).

## Conexões
- [[zmap-modulos-sondagem-probe-modules-tcp-synscan-icmp-udp-dns]] — Veja também: ZMap **Probe Modules (`-M`)**: Sondagem `tcp_synscan` (padrão), `icmp_echoscan`, `udp`, `dns` e `upnp` com **`--probe-args`**.
- [[zmap-listas-bloqueio-blocklist-allowlist-conformidade-rfc]] — Veja também: ZMap: Governança de Escopo com **`/etc/zmap/blocklist.conf` (`-b`)**, **Allowlist (`-w`)** e **`--ignore-blocklist-errors`**.
- [[zmap-arquitetura-varredura-internet-grupos-ciclicos-multiplicativos-stateless]] — Referência cruzada direta com zmap-arquitetura-varredura-internet-grupos-ciclicos-multiplicativos-stateless.
- [[masscan-controle-taxa-rate-pf-ring-excludefile-protecao-rede]] — Referência cruzada direta com masscan-controle-taxa-rate-pf-ring-excludefile-protecao-rede.

## Fontes
- [ZMap Official GitHub — Fast Single-Packet Network Scanner Architecture](https://raw.githubusercontent.com/zmap/zmap/main/README.md) — documentação oficial do ZMap cobrindo permutação por grupos cíclicos multiplicativos, módulos de sondagem/saída e controle de banda; consultado em 2026-10-03.
- [ZGrab 2.0 Official GitHub — Modular Application-Layer (L7) Network Scanner](https://raw.githubusercontent.com/zmap/zgrab2/master/README.md) — documentação oficial do ZGrab 2.0 cobrindo os 30 módulos de protocolo de camada 7, encadeamento com o ZMap e modo multiple.ini; consultado em 2026-10-03.
- [ZMap Official Wiki — Probe Modules, Output Filters, Blocklists & Ethical Scanning](https://github.com/zmap/zmap/wiki) — wiki técnica oficial do ZMap sobre listas de bloqueio RFC 1918, filtros de saída, sharding determinístico e boas práticas de varredura ética; consultado em 2026-10-03.
