---
id: software.testes.tranche16.000986
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
fontes: ["https://github.com/openjdk/jmh", "https://github.com/openjdk/jmh/tree/master/jmh-samples"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# JMH: isolar execuções com fork

## Em uma frase
O parâmetro de fork define quantos processos independentes executam o benchmark, cada um com sua própria máquina virtual.

## Por que importa
Forkar reduz a influência de otimizações residuais e de estado acumulado por execuções anteriores na mesma máquina virtual.

## Como funciona
Use mais de um fork para medições que sustentam decisão e reserve execução única para verificação rápida durante o desenvolvimento.

## Exemplo
Dois forks com aquecimento próprio produzem conjuntos independentes de medidas, permitindo avaliar a variância entre processos.

## Limites e trade-offs
Cada fork repete o custo de aquecimento, e máquinas com poucos núcleos podem sofrer interferência entre processos executados em paralelo.

## Como verificar
Compare a dispersão entre forks com a dispersão dentro das iterações para decidir se o número de processos é suficiente.

## Conexões
- [[jmh-warmup-and-measurement]] — Veja também: JMH: separar aquecimento de medição.
- [[jmh-state-scope]] — Veja também: JMH: escolher o escopo do estado.

## Fontes
- [JMH — repositório oficial](https://github.com/openjdk/jmh) — anotações, modos de medição, forking, estados, parâmetros e execução; consultado em 2026-10-03.
- [JMH — exemplos oficiais](https://github.com/openjdk/jmh/tree/master/jmh-samples) — amostras de parâmetros, estados, preparação e consumo de resultados; consultado em 2026-10-03.
