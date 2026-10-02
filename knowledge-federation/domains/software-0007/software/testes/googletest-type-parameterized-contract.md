---
id: software.testes.tranche13.000735
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

# GoogleTest: publicar teste por tipo para implementar depois

## Em uma frase
Type-parameterized tests definem padrões antes de conhecer a lista concreta de tipos que os instanciará.

## Por que importa
O padrão permite distribuir contrato de interface e deixar consumidores escolherem tipos compatíveis no ponto de uso.

## Como funciona
Declare suite com `TYPED_TEST_SUITE_P`, registre padrões, use `TypeParam` no corpo e instancie mais tarde com prefixo identificável.

## Exemplo
Biblioteca pode fornecer teste de conformidade para qualquer implementação de buffer que consumidor acople ao seu tipo concreto.

## Limites e trade-offs
Suite não exerce contrato até uma instanciação efetiva ser compilada e executada; registrar padrão não equivale a cobrir uma implementação.

## Como verificar
Adicione novo tipo consumidor e confirme que runner mostra prefixo da instanciação e executa todos os padrões esperados.

## Conexões
- [[googletest-typed-test-known-types]] — Veja também: GoogleTest: compartilhar testes por tipos conhecidos.
- [[googletest-filter-selected-tests]] — Veja também: GoogleTest: filtrar teste sem remover registro.

## Fontes
- [GoogleTest — Advanced Topics](https://google.github.io/googletest/advanced.html) — typed/value-parameterized tests and advanced assertions; consultado em 2026-10-02.
- [GoogleTest — Testing Reference](https://google.github.io/googletest/reference/testing.html) — test macros, fixtures and parameterized-test APIs; consultado em 2026-10-02.
