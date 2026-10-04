---
id: software.testes.tranche16.000985
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

# JMH: separar aquecimento de medição

## Em uma frase
As anotações definem quantas iterações preparam a máquina virtual e quantas produzem os números que entram no relatório.

## Por que importa
Compilação em tempo de execução e carregamento de classes distorcem as primeiras execuções, e misturá-las com a medição contamina o resultado.

## Como funciona
Configure iterações de aquecimento suficientes para estabilizar o desempenho e iterações de medição em quantidade que reduza a margem de erro.

## Exemplo
Um benchmark de algoritmo curto pode exigir mais iterações de aquecimento e medições curtas, enquanto um caso longo aceita menos repetições com tempo maior.

## Limites e trade-offs
Mais iterações aumentam a duração total, e um aquecimento insuficiente pode produzir diferença que não existe no uso continuado.

## Como verificar
Compare a dispersão entre iterações de medição e aumente o aquecimento quando as primeiras ainda mostrarem tendência de queda.

## Conexões
- [[jmh-modes]] — Veja também: JMH: escolher o modo de medição.
- [[jmh-forking]] — Veja também: JMH: isolar execuções com fork.

## Fontes
- [JMH — repositório oficial](https://github.com/openjdk/jmh) — anotações, modos de medição, forking, estados, parâmetros e execução; consultado em 2026-10-03.
- [JMH — exemplos oficiais](https://github.com/openjdk/jmh/tree/master/jmh-samples) — amostras de parâmetros, estados, preparação e consumo de resultados; consultado em 2026-10-03.
