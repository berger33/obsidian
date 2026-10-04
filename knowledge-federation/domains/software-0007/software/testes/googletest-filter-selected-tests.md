---
id: software.testes.tranche13.000736
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
fontes: ["https://google.github.io/googletest/reference/testing.html", "https://google.github.io/googletest/advanced.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# GoogleTest: filtrar teste sem remover registro

## Em uma frase
Filtro `--gtest_filter` seleciona suites e testes pelo padrão de nome durante execução.

## Por que importa
Seleção facilita reproduzir falha rápida sem alterar macros ou apagar teste do binário.

## Como funciona
Passe filtro no runner, use padrões documentados de inclusão/exclusão e confirme no output quantos casos foram realmente executados.

## Exemplo
`--gtest_filter=ParserTest.*` pode limitar diagnóstico à suite parser antes de uma execução completa de regressão.

## Limites e trade-offs
Filtro mal formado ou mais estreito do que esperado pode rodar zero ou poucos testes e ser confundido com cobertura completa.

## Como verificar
Verifique resumo de casos selecionados e rode sem filtro como etapa final da pipeline.

## Conexões
- [[googletest-type-parameterized-contract]] — Veja também: GoogleTest: publicar teste por tipo para implementar depois.
- [[googletest-death-test-process]] — Veja também: GoogleTest: isolar comportamento de morte em subprocesso.

## Fontes
- [GoogleTest — Testing Reference](https://google.github.io/googletest/reference/testing.html) — test macros, fixtures and parameterized-test APIs; consultado em 2026-10-02.
- [GoogleTest — Advanced Topics](https://google.github.io/googletest/advanced.html) — typed/value-parameterized tests and advanced assertions; consultado em 2026-10-02.
