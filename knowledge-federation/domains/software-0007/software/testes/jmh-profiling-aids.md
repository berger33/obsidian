---
id: software.testes.tranche16.000990
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

# JMH: complementar a medição com perfiladores

## Em uma frase
A execução aceita perfis embutidos, como contabilização de coleta de lixo, e permite escolher perfiladores externos por linha de comando.

## Por que importa
Números de tempo sem informação de alocação e de pausas levam a otimizações equivocadas, que trocam custo de CPU por pressão de memória.

## Como funciona
Acompanhe métricas de alocação junto do tempo, use perfiladores quando o resultado surpreender e registre a configuração usada na medição.

## Exemplo
Um método com tempo estável mas com taxa elevada de alocação pode degradar sob carga real por pressão no coletor de lixo.

## Limites e trade-offs
Perfiladores acrescentam custo e alteram o comportamento observado, portanto os valores de tempo com perfil ativo não devem ser comparados diretamente com os da execução limpa.

## Como verificar
Execute o mesmo caso com e sem perfil de coleta e confirme que a diferença de tempo é compatível com a descrição do próprio perfil.

## Conexões
- [[jmh-parameters]] — Veja também: JMH: variar entradas com parâmetros.
- [[jmh-execution-and-pitfalls]] — Veja também: JMH: executar e interpretar com critério.

## Fontes
- [JMH — repositório oficial](https://github.com/openjdk/jmh) — anotações, modos de medição, forking, estados, parâmetros e execução; consultado em 2026-10-03.
- [OpenJDK — JMH](https://openjdk.org/projects/code-tools/jmh/) — visão geral do harness oficial de microbenchmarks da JVM; consultado em 2026-10-03.
