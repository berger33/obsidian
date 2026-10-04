---
id: software.seguranca.tranche01.000050
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

# ZAP Fluxos Multi-Step e Customizados: jobs `requestor`, `sequence-import` (arquivos HAR), `sequence-activeScan` e `prune`

## Em uma frase
Conforme listado na visão geral oficial do Automation Framework, o ZAP inclui jobs avançados para guiar o scanner por fluxos de negócio de múltiplas etapas: **`requestor`** (envia requisições HTTP específicas para semear a árvore), **`sequence-import`** e **`sequence-activeScan`** (importam um fluxo multi-step a partir de um arquivo **HAR** e executam scan ativo respeitando a sequência exata de passos) e **`prune`** (remove nós indesejados da *Sites Tree*).

## Por que importa
Em um fluxo de checkout de e-commerce (`Passo 1: Criar Carrinho -> Passo 2: Informar Endereço -> Passo 3: Confirmar Pedido`), testar o endpoint do Passo 3 isoladamente fora de ordem retorna apenas erro de estado inválido, nunca exercitando a lógica interna.

## Como funciona
Com `sequence-import` (a partir de um arquivo `.har` gravado pelos testes E2E do Playwright/Cypress) seguido de `sequence-activeScan`, o ZAP reproduz a sequência completa em ordem enquanto injeta payloads em cada passo. E com o job `prune`, você remove rotas estáticas redundantes da árvore antes do `activeScan`.

## Exemplo
```yaml
jobs:
  - type: requestor
    requests:
      - url: "https://staging.example.com/api/v1/seed-state"
        method: "POST"
        responseCode: 200
```

## Limites e trade-offs
Reaproveitar arquivos `.har` gerados pela suíte de testes E2E funcional existente para alimentar o ZAP garante que o DAST cubra 100% dos fluxos reais de usuário.

## Como verificar
Verifique na saída do job `requestor` se todas as requisições retornaram o `responseCode` esperado.

## Conexões
- [[zaproxy-job-tests-assertions-exitstatus-report-sarif-quality-gates]] — Veja também: ZAP Quality Gates em CI/CD: *Job Tests* (`alert`, `stats`, `url`), geração de relatórios (`report`) e `exitStatus`.

## Fontes
- [OWASP ZAP Official Documentation — Automation Framework (Declarative YAML Plan, env Contexts, Discovery/Scan/Report Jobs & Job Tests)](https://www.zaproxy.org/docs/automate/automation-framework/) — Documentação oficial do Automation Framework do OWASP ZAP detalhando a estrutura YAML env/jobs, substituição dos Packaged Scans e lista completa de jobs suportados; consultado em 2026-10-03.
- [OWASP ZAP GitHub — README.md (Zed Attack Proxy Architecture, Passive & Active Scanners, Container Images & Add-ons)](https://raw.githubusercontent.com/zaproxy/zaproxy/main/README.md) — README oficial do zaproxy/zaproxy apresentando o projeto DAST open-source, modos de execução headless e ecossistema de extensões; consultado em 2026-10-03.
- [OWASP ZAP — Official GitHub Repository](https://github.com/zaproxy/zaproxy) — Repositório oficial Apache-2.0 do OWASP Zed Attack Proxy; consultado em 2026-10-03.
