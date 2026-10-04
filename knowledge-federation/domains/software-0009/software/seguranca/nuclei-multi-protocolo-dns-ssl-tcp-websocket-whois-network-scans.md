---
id: software.seguranca.tranche01.000054
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-01.md"
fontes: ["https://raw.githubusercontent.com/projectdiscovery/nuclei/main/README.md", "https://docs.projectdiscovery.io/opensource/nuclei/overview", "https://github.com/projectdiscovery/nuclei"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Nuclei Além do HTTP: templates multi-protocolo para auditoria de `DNS`, `SSL/TLS`, `TCP`, `WHOIS` e serviços de rede

## Em uma frase
O motor do Nuclei suporta nativamente múltiplos protocolos de rede além do HTTP: **`dns`** (verificação de takeover de subdomínio, registros SPF/DMARC, transferências de zona AXFR), **`ssl`** (inspeção de cifras fracas, TLS 1.0/1.1 depreciados, certificados expirados ou SANs), **`tcp`/`udp`** (envio de banners/payloads binários ou texto para portas de banco/cache como Redis, Memcached, SSH) e **`whois`**.

## Por que importa
Muitas falhas críticas de infraestrutura — como um subdomínio com `CNAME` órfão vulnerável a *Subdomain Takeover* ou uma porta Redis/Memcached exposta sem senha — ocorrem nas camadas DNS, TLS ou TCP pura.

## Como funciona
Passando uma lista de hosts/IPs (`-l hosts.txt`) ou CIDRs/ASNs, o Nuclei agrupa e executa os templates de rede e certificado TLS em paralelo com altíssima velocidade.

## Exemplo
```yaml
id: tls-deprecated-version-detect

info:
  name: Deprecated TLS 1.0/1.1 Protocol Enabled
  author: sec-team
  severity: medium
  tags: ssl,tls,misconfig

ssl:
  - address: "{{Host}}:{{Port}}"
    min_version: tls10
    max_version: tls11
    matchers:
      - type: dsl
        dsl:
          - "contains(version, 'tls10') || contains(version, 'tls11')"
```

## Limites e trade-offs
Ao rodar varreduras focadas apenas em DNS ou SSL sobre milhares de domínios, filtre por `-type dns` ou `-type ssl` para executar somente os templates daquele protocolo.

## Como verificar
Execute `nuclei -u example.com:443 -type ssl` para auditar rapidamente a postura TLS de um endpoint.

## Conexões
- [[nuclei-filtragem-templates-tags-severity-author-template-condition]] — Veja também: Nuclei Seleção e Filtragem de Templates: `-tags`, `-etags`, `-severity` (`critical,high`), `-tc` (Template Condition) e `-as` (Automatic Scan).
- [[nuclei-workflows-multi-step-flow-engine-variaveis-dinamicas]] — Veja também: Nuclei Workflows e `flow:` Engine: orquestração condicional multi-step e encadeamento de variáveis entre requisições.

## Fontes
- [ProjectDiscovery Nuclei GitHub — README.md (YAML Template Engine, Multi-Protocol Support, Filtering Flags, Rate Limiting & CI/CD Reporting)](https://raw.githubusercontent.com/projectdiscovery/nuclei/main/README.md) — README oficial do projectdiscovery/nuclei documentando instalação, flags de filtragem de templates, controle de concorrência, OAST Interactsh e formatos de saída; consultado em 2026-10-03.
- [ProjectDiscovery Official Documentation — Nuclei Overview (Template Anatomy, Matchers/Extractors, Request Clustering, Workflows & Authenticated Scans)](https://docs.projectdiscovery.io/opensource/nuclei/overview) — Visão geral oficial da documentação do Nuclei explicando a anatomia dos templates YAML, agrupamento de requisições, fluxos multi-step e varreduras autenticadas; consultado em 2026-10-03.
- [ProjectDiscovery Nuclei — Official GitHub Repository](https://github.com/projectdiscovery/nuclei) — Repositório oficial MIT do ProjectDiscovery Nuclei; consultado em 2026-10-03.
