---
id: software.testes.tranche22.001578
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
fontes: ["https://pester.dev/docs/usage/mocking", "https://pester.dev/docs/usage/code-coverage"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Pester: natives, $PesterBoundParameters e classes

## Em uma frase
Casos difíceis têm resposta própria: comandos nativos são mockados via $args porque não expõem parâmetros nomeados, o mock vê $PesterBoundParameters no lugar de $PSBoundParameters (sobreposto pelo proxy), e no Windows PowerShell 5.1 o cache de classes quebra o Mock.

## Por que importa
Scripts de deploy chamam git, curl e binários nativos, e a limitação de classe é justamente o que impede suítes legadas de fechar; a documentação descreve as três saídas.

## Como funciona
Para o nativo, filtre por posição: Should-Invoke -CommandName 'curl' -Exactly -Times 1 -ParameterFilter { $args[0] -eq '--url' }; para o repasse fiel, invoque o cmdlet real com & (Get-Command ...) @PesterBoundParameters.

## Exemplo
A página mostra também "$args" -match '--url https://google.com -I' como truque quando a ordem dos argumentos pode mudar.

## Limites e trade-offs
A limitação de classe atinge todas as versões do Windows PowerShell até 5.1 (a definição é cacheada e nunca redefinida); o workaround publicado é rodar cada teste em sessão nova via Start-Job — em PS6+ o problema não existe.

## Como verificar
Rode a suíte problemática dentro do proxy Invoke-PesterJob sugerido na página e compare com a execução direta para isolar a causa.

## Conexões
- [[pester-mock-scoping]] — Veja também: Pester: o mock vale onde foi declarado.
- [[pester-coverage]] — Veja também: Pester: cobertura com New-PesterConfiguration.

## Fontes
- [Pester — Mocking](https://pester.dev/docs/usage/mocking) — Mock, Should-Invoke, escopo, natives e classes; consultado em 2026-10-03.
- [Pester — Code coverage](https://pester.dev/docs/usage/code-coverage) — New-PesterConfiguration, formatos JaCoCo/Cobertura e tracer; consultado em 2026-10-03.
