---
id: software.testes.tranche11.000487
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

# Cucumber: limitar Background a contexto comum necessário

## Em uma frase
Background define steps comuns executados antes dos cenários aplicáveis dentro da Feature ou Rule.

## Por que importa
Duplicar login e setup em todos os cenários polui exemplos; um background longo, por outro lado, esconde a precondição do caso.

## Como funciona
Mantenha apenas contexto curto que todo cenário daquela seção compartilha e deixe variações importantes nos próprios Examples.

## Exemplo
A feature de conta declara “usuária autenticada” uma vez e cada cenário especifica papel ou saldo que diferencia o comportamento.

## Limites e trade-offs
Background não substitui isolamento de fixture e pode causar dependência de estado entre cenários se reutilizar dados persistentes.

## Como verificar
Execute cenários individualmente e em ordem aleatória para provar que o contexto é reconstruído para cada execução.

## Conexões
- [[cucumber-doc-string-corpo-multilinha]] — Veja também: Cucumber: usar Doc String para payload textual multilinha.
- [[cucumber-hooks-condicionais-com-tags]] — Veja também: Cucumber: restringir hooks por tag e escopo explícito.

## Fontes
- [Cucumber — Gherkin Reference](https://cucumber.io/docs/gherkin/reference/) — estrutura Feature, Rule, Scenario, Background, Outline, tags, steps e argumentos multilinha; consultado em 2026-10-02.
- [Cucumber — API Reference](https://cucumber.io/docs/cucumber/api/) — hooks, tags, tabelas, resultados e regras de execução dos steps; consultado em 2026-10-02.
