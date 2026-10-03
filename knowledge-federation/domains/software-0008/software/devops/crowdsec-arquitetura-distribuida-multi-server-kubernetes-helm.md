---
id: software.devops.tranche20.001979
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

# CrowdSec em Topologia Distribuída e Kubernetes: múltiplos `Log Processors` (DaemonSet) reportando para uma `LAPI` central

## Em uma frase
Em clusters Kubernetes ou frotas de dezenas de VMs, o CrowdSec opera em **arquitetura distribuída** (instalada via Helm chart oficial `crowdsec/crowdsec`): um `DaemonSet` de **Log Processors (`agent`)** lê os logs de containers (`/var/log/containers/*.log`) em cada worker node do cluster e envia os alertas para um `Deployment` central da **Local API (`lapi`)**, onde o Bouncer do Ingress Controller consulta as decisões.

## Por que importa
Se cada worker node do Kubernetes operasse uma LAPI isolada, um atacante cujas requisições HTTP caíssem em réplicas do Ingress espalhadas por 5 nós diferentes teria 5 vezes mais tentativas antes de ser detectado e só seria bloqueado em 1 dos 5 nós.

## Como funciona
Na instalação distribuída, novos nós de Log Processor registram-se na LAPI com `cscli lapi register -u http://lapi-service:8080` e são validados no servidor LAPI com `cscli machines validate <machine-name>` (ou automaticamente no Helm chart via token de registro em Secret).

## Exemplo
```bash
# No servidor central da Local API (LAPI), listando todas as máquinas de Log Processor registradas:
cscli machines list
```

## Limites e trade-offs
Para clusters com alto volume de alertas e múltiplos bouncers fazendo polling na LAPI, substitua o banco SQLite padrão da LAPI por **PostgreSQL** na seção `db_config` do `config.yaml`.

## Como verificar
Execute `cscli machines list` no Pod/servidor da LAPI para confirmar que todos os agentes/nós aparecem com `Status: ✔️`.

## Conexões
- [[crowdsec-central-api-capi-community-blocklist-compartilhamento-sinais]] — Veja também: CrowdSec Central API (`CAPI`) e Community Blocklist: inteligência coletiva de ameaças e privacidade dos sinais compartilhados.
- [[crowdsec-simulacao-modo-dry-run-prometheus-observabilidade-producao]] — Veja também: CrowdSec Mode de Simulação (`simulation.yaml`) e Observabilidade Prometheus: validação sem falsos positivos antes do bloqueio.

## Fontes
- [CrowdSec GitHub — README.md (Collaborative IPS, AppSec WAF on Coraza, Bot Detection PoW & Community Blocklist)](https://docs.crowdsec.net/docs/concepts/) — README oficial do crowdsecurity/crowdsec apresentando o motor comportamental, componente AppSec WAF compatível com ModSecurity/OWASP CRS e detecção de bots PoW; consultado em 2026-10-03.
- [CrowdSec Official Documentation — Concepts (Security Engine, Log Processor, Local API, Central API, Hub Collections, Scenarios & Bouncers)](https://raw.githubusercontent.com/crowdsecurity/crowdsec/master/README.md) — Documentação oficial de conceitos do CrowdSec detalhando Data Sources, Parsers, Enrichers, Scenarios Leaky Bucket, LAPI, Profiles, Decisions e Bouncers; consultado em 2026-10-03.
- [CrowdSec — Official GitHub Repository](https://github.com/crowdsecurity/crowdsec) — Repositório oficial MIT do CrowdSec; consultado em 2026-10-03.
