---
id: software.seguranca.tranche09.000814
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-09.md"
fontes: ["https://raw.githubusercontent.com/projectdiscovery/naabu/main/README.md", "https://raw.githubusercontent.com/projectdiscovery/naabu/main/go.mod", "https://docs.projectdiscovery.io/tools/naabu/overview"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Naabu **Host Discovery (`-sn` / `-wn`)**: Sondagem Híbrida de Hosts Vivos via **ICMP (`-pe`, `-pp`, `-pm`)**, **TCP Ping (`-ps`, `-pa`)**, **ARP (`-arp`)** e **IPv6 ND (`-nd`)**

## Em uma frase
Ao varrer blocos de rede grandes (`/16` ou `/24`) onde 90% dos endereços IP estão desocupados, testar 1.000 portas em cada IP inexistente desperdiça tempo; para isso, o Naabu inclui um motor completo de **Host Discovery** ativado por **`-sn` (`-host-discovery` — realiza apenas descoberta de hosts vivos)** ou **`-wn` (`-with-host-discovery` — descobre os hosts vivos primeiro e depois varre as portas apenas deles)**!

## Por que importa
Conforme documentado no `README.md` oficial do Naabu, você pode customizar exatamente quais probes de descoberta de host serão combinados: **`-pe`** (ICMP Echo Request), **`-pp`** (ICMP Timestamp Request), **`-pm`** (ICMP Address Mask), **`-ps 80,443,22`** (TCP SYN Ping), **`-pa 80,443`** (TCP ACK Ping), **`-arp`** (ARP Ping na LAN local) e **`-nd`** (IPv6 Neighbor Discovery)!

## Como funciona
E adicionando a flag **`-rev-ptr`**, o Naabu já realiza a consulta de DNS Reverso (`PTR`) para cada IP descoberto!

## Exemplo
```bash
# Descobrir todos os hosts ativos em uma sub-rede /24 combinando ARP, ICMP Echo e TCP SYN Ping (22,80,443) com Reverse PTR
sudo naabu -host 10.20.30.0/24 \
  -sn \
  -pe -ps 22,80,443,445,3389 \
  -rev-ptr \
  -o /cases/easm/live_hosts.txt
```

## Limites e trade-offs
Note na documentação recente do Naabu que a flag `-Pn` foi depreciada em favor do comportamento explícito: por padrão o Naabu já pula o host discovery (indo direto ao scan de portas) a menos que você passe **`-wn` (`-with-host-discovery`)** ou **`-sn` (`-host-discovery`)**.

## Como verificar
Em sub-redes onde firewalls bloqueiam ICMP Ping (`-pe`), inclua sempre **`-ps 22,80,443,445,3389,8080,8443`** junto com `-wn` para não perder servidores vivos que filtram ICMP.

## Conexões
- [[naabu-enumeracao-passiva-shodan-internetdb-passive-zero-pacotes]] — Veja também: Naabu **`-passive`**: Enumeração Passiva Instantânea de Portas Abertas via **Shodan InternetDB** com Zero Pacotes Enviados ao Alvo.
- [[naabu-integracao-nativa-nmap-cli-service-fingerprinting-nse]] — Veja também: Naabu + **Nmap (`-nmap-cli`)**: Handoff Automático de Portas Descobertas para Detecção de Versão (`-sV`) e Scripts NSE (`-sC`) do Nmap.
- [[naabu-arquitetura-varredura-portas-syn-connect-udp-deduplicacao-ip]] — Referência cruzada direta com naabu-arquitetura-varredura-portas-syn-connect-udp-deduplicacao-ip.
- [[zmap-modulos-sondagem-probe-modules-tcp-synscan-icmp-udp-dns]] — Referência cruzada direta com zmap-modulos-sondagem-probe-modules-tcp-synscan-icmp-udp-dns.

## Fontes
- [ProjectDiscovery Naabu Official GitHub — Fast Port Scanner Written in Go](https://raw.githubusercontent.com/projectdiscovery/naabu/main/README.md) — repositório oficial do ProjectDiscovery Naabu cobrindo arquitetura SYN/CONNECT, flags CLI, descoberta de hosts e integração com Nmap; consultado em 2026-10-03.
- [ProjectDiscovery Naabu Official Documentation — Usage, Configuration & Rate Tuning](https://raw.githubusercontent.com/projectdiscovery/naabu/main/go.mod) — documentação oficial do Naabu na plataforma ProjectDiscovery Docs; consultado em 2026-10-03.
- [Go Package Documentation — github.com/projectdiscovery/naabu/v2](https://docs.projectdiscovery.io/tools/naabu/overview) — documentação técnica do pacote Go e SDK `naabu/v2/pkg/runner`; consultado em 2026-10-03.
