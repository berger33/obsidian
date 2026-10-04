---
id: software.testes.tranche22.001571
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
fontes: ["https://pester.dev/docs/quick-start", "https://pester.dev/docs/usage/code-coverage"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Pester: convenção de nome é o registro

## Em uma frase
O Pester não usa registro explícito de testes: ele descobre casos por convenção de nome — arquivos de teste terminam em .Tests.ps1 — e a execução inteira parte de Invoke-Pester apontando para um caminho.

## Por que importa
Adicionar um arquivo novo à suíte não exige tocar em índice, fixture global ou config: a convenção de nome é o contrato, o que mantém a suíte de infraestrutura fácil de estender.

## Como funciona
Crie MeuComponente.Tests.ps1 ao lado do código e invoque Invoke-Pester -Output Detailed ./tests; o modo Detailed mostra cada Describe/Context/It com marcação de status.

## Exemplo
O resumo impresso termina com "Tests Passed: 1, Failed: 0, Skipped: 0, Inconclusive: 0, NotRun: 0" — a última categoria denuncia casos descobertos e não executados.

## Limites e trade-offs
Quem nomeia o arquivo como .test.ps1 (estilo JS) ou esquece o sufixo simplesmente sai da suíte sem nenhum erro; a descoberta silenciosa tem esse preço.

## Como verificar
Renomeie um arquivo de teste válido para .test.ps1, rode o Invoke-Pester no diretório e confirme que a contagem total cai para zero.

## Conexões
- [[pester-what-it-is]] — Veja também: Pester: testar e mockar PowerShell num só pacote.
- [[pester-install-module]] — Veja também: Pester: instalação pelo gallery e importação.

## Fontes
- [Pester — Quick start](https://pester.dev/docs/quick-start) — mini-DSL, convenção de nomes e primeira execução; consultado em 2026-10-03.
- [Pester — Code coverage](https://pester.dev/docs/usage/code-coverage) — New-PesterConfiguration, formatos JaCoCo/Cobertura e tracer; consultado em 2026-10-03.
