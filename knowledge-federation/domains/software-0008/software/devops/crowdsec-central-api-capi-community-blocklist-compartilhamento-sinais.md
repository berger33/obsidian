---
id: software.devops.tranche20.001978
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

# CrowdSec Central API (`CAPI`) e Community Blocklist: inteligência coletiva de ameaças e privacidade dos sinais compartilhados

## Em uma frase
A **Central API (`CAPI`)** do CrowdSec conecta os motores participantes à rede global de inteligência de ameaças: os Security Engines reportam sinais minimalistas de ataques bloqueados localmente e recebem de volta em tempo real a **Community Blocklist** — uma lista curada de endereços IP maliciosos confirmados que são bloqueados preventivamente antes mesmo de tocarem nos seus servidores.

## Por que importa
Quando uma botnet varre a internet explorando uma nova vulnerabilidade, se o IP atacante já foi detectado nos minutos anteriores por dezenas de outros participantes do CrowdSec, sua infraestrutura já terá esse IP bloqueado no firewall/proxy quando ele tentar a primeira conexão.

## Como funciona
Por privacidade, um sinal enviado à `CAPI` contém **apenas** o IP do atacante, o nome do cenário disparado e o timestamp — jamais enviando as linhas de log brutas, URLs internas ou dados de usuários. E para ambientes *air-gapped* ou que não desejam compartilhar sinais, a comunicação com a CAPI pode ser desabilitada no `config.yaml` (`online_client`).

## Exemplo
```bash
# Verificando as decisões recebidas da Community Blocklist (origem CAPI):
cscli decisions list --origin CAPI
```

## Limites e trade-offs
Somente cenários oficiais do Hub que estão intactos (não marcados como `tainted` nem customizados localmente) têm seus sinais compartilhados com a `CAPI`, evitando poluir a rede global com regras experimentais.

## Como verificar
Execute `cscli decisions list -o CAPI | wc -l` para ver quantos IPs maliciosos da Community Blocklist estão sendo bloqueados proativamente no seu ambiente.

## Conexões
- [[crowdsec-bot-detection-proof-of-work-js-challenge-scrapers]] — Veja também: CrowdSec Bot & Scraper Detection: desafios JavaScript *Proof-of-Work (PoW)* e proteção contra navegadores headless.
- [[crowdsec-arquitetura-distribuida-multi-server-kubernetes-helm]] — Veja também: CrowdSec em Topologia Distribuída e Kubernetes: múltiplos `Log Processors` (DaemonSet) reportando para uma `LAPI` central.

## Fontes
- [CrowdSec GitHub — README.md (Collaborative IPS, AppSec WAF on Coraza, Bot Detection PoW & Community Blocklist)](https://docs.crowdsec.net/docs/concepts/) — README oficial do crowdsecurity/crowdsec apresentando o motor comportamental, componente AppSec WAF compatível com ModSecurity/OWASP CRS e detecção de bots PoW; consultado em 2026-10-03.
- [CrowdSec Official Documentation — Concepts (Security Engine, Log Processor, Local API, Central API, Hub Collections, Scenarios & Bouncers)](https://raw.githubusercontent.com/crowdsecurity/crowdsec/master/README.md) — Documentação oficial de conceitos do CrowdSec detalhando Data Sources, Parsers, Enrichers, Scenarios Leaky Bucket, LAPI, Profiles, Decisions e Bouncers; consultado em 2026-10-03.
- [CrowdSec — Official GitHub Repository](https://github.com/crowdsecurity/crowdsec) — Repositório oficial MIT do CrowdSec; consultado em 2026-10-03.
