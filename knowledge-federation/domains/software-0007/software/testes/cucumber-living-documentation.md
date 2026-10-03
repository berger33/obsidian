---
id: software.testes.tranche17.001094
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

# Cucumber: manter a documentação viva

## Em uma frase
Como os cenários são executáveis, eles permanecem verdadeiros enquanto a suíte passa, servindo de documentação do comportamento acordado.

## Por que importa
Documentação escrita à parte envelhece, enquanto cenários revisados junto do código descrevem o sistema como ele realmente se comporta.

## Como funciona
Revise os cenários nas mesmas revisões de código, evite termos internos na descrição e remova cenários que deixaram de representar uma regra do negócio.

## Exemplo
Um cenário de limite de crédito pode ser lido por qualquer pessoa da área e permanecer válido após a troca de biblioteca de automação.

## Limites e trade-offs
Cenários que testam detalhes de interface ou repetem passos de implementação deixam de ser documentação e passam a exigir manutenção constante.

## Como verificar
Peça a alguém de fora do time para descrever a regra lendo apenas os cenários e verifique se a descrição corresponde ao comportamento implementado.

## Conexões
- [[cucumber-reports]] — Veja também: Cucumber: escolher formatos de relatório.
- [[cucumber-limits-and-maintenance]] — Veja também: Cucumber: sustentar a suíte ao longo do tempo.

## Fontes
- [Cucumber — Gherkin reference](https://cucumber.io/docs/gherkin/reference/) — funcionalidades, cenários, antecedentes, esquemas de cenário e tabelas; consultado em 2026-10-03.
- [Cucumber — repositório oficial](https://github.com/cucumber/cucumber-js) — implementação de referência, exemplos e documentação do projeto; consultado em 2026-10-03.
