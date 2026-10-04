---
id: software.testes.tranche13.000731
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
fontes: ["https://google.github.io/googletest/primer.html", "https://google.github.io/googletest/advanced.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# GoogleTest: criar fixture independente por TEST_F

## Em uma frase
`TEST_F` liga caso a uma classe derivada de `testing::Test`, e cada teste usa objeto fixture próprio.

## Por que importa
Instância fresca impede que membros mutáveis de um exemplo contaminem outro sem perder helpers de setup compartilhados.

## Como funciona
Coloque estado por teste em membros, inicialize em `SetUp()` e limpe em `TearDown()` quando destruição normal não bastar.

## Exemplo
Fixture de parser pode abrir arquivo temporário em SetUp e carregar entrada nova para cada teste de erro ou sucesso.

## Limites e trade-offs
`SetUpTestSuite()` é outro escopo e seus recursos podem atravessar casos; declare e limpe estado compartilhado com disciplina independente.

## Como verificar
Altere membro no primeiro teste, execute segundo sozinho e em suite completa e confirme que começa com valor inicial.

## Conexões
- [[googletest-test-suite-registration]] — Veja também: GoogleTest: nomear suite e teste com TEST.
- [[googletest-fatal-vs-nonfatal]] — Veja também: GoogleTest: escolher ASSERT ou EXPECT pelo fluxo.

## Fontes
- [GoogleTest — Primer](https://google.github.io/googletest/primer.html) — TEST/TEST_F, assertions, fixtures and independence; consultado em 2026-10-02.
- [GoogleTest — Advanced Topics](https://google.github.io/googletest/advanced.html) — typed/value-parameterized tests and advanced assertions; consultado em 2026-10-02.
