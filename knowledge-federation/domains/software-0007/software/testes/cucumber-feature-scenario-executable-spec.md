---
id: software.testes.tranche11.000480
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
fontes: ["https://cucumber.io/docs/gherkin/reference/", "https://cucumber.io/docs/cucumber/step-definitions/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Cucumber: escrever Feature e Example como regra verificável

## Em uma frase
Uma Feature agrupa cenários relacionados e cada Example ou Scenario descreve contexto, evento e resultado esperado em steps.

## Por que importa
Gherkin estrutura exemplos em linguagem de domínio e Cucumber associa steps a código; erros de semântica, matching ou preparação podem tornar especificações duplicadas ou frágeis. Descrições que só repetem detalhes de implementação não ajudam produto e engenharia a identificar qual regra está sendo exercitada.

## Como funciona
Escreva exemplos curtos que exponham regra e resultado, mantenha steps observáveis, tipifique parâmetros e isole estado por cenário; use tags e hooks para seleção e preparação transversal justificadas. Dê ao arquivo uma única Feature clara e escreva cenários com precondição, ação e observação de saída compreensíveis no domínio.

## Exemplo
Uma feature de cobrança descreve saldo vencido, pagamento recebido e estado final da fatura sem citar nome de controller.

## Limites e trade-offs
Executar uma feature não comprova que os exemplos cobrem todas as regras nem que passos descrevam comportamento de usuário. Hooks e steps podem esconder lógica, efeitos e dependências externas. Descrição textual de Feature ajuda documentação, mas é ignorada na execução como steps.

## Como verificar
Revise os cenários com pessoa de produto e confirme que cada Then pode ser observado pelo teste.

## Conexões
- [[cucumber-keywords-nao-fazem-parte-do-matching]] — Veja também: Cucumber: não tratar Given When Then como namespaces de step.

## Fontes
- [Cucumber — Gherkin Reference](https://cucumber.io/docs/gherkin/reference/) — estrutura Feature, Rule, Scenario, Background, Outline, tags, steps e argumentos multilinha; consultado em 2026-10-02.
- [Cucumber — Step Definitions](https://cucumber.io/docs/cucumber/step-definitions/) — expressões, correspondência de steps e parâmetros tipados; consultado em 2026-10-02.
