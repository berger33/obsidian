---
id: software.testes.tranche17.001088
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-17.md"
fontes: ["https://cucumber.io/docs/gherkin/reference/", "https://cucumber.io/docs/cucumber/api/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Cucumber: variar entradas com esquema de cenário

## Em uma frase
O esquema de cenário usa marcadores no texto e uma tabela de exemplos, gerando uma execução por linha e um relatório por combinação.

## Por que importa
Variações da mesma regra ficam visíveis em uma única descrição e os casos gerados aparecem individualmente no relatório.

## Como funciona
Substitua valores por marcadores, mantenha a tabela com cabeçalho explícito e evite linhas que testem regras diferentes.

## Exemplo
Uma regra de desconto pode listar combinações de valor e percentual esperado em linhas separadas da mesma tabela.

## Limites e trade-offs
Tabelas grandes escondem a intenção e a falha em uma linha específica exige leitura cuidadosa do relatório gerado.

## Como verificar
Acrescente uma linha com valor-limite e confirme que ela aparece como cenário próprio, com o resultado da regra verificada.

## Conexões
- [[cucumber-step-definitions]] — Veja também: Cucumber: ligar passos a código.
- [[cucumber-hooks-lifecycle]] — Veja também: Cucumber: usar ganchos de preparação e limpeza.

## Fontes
- [Cucumber — Gherkin reference](https://cucumber.io/docs/gherkin/reference/) — funcionalidades, cenários, antecedentes, esquemas de cenário e tabelas; consultado em 2026-10-03.
- [Cucumber — Reference](https://cucumber.io/docs/cucumber/api/) — definições de passo, ganchos, etiquetas, paralelismo e relatórios; consultado em 2026-10-03.
