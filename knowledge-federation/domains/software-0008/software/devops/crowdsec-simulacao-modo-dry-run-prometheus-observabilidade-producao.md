---
id: software.devops.tranche20.001980
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

# CrowdSec Mode de Simulação (`simulation.yaml`) e Observabilidade Prometheus: validação sem falsos positivos antes do bloqueio

## Em uma frase
Antes de ativar um novo cenário de detecção ou regra em produção com bloqueio real, o arquivo **`/etc/crowdsec/simulation.yaml`** (gerenciado via **`cscli simulation`**) permite colocar qualquer cenário individual (ou todos os cenários globalmente) em **Modo de Simulação**, além de exportar métricas detalhadas para o **Prometheus** (`:6060/metrics`).

## Por que importa
Ativar um cenário agressivo de detecção de HTTP crawling ou API rate-limiting diretamente em modo de bloqueio pode barrar integrações de parceiros B2B ou aplicativos móveis legítimos caso o limiar precise de ajuste.

## Como funciona
Quando um cenário está em modo de simulação (`cscli simulation enable crowdsecurity/http-crawl-non_statics`), o Log Processor continua processando os logs normalmente, a LAPI registra o alerta e cria a decisão marcada como `simulated: true`, mas os **Bouncers ignoram decisões simuladas** por padrão, permitindo auditar no painel ou no Prometheus exatamente quem teria sido bloqueado.

## Exemplo
```bash
# Habilitando modo de simulação para um cenário específico e verificando seu status:
cscli simulation enable crowdsecurity/http-crawl-non_statics
cscli simulation status
```

## Limites e trade-offs
Monitore o endpoint Prometheus do CrowdSec (`http://127.0.0.1:6060/metrics`) para acompanhar taxas de linhas lidas vs linhas parseadas (`cs_parser_hits_ok_total` vs `cs_parser_hits_ko_total`); um aumento súbito em `ko` indica que o formato de log da aplicação mudou.

## Como verificar
Execute `cscli simulation status` e `cscli alerts list` para auditar alertas simulados antes de desativar a simulação em produção.

## Conexões
- [[crowdsec-arquitetura-distribuida-multi-server-kubernetes-helm]] — Veja também: CrowdSec em Topologia Distribuída e Kubernetes: múltiplos `Log Processors` (DaemonSet) reportando para uma `LAPI` central.

## Fontes
- [CrowdSec GitHub — README.md (Collaborative IPS, AppSec WAF on Coraza, Bot Detection PoW & Community Blocklist)](https://docs.crowdsec.net/docs/concepts/) — README oficial do crowdsecurity/crowdsec apresentando o motor comportamental, componente AppSec WAF compatível com ModSecurity/OWASP CRS e detecção de bots PoW; consultado em 2026-10-03.
- [CrowdSec Official Documentation — Concepts (Security Engine, Log Processor, Local API, Central API, Hub Collections, Scenarios & Bouncers)](https://raw.githubusercontent.com/crowdsecurity/crowdsec/master/README.md) — Documentação oficial de conceitos do CrowdSec detalhando Data Sources, Parsers, Enrichers, Scenarios Leaky Bucket, LAPI, Profiles, Decisions e Bouncers; consultado em 2026-10-03.
- [CrowdSec — Official GitHub Repository](https://github.com/crowdsecurity/crowdsec) — Repositório oficial MIT do CrowdSec; consultado em 2026-10-03.
