---
id: software.seguranca.tranche01.000042
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
fontes: ["https://www.zaproxy.org/docs/automate/automation-framework/", "https://raw.githubusercontent.com/zaproxy/zaproxy/main/README.md", "https://github.com/zaproxy/zaproxy"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# ZAP Automation Framework (`zap.sh -cmd -autorun`): controle declarativo em arquivo YAML único para CI/CD

## Em uma frase
Conforme a documentação oficial do ZAP, o **Automation Framework** controla todo o ciclo de vida do ZAP através de **um único arquivo YAML** (`env:` + `jobs:`), substituindo progressivamente as opções legadas de linha de comando e os antigos scripts Python de *Packaged Scans* (`zap-baseline.py`, `zap-full-scan.py`, `zap-api-scan.py`) sem acoplamento a uma tecnologia específica de container.

## Por que importa
Os antigos scripts empacotados em Docker eram difíceis de depurar localmente fora do container e limitados quando a equipe precisava encadear autenticação complexa, importação de múltiplos schemas, filtros de alerta e assertions de qualidade.

## Como funciona
No plano YAML do Automation Framework: a seção **`env:`** declara os `contexts` (URLs incluídas/excluídas, autenticação, gerenciamento de sessão, tecnologia do alvo) e `parameters` (`failOnError`, `progressToStdout`), enquanto a lista ordenada **`jobs:`** executa cada etapa (`passiveScan-config`, `openapi`, `spider`, `spiderAjax`, `passiveScan-wait`, `activeScan`, `report`, `exitStatus`).

## Exemplo
```yaml
env:
  contexts:
    - name: "staging-api"
      urls:
        - "https://staging.example.com"
      includePaths:
        - "https://staging.example.com/.*"
  parameters:
    failOnError: true
    progressToStdout: true
jobs:
  - type: passiveScan-config
    parameters:
      maxAlertsPerRule: 10
  - type: spider
    parameters:
      maxDuration: 2
  - type: passiveScan-wait
  - type: report
    parameters:
      template: "sarif-json"
      reportDir: "/zap/wrk"
      reportFile: "zap-report.sarif"
```

## Limites e trade-offs
Você pode gerar um template YAML inicial diretamente pela CLI com `zap.sh -cmd -autogenmin zap-min.yaml` ou `zap.sh -cmd -autogenmax zap-max.yaml`.

## Como verificar
Execute `zap.sh -cmd -autorun zap-plan.yaml` e verifique o relatório gerado no diretório configurado.

## Conexões
- [[zaproxy-arquitetura-zed-attack-proxy-dast-passive-active-scanner]] — Veja também: OWASP ZAP (Zed Attack Proxy): arquitetura de proxy interceptador, `Passive Scanner` e `Active Scanner` para DAST.
- [[zaproxy-descoberta-superficie-spider-spiderajax-spiderclient-spas]] — Veja também: ZAP Crawling e Descoberta (`spider`, `spiderAjax` e `spiderClient`): mapeamento de aplicações tradicionais e SPAs modernas.

## Fontes
- [OWASP ZAP Official Documentation — Automation Framework (Declarative YAML Plan, env Contexts, Discovery/Scan/Report Jobs & Job Tests)](https://www.zaproxy.org/docs/automate/automation-framework/) — Documentação oficial do Automation Framework do OWASP ZAP detalhando a estrutura YAML env/jobs, substituição dos Packaged Scans e lista completa de jobs suportados; consultado em 2026-10-03.
- [OWASP ZAP GitHub — README.md (Zed Attack Proxy Architecture, Passive & Active Scanners, Container Images & Add-ons)](https://raw.githubusercontent.com/zaproxy/zaproxy/main/README.md) — README oficial do zaproxy/zaproxy apresentando o projeto DAST open-source, modos de execução headless e ecossistema de extensões; consultado em 2026-10-03.
- [OWASP ZAP — Official GitHub Repository](https://github.com/zaproxy/zaproxy) — Repositório oficial Apache-2.0 do OWASP Zed Attack Proxy; consultado em 2026-10-03.
