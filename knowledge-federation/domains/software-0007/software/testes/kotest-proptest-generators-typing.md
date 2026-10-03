---
id: software.testes.tranche22.001619
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
fontes: ["https://kotest.io/docs/proptest/property-test-functions.html", "https://kotest.io/docs/proptest/property-test-generators.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Kotest: tipos nos parâmetros são o registro de generators

## Em uma frase
A resolução de geradores é feita pelos type parameters da chamada — forAll<String, Int, Boolean> amarra cada posição a um generator — e a mesma lógica permite ao Kotest cobrir aridades de até 14 argumentos sem reflection sobre o lambda.

## Por que importa
O contrato fica no tipo, não em anotação ou string de nome de método: erro de espaço de amostragem vira erro de compilação de teste, mais cedo que em qualquer registro dinâmico.

## Como funciona
Para trocar o gerador de uma posição, passa-se o Arb posicional e os tipos restantes continuam resolvidos automaticamente, misturando modos na mesma chamada.

## Exemplo
A página exemplifica a tripla <String, Int, Boolean> como "3-arity property test" com random String, random int e random boolean nas posições.

## Limites e trade-offs
Aridade alta rima com relatório proporcionalmente ruidoso; 14 parâmetros sorteando 1000 vezes pede recorte de geradores ou falhas difíceis de ler.

## Como verificar
Declare um forAll com um tipo sem generator embutido (sua data class) e veja a mensagem de localização de gerador reclamando em tempo de execução.

## Conexões
- [[kotest-proptest-in-specs]] — Veja também: Kotest: propriedade dentro de spec e versão da doc.

## Fontes
- [Kotest — Property Test Functions](https://kotest.io/docs/proptest/property-test-functions.html) — forAll, checkAll, iterações e generators; consultado em 2026-10-03.
- [Kotest — Property Test Generators](https://kotest.io/docs/proptest/property-test-generators.html) — catálogo de generators embutidos citado pela página de funções; consultado em 2026-10-03.
