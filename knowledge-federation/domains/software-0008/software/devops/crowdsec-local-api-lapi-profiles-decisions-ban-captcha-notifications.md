---
id: software.devops.tranche20.001974
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

# CrowdSec Local API (`LAPI`) e `profiles.yaml`: conversão de Alertas em Decisões (`ban`, `captcha`), durações dinâmicas e notificações

## Em uma frase
A **Local API (`LAPI`)** é o componente central de estado do CrowdSec Security Engine: ela recebe os alertas emitidos pelos Log Processors, avalia o arquivo **`/etc/crowdsec/profiles.yaml`** para transformar cada alerta em uma ou mais **Decisions** (como `ban` por 4 horas ou `captcha` para tráfego web), aciona plugins de notificação (Slack, Webhook, Splunk, e-mail) e serve as decisões aos Bouncers.

## Por que importa
Separar o cenário de detecção ("houve um portscan") da decisão de resposta (`profiles.yaml`) permite que uma empresa decida aplicar um `captcha` de 1 hora na primeira infração de um IP residencial e um `ban` progressivo (`duration_expr`) para infratores reincidentes, sem alterar os cenários do Hub.

## Como funciona
Além das decisões automáticas geradas pelos perfis, o operador pode criar ou remover decisões manualmente via CLI com `cscli decisions add --ip 198.51.100.99 --duration 24h --type ban --reason "manual block"` ou `cscli decisions delete --ip 198.51.100.99`.

## Exemplo
```yaml
name: default_ip_remediation
filters:
  - Alert.Remediation == true && Alert.GetScope() == "Ip"
decisions:
  - type: ban
    duration: 4h
on_success: break
```

## Limites e trade-offs
Configure **Centralized AllowLists** (`cscli allowlists create`) na LAPI com as sub-redes da sua infraestrutura interna, IPs de monitoramento de uptime e gateways corporativos para garantir que nenhuma decisão de banimento seja emitida contra seus próprios sistemas.

## Como verificar
Execute `cscli allowlists list` e `cscli decisions list` para auditar as listas de permissão e os bloqueios ativos na LAPI.

## Conexões
- [[crowdsec-hub-collections-cscli-instalacao-atualizacao-deteccoes]] — Veja também: CrowdSec Hub e `Collections` (`cscli hub`): gerenciamento de pacotes de parsers, cenários e contextos de alerta.
- [[crowdsec-remediation-components-bouncers-firewall-nginx-traefik-cloudflare]] — Veja também: CrowdSec Remediation Components (`Bouncers`): aplicação de bloqueios em `nftables`/`iptables`, NGINX, Traefik, Ingress e Cloudflare.

## Fontes
- [CrowdSec GitHub — README.md (Collaborative IPS, AppSec WAF on Coraza, Bot Detection PoW & Community Blocklist)](https://docs.crowdsec.net/docs/concepts/) — README oficial do crowdsecurity/crowdsec apresentando o motor comportamental, componente AppSec WAF compatível com ModSecurity/OWASP CRS e detecção de bots PoW; consultado em 2026-10-03.
- [CrowdSec Official Documentation — Concepts (Security Engine, Log Processor, Local API, Central API, Hub Collections, Scenarios & Bouncers)](https://raw.githubusercontent.com/crowdsecurity/crowdsec/master/README.md) — Documentação oficial de conceitos do CrowdSec detalhando Data Sources, Parsers, Enrichers, Scenarios Leaky Bucket, LAPI, Profiles, Decisions e Bouncers; consultado em 2026-10-03.
- [CrowdSec — Official GitHub Repository](https://github.com/crowdsecurity/crowdsec) — Repositório oficial MIT do CrowdSec; consultado em 2026-10-03.
