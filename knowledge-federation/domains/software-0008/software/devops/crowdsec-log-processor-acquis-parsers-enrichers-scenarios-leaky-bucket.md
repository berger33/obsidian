---
id: software.devops.tranche20.001972
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

# CrowdSec Log Processor (`LP`): pipeline de aquisição (`acquis.yaml`), `Parsers`, `Enrichers` e `Scenarios` baseados em *Leaky Bucket*

## Em uma frase
O **Log Processor (`LP`)** do CrowdSec ingere eventos de múltiplas fontes de dados (`file`, `journalctl`, `syslog`, `docker`, `kubernetes`, `kafka`, `cloudwatch`, `appsec`), normaliza e enriquece cada evento por meio de **Parsers** e **Enrichers** (GeoIP, ASN, rDNS) e avalia comportamentos maliciosos usando **Scenarios** baseados no algoritmo **Leaky Bucket**.

## Por que importa
Bloquear um IP na primeira falha de senha puniria usuários legítimos que erraram a digitação; já um *Leaky Bucket* com capacidade `capacity: 5` e velocidade de vazamento `leakspeed: 10s` agrupado por `evt.Meta.source_ip` detecta com precisão rajadas de força bruta ou varreduras lentas.

## Como funciona
Quando um evento enriquecido corresponde ao `filter` de um cenário YAML (ex.: `crowdsecurity/ssh-bf` ou `crowdsecurity/http-probing`), ele é despejado no bucket correspondente. Se o bucket transbordar (*overflow*), o Log Processor gera um **Alert** contendo o contexto e o envia para a `LAPI`.

## Exemplo
```bash
# Testando como o CrowdSec faz parsing e avalia cenários sobre uma linha de log com cscli explain:
cscli explain --log '198.51.100.77 - - [03/Oct/2026:12:00:01 +0000] "GET /.env HTTP/1.1" 404 153 "-" "curl/8.5.0"' --type nginx
```

## Limites e trade-offs
O comando **`cscli explain`** é a ferramenta mais valiosa para depurar parsers e cenários: ele mostra passo a passo na árvore visual quais parsers transformaram a linha de log e em quais buckets de cenários o evento entrou.

## Como verificar
Execute `cscli explain --file /var/log/nginx/access.log --type nginx` para auditar o funcionamento dos parsers sobre seus logs reais.

## Conexões
- [[crowdsec-arquitetura-detect-here-remedy-there-log-processor-lapi-bouncers]] — Veja também: CrowdSec: arquitetura colaborativa *Detect Here, Remedy There* com `Log Processor`, `Local API (LAPI)`, `Bouncers` e `Central API`.
- [[crowdsec-hub-collections-cscli-instalacao-atualizacao-deteccoes]] — Veja também: CrowdSec Hub e `Collections` (`cscli hub`): gerenciamento de pacotes de parsers, cenários e contextos de alerta.

## Fontes
- [CrowdSec GitHub — README.md (Collaborative IPS, AppSec WAF on Coraza, Bot Detection PoW & Community Blocklist)](https://docs.crowdsec.net/docs/concepts/) — README oficial do crowdsecurity/crowdsec apresentando o motor comportamental, componente AppSec WAF compatível com ModSecurity/OWASP CRS e detecção de bots PoW; consultado em 2026-10-03.
- [CrowdSec Official Documentation — Concepts (Security Engine, Log Processor, Local API, Central API, Hub Collections, Scenarios & Bouncers)](https://raw.githubusercontent.com/crowdsecurity/crowdsec/master/README.md) — Documentação oficial de conceitos do CrowdSec detalhando Data Sources, Parsers, Enrichers, Scenarios Leaky Bucket, LAPI, Profiles, Decisions e Bouncers; consultado em 2026-10-03.
- [CrowdSec — Official GitHub Repository](https://github.com/crowdsecurity/crowdsec) — Repositório oficial MIT do CrowdSec; consultado em 2026-10-03.
