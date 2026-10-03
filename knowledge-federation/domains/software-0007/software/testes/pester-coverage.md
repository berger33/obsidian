---
id: software.testes.tranche22.001579
tipo: tecnica
dominio: software
subdominio: testes
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-22.md"
fontes: ["https://pester.dev/docs/usage/code-coverage", "https://pester.dev/docs/commands/New-PesterConfiguration"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Pester: cobertura com New-PesterConfiguration

## Em uma frase
A cobertura do Pester v6 se configura por objeto: New-PesterConfiguration, ligar CodeCoverage.Enabled, opcionalmente restringir com CodeCoverage.Path e chamar Invoke-Pester -Configuration $config — o parâmetro -CodeCoverage direto caiu de uso.

## Por que importa
Cobertura em script de shell é raro e valioso: a linha "Covered 11.7% / 75%" mostra o percentual medido contra a meta configurável CoveragePercentTarget, que falha o run por baixo da régua.

## Como funciona
No Output Detailed, o relatório lista as Missed commands por arquivo, função e linha — no exemplo oficial, a linha unreachable (return 'I do not') aparece como não coberta.

## Exemplo
Para zerar um trecho do cálculo, anote a função com [System.Diagnostics.CodeAnalysis.ExcludeFromCodeCoverage()] antes do param block.

## Limites e trade-offs
O coletor padrão é um tracer baseado em profiler, bem mais rápido que o collector por breakpoints do v5, preservado no flag UseBreakpoints; relatórios gravam caminhos relativos ao RepoRoot (achado pelo .git), ajustável via CodeCoverage.ReportRoot.

## Como verificar
Gere o coverage.xml padrão (JaCoCo, com Cobertura disponível em OutputFormat) e confirme que o CI o lê sem path absoluto de máquina.

## Conexões
- [[pester-mock-advanced]] — Veja também: Pester: natives, $PesterBoundParameters e classes.

## Fontes
- [Pester — Code coverage](https://pester.dev/docs/usage/code-coverage) — New-PesterConfiguration, formatos JaCoCo/Cobertura e tracer; consultado em 2026-10-03.
- [Pester — New-PesterConfiguration](https://pester.dev/docs/commands/New-PesterConfiguration) — comando de configuração citado pela página de cobertura; consultado em 2026-10-03.
