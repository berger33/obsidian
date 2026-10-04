---
id: software.testes.tranche17.001095
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
fontes: ["https://cucumber.io/docs/cucumber/api/", "https://github.com/cucumber/cucumber-js"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Cucumber: sustentar a suíte ao longo do tempo

## Em uma frase
A camada de cenários precisa de manutenção, com passos reutilizáveis, dados controlados e decisão explícita sobre o que pertence a ela.

## Por que importa
Suítes de aceitação apodrecem quando tentam cobrir cada detalhe, e o custo de manutenção supera o benefício de manter tudo no mesmo formato.

## Como funciona
Reserve os cenários para regras de negócio revisáveis, deixe detalhes técnicos nas suítes de unidade e integração e trate os passos como código compartilhado.

## Exemplo
Regras de cálculo complexo ficam melhor em testes parametrizados, enquanto o fluxo principal revisável permanece descrito em Gherkin.

## Limites e trade-offs
Duplicar a mesma regra em vários cenários cria manutenção tripla, e passos com muitos parâmetros opcionais indicam abstração no lugar errado.

## Como verificar
Escolha um cenário duplicado e verifique se a regra pode ser representada uma única vez com esquema de cenário antes de remover a repetição.

## Conexões
- [[cucumber-living-documentation]] — Veja também: Cucumber: manter a documentação viva.

## Fontes
- [Cucumber — Reference](https://cucumber.io/docs/cucumber/api/) — definições de passo, ganchos, etiquetas, paralelismo e relatórios; consultado em 2026-10-03.
- [Cucumber — repositório oficial](https://github.com/cucumber/cucumber-js) — implementação de referência, exemplos e documentação do projeto; consultado em 2026-10-03.
