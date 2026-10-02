---
id: software.testes.tranche13.000732
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
fontes: ["https://google.github.io/googletest/primer.html", "https://google.github.io/googletest/reference/assertions.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# GoogleTest: escolher ASSERT ou EXPECT pelo fluxo

## Em uma frase
`ASSERT_*` interrompe a função de teste no primeiro erro, enquanto `EXPECT_*` registra falha não fatal e continua.

## Por que importa
Escolha depende de se o restante do teste consegue produzir evidência válida após a condição falhar.

## Como funciona
Use `ASSERT_*` quando ausência de objeto torna chamadas seguintes inválidas; use `EXPECT_*` para acumular verificações independentes do mesmo resultado.

## Exemplo
Se vetor precisa ter três elementos antes de comparar cada item, assertion fatal protege indexação; diferenças de valores podem acumular expectations.

## Limites e trade-offs
Retorno antecipado por ASSERT pode pular cleanup manual colocado depois, então prefira RAII ou escopo garantido em C++ para recursos.

## Como verificar
Provoque tamanho incorreto e verifique que teste para sem acesso inválido; provoque valores distintos e confirme múltiplas falhas aparecem.

## Conexões
- [[googletest-test-fixture-instance]] — Veja também: GoogleTest: criar fixture independente por TEST_F.
- [[googletest-value-parameterized-suite]] — Veja também: GoogleTest: instanciar teste para conjunto de valores.

## Fontes
- [GoogleTest — Primer](https://google.github.io/googletest/primer.html) — TEST/TEST_F, assertions, fixtures and independence; consultado em 2026-10-02.
- [GoogleTest — Assertions Reference](https://google.github.io/googletest/reference/assertions.html) — fatal/nonfatal assertions and assertion helpers; consultado em 2026-10-02.
