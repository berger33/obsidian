---
id: software.testes.tranche13.000717
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-13.md"
fontes: ["https://www.scalatest.org/scaladoc/3.2.20/org/scalatest/prop/TableDrivenPropertyChecks.html", "https://www.scalatest.org/user_guide/using_assertions"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# ScalaTest: associar cada linha de tabela a uma propriedade

## Em uma frase
`TableDrivenPropertyChecks` aplica uma propriedade às linhas tipadas de `Table` usando métodos como `forAll` e `forEvery`.

## Por que importa
Matriz pequena torna fronteiras explícitas e reduz cópia de assertions mantendo valores e nome de coluna legíveis.

## Como funciona
Defina cabeçalho com nomes string e linhas com aridade e tipos consistentes; use `forAll` para parar na primeira falha ou `forEvery` quando a revisão precisa registrar todas.

## Exemplo
Uma tabela de numerador e denominador pode cobrir sinais e zero; `whenever` descarta entradas que não satisfazem a pré-condição da propriedade.

## Limites e trade-offs
Tabela exercita apenas os valores enumerados, e `forAll` não continua depois da primeira linha que falha.

## Como verificar
Introduza uma linha inválida e confira o diagnóstico que associa a falha ao caso; em seguida compare com `forEvery` para verificar coleta de todas as falhas.

## Conexões
- [[scalatest-loan-fixture-cleanup]] — Veja também: ScalaTest: liberar fixture por loan pattern.
- [[scalatest-matcher-composition]] — Veja também: ScalaTest: compor matcher para expectativa legível.

## Fontes
- [ScalaTest 3.2.20 — TableDrivenPropertyChecks API](https://www.scalatest.org/scaladoc/3.2.20/org/scalatest/prop/TableDrivenPropertyChecks.html) — forAll over TableFor1 through TableFor22 and failure reporting per row; consultado em 2026-10-02.
- [ScalaTest — Assertions](https://www.scalatest.org/user_guide/using_assertions) — assertion APIs and diagnostic output; consultado em 2026-10-02.
