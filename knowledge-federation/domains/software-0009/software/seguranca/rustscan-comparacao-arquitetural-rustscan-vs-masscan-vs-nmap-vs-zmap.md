---
id: software.seguranca.tranche08.000789
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
fontes: ["https://raw.githubusercontent.com/bee-san/RustScan/master/README.md", "https://raw.githubusercontent.com/bee-san/RustScan/master/Cargo.toml", "https://github.com/bee-san/RustScan/wiki"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Decisão Arquitetural de Scanners de Portas: Quando Usar **RustScan** vs **Masscan** vs **ZMap** vs **Nmap** em Engajamentos Reais

## Em uma frase
Uma dúvida frequente em equipes de Pentest, Red Team e Gestão de Superfície de Ataque (EASM) é qual scanner de portas escolher para cada cenário, já que **RustScan**, **Masscan**, **ZMap** e **Nmap** possuem arquiteturas de rede fundamentalmente diferentes.

## Por que importa
Compare os quatro modelos: **(1) Nmap**: o padrão ouro para **profundidade por host** (`-sV`, `-O`, 600+ scripts NSE, TCP/UDP/SCTP, controle fino de retransmissão), porém mais lento para descobrir todas as 65.535 portas em muitos hosts; **(2) RustScan**: usa sockets assíncronos do SO (`tokio`), funciona **sem root e sobre VPNs/túneis**, varre as **65.535 portas de poucos hosts em segundos** e já chama o Nmap automaticamente; **(3) Masscan**: usa pilha TCP/IP própria em user-space e cifra BlackRock para varrer **milhares de hosts × muitas portas** a milhões de pps; e **(4) ZMap**: usa grupos cíclicos multiplicativos ($\mathbb{Z}_p^*$) otimizados para varrer **1 porta (ex.: 443) em milhões/bilhões de IPs (escala de internet)**!

## Como funciona
Portanto, em um pentest via VPN contra 1 a 50 servidores onde você quer todas as 65.535 portas + Nmap `-sV -sC`, **RustScan** é imbatível; já para inventariar uma rede `/8` ou `/16` inteira, **Masscan** ou **ZMap** são as ferramentas arquiteturalmente corretas!

## Exemplo
```bash
# Fluxo ideal para 1 host via VPN (RustScan -> Nmap) vs Fluxo para sub-rede /16 inteira na porta 443 (ZMap/Masscan)
rustscan -a 10.10.10.50 -b 1500 --ulimit 5000 -- -sV -sC -oA /cases/pentest/single_host_full
```

## Limites e trade-offs
Note uma limitação importante do RustScan atual: como ele é construído sobre `tokio::net::TcpStream` (TCP Connect assíncrono), o RustScan descobre apenas portas **TCP**; para enumerar portas **UDP** (`53`, `123`, `161`, `500`), utilize `nmap -sU`, `masscan -pU:...` ou `zmap -M udp`!

## Como verificar
Documente no plano de testes da equipe qual ferramenta deve ser usada conforme o tamanho do bloco CIDR e o tipo de transporte (LAN direta vs túnel VPN).

## Conexões
- [[rustscan-execucao-container-docker-ulimit-rede-host-alias]] — Veja também: RustScan em Containers **Docker (`rustscan/rustscan`)**: Configuração de `--network host`, `ulimit` do Container e Montagem de Volumes para o Nmap.
- [[rustscan-varredura-ipv6-dual-stack-resolucao-hickory-dns-timeout]] — Veja também: RustScan em Redes **IPv6 e Dual-Stack**: Varredura de Endereços IPv6, Resolução Assíncrona (`hickory-resolver`) e Mitigação de Exaustão de *Conntrack* Local.
- [[rustscan-arquitetura-tokio-async-descoberta-portas-handoff-nmap]] — Referência cruzada direta com rustscan-arquitetura-tokio-async-descoberta-portas-handoff-nmap.
- [[masscan-arquitetura-assincrona-pilha-tcp-ip-userspace-blackrock-syn-cookies]] — Referência cruzada direta com masscan-arquitetura-assincrona-pilha-tcp-ip-userspace-blackrock-syn-cookies.
- [[zmap-arquitetura-varredura-internet-grupos-ciclicos-multiplicativos-stateless]] — Referência cruzada direta com zmap-arquitetura-varredura-internet-grupos-ciclicos-multiplicativos-stateless.

## Fontes
- [RustScan Official GitHub — The Modern Port Scanner & Automatic Nmap Integration](https://raw.githubusercontent.com/bee-san/RustScan/master/README.md) — documentação oficial do RustScan cobrindo varredura assíncrona de 65.535 portas, handoff para o Nmap, batch-size, ulimit, accessible e Docker; consultado em 2026-10-03.
- [RustScan Official Cargo Manifest — Tokio Async Runtime & Hickory DNS Dependencies](https://raw.githubusercontent.com/bee-san/RustScan/master/Cargo.toml) — especificação oficial de dependências e crates do RustScan (tokio, futures, rlimit, cidr-utils, hickory-resolver); consultado em 2026-10-03.
- [RustScan Official Wiki — Configuration File & Custom Scripting Engine](https://github.com/bee-san/RustScan/wiki) — wiki oficial do RustScan cobrindo o arquivo .rustscan.toml e o motor de scripts customizados .rustscan_scripts.toml; consultado em 2026-10-03.
