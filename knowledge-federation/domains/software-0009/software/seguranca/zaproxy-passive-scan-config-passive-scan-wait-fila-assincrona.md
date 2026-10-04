---
id: software.seguranca.tranche01.000046
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

# ZAP `passiveScan-config` e `passiveScan-wait`: ajuste de regras passivas e sincronização obrigatória da fila de análise

## Em uma frase
No ZAP, o scanner passivo roda em uma thread assíncrona em background analisando as mensagens HTTP à medida que o `spider`, o `openapi` ou o `requestor` geram tráfego; por isso, o Automation Framework fornece o job **`passiveScan-config`** (no início do plano) e o job **`passiveScan-wait`** (antes de gerar o relatório).

## Por que importa
Se o plano YAML executar o `spider` e pular imediatamente para o job `report` sem incluir `passiveScan-wait`, o ZAP encerrará o processo e gerará o relatório enquanto dezenas de respostas HTTP ainda estavam na fila de processamento do scanner passivo!

## Como funciona
No `passiveScan-config`, você define parâmetros como `maxAlertsPerRule: 10`, `scanOnlyInScope: true` e `maxBodySizeInBytesToScan`, além de poder ajustar o limiar (`LOW`, `MEDIUM`, `HIGH`, `OFF`) de regras específicas por `id`. Logo após os jobs de descoberta, o job **`passiveScan-wait`** bloqueia o plano até que a fila do scanner passivo chegue a zero.

## Exemplo
```yaml
jobs:
  - type: passiveScan-config
    parameters:
      maxAlertsPerRule: 10
      scanOnlyInScope: true
    rules:
      - id: 10021
        name: "X-Content-Type-Options Header Missing"
        threshold: "LOW"
  - type: spider
  - type: passiveScan-wait
    parameters:
      maxDuration: 5
```

## Limites e trade-offs
Mantenha `scanOnlyInScope: true` no `passiveScan-config` para evitar que chamadas para CDNs de terceiros (Google Fonts, Analytics) poluam o relatório de segurança da sua aplicação.

## Como verificar
Verifique na saída do job `passiveScan-wait` que a fila de registros pendentes chegou a `0` antes do job `report`.

## Conexões
- [[zaproxy-autenticacao-browser-auth-autodetect-replacer-bearer-tokens]] — Veja também: ZAP Autenticação no Automation Framework: `browser` auth, `autodetect` de sessão e injeção de tokens com o job `replacer`.
- [[zaproxy-active-scan-policy-strength-threshold-technologies-tuning]] — Veja também: ZAP `activeScan`, `activeScan-policy` e `activeScan-config`: sintonia de *Attack Strength*, *Alert Threshold* e tecnologias do alvo.

## Fontes
- [OWASP ZAP Official Documentation — Automation Framework (Declarative YAML Plan, env Contexts, Discovery/Scan/Report Jobs & Job Tests)](https://www.zaproxy.org/docs/automate/automation-framework/) — Documentação oficial do Automation Framework do OWASP ZAP detalhando a estrutura YAML env/jobs, substituição dos Packaged Scans e lista completa de jobs suportados; consultado em 2026-10-03.
- [OWASP ZAP GitHub — README.md (Zed Attack Proxy Architecture, Passive & Active Scanners, Container Images & Add-ons)](https://raw.githubusercontent.com/zaproxy/zaproxy/main/README.md) — README oficial do zaproxy/zaproxy apresentando o projeto DAST open-source, modos de execução headless e ecossistema de extensões; consultado em 2026-10-03.
- [OWASP ZAP — Official GitHub Repository](https://github.com/zaproxy/zaproxy) — Repositório oficial Apache-2.0 do OWASP Zed Attack Proxy; consultado em 2026-10-03.
