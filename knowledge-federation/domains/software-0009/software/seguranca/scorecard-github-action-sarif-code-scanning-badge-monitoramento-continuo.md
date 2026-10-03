---
id: software.seguranca.tranche01.000099
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
fontes: ["https://raw.githubusercontent.com/ossf/scorecard/main/README.md", "https://raw.githubusercontent.com/ossf/scorecard/main/docs/checks.md", "https://github.com/ossf/scorecard"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# OpenSSF Scorecard GitHub Action (`ossf/scorecard-action`): publicação de alertas SARIF no GitHub Code Scanning e Badge oficial

## Em uma frase
A **`ossf/scorecard-action`** oficial integra o Scorecard diretamente ao GitHub Actions do repositório, executando a auditoria a cada alteração na branch padrão, em alterações de proteção de branch e em agendamento semanal (`schedule`), enviando um relatório **SARIF** para a aba **GitHub Security / Code Scanning** e atualizando o badge público do projeto (`api.scorecard.dev`).

## Por que importa
Rodar o Scorecard manualmente uma única vez pela CLI melhora a postura naquele dia, mas semanas depois um desenvolvedor pode adicionar uma nova Action sem hash SHA ou alterar uma permissão de workflow sem perceber a queda na pontuação.

## Como funciona
Com a `ossf/scorecard-action` configurada com `publish_results: true` (para repositórios públicos) e upload via `github/codeql-action/upload-sarif`, cada regressão em `Pinned-Dependencies` ou `Token-Permissions` aparece imediatamente como alerta acionável na linha exata do arquivo `.github/workflows/*.yml`!

## Exemplo
```yaml
name: Scorecard supply-chain security
on:
  branch_protection_rule:
  schedule:
    - cron: '30 1 * * 6'
  push:
    branches: [ "main" ]

permissions: read-all

jobs:
  analysis:
    name: Scorecard analysis
    runs-on: ubuntu-latest
    permissions:
      security-events: write
      id-token: write
    steps:
      - name: "Checkout code"
        uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683
        with:
          persist-credentials: false
      - name: "Run analysis"
        uses: ossf/scorecard-action@62b2cac7ed8198b15735ed49ab1e5cf35480ba46
        with:
          results_file: results.sarif
          results_format: sarif
          publish_results: true
```

## Limites e trade-offs
Observe no exemplo oficial como `persist-credentials: false` é passado para o `actions/checkout` e como as permissões `security-events: write` e `id-token: write` ficam restritas apenas ao job `analysis`.

## Como verificar
Acesse `https://scorecard.dev/viewer/?uri=github.com/<org>/<repo>` para visualizar o relatório público do repositório.

## Conexões
- [[scorecard-checks-maintained-cii-best-practices-security-policy-license]] — Veja também: OpenSSF Scorecard Governança e Saúde do Projeto: `Maintained`, `Security-Policy` (`SECURITY.md`), `License` e `CII-Best-Practices`.
- [[scorecard-probes-structured-results-bigquery-api-rest-avaliacao-escala]] — Veja também: OpenSSF Scorecard em Escala: *Probes* estruturadas (V5), API REST (`api.scorecard.dev`) e dataset público no BigQuery.

## Fontes
- [OpenSSF Scorecard GitHub — README.md (Automated Security Assessment for Open Source, CLI & GitHub Action, Structured Results Probes & BigQuery Dataset)](https://raw.githubusercontent.com/ossf/scorecard/main/README.md) — README oficial do ossf/scorecard cobrindo objetivos do projeto, execução via CLI/Docker/GitHub Action, sistema de Probes V5 e dataset público semanal no BigQuery; consultado em 2026-10-03.
- [OpenSSF Scorecard Official Documentation — Checks Reference (docs/checks.md: Branch-Protection 5 Tiers, Binary-Artifacts, Token-Permissions, Pinned-Dependencies & Signed-Releases)](https://raw.githubusercontent.com/ossf/scorecard/main/docs/checks.md) — Catálogo técnico oficial docs/checks.md detalhando risco, critérios de pontuação e passos de remediação de cada check do OpenSSF Scorecard; consultado em 2026-10-03.
- [OpenSSF Scorecard — Official GitHub Repository](https://github.com/ossf/scorecard) — Repositório oficial Apache-2.0 do OpenSSF Scorecard; consultado em 2026-10-03.
