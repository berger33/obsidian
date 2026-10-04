---
id: software.testes.tranche22.001574
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

# Pester: asserções Should e a mensagem de falha

## Em uma frase
O lado de afirmação do mini-DSL é o Should: os exemplos oficiais escrevem $result | Should-Be 5 e $allPlanets.Count | Should-Be 8, encadeando o valor real pelo pipeline até a expectativa.

## Por que importa
Mensagens de falha boas são metade do trabalho de depuração; o Should do Pester imprime tipo e valor dos dois lados, o que em PowerShell tipado faz diferença quando um null disfarçado de inteiro aparece.

## Como funciona
Pipe a saída do comando sob teste para Should com o valor esperado; ao rodar via Pester, a falha vem formatada com os tipos .NET em jogo.

## Exemplo
Quando Add-Numbers devolve nada, o relatório registra Expected [int] 8, but got [int]. — o tipo aparece dos dois lados e denuncia o vazio.

## Limites e trade-offs
A sintaxe demonstrada no quick start é a forma legada de asserção; migrações entre versões do Pester trocam o estilo das palavras-chave de asserção, e copiar exemplo antigo produz erro de comando desconhecido.

## Como verificar
Cause deliberadamente um tipo trocado (string '8' vs [int] 8) e veja como a mensagem do Should distingue os dois.

## Conexões
- [[pester-dsl-blocks]] — Veja também: Pester: Describe, Context e It aninhados.
- [[pester-mock-basics]] — Veja também: Pester: Mock substitui qualquer comando.

## Fontes
- [Pester — Quick start](https://pester.dev/docs/quick-start) — mini-DSL, convenção de nomes e primeira execução; consultado em 2026-10-03.
- [Pester — Mocking](https://pester.dev/docs/usage/mocking) — Mock, Should-Invoke, escopo, natives e classes; consultado em 2026-10-03.
