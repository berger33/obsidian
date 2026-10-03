---
id: software.seguranca.tranche09.000811
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

# ProjectDiscovery **Naabu**: Arquitetura de Varredura de Portas **SYN / CONNECT / UDP** em Go, Permutação `BlackRock` e **Deduplicação Automática de IP**

## Em uma frase
**Naabu** (`projectdiscovery/naabu`, licença MIT, escrito em Go sobre `gopacket`, `retryabledns`, `cdncheck` e `blackrock`) é o scanner de portas rápido e confiável do ecossistema ProjectDiscovery, projetado para conectar a descoberta de subdomínios (`subfinder` / `dnsx`) à sondagem de aplicação (`httpx` / `tlsx` / `nuclei`).

## Por que importa
Um diferencial arquitetural fundamental do Naabu ao receber uma lista de **milhares de subdomínios via `stdin`** (onde frequentemente 200 subdomínios apontam para o mesmo endereço IP de um balanceador ou proxy reverso) é a **Deduplicação Automática de IP para DNS Port Scan**: em vez de varrer as mesmas 1.000 portas 200 vezes no mesmo IP, o Naabu resolve todos os hostnames, varre o endereço IP físico **uma única vez** e mapeia as portas abertas de volta para todos os subdomínios associados (`sub1.exemplo.com:8443`, `sub2.exemplo.com:8443`)!

## Como funciona
O Naabu suporta três modos de varredura: **`-s s` (SYN Scan)** com raw sockets quando executado como `root`/CAP_NET_RAW, **`-s c` (CONNECT Scan)** em user-space sem privilégios e sondagem **UDP**.

## Exemplo
```bash
# Verificar a versao do Naabu e varrer as top 100 portas de uma lista de subdominios com deduplicacao automatica de IP
naabu -version
naabu -list /cases/easm/subdomains.txt -top-ports 100 -rate 1000 -o /cases/easm/open_host_ports.txt
```

## Limites e trade-offs
Para permitir que o Naabu execute **SYN Scan (`-s s`)** rápido em Linux **sem precisar rodar o binário inteiro como `root`**, atribua a capability de rede ao binário com **`sudo setcap cap_net_raw,cap_net_admin+eip $(which naabu)`**!

## Como verificar
Verifique na saída que o Naabu preserva o formato `hostname:porta` para alimentar diretamente o `httpx` via pipe.

## Conexões
- [[naabu-exclusao-cdn-waf-exclude-cdn-port-threshold-protecao]] — Veja também: Naabu: Exclusão Inteligente de **IPs de CDN / WAF (`-exclude-cdn` / `-ec`)** e Proteção contra Honeypots/Port-Spoofing (**`-port-threshold` / `-pts`**).
- [[naabu-integracao-pipeline-subfinder-dnsx-naabu-httpx-nuclei]] — Referência cruzada direta com naabu-integracao-pipeline-subfinder-dnsx-naabu-httpx-nuclei.

## Fontes
- [ProjectDiscovery Naabu Official GitHub — Fast Port Scanner Written in Go](https://raw.githubusercontent.com/projectdiscovery/naabu/main/README.md) — repositório oficial do ProjectDiscovery Naabu cobrindo arquitetura SYN/CONNECT, flags CLI, descoberta de hosts e integração com Nmap; consultado em 2026-10-03.
- [ProjectDiscovery Naabu Official Documentation — Usage, Configuration & Rate Tuning](https://raw.githubusercontent.com/projectdiscovery/naabu/main/go.mod) — documentação oficial do Naabu na plataforma ProjectDiscovery Docs; consultado em 2026-10-03.
- [Go Package Documentation — github.com/projectdiscovery/naabu/v2](https://docs.projectdiscovery.io/tools/naabu/overview) — documentação técnica do pacote Go e SDK `naabu/v2/pkg/runner`; consultado em 2026-10-03.
