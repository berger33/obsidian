---
id: software.testes.tranche11.000485
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
fontes: ["https://cucumber.io/docs/cucumber/api/", "https://cucumber.io/docs/gherkin/reference/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Cucumber: modelar DataTable como argumento do step

## Em uma frase
Uma DataTable é passada como argumento multilinha final à step definition e pode ser convertida conforme sua forma e tipo.

## Por que importa
Gherkin estrutura exemplos em linguagem de domínio e Cucumber associa steps a código; erros de semântica, matching ou preparação podem tornar especificações duplicadas ou frágeis. Compactar várias entidades em uma frase torna o cenário difícil de revisar e pode esconder diferença entre colunas e linhas.

## Como funciona
Escreva exemplos curtos que exponham regra e resultado, mantenha steps observáveis, tipifique parâmetros e isole estado por cenário; use tags e hooks para seleção e preparação transversal justificadas. Use cabeçalho com nomes estáveis e converta para coleção tipada adequada; valide cardinalidade e valores na fronteira do teste.

## Exemplo
A tabela de usuários vira uma lista de maps com name/email e o teste confirma que cada usuário foi criado uma vez.

## Limites e trade-offs
Executar uma feature não comprova que os exemplos cobrem todas as regras nem que passos descrevam comportamento de usuário. Hooks e steps podem esconder lógica, efeitos e dependências externas. Conversão disponível depende da forma da tabela e dos tipos registrados; não confunda tabela com vários parâmetros capturados na expressão.

## Como verificar
Teste tabela vazia, coluna faltante e valor inválido e confira que a falha aponta linha ou campo relevante.

## Conexões
- [[cucumber-scenario-outline-examples-linhas]] — Veja também: Cucumber: tratar cada linha de Examples como invocação do outline.
- [[cucumber-doc-string-corpo-multilinha]] — Veja também: Cucumber: usar Doc String para payload textual multilinha.

## Fontes
- [Cucumber — API Reference](https://cucumber.io/docs/cucumber/api/) — hooks, tags, tabelas, resultados e regras de execução dos steps; consultado em 2026-10-02.
- [Cucumber — Gherkin Reference](https://cucumber.io/docs/gherkin/reference/) — estrutura Feature, Rule, Scenario, Background, Outline, tags, steps e argumentos multilinha; consultado em 2026-10-02.
