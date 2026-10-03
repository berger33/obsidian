---
id: software.testes.tranche22.001611
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

# Kotest: checkAll com asserções infixas

## Em uma frase
checkAll considera o teste válido enquanto nenhuma exceção for lançada, então o corpo usa as asserções normais do Kotest — a + b shouldHaveLength a.length + b.length é a forma documentada de expresar a propriedade com o vocabulário de asserções do framework.

## Por que importa
Reaproveitar os matchers should já conhecidos do time elimina o "estilo booleano" que esconde qual lado da igualdade falhou; a mensagem do matcher entra no relatório da propriedade.

## Como funciona
Envolva o bloco num spec FreeSpec e o property test é um caso comum da suíte, descoberto e reportado como qualquer outro teste Kotest.

## Exemplo
Na página oficial o teste "String size" aparece escrito duas vezes, em forAll e checkAll, e as duas versões são declaradas equivalentes.

## Limites e trade-offs
O guia documenta que o estilo booleano vem das bibliotecas Haskell que inspiraram o projeto; quem espera shrinking customizado sobre o valor de retorno precisa ler a página própria de shrinking.

## Como verificar
Converta um forAll que retorna comparação de listas para checkAll com shouldBe e compare a clareza da falha injetada.

## Conexões
- [[kotest-proptest-what]] — Veja também: Kotest: propriedades com duas funções, forAll e checkAll.
- [[kotest-iterations]] — Veja também: Kotest: mil iterações por padrão, ajustáveis por argumento.

## Fontes
- [Kotest — Property Test Functions](https://kotest.io/docs/proptest/property-test-functions.html) — forAll, checkAll, iterações e generators; consultado em 2026-10-03.
- [Kotest — Property Test Configuration](https://kotest.io/docs/proptest/property-test-config.html) — PropTestConfig: maxFailure, listeners e saída hex; consultado em 2026-10-03.
