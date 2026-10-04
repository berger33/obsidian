---
id: software.testes.tranche16.000989
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

# JMH: variar entradas com parâmetros

## Em uma frase
Campos anotados como parâmetros recebem cada valor declarado, e o benchmark é expandido em uma execução por combinação de valores.

## Por que importa
Explorar tamanhos e configurações dentro de um único código evita duplicar benchmarks e torna visível a sensibilidade do resultado à entrada.

## Como funciona
Declare os valores como constantes nomeadas, mantenha o número de combinações sob controle e interprete cada resultado separadamente.

## Exemplo
Avaliar um algoritmo com conjuntos de dados pequenos, médios e grandes revela o ponto em que a escolha de estrutura deixa de compensar.

## Limites e trade-offs
A expansão multiplica o tempo total de execução, e valores gerados aleatoriamente sem semente fixa impedem a reprodução do experimento.

## Como verificar
Confirme no relatório que cada combinação declarada aparece com resultado próprio e que a soma corresponde ao esperado.

## Conexões
- [[jmh-setup-and-teardown]] — Veja também: JMH: preparar em níveis adequados.
- [[jmh-profiling-aids]] — Veja também: JMH: complementar a medição com perfiladores.

## Fontes
- [JMH — exemplos oficiais](https://github.com/openjdk/jmh/tree/master/jmh-samples) — amostras de parâmetros, estados, preparação e consumo de resultados; consultado em 2026-10-03.
- [JMH — repositório oficial](https://github.com/openjdk/jmh) — anotações, modos de medição, forking, estados, parâmetros e execução; consultado em 2026-10-03.
