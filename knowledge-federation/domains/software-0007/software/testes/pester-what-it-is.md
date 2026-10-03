---
id: software.testes.tranche22.001570
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
fontes: ["https://pester.dev/docs/quick-start", "https://pester.dev/docs/usage/mocking"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Pester: testar e mockar PowerShell num só pacote

## Em uma frase
O Pester é simultaneamente framework de testes e de mocking para PowerShell: cobre testes unitários e de integração (sem limitar-se a eles) e serve de base para ferramentas de validação de ambiente e de implantação.

## Por que importa
Ambiente Windows, Azure e M365 são administrados por scripts PowerShell, e sem um framework nativo esses scripts ficam sem teste algum; o Pester fecha esse buraco dentro do próprio shell.

## Como funciona
Um mini-DSL formado por Describe, Context, It, Should e Mock declara suítes em arquivos .Tests.ps1, e o comando Invoke-Pester descobre e executa tudo a partir de um caminho.

## Exemplo
Describe 'Calculator' { BeforeAll { . $PSCommandPath.Replace('.Tests.ps1','.ps1') } It 'adds' { (Add-Numbers 2 3) | Should-Be 5 } } captura o padrão completo do quick start.

## Limites e trade-offs
O quick start demonstra a sintaxe legada de pipe Should-Be; suítes novas em Pester v5/v6 convivem com variações de sintaxe, então fixe a versão usada antes de copiar exemplos de blog.

## Como verificar
Instale o módulo, rode o exemplo do quick start contra o módulo de cálculo ausente e observe a falha "Expected [int] 8, but got [int]." antes de implementar.

## Conexões
- [[pester-naming-discovery]] — Veja também: Pester: convenção de nome é o registro.

## Fontes
- [Pester — Quick start](https://pester.dev/docs/quick-start) — mini-DSL, convenção de nomes e primeira execução; consultado em 2026-10-03.
- [Pester — Mocking](https://pester.dev/docs/usage/mocking) — Mock, Should-Invoke, escopo, natives e classes; consultado em 2026-10-03.
