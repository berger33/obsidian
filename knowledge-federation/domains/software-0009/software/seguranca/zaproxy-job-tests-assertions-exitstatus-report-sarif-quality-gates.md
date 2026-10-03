---
id: software.seguranca.tranche01.000049
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

# ZAP Quality Gates em CI/CD: *Job Tests* (`alert`, `stats`, `url`), geração de relatórios (`report`) e `exitStatus`

## Em uma frase
O Automation Framework do ZAP oferece dois mecanismos complementares para atuar como *Quality Gate* automatizado em pipelines DevSecOps: **Job Tests** (asserções anexadas a qualquer job, como `alert`, `stats`, `url`, `monitor`) e o job dedicado **`exitStatus`** (que define o código de saída do processo ZAP com base na severidade máxima encontrada, como `errorLevel: Medium`).

## Por que importa
Rodar uma varredura DAST no CI que gera um arquivo HTML mas sempre termina com código de saída `0` (`SUCCESS`) mesmo quando descobre um SQL Injection de risco `High` faz com que deploys vulneráveis avancem para produção sem bloqueio.

## Como funciona
Combinando o job **`report`** (exportando `template: "sarif-json"` ou `"traditional-html-plus"`) com o job **`exitStatus`** no final do plano YAML (`errorLevel: "High"`, `warnLevel: "Medium"`, `okExitValue: 0`, `errorExitValue: 1`), a pipeline falha deterministicamente sempre que um alerta acima do limiar permitido for detectado.

## Exemplo
```yaml
jobs:
  - type: report
    parameters:
      template: "sarif-json"
      reportDir: "/zap/wrk"
      reportFile: "zap-results.sarif"
  - type: exitStatus
    parameters:
      errorLevel: "High"
      warnLevel: "Medium"
      okExitValue: 0
      errorExitValue: 1
```

## Limites e trade-offs
Coloque o job `exitStatus` sempre como o **último** job da lista `jobs:`, logo após o job `report`, garantindo que todos os relatórios sejam gravados em disco antes que o ZAP encerre com o código de saída configurado.

## Como verificar
Execute o plano e verifique `echo $?` e o arquivo `zap-results.sarif` gerado.

## Conexões
- [[zaproxy-alert-filter-triagem-falsos-positivos-rebaixamento-risco]] — Veja também: ZAP `alertFilter`: supressão e reklasificação declarativa de falsos positivos por `ruleId`, `url` e `parameter`.
- [[zaproxy-requestor-sequence-har-import-prune-fluxos-multi-step]] — Veja também: ZAP Fluxos Multi-Step e Customizados: jobs `requestor`, `sequence-import` (arquivos HAR), `sequence-activeScan` e `prune`.

## Fontes
- [OWASP ZAP Official Documentation — Automation Framework (Declarative YAML Plan, env Contexts, Discovery/Scan/Report Jobs & Job Tests)](https://www.zaproxy.org/docs/automate/automation-framework/) — Documentação oficial do Automation Framework do OWASP ZAP detalhando a estrutura YAML env/jobs, substituição dos Packaged Scans e lista completa de jobs suportados; consultado em 2026-10-03.
- [OWASP ZAP GitHub — README.md (Zed Attack Proxy Architecture, Passive & Active Scanners, Container Images & Add-ons)](https://raw.githubusercontent.com/zaproxy/zaproxy/main/README.md) — README oficial do zaproxy/zaproxy apresentando o projeto DAST open-source, modos de execução headless e ecossistema de extensões; consultado em 2026-10-03.
- [OWASP ZAP — Official GitHub Repository](https://github.com/zaproxy/zaproxy) — Repositório oficial Apache-2.0 do OWASP Zed Attack Proxy; consultado em 2026-10-03.
