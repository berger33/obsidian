---
id: software.testes.tranche22.001612
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-22.md"
fontes: ["https://kotest.io/docs/proptest/property-test-functions.html", "https://kotest.io/docs/proptest/property-test-config.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Kotest: mil iterações por padrão, ajustáveis por argumento

## Em uma frase
Por padrão cada propriedade roda 1000 iterações, e o número se muda passando o valor direto na invocação — checkAll<Double, Double>(10_000) roda dez mil amostras daquele teste.

## Por que importa
Iteração em Kotlin é barata, mas não grátis: a régua padrão equilibra confiança e tempo de build, e subilas por teste (não globalmente) mantém o suite viável.

## Como funciona
Use contagens altas para código com caminhos raros e baixas para gerações caras; o argumento vive junto da lista de geradores na chamada.

## Exemplo
O exemplo documentado "a many iterations test" roda 10_000 passes com dois Doubles aleatórios por chamada.

## Limites e trade-offs
Iteração alta com gerador que faz I/O transforma a suíte em stress test; a página não oferece cota de tempo, só contagem.

## Como verificar
Rode a mesma propriedade com 100 e 10_000 iterações e compare tempo de wall-clock na saída do runner.

## Conexões
- [[kotest-checkall-assertions]] — Veja também: Kotest: checkAll com asserções infixas.
- [[kotest-generators]] — Veja também: Kotest: generators automáticos e Arb explícitos.

## Fontes
- [Kotest — Property Test Functions](https://kotest.io/docs/proptest/property-test-functions.html) — forAll, checkAll, iterações e generators; consultado em 2026-10-03.
- [Kotest — Property Test Configuration](https://kotest.io/docs/proptest/property-test-config.html) — PropTestConfig: maxFailure, listeners e saída hex; consultado em 2026-10-03.
