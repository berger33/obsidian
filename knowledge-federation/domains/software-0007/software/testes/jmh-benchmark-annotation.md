---
id: software.testes.tranche16.000982
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
fontes: ["https://github.com/openjdk/jmh", "https://openjdk.org/projects/code-tools/jmh/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# JMH: escrever o núcleo do benchmark

## Em uma frase
O método anotado como benchmark é envolvido em código gerado que executa e mede repetidamente a mesma operação.

## Por que importa
Medir com cronômetro manual dentro do teste sofre com otimizações do compilador que podem eliminar trabalho cujo resultado não é usado.

## Como funciona
Anote o método, devolva ou consuma o resultado para que ele não seja descartado e deixe a ferramenta controlar as repetições.

## Exemplo
Comparar duas formas de montar um texto exige consumir a string resultante, preservando o custo real da operação dentro da medição.

## Limites e trade-offs
O compilador just-in-time pode transformar um laço em código trivial, e a anotação sozinha não impede todas as formas de eliminação de código morto.

## Como verificar
Execute o mesmo método com e sem consumo do resultado e observe a diferença de ordem de grandeza no relatório.

## Conexões
- [[jmh-blackhole-consumption]] — Veja também: JMH: consumir resultados para evitar eliminação.

## Fontes
- [JMH — repositório oficial](https://github.com/openjdk/jmh) — anotações, modos de medição, forking, estados, parâmetros e execução; consultado em 2026-10-03.
- [OpenJDK — JMH](https://openjdk.org/projects/code-tools/jmh/) — visão geral do harness oficial de microbenchmarks da JVM; consultado em 2026-10-03.
