---
id: software.seguranca.tranche09.000815
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

# Naabu + **Nmap (`-nmap-cli`)**: Handoff Automático de Portas Descobertas para Detecção de Versão (`-sV`) e Scripts NSE (`-sC`) do Nmap

## Em uma frase
Assim como o RustScan e os pipelines de dois estágios do Masscan, o Naabu possui integração nativa embutida com o **Nmap** através da flag **`-nmap-cli '<comando_nmap>'`** (implementada com suporte à biblioteca `Ullaakut/nmap/v3`).

## Por que importa
Quando você executa **`naabu -list targets.txt -p - -rate 2000 -nmap-cli 'nmap -sV -sC -oA nmap_out'`**, o Naabu realiza a descoberta rápida de todas as portas abertas em todos os alvos (aplicando deduplicação de IP e exclusão de CDN `-ec` se configurado) e, ao final, **invoca automaticamente o Nmap passando apenas os endereços e as portas abertas confirmadas**!

## Como funciona
Isso une o melhor do ecossistema ProjectDiscovery (resolução DNS resiliente, filtro de CDN Cloudflare/Akamai, suporte a ASN/CIDR) com o profundo banco de probes de versão `-sV` e scripts NSE do Nmap.

## Exemplo
```bash
# Descobrir portas abertas com o Naabu (excluindo CDNs) e disparar automaticamente o Nmap (-sV -sC) apenas nas portas ativas
sudo naabu -list /cases/easm/subdomains.txt \
  -top-ports 1000 \
  -exclude-cdn \
  -rate 1500 \
  -nmap-cli 'nmap -sV -sC -T4 -oX /cases/easm/naabu_nmap_services.xml'
```

## Limites e trade-offs
Atenção: no modo streaming (`-stream`), a integração `-nmap-cli`, a verificação dupla (`-verify`) e a retomada (`-resume`) ficam desabilitadas porque o modo `-stream` emite resultados imediatamente sem acumular a matriz final de portas por host.

## Como verificar
Verifique o arquivo XML `/cases/easm/naabu_nmap_services.xml` gerado pelo handoff automático do Naabu para o Nmap.

## Conexões
- [[naabu-descoberta-hosts-ativos-host-discovery-sn-wn-icmp-arp-tcp]] — Veja também: Naabu **Host Discovery (`-sn` / `-wn`)**: Sondagem Híbrida de Hosts Vivos via **ICMP (`-pe`, `-pp`, `-pm`)**, **TCP Ping (`-ps`, `-pa`)**, **ARP (`-arp`)** e **IPv6 ND (`-nd`)**.
- [[naabu-selecao-portas-top-ports-full-smart-scan-preditivo-verify]] — Veja também: Naabu: Seleção de Portas (`-p -`, `-top-ports full|100|1000`), Verificação Dupla TCP (**`-verify`**) e **Smart Scan Preditivo (`-ss` / `-smart-scan`)**.
- [[naabu-arquitetura-varredura-portas-syn-connect-udp-deduplicacao-ip]] — Referência cruzada direta com naabu-arquitetura-varredura-portas-syn-connect-udp-deduplicacao-ip.
- [[rustscan-arquitetura-tokio-async-descoberta-portas-handoff-nmap]] — Referência cruzada direta com rustscan-arquitetura-tokio-async-descoberta-portas-handoff-nmap.
- [[masscan-integracao-dois-estagios-masscan-descoberta-nmap-profundo]] — Referência cruzada direta com masscan-integracao-dois-estagios-masscan-descoberta-nmap-profundo.

## Fontes
- [ProjectDiscovery Naabu Official GitHub — Fast Port Scanner Written in Go](https://raw.githubusercontent.com/projectdiscovery/naabu/main/README.md) — repositório oficial do ProjectDiscovery Naabu cobrindo arquitetura SYN/CONNECT, flags CLI, descoberta de hosts e integração com Nmap; consultado em 2026-10-03.
- [ProjectDiscovery Naabu Official Documentation — Usage, Configuration & Rate Tuning](https://raw.githubusercontent.com/projectdiscovery/naabu/main/go.mod) — documentação oficial do Naabu na plataforma ProjectDiscovery Docs; consultado em 2026-10-03.
- [Go Package Documentation — github.com/projectdiscovery/naabu/v2](https://docs.projectdiscovery.io/tools/naabu/overview) — documentação técnica do pacote Go e SDK `naabu/v2/pkg/runner`; consultado em 2026-10-03.
