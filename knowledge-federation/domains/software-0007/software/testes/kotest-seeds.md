---
id: software.testes.tranche22.001616
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
fontes: ["https://kotest.io/docs/proptest/property-test-seeds.html", "https://kotest.io/docs/proptest/property-test-functions.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Kotest: semente da geração e seed fixa

## Em uma frase
Cada execução sorteia valores a partir de uma semente derivada do kotlin.random.Random default; PropTestConfig(seed = 127305235) fixa a sequência, e PropertyTesting.defaultSeed muda a semente base de todos os testes.

## Por que importa
Sem semente, o achado de ontem é irrecuperável hoje; a página trata exatamente de transformar uma falha encontrada em teste de regressão permanente.

## Como funciona
Quando uma propriedade falha, o Kotest imprime a semente usada — o workflow oficial sugerido é duplicar o teste, cravar essa semente e congelar aquele conjunto de valores como caso de regressão.

## Exemplo
O seed fixo convive com o padrão aleatório no mesmo suíte: só o teste duplicado passa a ver sempre os mesmos 1000 inputs.

## Limites e trade-offs
Um teste com seed fixa envelhece: ele só cobre os valores daquela semente, então mantenha também a variante aleatória ao lado.

## Como verificar
Reproduza uma falha com seed extraída do log, apague o teste original e confirme que a versão cravada falha de novo em qualquer máquina.

## Conexões
- [[kotest-config-listeners-hex]] — Veja também: Kotest: listeners por iteração e hex para não imprimíveis.
- [[kotest-rerun-seeds]] — Veja também: Kotest: reexecução automática dos seeds que falharam.

## Fontes
- [Kotest — Property Test Seeds](https://kotest.io/docs/proptest/property-test-seeds.html) — sementes, rerun de falhas e ~/.kotest/seeds; consultado em 2026-10-03.
- [Kotest — Property Test Functions](https://kotest.io/docs/proptest/property-test-functions.html) — forAll, checkAll, iterações e generators; consultado em 2026-10-03.
