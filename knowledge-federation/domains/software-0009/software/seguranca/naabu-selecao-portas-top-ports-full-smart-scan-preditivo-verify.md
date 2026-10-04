---
id: software.seguranca.tranche09.000816
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

# Naabu: Seleção de Portas (`-p -`, `-top-ports full|100|1000`), Verificação Dupla TCP (**`-verify`**) e **Smart Scan Preditivo (`-ss` / `-smart-scan`)**

## Em uma frase
O Naabu oferece opções flexíveis de seleção de portas: **`-top-ports 100`** (padrão, as 100 portas mais comuns do Nmap), **`-top-ports 1000`**, **`-top-ports full`** (ou **`-p -`**, todas as 65.535 portas), faixas customizadas (`-p 80,443,8000-9000`) e exclusão de portas (`-ep 22,9100`).

## Por que importa
Para eliminar falsos positivos causados por middleboxes ou *SYN proxies* durante uma varredura SYN (`-s s`), a flag **`-verify`** instrui o Naabu a realizar uma **segunda verificação via handshake TCP completo (`CONNECT`)** em cada porta que respondeu `SYN-ACK` antes de reportá-la como aberta!

## Como funciona
Além disso, versões recentes do Naabu introduziram o **`-ss` / `-smart-scan`** (com `-pt` / `-prediction-threshold`, padrão `20%`), que usa um **modelo estatístico de correlação de portas** (ex.: se o host abriu `80, 443, 3306`, quais outras portas têm maior probabilidade condicional de estarem abertas naquele perfil de servidor) para priorizar a varredura!

## Exemplo
```bash
# Executar SYN scan nas top 1000 portas com re-verificacao TCP (-verify) e Smart Scan preditivo (-ss)
sudo naabu -list /cases/easm/subdomains.txt \
  -s s \
  -top-ports 1000 \
  -verify \
  -smart-scan -prediction-threshold 25 \
  -o /cases/easm/verified_smart_ports.txt
```

## Limites e trade-offs
Se um servidor tiver múltiplos endereços IP (registro DNS Round-Robin `A` e `AAAA`), por padrão o Naabu varre apenas um IP por hostname; passe **`-scan-all-ips` (`-sa`)** e **`-ip-version 4,6` (`-iv 4,6`)** quando quiser auditar todos os nós individuais atrás de um DNS Round-Robin!

## Como verificar
Compare os resultados com e sem `-verify` quando estiver auditando alvos protegidos por firewalls corporativos com *SYN cookies*.

## Conexões
- [[naabu-integracao-nativa-nmap-cli-service-fingerprinting-nse]] — Veja também: Naabu + **Nmap (`-nmap-cli`)**: Handoff Automático de Portas Descobertas para Detecção de Versão (`-sV`) e Scripts NSE (`-sC`) do Nmap.
- [[naabu-varredura-atraves-proxies-socks5-connect-payload-ipv6]] — Veja também: Naabu em Operações Red Team e Pivoting: Varredura `CONNECT` via **Proxy SOCKS5 (`-proxy`, `-proxy-auth`)** e **`-connect-payload` (`-cp`)**.
- [[naabu-arquitetura-varredura-portas-syn-connect-udp-deduplicacao-ip]] — Referência cruzada direta com naabu-arquitetura-varredura-portas-syn-connect-udp-deduplicacao-ip.
- [[naabu-exclusao-cdn-waf-exclude-cdn-port-threshold-protecao]] — Referência cruzada direta com naabu-exclusao-cdn-waf-exclude-cdn-port-threshold-protecao.

## Fontes
- [ProjectDiscovery Naabu Official GitHub — Fast Port Scanner Written in Go](https://raw.githubusercontent.com/projectdiscovery/naabu/main/README.md) — repositório oficial do ProjectDiscovery Naabu cobrindo arquitetura SYN/CONNECT, flags CLI, descoberta de hosts e integração com Nmap; consultado em 2026-10-03.
- [ProjectDiscovery Naabu Official Documentation — Usage, Configuration & Rate Tuning](https://raw.githubusercontent.com/projectdiscovery/naabu/main/go.mod) — documentação oficial do Naabu na plataforma ProjectDiscovery Docs; consultado em 2026-10-03.
- [Go Package Documentation — github.com/projectdiscovery/naabu/v2](https://docs.projectdiscovery.io/tools/naabu/overview) — documentação técnica do pacote Go e SDK `naabu/v2/pkg/runner`; consultado em 2026-10-03.
