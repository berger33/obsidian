---
id: software.testes.tranche16.000988
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-16.md"
fontes: ["https://github.com/openjdk/jmh/tree/master/jmh-samples", "https://github.com/openjdk/jmh"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# JMH: preparar em níveis adequados

## Em uma frase
A preparação e a limpeza podem ocorrer uma vez por execução, por iteração ou por invocação, conforme o nível escolhido.

## Por que importa
Preparar dados dentro do trecho medido contamina a medição, enquanto preparar uma única vez pode acumular efeitos entre iterações.

## Como funciona
Coloque a construção do cenário no nível da execução e a restauração de invariantes no nível da iteração, mantendo a invocação livre de trabalho acessório.

## Exemplo
Um caso que altera uma coleção precisa restaurá-la a cada iteração, enquanto a criação do objeto medido pode acontecer uma vez por execução.

## Limites e trade-offs
Níveis mais finos repetem a preparação e encarecem o benchmark, distorcendo a comparação quando o custo de preparação não é desprezível.

## Como verificar
Registre o tempo total e a quantidade de invocações e confirme que o custo de preparação não domina o resultado.

## Conexões
- [[jmh-state-scope]] — Veja também: JMH: escolher o escopo do estado.
- [[jmh-parameters]] — Veja também: JMH: variar entradas com parâmetros.

## Fontes
- [JMH — exemplos oficiais](https://github.com/openjdk/jmh/tree/master/jmh-samples) — amostras de parâmetros, estados, preparação e consumo de resultados; consultado em 2026-10-03.
- [JMH — repositório oficial](https://github.com/openjdk/jmh) — anotações, modos de medição, forking, estados, parâmetros e execução; consultado em 2026-10-03.
