---
id: software.testes.tranche22.001615
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
fontes: ["https://kotest.io/docs/proptest/property-test-config.html", "https://kotest.io/docs/proptest/property-test-functions.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Kotest: listeners por iteração e hex para não imprimíveis

## Em uma frase
O PropTestConfig aceita listeners (PropTestListener registrados via listeners = listOf(...)) que executam setup e teardown dentro de cada iteração da propriedade, não uma vez por teste.

## Por que importa
Setup por iteração é o que falta quando cada amostra exige estado fresco — criar e descartar um banco in-memory por par de strings, por exemplo.

## Como funciona
Outro flag da mesma página: outputHexForUnprintableChars = true imprime caracteres não imprimíveis em hexadecimal na mensagem de falha, porque strings de geradores aleatórios enchem o console de código de escape.

## Exemplo
O default é false — o guia registra isso explicitamente —, e o comportamento pode virar projeto-wide por kotest.properties no classpath sem tocar em cada teste.

## Limites e trade-offs
Listeners por iteração encarecem as 1000 execuções de forma invisível; meça o overhead antes de abrir mão do BeforeTest do spec.

## Como verificar
Configure o flag hex, force uma falha com um caractere nulo na string e compare a saída legível com a versão padrão.

## Conexões
- [[kotest-config-maxfailure]] — Veja também: Kotest: PropTestConfig e a tolerância a falhas.
- [[kotest-seeds]] — Veja também: Kotest: semente da geração e seed fixa.

## Fontes
- [Kotest — Property Test Configuration](https://kotest.io/docs/proptest/property-test-config.html) — PropTestConfig: maxFailure, listeners e saída hex; consultado em 2026-10-03.
- [Kotest — Property Test Functions](https://kotest.io/docs/proptest/property-test-functions.html) — forAll, checkAll, iterações e generators; consultado em 2026-10-03.
