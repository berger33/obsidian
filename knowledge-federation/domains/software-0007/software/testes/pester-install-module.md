---
id: software.testes.tranche22.001572
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
fontes: ["https://pester.dev/docs/quick-start", "https://pester.dev/docs/commands/New-PesterConfiguration"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Pester: instalação pelo gallery e importação

## Em uma frase
O caminho oficial de instalação é Install-Module Pester -Force seguido de Import-Module Pester -PassThru, que devolve o módulo carregado com sua versão — o exemplo do quick start mostra um Script module versão 6.1.0.

## Por que importa
O gallery entrega a PowerShellGet do repositório interno ou da PSGallery pública, e a importação explícita evita pegar a versão vinda por padrão do Windows, que quase sempre é antiga.

## Como funciona
AfterInstall-Module, confira a versão devolvida pelo Import-Module -PassThru e garanta que a suíte roda exatamente contra aquele build do Pester.

## Exemplo
PS C:\> Import-Module Pester -PassThru mostra ModuleType Script, Version 6.1.0 — é assim que o quick start registra a versão da demonstração.

## Limites e trade-offs
O -Force sobrescreve instalações existentes sem perguntar; em máquina com suítes legadas compartilhadas, fixe a versão ou use caminho absoluto do módulo.

## Como verificar
Rode Get-Module Pester antes e depois do import e compare as versões carregadas no mesmo PowerShell.

## Conexões
- [[pester-naming-discovery]] — Veja também: Pester: convenção de nome é o registro.
- [[pester-dsl-blocks]] — Veja também: Pester: Describe, Context e It aninhados.

## Fontes
- [Pester — Quick start](https://pester.dev/docs/quick-start) — mini-DSL, convenção de nomes e primeira execução; consultado em 2026-10-03.
- [Pester — New-PesterConfiguration](https://pester.dev/docs/commands/New-PesterConfiguration) — comando de configuração citado pela página de cobertura; consultado em 2026-10-03.
