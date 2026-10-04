---
id: software.testes.tranche17.001089
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

# Cucumber: usar ganchos de preparação e limpeza

## Em uma frase
Ganchos executados antes e depois de cenários, passos ou da execução permitem preparar estado e liberar recursos em pontos controlados.

## Por que importa
A preparação comum evita repetir passos em cada cenário e a limpeza garante que dados de um caso não contaminem o seguinte.

## Como funciona
Use ganchos globais para recursos compartilhados, ganchos condicionais por etiqueta para grupos específicos e mantenha a limpeza próxima da preparação.

## Exemplo
Um gancho etiquetado pode limpar apenas as contas criadas pelos cenários de cadastro, sem afetar os demais.

## Limites e trade-offs
Ganchos que falham interrompem o cenário com erro pouco informativo, e a ordem de execução entre vários ganchos precisa ser compreendida pelo time.

## Como verificar
Provoque falha em um gancho de preparação e confirme que o relatório distingue o erro do gancho do erro do passo.

## Conexões
- [[cucumber-scenario-outline-examples]] — Veja também: Cucumber: variar entradas com esquema de cenário.
- [[cucumber-tags-and-expressions]] — Veja também: Cucumber: filtrar execuções com etiquetas.

## Fontes
- [Cucumber — Reference](https://cucumber.io/docs/cucumber/api/) — definições de passo, ganchos, etiquetas, paralelismo e relatórios; consultado em 2026-10-03.
- [Cucumber — repositório oficial](https://github.com/cucumber/cucumber-js) — implementação de referência, exemplos e documentação do projeto; consultado em 2026-10-03.
