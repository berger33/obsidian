---
id: software.testes.tranche21.001550
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-21.md"
fontes: ["https://github.com/CodeIntelligenceTesting/jazzer", "https://github.com/CodeIntelligenceTesting/jazzer/blob/main/docs/arguments-and-configuration-options.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Jazzer: fuzzing em processo para a JVM

## Em uma frase
O Jazzer faz fuzzing dirigido por cobertura, no próprio processo da JVM, gerando e mutando entradas de um método de teste para maximizar o alcance de código e encontrar falhas.

## Por que importa
Um fuzzer em processo evita o custo de reiniciar a máquina virtual por iteração e aproveita a instrumentação de cobertura da própria JVM para decidir o que vale a pena mutar.

## Como funciona
Escreva um fuzz test que receba entradas arbitrárias, passe a classe como alvo e deixe o Jazzer conduzir a geração de casos.

## Exemplo
O programa de teste recebe uma String, um int ou arrays e chama o analisador real em cada iteração, sem dados de exemplo fixos.

## Limites e trade-offs
O alvo precisa tolerar entradas malformadas como dados, não como exceção; fuzz test sem fronteira clara gera montanhas de crashes de parser alheio.

## Como verificar
Rode o exemplo mínimo do repositório e confirme a contagem de execuções crescente no resumo.

## Conexões
- [[jazzer-standalone-binary]] — Veja também: Jazzer: binário standalone da página de releases.

## Fontes
- [Jazzer — repositório oficial](https://github.com/CodeIntelligenceTesting/jazzer) — modos standalone e JUnit, corpus, inputs e sanitizers; consultado em 2026-10-03.
- [Jazzer — Arguments and configuration options](https://github.com/CodeIntelligenceTesting/jazzer/blob/main/docs/arguments-and-configuration-options.md) — argumentos do agente e hooks desativáveis; consultado em 2026-10-03.
