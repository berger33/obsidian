---
id: software.testes.tranche16.000983
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

# JMH: consumir resultados para evitar eliminação

## Em uma frase
A estrutura oferece objeto de consumo que registra o valor produzido, impedindo que o compilador remova o cálculo por falta de uso aparente.

## Por que importa
Benchmarks que devolvem valores descartados medem menos do que se propõem a medir, e o resultado parece bom por um motivo falso.

## Como funciona
Aceite o objeto de consumo como parâmetro e registre todo valor derivado quando ele não estiver sendo devolvido pelo método.

## Exemplo
Em um benchmark de soma sobre coleção, o acumulador final precisa ser consumido para que o laço não seja otimizado para nada.

## Limites e trade-offs
Consumir tudo indiscriminadamente também esconde custos, então apenas os valores que representam o trabalho realizado devem ser registrados.

## Como verificar
Compare a medição de um laço com resultado devolvido e com resultado consumido para verificar convergência entre as duas formas.

## Conexões
- [[jmh-benchmark-annotation]] — Veja também: JMH: escrever o núcleo do benchmark.
- [[jmh-modes]] — Veja também: JMH: escolher o modo de medição.

## Fontes
- [JMH — repositório oficial](https://github.com/openjdk/jmh) — anotações, modos de medição, forking, estados, parâmetros e execução; consultado em 2026-10-03.
- [JMH — exemplos oficiais](https://github.com/openjdk/jmh/tree/master/jmh-samples) — amostras de parâmetros, estados, preparação e consumo de resultados; consultado em 2026-10-03.
