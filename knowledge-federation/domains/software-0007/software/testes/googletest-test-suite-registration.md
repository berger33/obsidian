---
id: software.testes.tranche13.000730
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
fontes: ["https://google.github.io/googletest/primer.html", "https://google.github.io/googletest/reference/testing.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# GoogleTest: nomear suite e teste com TEST

## Em uma frase
Macro `TEST()` registra função de teste associada a uma suite nomeada, sem exigir lista manual para executar os casos.

## Por que importa
Descoberta automática reduz manutenção de registry e facilita selecionar unidade de comportamento pelo nome emitido no relatório.

## Como funciona
Escolha suite que represente componente, use nome de teste para expectativa e mantenha assertions no corpo da função gerada pela macro.

## Exemplo
`TEST(ParserTest, RejectsTruncatedHeader)` mostra qual comportamento da classe foi exercitado quando o runner informa falha.

## Limites e trade-offs
Nomes longos não substituem setup independente; macros geram função registrada e não devem ser encapsuladas em loop de runtime.

## Como verificar
Execute filtro para suite e teste escolhidos e confirme que runner descobre exatamente o caso registrado.

## Conexões
- [[googletest-test-fixture-instance]] — Veja também: GoogleTest: criar fixture independente por TEST_F.

## Fontes
- [GoogleTest — Primer](https://google.github.io/googletest/primer.html) — TEST/TEST_F, assertions, fixtures and independence; consultado em 2026-10-02.
- [GoogleTest — Testing Reference](https://google.github.io/googletest/reference/testing.html) — test macros, fixtures and parameterized-test APIs; consultado em 2026-10-02.
