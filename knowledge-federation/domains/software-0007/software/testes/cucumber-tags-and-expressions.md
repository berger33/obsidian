---
id: software.testes.tranche17.001090
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

# Cucumber: filtrar execuções com etiquetas

## Em uma frase
Etiquetas aplicadas a funcionalidades, cenários e exemplos podem ser combinadas em expressões lógicas para selecionar o que será executado.

## Por que importa
Recortes por risco, área ou estágio permitem usar a mesma suíte em momentos diferentes sem duplicar arquivos.

## Como funciona
Aplique poucas etiquetas com significado estável e escreva expressões explícitas na linha de comando ou na configuração do projeto.

## Exemplo
Uma verificação rápida pode rodar os cenários marcados como críticos, deixando os fluxos demorados para a execução completa.

## Limites e trade-offs
Expressões complexas dificultam prever o conjunto selecionado, e uma etiqueta esquecida exclui cenários sem que ninguém perceba.

## Como verificar
Liste os cenários que seriam executados e compare com a intenção antes de fixar a expressão na esteira.

## Conexões
- [[cucumber-hooks-lifecycle]] — Veja também: Cucumber: usar ganchos de preparação e limpeza.
- [[cucumber-background-and-data-tables]] — Veja também: Cucumber: compartilhar contexto e tabelas.

## Fontes
- [Cucumber — Reference](https://cucumber.io/docs/cucumber/api/) — definições de passo, ganchos, etiquetas, paralelismo e relatórios; consultado em 2026-10-03.
- [Cucumber — repositório oficial](https://github.com/cucumber/cucumber-js) — implementação de referência, exemplos e documentação do projeto; consultado em 2026-10-03.
