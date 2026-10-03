---
id: software.testes.tranche18.001249
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-18.md"
fontes: ["https://allurereport.org/docs/steps/", "https://allurereport.org/docs/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Allure: descrever passos do teste

## Em uma frase
Anotações de passo dividem o teste em ações nomeadas, com possibilidade de aninhamento e parametrização do nome exibido.

## Por que importa
A divisão em passos mostra em que ponto da jornada a falha ocorreu, sem exigir leitura do código do teste.

## Como funciona
Anote as ações relevantes com nome legível, evite passos triviais e mantenha a hierarquia correspondente às etapas do fluxo.

## Exemplo
Um caso de compra pode exibir os passos de escolher produto, preencher pagamento e confirmar pedido, indicando qual deles falhou.

## Limites e trade-offs
Excesso de passos de granularidade mínima polui o relatório, e nomes técnicos reduzem o valor para quem não escreveu o teste.

## Como verificar
Provoque falha em um passo intermediário e confirme que o relatório destaca exatamente esse passo, e não o teste inteiro.

## Conexões
- [[allure-results-and-report]] — Veja também: Allure: gerar relatório a partir de resultados.
- [[allure-attachments]] — Veja também: Allure: anexar evidências ao resultado.

## Fontes
- [Allure Report — Steps](https://allurereport.org/docs/steps/) — divisão do teste em passos nomeados e aninhados; consultado em 2026-10-03.
- [Allure Report — Documentation](https://allurereport.org/docs/) — resultados, passos, anexos, histórico, tendências e publicação; consultado em 2026-10-03.
