---
id: software.testes.tranche22.001618
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

# Kotest: propriedade dentro de spec e versão da doc

## Em uma frase
A doc de property testing vive dentro do framework de specs: todos os exemplos empacotam a propriedade como bloco de teste de um FreeSpec, com hooks, tags e relatório do próprio Kotest — sem executor separado.

## Por que importa
Adicionar uma propriedade ao projeto Kotest existente é escrever mais um bloco de teste, não introduzir plugin, engine ou build novo na esteira.

## Como funciona
O seletor de versão da página (v6.2 no cabeçalho) lembra que a documentação é versionada junto do framework ao consultar PropTestConfig.

## Exemplo
class PropertyExample: FreeSpec({ "String size" { forAll<String, String> { a, b -> ... } } }) — o invólucro repetido em todas as páginas da seção.

## Limites e trade-offs
Quem usa Kotest Assertions sem o runner completo precisa das dependências de property testing explícitas no build; a doc de proptest assume o framework ativo.

## Como verificar
Rode o PropertyExample acima num projeto vazio com o plugin Kotest e veja a propriedade aparecer como teste comum do spec.

## Conexões
- [[kotest-rerun-seeds]] — Veja também: Kotest: reexecução automática dos seeds que falharam.
- [[kotest-proptest-generators-typing]] — Veja também: Kotest: tipos nos parâmetros são o registro de generators.

## Fontes
- [Kotest — Property Test Functions](https://kotest.io/docs/proptest/property-test-functions.html) — forAll, checkAll, iterações e generators; consultado em 2026-10-03.
- [Kotest — Property Test Configuration](https://kotest.io/docs/proptest/property-test-config.html) — PropTestConfig: maxFailure, listeners e saída hex; consultado em 2026-10-03.
