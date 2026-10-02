---
id: software.testes.tranche11.000484
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-11.md"
fontes: ["https://cucumber.io/docs/gherkin/reference/", "https://cucumber.io/docs/cucumber/api/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Cucumber: tratar cada linha de Examples como invocação do outline

## Em uma frase
Scenario Outline é um template; suas steps recebem valores de placeholders e o outline executa uma vez para cada linha em Examples.

## Por que importa
Contar o template como caso isolado pode subestimar invocações e deixar coluna sem valor ou combinação de dados sem cobertura.

## Como funciona
Declare cabeçalhos coerentes com placeholders e forneça exemplos representativos incluindo limites e resultado esperado.

## Exemplo
Duas linhas em Examples validam saldo suficiente e insuficiente; cada execução recebe os valores de uma linha.

## Limites e trade-offs
Outline replica somente combinações escritas, não gera automaticamente produto cartesiano nem cobre valores omitidos.

## Como verificar
Inspecione relatório do runner para confirmar número de invocações e associe falha à linha/valores exibidos.

## Conexões
- [[cucumber-step-definitions-ambiguos-unicos]] — Veja também: Cucumber: impedir step definitions ambíguos e duplicados.
- [[cucumber-data-tables-argumento-final]] — Veja também: Cucumber: modelar DataTable como argumento do step.

## Fontes
- [Cucumber — Gherkin Reference](https://cucumber.io/docs/gherkin/reference/) — estrutura Feature, Rule, Scenario, Background, Outline, tags, steps e argumentos multilinha; consultado em 2026-10-02.
- [Cucumber — API Reference](https://cucumber.io/docs/cucumber/api/) — hooks, tags, tabelas, resultados e regras de execução dos steps; consultado em 2026-10-02.
