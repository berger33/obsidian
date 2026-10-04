---
id: software.devops.tranche20.001971
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-20.md"
fontes: ["https://raw.githubusercontent.com/crowdsecurity/crowdsec/master/README.md", "https://docs.crowdsec.net/docs/concepts/", "https://github.com/crowdsecurity/crowdsec"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# CrowdSec: arquitetura colaborativa *Detect Here, Remedy There* com `Log Processor`, `Local API (LAPI)`, `Bouncers` e `Central API`

## Em uma frase
O **CrowdSec** (licenciado sob MIT) é uma solução de segurança open-source colaborativa que combina **IDS/IPS**, **WAF (AppSec)** e detecção de bots sob a filosofia **"Detect Here, Remedy There"**, separando a detecção de ataques (**Security Engine**: `Log Processor` + `Local API`) da aplicação do bloqueio (**Remediation Components / Bouncers**).

## Por que importa
No `fail2ban` tradicional, a leitura de logs e o bloqueio de IP no `iptables` são acoplados na mesma máquina; em arquiteturas modernas (Kubernetes, proxies reversos, CDNs Cloudflare/AWS WAF), você analisa logs nos Pods ou servidores de aplicação mas precisa aplicar o bloqueio na borda da rede.

## Como funciona
Conforme a documentação oficial de conceitos do CrowdSec, a arquitetura divide-se em: 1) **Log Processor (`LP`)**: adquire logs e requisições HTTP, faz parsing/enriquecimento e avalia *scenarios* e *AppSec rules*; 2) **Local API (`LAPI`)**: recebe *alerts* dos Log Processors, converte-os em *decisions* (`ban`, `captcha`) conforme `profiles.yaml` e serve essas decisões; 3) **Remediation Components (`Bouncers`)**: consultam a LAPI para aplicar os bloqueios em firewalls, NGINX, Traefik, HAProxy, Ingress ou Cloudflare; e 4) **Central API (`CAPI`)**: compartilha sinais anônimos de ataque e distribui a **Community Blocklist**.

## Exemplo
```bash
# Inspecionando métricas de aquisição/parsing, alertas recentes e decisões ativas via cscli:
cscli metrics
cscli alerts list
cscli decisions list
```

## Limites e trade-offs
O Security Engine pode rodar tanto em modo **standalone** (`LP` + `LAPI` na mesma máquina) quanto em modo **distribuído multi-servidor** (vários nós `LP` enviando alertas para uma única `LAPI` central apoiada por SQLite, PostgreSQL ou MySQL).

## Como verificar
Execute `cscli lapi status` e `cscli capi status` para verificar a conectividade do motor com a API local e com a Central API.

## Conexões
- [[crowdsec-log-processor-acquis-parsers-enrichers-scenarios-leaky-bucket]] — Veja também: CrowdSec Log Processor (`LP`): pipeline de aquisição (`acquis.yaml`), `Parsers`, `Enrichers` e `Scenarios` baseados em *Leaky Bucket*.

## Fontes
- [CrowdSec GitHub — README.md (Collaborative IPS, AppSec WAF on Coraza, Bot Detection PoW & Community Blocklist)](https://raw.githubusercontent.com/crowdsecurity/crowdsec/master/README.md) — README oficial do crowdsecurity/crowdsec apresentando o motor comportamental, componente AppSec WAF compatível com ModSecurity/OWASP CRS e detecção de bots PoW; consultado em 2026-10-03.
- [CrowdSec Official Documentation — Concepts (Security Engine, Log Processor, Local API, Central API, Hub Collections, Scenarios & Bouncers)](https://docs.crowdsec.net/docs/concepts/) — Documentação oficial de conceitos do CrowdSec detalhando Data Sources, Parsers, Enrichers, Scenarios Leaky Bucket, LAPI, Profiles, Decisions e Bouncers; consultado em 2026-10-03.
- [CrowdSec — Official GitHub Repository](https://github.com/crowdsecurity/crowdsec) — Repositório oficial MIT do CrowdSec; consultado em 2026-10-03.
