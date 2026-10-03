---
id: software.testes.tranche18.001190
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-18.md"
fontes: ["https://google.github.io/googletest/advanced.html", "https://github.com/google/googletest"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# GoogleTest: compartilhar preparação com fixtures

## Em uma frase
Uma classe de fixture herda da classe base de teste e define preparação e limpeza, que são executadas para cada caso que usa a fixture.

## Por que importa
A preparação reutilizada evita duplicação e garante que cada caso parta do mesmo estado explícito.

## Como funciona
Defina a classe, sobrescreva preparação e limpeza com a grafia correta e acesse os membros por meio da macro de caso.

## Exemplo
Uma fixture pode criar o objeto sob teste e uma coleção conhecida, e cada caso executa a partir desse estado recém-construído.

## Limites e trade-offs
A grafia incorreta do método de preparação faz o compilador criar um método novo, silenciosamente ignorado pela execução.

## Como verificar
Altere a preparação e confirme que todos os casos da fixture refletem a mudança, provando que a mesma rotina é executada.

## Conexões
- [[googletest-comparisons]] — Veja também: GoogleTest: comparar valores com veredito claro.
- [[googletest-parameterized]] — Veja também: GoogleTest: variar entradas com testes parametrizados.

## Fontes
- [GoogleTest — Advanced](https://google.github.io/googletest/advanced.html) — fixtures, parametrização, testes por tipo, filtros e asserções de morte; consultado em 2026-10-03.
- [GoogleTest — repositório oficial](https://github.com/google/googletest) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
