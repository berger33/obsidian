---
id: software.testes.tranche20.001362
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-20.md"
fontes: ["https://docs.gauge.org/execution", "https://github.com/getgauge/gauge"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Gauge: selecionar execuções por etiquetas

## Em uma frase
Especificações e cenários podem receber etiquetas, e a execução aceita expressões com conjunção, disjunção e negação sobre elas.

## Por que importa
A seleção por etiqueta permite rodar o conjunto relevante em cada momento sem manter listas de arquivos separadas.

## Como funciona
Aplique etiquetas por tipo de verificação e por área, e escreva expressões explícitas combinando os critérios desejados.

## Exemplo
O comando pode executar apenas o conjunto de fumaça em uma revisão e o conjunto completo antes da entrega.

## Limites e trade-offs
Etiquetas inconsistentes entre times quebram as expressões, e etiquetas demais tornam a seleção difícil de entender.

## Como verificar
Liste as etiquetas em uso e confirme que a expressão escolhida seleciona exatamente os cenários esperados.

## Conexões
- [[gauge-concepts]] — Veja também: Gauge: agrupar passos em conceitos.
- [[gauge-context-and-hooks]] — Veja também: Gauge: preparar estado com ganchos e contexto.

## Fontes
- [Gauge — Executar especificações](https://docs.gauge.org/execution) — ganchos, ambientes, etiquetas e execução paralela; consultado em 2026-10-03.
- [Gauge — repositório oficial](https://github.com/getgauge/gauge) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
