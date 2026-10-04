---
id: software.seguranca.tranche09.000812
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

# Naabu: Exclusão Inteligente de **IPs de CDN / WAF (`-exclude-cdn` / `-ec`)** e Proteção contra Honeypots/Port-Spoofing (**`-port-threshold` / `-pts`**)

## Em uma frase
Ao realizar uma varredura de portas externas em centenas de subdomínios de uma organização, muitos subdomínios estão atrás de redes Anycast de **CDN / WAF** (como Cloudflare, Akamai, Fastly, CloudFront ou Incapsula): varrer 65.535 portas de um IP da Cloudflare é inútil (pois a Cloudflare responde em dezenas de portas proxy padrão como `80, 443, 2052, 2053, 2082, 2083, 2086, 2087, 2095, 2096, 8080, 8443, 8880` sem que aquilo seja o servidor real do cliente!) e desperdiça horas de scan.

## Por que importa
Usando a biblioteca `projectdiscovery/cdncheck` embutida, a flag **`-exclude-cdn` (`-ec`)** do Naabu identifica instantaneamente se o IP pertence a uma CDN/WAF conhecida e **pula a varredura completa de portas daquele IP, testando apenas as portas `80` e `443`**!

## Como funciona
Outro problema clássico em varreduras externas são firewalls com *SYN Proxy* ou honeypots (como `Portspoof`) que respondem `SYN-ACK` para todas as 65.535 portas: configurar **`-port-threshold 500` (`-pts 500`)** faz o Naabu abortar e descartar automaticamente qualquer host que aparente ter mais de 500 portas abertas!

## Exemplo
```bash
# Varrer as top 1000 portas pulando full-scan em IPs de CDN/WAF (-ec) e descartando hosts com mais de 200 portas falsas (-pts 200)
naabu -list /cases/easm/subdomains.txt \
  -top-ports 1000 \
  -exclude-cdn -display-cdn \
  -port-threshold 200 \
  -o /cases/easm/filtered_ports.txt
```

## Limites e trade-offs
A flag **`-display-cdn` (`-cdn`)** adiciona na saída o nome do provedor de CDN/WAF detectado (`[cloudflare]`, `[cloudfront]`, `[akamai]`), permitindo separar imediatamente quais ativos estão protegidos por WAF e quais **IPs de Origem (*Origin Servers*)** estão expostos diretamente na internet!

## Como verificar
Inspecione no JSON (`-json`) o campo `"cdn_name"` e filtre ativos com `"cdn": false` para priorizar testes nos servidores de origem.

## Conexões
- [[naabu-arquitetura-varredura-portas-syn-connect-udp-deduplicacao-ip]] — Veja também: ProjectDiscovery **Naabu**: Arquitetura de Varredura de Portas **SYN / CONNECT / UDP** em Go, Permutação `BlackRock` e **Deduplicação Automática de IP**.
- [[naabu-enumeracao-passiva-shodan-internetdb-passive-zero-pacotes]] — Veja também: Naabu **`-passive`**: Enumeração Passiva Instantânea de Portas Abertas via **Shodan InternetDB** com Zero Pacotes Enviados ao Alvo.
- [[dnsx-deteccao-asn-cdn-filtragem-wildcards-auto-wildcard-wd]] — Referência cruzada direta com dnsx-deteccao-asn-cdn-filtragem-wildcards-auto-wildcard-wd.
- [[masscan-controle-taxa-rate-pf-ring-excludefile-protecao-rede]] — Referência cruzada direta com masscan-controle-taxa-rate-pf-ring-excludefile-protecao-rede.

## Fontes
- [ProjectDiscovery Naabu Official GitHub — Fast Port Scanner Written in Go](https://raw.githubusercontent.com/projectdiscovery/naabu/main/README.md) — repositório oficial do ProjectDiscovery Naabu cobrindo arquitetura SYN/CONNECT, flags CLI, descoberta de hosts e integração com Nmap; consultado em 2026-10-03.
- [ProjectDiscovery Naabu Official Documentation — Usage, Configuration & Rate Tuning](https://raw.githubusercontent.com/projectdiscovery/naabu/main/go.mod) — documentação oficial do Naabu na plataforma ProjectDiscovery Docs; consultado em 2026-10-03.
- [Go Package Documentation — github.com/projectdiscovery/naabu/v2](https://docs.projectdiscovery.io/tools/naabu/overview) — documentação técnica do pacote Go e SDK `naabu/v2/pkg/runner`; consultado em 2026-10-03.
