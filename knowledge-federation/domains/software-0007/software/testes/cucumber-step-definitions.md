---
id: software.testes.tranche17.001087
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

# Cucumber: ligar passos a código

## Em uma frase
Cada passo do cenário corresponde a uma definição de passo que reconhece o texto, extrai parâmetros e executa a ação sobre o sistema.

## Por que importa
A ligação explícita entre texto e código evita que o cenário vire documentação decorativa sem efeito sobre o comportamento.

## Como funciona
Escreva definições específicas o suficiente para não colidirem, extraia parâmetros em vez de frases inteiras e mantenha o corpo curto delegando às bibliotecas do projeto.

## Exemplo
Um passo de preenchimento pode capturar o nome do campo e o valor, chamando o mesmo adaptador usado pelo restante da suíte.

## Limites e trade-offs
Definições genéricas com expressões amplas capturam passos de outros cenários, e o passo ambíguo falha ou executa a ação errada.

## Como verificar
Renomeie um passo no arquivo e confirme que a execução acusa a ausência de definição correspondente antes de rodar o cenário.

## Conexões
- [[cucumber-gherkin-structure]] — Veja também: Cucumber: estruturar o cenário em Gherkin.
- [[cucumber-scenario-outline-examples]] — Veja também: Cucumber: variar entradas com esquema de cenário.

## Fontes
- [Cucumber — Reference](https://cucumber.io/docs/cucumber/api/) — definições de passo, ganchos, etiquetas, paralelismo e relatórios; consultado em 2026-10-03.
- [Cucumber — repositório oficial](https://github.com/cucumber/cucumber-js) — implementação de referência, exemplos e documentação do projeto; consultado em 2026-10-03.
