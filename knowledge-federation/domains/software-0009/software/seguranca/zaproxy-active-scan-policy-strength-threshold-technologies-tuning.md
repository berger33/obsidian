---
id: software.seguranca.tranche01.000047
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

# ZAP `activeScan`, `activeScan-policy` e `activeScan-config`: sintonia de *Attack Strength*, *Alert Threshold* e tecnologias do alvo

## Em uma frase
Para controlar a duração e a agressividade dos testes intrusivos no Automation Framework, o ZAP separa os jobs **`activeScan-policy`** (que define uma política reutilizável com `defaultStrength` e `defaultThreshold`), **`activeScan-config`** (limites de threads, hosts e tempo) e **`activeScan`** (execução do scan ativo sobre um `context`).

## Por que importa
Habilitar todas as regras de injeção de SQL para MySQL, Oracle, MSSQL, DB2, SQLite e PostgreSQL com força `INSANE` quando seu microserviço usa apenas PostgreSQL multiplica por 10 o tempo de varredura sem ganho de segurança.

## Como funciona
Declarando apenas as tecnologias reais do serviço no bloco `technology` do `context` (ex.: `OS.Linux`, `Db.PostgreSQL`, `Language.Java.Spring`) e definindo `defaultStrength: MEDIUM` e `defaultThreshold: MEDIUM` na `activeScan-policy`, o ZAP executa exclusivamente os vetores de ataque pertinentes à sua stack.

## Exemplo
```yaml
jobs:
  - type: activeScan-policy
    parameters:
      name: "api-fast-policy"
      defaultStrength: "MEDIUM"
      defaultThreshold: "MEDIUM"
  - type: activeScan
    parameters:
      context: "staging-api"
      policy: "api-fast-policy"
      maxRuleDurationInMins: 5
      maxScanDurationInMins: 20
```

## Limites e trade-offs
Defina sempre `maxRuleDurationInMins` (ex.: `5`) e `maxScanDurationInMins` (ex.: `20`) no job `activeScan` para garantir que um endpoint lento nunca estoure o timeout global do pipeline de CI/CD.

## Como verificar
Audite no log final de progresso do `activeScan` o tempo gasto por cada regra (`Plugin`) executada.

## Conexões
- [[zaproxy-passive-scan-config-passive-scan-wait-fila-assincrona]] — Veja também: ZAP `passiveScan-config` e `passiveScan-wait`: ajuste de regras passivas e sincronização obrigatória da fila de análise.
- [[zaproxy-alert-filter-triagem-falsos-positivos-rebaixamento-risco]] — Veja também: ZAP `alertFilter`: supressão e reklasificação declarativa de falsos positivos por `ruleId`, `url` e `parameter`.

## Fontes
- [OWASP ZAP Official Documentation — Automation Framework (Declarative YAML Plan, env Contexts, Discovery/Scan/Report Jobs & Job Tests)](https://www.zaproxy.org/docs/automate/automation-framework/) — Documentação oficial do Automation Framework do OWASP ZAP detalhando a estrutura YAML env/jobs, substituição dos Packaged Scans e lista completa de jobs suportados; consultado em 2026-10-03.
- [OWASP ZAP GitHub — README.md (Zed Attack Proxy Architecture, Passive & Active Scanners, Container Images & Add-ons)](https://raw.githubusercontent.com/zaproxy/zaproxy/main/README.md) — README oficial do zaproxy/zaproxy apresentando o projeto DAST open-source, modos de execução headless e ecossistema de extensões; consultado em 2026-10-03.
- [OWASP ZAP — Official GitHub Repository](https://github.com/zaproxy/zaproxy) — Repositório oficial Apache-2.0 do OWASP Zed Attack Proxy; consultado em 2026-10-03.
