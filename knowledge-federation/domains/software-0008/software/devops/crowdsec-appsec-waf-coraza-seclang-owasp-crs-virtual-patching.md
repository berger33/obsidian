---
id: software.devops.tranche20.001976
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

# CrowdSec AppSec Component (WAF): inspeção HTTP em tempo real sobre `Coraza`, compatibilidade `SecLang`/OWASP CRS e regras YAML

## Em uma frase
O componente **AppSec** do CrowdSec transforma o Security Engine em um **Web Application Firewall (WAF)** moderno construído sobre o motor **Coraza**, capaz de carregar regras **SecLang** (ModSecurity) e o **OWASP Core Rule Set (CRS)** sem modificações, além de um formato nativo de regras YAML para *virtual patching* de CVEs recém-divulgadas.

## Por que importa
Analisar apenas logs de acesso HTTP *após* a requisição já ter sido processada pelo backend (`Log Processor` tradicional) não impede que o primeiro pacote de um exploit de *Remote Code Execution* (como Log4Shell ou SQL Injection) atinja a aplicação vulnerável.

## Como funciona
Com o AppSec habilitado, o proxy reverso (NGINX, Traefik, HAProxy, Envoy) envia a requisição HTTP em tempo real (*in-band*) para a porta do componente AppSec do CrowdSec: 1) regras críticas de virtual patching (`inband_rules`) bloqueiam a requisição maliciosa imediatamente com HTTP `403` antes que ela chegue ao backend; e 2) regras mais pesadas ou comportamentais (`outofband_rules`) são avaliadas de forma assíncrona sem adicionar latência à requisição do usuário, alimentando a mesma camada de reputação de IP e `LAPI`!

## Exemplo
```bash
# Instalando a coleção de virtual patching e regras genéricas do AppSec a partir do Hub:
cscli collections install crowdsecurity/appsec-virtual-patching crowdsecurity/appsec-generic-rules
cscli appsec-configs list
cscli appsec-rules list
```

## Limites e trade-offs
Combinar regras *in-band* (bloqueio síncrono do exploit) com cenários de múltiplos eventos (banimento do IP por 4h na LAPI se o mesmo IP disparar 3 regras AppSec) une o melhor de um WAF com o melhor de um IPS comportamental.

## Como verificar
Execute `cscli metrics show appsec` para monitorar o volume de requisições inspecionadas e bloqueadas pelo motor AppSec.

## Conexões
- [[crowdsec-remediation-components-bouncers-firewall-nginx-traefik-cloudflare]] — Veja também: CrowdSec Remediation Components (`Bouncers`): aplicação de bloqueios em `nftables`/`iptables`, NGINX, Traefik, Ingress e Cloudflare.
- [[crowdsec-bot-detection-proof-of-work-js-challenge-scrapers]] — Veja também: CrowdSec Bot & Scraper Detection: desafios JavaScript *Proof-of-Work (PoW)* e proteção contra navegadores headless.

## Fontes
- [CrowdSec GitHub — README.md (Collaborative IPS, AppSec WAF on Coraza, Bot Detection PoW & Community Blocklist)](https://raw.githubusercontent.com/crowdsecurity/crowdsec/master/README.md) — README oficial do crowdsecurity/crowdsec apresentando o motor comportamental, componente AppSec WAF compatível com ModSecurity/OWASP CRS e detecção de bots PoW; consultado em 2026-10-03.
- [CrowdSec Official Documentation — Concepts (Security Engine, Log Processor, Local API, Central API, Hub Collections, Scenarios & Bouncers)](https://docs.crowdsec.net/docs/concepts/) — Documentação oficial de conceitos do CrowdSec detalhando Data Sources, Parsers, Enrichers, Scenarios Leaky Bucket, LAPI, Profiles, Decisions e Bouncers; consultado em 2026-10-03.
- [CrowdSec — Official GitHub Repository](https://github.com/crowdsecurity/crowdsec) — Repositório oficial MIT do CrowdSec; consultado em 2026-10-03.
