---
id: software.testes.tranche16.000984
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
fontes: ["https://openjdk.org/projects/code-tools/jmh/", "https://github.com/openjdk/jmh"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# JMH: escolher o modo de medição

## Em uma frase
Os modos disponíveis medem vazão por unidade de tempo, tempo médio por operação, amostragem de distribuição e execução única.

## Por que importa
Cada modo responde a uma pergunta diferente, e usar tempo médio para medir capacidade de processamento leva a conclusões invertidas.

## Como funciona
Escolha vazão para capacidade, tempo médio para custo por operação, amostragem para distribuição e execução única para custo de inicialização.

## Exemplo
Comparar tempo de inicialização de um componente faz sentido no modo de execução única, em que o aquecimento é deliberadamente excluído.

## Limites e trade-offs
Modos com tempo fixo de iteração não medem operações isoladas de duração longa, e a amostragem acrescenta custo próprio à coleta.

## Como verificar
Execute o mesmo benchmark em dois modos e confirme que o resultado é coerente entre eles ao converter unidade de medida.

## Conexões
- [[jmh-blackhole-consumption]] — Veja também: JMH: consumir resultados para evitar eliminação.
- [[jmh-warmup-and-measurement]] — Veja também: JMH: separar aquecimento de medição.

## Fontes
- [OpenJDK — JMH](https://openjdk.org/projects/code-tools/jmh/) — visão geral do harness oficial de microbenchmarks da JVM; consultado em 2026-10-03.
- [JMH — repositório oficial](https://github.com/openjdk/jmh) — anotações, modos de medição, forking, estados, parâmetros e execução; consultado em 2026-10-03.
