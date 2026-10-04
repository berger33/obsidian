---
id: software.testes.tranche17.001086
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
fontes: ["https://cucumber.io/docs/gherkin/reference/", "https://github.com/cucumber/cucumber-js"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Cucumber: estruturar o cenário em Gherkin

## Em uma frase
O arquivo de funcionalidade descreve cenários com passos iniciados por palavras reservadas e um contexto curto no topo da funcionalidade.

## Por que importa
A linguagem comum permite que pessoas de negócio revisem o comportamento esperado e participem da definição do que será automatizado.

## Como funciona
Escreva a funcionalidade com um título claro, use antecedentes para o contexto compartilhado e limite cada cenário a um comportamento observável.

## Exemplo
Um cenário de recuperação de senha pode descrever o pedido, a mensagem exibida e o efeito no acesso sem citar detalhes de implementação.

## Limites e trade-offs
Cenários longos com muitos passos encadeados perdem legibilidade e se tornam frágeis; o excesso de antecedentes também esconde pré-condições importantes.

## Como verificar
Leia o cenário com uma pessoa não técnica e confirme que ela consegue descrever o comportamento esperado sem consultar o código.

## Conexões
- [[cucumber-step-definitions]] — Veja também: Cucumber: ligar passos a código.

## Fontes
- [Cucumber — Gherkin reference](https://cucumber.io/docs/gherkin/reference/) — funcionalidades, cenários, antecedentes, esquemas de cenário e tabelas; consultado em 2026-10-03.
- [Cucumber — repositório oficial](https://github.com/cucumber/cucumber-js) — implementação de referência, exemplos e documentação do projeto; consultado em 2026-10-03.
