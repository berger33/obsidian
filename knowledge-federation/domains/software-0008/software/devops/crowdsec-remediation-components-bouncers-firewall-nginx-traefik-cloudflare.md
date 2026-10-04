---
id: software.devops.tranche20.001975
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
fontes: ["https://docs.crowdsec.net/docs/concepts/", "https://raw.githubusercontent.com/crowdsecurity/crowdsec/master/README.md", "https://github.com/crowdsecurity/crowdsec"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# CrowdSec Remediation Components (`Bouncers`): aplicação de bloqueios em `nftables`/`iptables`, NGINX, Traefik, Ingress e Cloudflare

## Em uma frase
Os **Remediation Components** (também conhecidos como **Bouncers**) são agentes externos leves que se autenticam na `Local API (LAPI)` usando uma chave gerada por **`cscli bouncers add`** e aplicam as decisões (`ban`, `captcha`) diretamente na camada de infraestrutura mais adequada.

## Por que importa
Enquanto um bouncer de firewall (`cs-firewall-bouncer` usando conjuntos `ipset`/`nftables` no kernel Linux) descarta pacotes TCP/UDP na camada L3/L4 com custo quase zero de CPU, um bouncer de proxy reverso (NGINX, Traefik, Envoy, Ingress-NGINX) ou CDN (Cloudflare, AWS WAF) consegue enxergar o IP real do cliente atrás de `X-Forwarded-For` e exibir páginas de **CAPTCHA** em vez de apenas cortar a conexão.

## Como funciona
Os Bouncers operam em modo *stream* (consultando periodicamente `/v1/decisions/stream` na LAPI para manter um cache em memória local ultra-rápido) ou em modo *live* (consultando a LAPI sob demanda).

## Exemplo
```bash
# Registrando uma chave de API na LAPI para um novo Bouncer de firewall ou Traefik:
cscli bouncers add prod-edge-traefik-bouncer
cscli bouncers list
```

## Limites e trade-offs
Na saída de `cscli bouncers list`, verifique a coluna `Last API Pull`: se um bouncer registrado não estiver fazendo pull há vários minutos, os bloqueios gerados pela LAPI não estarão sendo aplicados naquele ponto de borda.

## Como verificar
Execute `cscli bouncers list` para auditar todos os Remediation Components conectados, seus IPs, versões e horário do último pull.

## Conexões
- [[crowdsec-local-api-lapi-profiles-decisions-ban-captcha-notifications]] — Veja também: CrowdSec Local API (`LAPI`) e `profiles.yaml`: conversão de Alertas em Decisões (`ban`, `captcha`), durações dinâmicas e notificações.
- [[crowdsec-appsec-waf-coraza-seclang-owasp-crs-virtual-patching]] — Veja também: CrowdSec AppSec Component (WAF): inspeção HTTP em tempo real sobre `Coraza`, compatibilidade `SecLang`/OWASP CRS e regras YAML.

## Fontes
- [CrowdSec GitHub — README.md (Collaborative IPS, AppSec WAF on Coraza, Bot Detection PoW & Community Blocklist)](https://docs.crowdsec.net/docs/concepts/) — README oficial do crowdsecurity/crowdsec apresentando o motor comportamental, componente AppSec WAF compatível com ModSecurity/OWASP CRS e detecção de bots PoW; consultado em 2026-10-03.
- [CrowdSec Official Documentation — Concepts (Security Engine, Log Processor, Local API, Central API, Hub Collections, Scenarios & Bouncers)](https://raw.githubusercontent.com/crowdsecurity/crowdsec/master/README.md) — Documentação oficial de conceitos do CrowdSec detalhando Data Sources, Parsers, Enrichers, Scenarios Leaky Bucket, LAPI, Profiles, Decisions e Bouncers; consultado em 2026-10-03.
- [CrowdSec — Official GitHub Repository](https://github.com/crowdsecurity/crowdsec) — Repositório oficial MIT do CrowdSec; consultado em 2026-10-03.
