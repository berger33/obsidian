---
id: software.testes.tranche21.001558
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
fontes: ["https://github.com/CodeIntelligenceTesting/jazzer", "https://github.com/CodeIntelligenceTesting/jazzer/blob/main/examples/junit/src/test/java/com/example/JavaSeedFuzzTest.java"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Jazzer: sementes vindas de parâmetros do JUnit

## Em uma frase
Um @FuzzTest aceita sementes iniciais pelos parameter sources padrão do JUnit — @MethodSource, @CsvSource, @ValueSource ou ArgumentsSource próprios — que rodam como casos na regressão e como base de mutação no fuzzing.

## Por que importa
O que o time já escreve como testes parametrizados vira insumo do fuzzer sem camada extra, e a linha entre exemplo bom e semente deixa de existir.

## Como funciona
Liste nas fontes os inputs conhecidos por exercitar caminhos difíceis e deixe o modo de fuzzing partir deles para mutar.

## Exemplo
O exemplo JavaSeedFuzzTest.java do repositório mostra um @MethodSource alimentando o @FuzzTest.

## Limites e trade-offs
Objetos sem getters serializáveis no @MethodSource caem no mutador de construtores e são ignorados com aviso no start do Jazzer.

## Como verificar
Converta um teste parametrizado existente em fonte de sementes e confirme no log que a regressão executa cada conjunto.

## Conexões
- [[jazzer-gitattributes-binary]] — Veja também: Jazzer: marcar corpus e inputs como binários no git.
- [[jazzer-sanitizers-hooks]] — Veja também: Jazzer: sanitizers que denunciam a vulnerabilidade.

## Fontes
- [Jazzer — repositório oficial](https://github.com/CodeIntelligenceTesting/jazzer) — modos standalone e JUnit, corpus, inputs e sanitizers; consultado em 2026-10-03.
- [Jazzer — exemplo JavaSeedFuzzTest](https://github.com/CodeIntelligenceTesting/jazzer/blob/main/examples/junit/src/test/java/com/example/JavaSeedFuzzTest.java) — sementes de @MethodSource em @FuzzTest; consultado em 2026-10-03.
