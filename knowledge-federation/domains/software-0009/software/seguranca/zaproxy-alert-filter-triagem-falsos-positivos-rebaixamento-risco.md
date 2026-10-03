---
id: software.seguranca.tranche01.000048
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

# ZAP `alertFilter`: supressão e reklasificação declarativa de falsos positivos por `ruleId`, `url` e `parameter`

## Em uma frase
O job **`alertFilter`** (fornecido pelo add-on *Alert Filters* no Automation Framework) permite reclassificar o nível de risco (`newRisk`: `False Positive`, `Info`, `Low`, `Medium`, `High`) de alertas específicos que correspondam a uma combinação exata de `ruleId`, `context`, `url` (literal ou regex), `parameter` e `evidence`.

## Por que importa
Em vez de desligar uma regra inteira de XSS ou CSP para toda a aplicação só porque um endpoint específico de legado tem um comportamento aceito pela equipe de arquitetura, o `alertFilter` marca como `False Positive` apenas aquele `ruleId` naquela `url` e `parameter` exatos.

## Como funciona
O job `alertFilter` deve ser declarado no plano YAML **antes** dos jobs de varredura e relatório; assim, sempre que o scanner passivo ou ativo emitir um alerta que case com os critérios do filtro, seu risco é ajustado automaticamente antes do `report` e do `exitStatus`.

## Exemplo
```yaml
jobs:
  - type: alertFilter
    alertFilters:
      - ruleId: 10038
        newRisk: "False Positive"
        context: "staging-api"
        url: "https://staging\\.example\\.com/api/v1/healthz.*"
        urlIsRegex: true
```

## Limites e trade-offs
Prefira sempre usar `urlIsRegex: true` ancorado no caminho específico da rota e documente o motivo da exceção em comentário no YAML versionado.

## Como verificar
Verifique no relatório gerado que o alerta filtrado aparece classificado sob `False Positive` (ou não aciona falha no `exitStatus`).

## Conexões
- [[zaproxy-active-scan-policy-strength-threshold-technologies-tuning]] — Veja também: ZAP `activeScan`, `activeScan-policy` e `activeScan-config`: sintonia de *Attack Strength*, *Alert Threshold* e tecnologias do alvo.
- [[zaproxy-job-tests-assertions-exitstatus-report-sarif-quality-gates]] — Veja também: ZAP Quality Gates em CI/CD: *Job Tests* (`alert`, `stats`, `url`), geração de relatórios (`report`) e `exitStatus`.

## Fontes
- [OWASP ZAP Official Documentation — Automation Framework (Declarative YAML Plan, env Contexts, Discovery/Scan/Report Jobs & Job Tests)](https://www.zaproxy.org/docs/automate/automation-framework/) — Documentação oficial do Automation Framework do OWASP ZAP detalhando a estrutura YAML env/jobs, substituição dos Packaged Scans e lista completa de jobs suportados; consultado em 2026-10-03.
- [OWASP ZAP GitHub — README.md (Zed Attack Proxy Architecture, Passive & Active Scanners, Container Images & Add-ons)](https://raw.githubusercontent.com/zaproxy/zaproxy/main/README.md) — README oficial do zaproxy/zaproxy apresentando o projeto DAST open-source, modos de execução headless e ecossistema de extensões; consultado em 2026-10-03.
- [OWASP ZAP — Official GitHub Repository](https://github.com/zaproxy/zaproxy) — Repositório oficial Apache-2.0 do OWASP Zed Attack Proxy; consultado em 2026-10-03.
