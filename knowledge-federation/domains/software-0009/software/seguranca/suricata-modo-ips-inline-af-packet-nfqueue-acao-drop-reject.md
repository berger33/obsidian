---
id: software.seguranca.tranche02.000196
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-02.md"
fontes: ["https://raw.githubusercontent.com/OISF/suricata/main/README.md", "https://docs.suricata.io/en/latest/what-is-suricata.html", "https://github.com/OISF/suricata"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Suricata em Modo IPS Inline (`AF_PACKET` Layer 2 Bridge e `NFQUEUE`): bloqueio ativo de ataques com ações `drop` e `reject`

## Em uma frase
Conforme destaca o README oficial do Suricata, além de operar como IDS passivo (via *TAP* ou *SPAN/Mirror Port*), o Suricata opera como **IPS (*Intrusion Prevention System*) inline** usando dois modos principais no Linux: **IPS via `AF_PACKET` copy-mode** (ponte de camada 2 de altíssima velocidade entre duas interfaces de rede, ex.: `eth0 <-> eth1`) ou **IPS via Netfilter `NFQUEUE`** (integrado ao `nftables` / `iptables` na mesma máquina ou roteador).

## Por que importa
Um IDS passivo rodando em porta espelhada detecta o ataque e envia o alerta para o SIEM, mas os pacotes maliciosos já chegaram ao servidor alvo; no modo IPS inline, uma regra com ação **`drop`** descarta o pacote malicioso instantaneamente e marca todo o fluxo para bloqueio.

## Como funciona
Além disso, o Suricata implementa **Exception Policies (`exception-policy`):** você define explicitamente se, em caso de esgotamento de memória (`memcap`) ou falha de realinhamento de stream TCP, o IPS deve operar em `drop-flow` (*fail-closed*, priorizando segurança máxima) ou `pass-flow` (*fail-open*, priorizando disponibilidade).

## Exemplo
```yaml
# Exemplo de configuração IPS inline de alta velocidade via AF_PACKET copy-mode no suricata.yaml:
af-packet:
  - interface: eth0
    threads: auto
    cluster-id: 99
    cluster-type: cluster_flow
    defrag: yes
    copy-mode: ips
    copy-iface: eth1
  - interface: eth1
    threads: auto
    cluster-id: 98
    cluster-type: cluster_flow
    defrag: yes
    copy-mode: ips
    copy-iface: eth0
```

## Limites e trade-offs
Ao converter regras de `alert` para `drop` via `/etc/suricata/drop.conf` do `suricata-update`, promova apenas regras de alta confiança já validadas em modo IDS sem falsos positivos na sua rede.

## Como verificar
Verifique no `eve.json` os eventos com `"action": "blocked"` quando uma regra `drop` é acionada em modo IPS.

## Conexões
- [[suricata-inspecao-tls-fingerprinting-ja3-ja4-sni-certificados-c2]] — Veja também: Suricata Inspeção de Tráfego Criptografado TLS: fingerprinting de clientes/servidores (`JA3`, `JA3S`, `JA4`), `tls.sni` e certificados X.509.
- [[suricata-file-extraction-file-store-sha256-deteccao-malware-rede]] — Veja também: Suricata File Extraction e Hashing (`file-store` v2 e `fileinfo`): cálculo de SHA-256 em tempo real e captura forense de arquivos trafegados.

## Fontes
- [OISF Suricata Official Documentation — What is Suricata (Multi-Threaded IDS/IPS/NSM Engine, EVE JSON Telemetry, Protocol Parsers & File Extraction)](https://raw.githubusercontent.com/OISF/suricata/main/README.md) — Documentação oficial da OISF explicando a arquitetura multi-thread do Suricata como IDS, IPS e NSM, logs estruturados EVE JSON, inspeção TLS e extração de arquivos; consultado em 2026-10-03.
- [OISF Suricata GitHub — README.md (High-Performance Network Threat Detection Engine, Rust Parsers, AF_PACKET/eBPF IPS & PCAP Processing)](https://docs.suricata.io/en/latest/what-is-suricata.html) — README oficial do OISF/suricata detalhando recursos de captura de pacotes em alta velocidade, segurança de memória com Rust, testes de regressão e operação via Unix Socket; consultado em 2026-10-03.
- [OISF Suricata — Official GitHub Repository](https://github.com/OISF/suricata) — Repositório oficial GPL-2.0 do OISF Suricata; consultado em 2026-10-03.
