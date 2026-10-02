---
id: software.testes.tranche11.000488
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

# Cucumber: restringir hooks por tag e escopo explícito

## Em uma frase
Hooks podem ser associados a expressões de tags para executar preparação ou limpeza em cenários selecionados.

## Por que importa
Hook global que inicia browser para toda feature aumenta duração e pode adicionar dependência não visível ao cenário.

## Como funciona
Use tag expression para restringir hook a cenários que precisam do recurso e mantenha asserts centrais no fluxo da feature.

## Exemplo
Somente cenários @browser criam e encerram sessão WebDriver; testes de regra de negócio não iniciam navegador.

## Limites e trade-offs
Hook não é substituto de Given/Then quando a preparação ou resultado é parte do comportamento que precisa aparecer no exemplo.

## Como verificar
Execute casos com e sem tag e observe que somente o grupo designado dispara a inicialização.

## Conexões
- [[cucumber-background-precondicao-compartilhada]] — Veja também: Cucumber: limitar Background a contexto comum necessário.
- [[cucumber-tags-selecao-e-inclusao]] — Veja também: Cucumber: verificar filtros de tags contra casos descobertos.

## Fontes
- [Cucumber — API Reference](https://cucumber.io/docs/cucumber/api/) — hooks, tags, tabelas, resultados e regras de execução dos steps; consultado em 2026-10-02.
- [Cucumber — Gherkin Reference](https://cucumber.io/docs/gherkin/reference/) — estrutura Feature, Rule, Scenario, Background, Outline, tags, steps e argumentos multilinha; consultado em 2026-10-02.
