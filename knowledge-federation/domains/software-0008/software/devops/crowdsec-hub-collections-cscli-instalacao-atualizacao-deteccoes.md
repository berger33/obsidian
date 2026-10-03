---
id: software.devops.tranche20.001973
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

# CrowdSec Hub e `Collections` (`cscli hub`): gerenciamento de pacotes de parsers, cenários e contextos de alerta

## Em uma frase
O **CrowdSec Hub** (`hub.crowdsec.net`) é o repositório aberto (licenciado sob MIT) onde a comunidade e a equipe do CrowdSec publicam **Collections** — pacotes coerentes que agrupam `parsers`, `scenarios`, `postoverflows` e `appsec-rules` para uma tecnologia específica (como `crowdsecurity/linux`, `crowdsecurity/nginx`, `crowdsecurity/traefik`, `crowdsecurity/kubernetes-audit`).

## Por que importa
Escrever expressões regulares Grok e cenários de detecção do zero para dezenas de serviços (SSH, NGINX, PostgreSQL, Nextcloud, Keycloak) consumiria semanas; instalar uma Collection oficial entrega toda a árvore de dependências pronta.

## Como funciona
A ferramenta **`cscli`** gerencia todo o ciclo de vida de conteúdo do Hub: `cscli hub update` atualiza o índice local, `cscli collections install crowdsecurity/nginx` instala os parsers e cenários do NGINX e `cscli hub upgrade` atualiza todas as coleções instaladas para as versões mais recentes.

## Exemplo
```bash
cscli hub update
cscli collections install crowdsecurity/linux crowdsecurity/nginx
cscli hub upgrade
systemctl reload crowdsec
```

## Limites e trade-offs
Se você editar manualmente um arquivo YAML baixado do Hub dentro de `/etc/crowdsec/scenarios/`, ele ficará marcado como `tainted` (modificado localmente) e deixará de receber atualizações automáticas no `cscli hub upgrade`.

## Como verificar
Liste todas as coleções, parsers e cenários instalados e verifique se algum item está `tainted` com `cscli collections list` e `cscli scenarios list`.

## Conexões
- [[crowdsec-log-processor-acquis-parsers-enrichers-scenarios-leaky-bucket]] — Veja também: CrowdSec Log Processor (`LP`): pipeline de aquisição (`acquis.yaml`), `Parsers`, `Enrichers` e `Scenarios` baseados em *Leaky Bucket*.
- [[crowdsec-local-api-lapi-profiles-decisions-ban-captcha-notifications]] — Veja também: CrowdSec Local API (`LAPI`) e `profiles.yaml`: conversão de Alertas em Decisões (`ban`, `captcha`), durações dinâmicas e notificações.

## Fontes
- [CrowdSec GitHub — README.md (Collaborative IPS, AppSec WAF on Coraza, Bot Detection PoW & Community Blocklist)](https://docs.crowdsec.net/docs/concepts/) — README oficial do crowdsecurity/crowdsec apresentando o motor comportamental, componente AppSec WAF compatível com ModSecurity/OWASP CRS e detecção de bots PoW; consultado em 2026-10-03.
- [CrowdSec Official Documentation — Concepts (Security Engine, Log Processor, Local API, Central API, Hub Collections, Scenarios & Bouncers)](https://raw.githubusercontent.com/crowdsecurity/crowdsec/master/README.md) — Documentação oficial de conceitos do CrowdSec detalhando Data Sources, Parsers, Enrichers, Scenarios Leaky Bucket, LAPI, Profiles, Decisions e Bouncers; consultado em 2026-10-03.
- [CrowdSec — Official GitHub Repository](https://github.com/crowdsecurity/crowdsec) — Repositório oficial MIT do CrowdSec; consultado em 2026-10-03.
