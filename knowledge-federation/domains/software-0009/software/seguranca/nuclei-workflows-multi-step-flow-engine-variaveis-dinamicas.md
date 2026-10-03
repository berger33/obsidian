---
id: software.seguranca.tranche01.000055
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-01.md"
fontes: ["https://docs.projectdiscovery.io/opensource/nuclei/overview", "https://raw.githubusercontent.com/projectdiscovery/nuclei/main/README.md", "https://github.com/projectdiscovery/nuclei"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Nuclei Workflows e `flow:` Engine: orquestração condicional multi-step e encadeamento de variáveis entre requisições

## Em uma frase
Para cenários onde uma verificação depende do resultado da anterior, o Nuclei oferece **Workflows (`workflows:`)** (que encadeiam subtemplates somente se o template anterior detectar uma tecnologia específica) e o motor de **Fluxo (`flow:` em JavaScript)** dentro de um template (para lógica condicional e loops entre múltiplas requisições).

## Por que importa
Por exemplo, não faz sentido executar 40 templates de vulnerabilidades de plugins do Grafana contra um host se a primeira requisição confirmar que aquele host não é um servidor Grafana.

## Como funciona
Em um template multi-request ou workflow, valores capturados na Requisição 1 por um `extractor` com `internal: true` (como um `csrf_token` ou `session_id`) ficam imediatamente disponíveis como variável `{{csrf_token}}` na Requisição 2 do mesmo fluxo!

## Exemplo
```yaml
id: grafana-conditional-workflow

info:
  name: Grafana Detection and CVE Workflow
  author: sec-team
  severity: info

workflows:
  - template: technologies/grafana-detect.yaml
    subtemplates:
      - tags: grafana
```

## Limites e trade-offs
Use `extractors` com `internal: true` para passar tokens dinâmicos (CSRF, nonces, IDs criados) de um passo HTTP `POST` para o passo subsequente de verificação.

## Como verificar
Valide o seu workflow executando `nuclei -w ./grafana-workflow.yaml -u https://staging.example.com`.

## Conexões
- [[nuclei-multi-protocolo-dns-ssl-tcp-websocket-whois-network-scans]] — Veja também: Nuclei Além do HTTP: templates multi-protocolo para auditoria de `DNS`, `SSL/TLS`, `TCP`, `WHOIS` e serviços de rede.
- [[nuclei-interactsh-oast-out-of-band-blind-ssrf-rce-log4shell]] — Veja também: Nuclei OAST com `Interactsh` (`{{interactsh-url}}`): detecção *Out-of-Band* sem falsos positivos para Blind SSRF, XXE e RCE.

## Fontes
- [ProjectDiscovery Nuclei GitHub — README.md (YAML Template Engine, Multi-Protocol Support, Filtering Flags, Rate Limiting & CI/CD Reporting)](https://docs.projectdiscovery.io/opensource/nuclei/overview) — README oficial do projectdiscovery/nuclei documentando instalação, flags de filtragem de templates, controle de concorrência, OAST Interactsh e formatos de saída; consultado em 2026-10-03.
- [ProjectDiscovery Official Documentation — Nuclei Overview (Template Anatomy, Matchers/Extractors, Request Clustering, Workflows & Authenticated Scans)](https://raw.githubusercontent.com/projectdiscovery/nuclei/main/README.md) — Visão geral oficial da documentação do Nuclei explicando a anatomia dos templates YAML, agrupamento de requisições, fluxos multi-step e varreduras autenticadas; consultado em 2026-10-03.
- [ProjectDiscovery Nuclei — Official GitHub Repository](https://github.com/projectdiscovery/nuclei) — Repositório oficial MIT do ProjectDiscovery Nuclei; consultado em 2026-10-03.
