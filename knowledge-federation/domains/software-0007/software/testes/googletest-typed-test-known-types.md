---
id: software.testes.tranche13.000734
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
fontes: ["https://google.github.io/googletest/advanced.html", "https://google.github.io/googletest/reference/testing.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# GoogleTest: compartilhar testes por tipos conhecidos

## Em uma frase
Typed tests executam o mesmo conjunto de definições para uma lista de tipos conhecida na compilação.

## Por que importa
Uma única propriedade pode comparar implementações que oferecem o mesmo contrato sem manter suites quase idênticas.

## Como funciona
Defina fixture template, associe tipos com `TYPED_TEST_SUITE` e use `TypeParam` e `TestFixture` dentro do corpo conforme exigência de C++.

## Exemplo
Um adaptador de coleção pode testar mesma operação para `std::vector<int>` e `std::deque<int>` com fixture template comum.

## Limites e trade-offs
Templates podem falhar por detalhe de compilação que não aparece em tipo concreto; erros de cada tipo exigem leitura de instância gerada.

## Como verificar
Inclua cada tipo previsto e confirme no relatório que a suíte foi instanciada para todos, não apenas compilada para alias padrão.

## Conexões
- [[googletest-value-parameterized-suite]] — Veja também: GoogleTest: instanciar teste para conjunto de valores.
- [[googletest-type-parameterized-contract]] — Veja também: GoogleTest: publicar teste por tipo para implementar depois.

## Fontes
- [GoogleTest — Advanced Topics](https://google.github.io/googletest/advanced.html) — typed/value-parameterized tests and advanced assertions; consultado em 2026-10-02.
- [GoogleTest — Testing Reference](https://google.github.io/googletest/reference/testing.html) — test macros, fixtures and parameterized-test APIs; consultado em 2026-10-02.
