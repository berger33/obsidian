---
id: software.testes.tranche13.000738
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

# GoogleTest: reservar environment global para recurso de programa

## Em uma frase
Test environment oferece `SetUp` e `TearDown` de escopo do programa, diferente de fixture por teste.

## Por que importa
Inicialização cara pode ocorrer uma vez, mas seu estado torna-se compartilhado por todas as suites.

## Como funciona
Use environment apenas para infraestrutura verdadeiramente global, registre-o antes de `RUN_ALL_TESTS()` e mantenha dados mutáveis por caso em fixture local.

## Exemplo
Um servidor de apoio pode inicializar uma vez enquanto cada teste cria seu próprio namespace e remove registros no teardown.

## Limites e trade-offs
Falha de setup global pode impedir diversas suites e cleanup global não substitui liberação em teste que cria recurso próprio.

## Como verificar
Faça setup global falhar em ambiente de teste e confirme relatório, status de saída e ausência de servidor órfão após o processo.

## Conexões
- [[googletest-death-test-process]] — Veja também: GoogleTest: isolar comportamento de morte em subprocesso.
- [[gmock-interaction-expectation]] — Veja também: gMock: expressar cardinalidade e argumento em EXPECT_CALL.

## Fontes
- [GoogleTest — Advanced Topics](https://google.github.io/googletest/advanced.html) — typed/value-parameterized tests and advanced assertions; consultado em 2026-10-02.
- [GoogleTest — Testing Reference](https://google.github.io/googletest/reference/testing.html) — test macros, fixtures and parameterized-test APIs; consultado em 2026-10-02.
