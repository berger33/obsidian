---
id: software.seguranca.tranche08.000780
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
fontes: ["https://raw.githubusercontent.com/robertdavidgraham/masscan/master/README.md", "https://raw.githubusercontent.com/robertdavidgraham/masscan/master/doc/masscan.8.markdown", "https://github.com/robertdavidgraham/masscan"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Defesa e Detecção contra Varreduras **Masscan**: Proteção da Tabela **`nf_conntrack`** em Firewalls e Detecção de Varreduras Espalhadas no **Suricata / Zeek**

## Em uma frase
Porque a cifra **BlackRock** do Masscan randomiza a ordem tanto dos IPs de destino quanto das portas (`IP_A:443`, depois `IP_Z:22`, depois `IP_M:8080`), uma varredura Masscan contra uma rede `/16` **passa abaixo do limiar de detectores ingênuos de portscan que contam apenas quantas portas de um único host destino foram tocadas em 5 segundos**!

## Por que importa
Porém, a assinatura de rede do Masscan é claríssima quando o sensor (**Suricata**, **Zeek** ou NetFlow) agrega por **IP de Origem (`by_src`)** contando o número de pares `(dst_ip, dst_port)` distintos que receberam `SYN` sem completar o handshake (ou responderam `RST` em janelas curtas).

## Como funciona
Além da detecção no IDS, o maior risco operacional que um Masscan interno ou externo causa à infraestrutura defensiva é o **esgotamento da tabela de estado `nf_conntrack` (`nf_conntrack: table full, dropping packet`)** em firewalls Linux stateful: se um pentester interno disparar 500.000 pacotes `SYN`/s através de um firewall Linux com `nf_conntrack_max = 65536`, o firewall criará 65.536 entradas `SYN_SENT` e derrubará o tráfego de produção!

## Exemplo
```bash
# Auditar no firewall Linux a utilizacao atual da tabela nf_conntrack e os timeouts de conexoes TCP nao-estabelecidas
sysctl net.netfilter.nf_conntrack_count net.netfilter.nf_conntrack_max
sysctl net.netfilter.nf_conntrack_tcp_timeout_syn_sent net.netfilter.nf_conntrack_tcp_timeout_syn_recv
```

## Limites e trade-offs
Para proteger roteadores e firewalls Linux de borda/core contra exaustão de estado por varreduras SYN em massa, dimensione adequadamente `net.netfilter.nf_conntrack_max`, reduza `nf_conntrack_tcp_timeout_syn_sent` (ex.: `30`s) e aplique `notrack` em regras `raw` para tráfego que não exige inspeção stateful.

## Como verificar
No Zeek (`Scan::port_scan` / `Scan::addr_scan`) e no Suricata (`threshold: type both, track by_src`), monitore qualquer IP de origem que tente conexões `SYN` para mais de 100 destinos/portas distintos com falha (`S0` / `REJ` no `conn.log` do Zeek) em 60 segundos.

## Conexões
- [[masscan-ajustes-rede-arp-router-mac-adapter-vlan-bpf-pcap]] — Veja também: Masscan: Ajustes de Camada de Enlace (**`--interface`**, **`--adapter-ip`**, **`--adapter-mac`**, **`--router-mac`**), Tags **802.1Q VLAN** e Diagnóstico `--packet-trace`.
- [[masscan-arquitetura-assincrona-pilha-tcp-ip-userspace-blackrock-syn-cookies]] — Referência cruzada direta com masscan-arquitetura-assincrona-pilha-tcp-ip-userspace-blackrock-syn-cookies.

## Fontes
- [Masscan Official GitHub — Mass IP Port Scanner Architecture & Banner Checking](https://raw.githubusercontent.com/robertdavidgraham/masscan/master/README.md) — documentação oficial do Masscan cobrindo transmissão assíncrona, cifra BlackRock, captura de banners, prevenção de TCP RST e PF_RING; consultado em 2026-10-03.
- [Masscan Official Manual Page — masscan(8) Complete CLI & Configuration Reference](https://raw.githubusercontent.com/robertdavidgraham/masscan/master/doc/masscan.8.markdown) — manual oficial masscan(8) cobrindo taxas, excludefile, paused.conf, shards, formatos binários/JSON/XML e payloads UDP/HTTP; consultado em 2026-10-03.
- [Masscan Project Repository — robertdavidgraham/masscan](https://github.com/robertdavidgraham/masscan) — repositório oficial do código-fonte do Masscan; consultado em 2026-10-03.
