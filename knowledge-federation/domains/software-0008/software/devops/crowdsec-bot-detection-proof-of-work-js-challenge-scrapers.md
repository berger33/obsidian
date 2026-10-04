---
id: software.devops.tranche20.001977
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

# CrowdSec Bot & Scraper Detection: desafios JavaScript *Proof-of-Work (PoW)* e proteção contra navegadores headless

## Em uma frase
Conforme destacado na documentação oficial do CrowdSec, o componente **AppSec** inclui capacidades avançadas de **detecção de bots e scrapers**, podendo responder a requisições suspeitas com um **desafio JavaScript *Proof-of-Work (PoW)*** de dificuldade ajustável ou CAPTCHA, barrando navegadores headless e scrapers agressivos enquanto libera crawlers legítimos verificados (como `Googlebot` ou `Bingbot`).

## Por que importa
Com a explosão de scrapers automatizados e bots de treinamento de IA que varrem sites e APIs inteiras distribuídos por milhares de IPs residenciais/móveis, bloquear apenas por taxa simples de IP gera falsos positivos para usuários atrás de CGNAT.

## Como funciona
Quando um comportamento de scraping ou fingerprint suspeito é detectado, em vez de emitir um banimento cego (`403 Forbidden`), o CrowdSec instrui o componente de remediação a exigir um desafio PoW em JavaScript no navegador do cliente, encarecendo computacionalmente a raspagem automatizada em larga escala.

## Exemplo
```bash
# Verificando parsers de whitelists de crawlers de busca legítimos (SEO) instalados no Hub:
cscli parsers install crowdsecurity/whitelists crowdsecurity/seo-bots-whitelist
cscli postoverflows list
```

## Limites e trade-offs
Instale o postoverflow `crowdsecurity/seo-bots-whitelist` (que faz verificação reversa e direta de DNS dos ranges do Googlebot/Bingbot apenas quando um bucket transborda) para nunca penalizar a indexação de SEO do seu site.

## Como verificar
Inspecione os `postoverflows` ativos com `cscli postoverflows list` e as métricas de decisões por tipo (`ban` vs `captcha`) em `cscli decisions list`.

## Conexões
- [[crowdsec-appsec-waf-coraza-seclang-owasp-crs-virtual-patching]] — Veja também: CrowdSec AppSec Component (WAF): inspeção HTTP em tempo real sobre `Coraza`, compatibilidade `SecLang`/OWASP CRS e regras YAML.
- [[crowdsec-central-api-capi-community-blocklist-compartilhamento-sinais]] — Veja também: CrowdSec Central API (`CAPI`) e Community Blocklist: inteligência coletiva de ameaças e privacidade dos sinais compartilhados.

## Fontes
- [CrowdSec GitHub — README.md (Collaborative IPS, AppSec WAF on Coraza, Bot Detection PoW & Community Blocklist)](https://raw.githubusercontent.com/crowdsecurity/crowdsec/master/README.md) — README oficial do crowdsecurity/crowdsec apresentando o motor comportamental, componente AppSec WAF compatível com ModSecurity/OWASP CRS e detecção de bots PoW; consultado em 2026-10-03.
- [CrowdSec Official Documentation — Concepts (Security Engine, Log Processor, Local API, Central API, Hub Collections, Scenarios & Bouncers)](https://docs.crowdsec.net/docs/concepts/) — Documentação oficial de conceitos do CrowdSec detalhando Data Sources, Parsers, Enrichers, Scenarios Leaky Bucket, LAPI, Profiles, Decisions e Bouncers; consultado em 2026-10-03.
- [CrowdSec — Official GitHub Repository](https://github.com/crowdsecurity/crowdsec) — Repositório oficial MIT do CrowdSec; consultado em 2026-10-03.
