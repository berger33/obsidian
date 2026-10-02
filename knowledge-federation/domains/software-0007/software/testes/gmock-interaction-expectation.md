---
id: software.testes.tranche13.000739
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
fontes: ["https://google.github.io/googletest/gmock_for_dummies.html", "https://google.github.io/googletest/gmock_cook_book.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# gMock: expressar cardinalidade e argumento em EXPECT_CALL

## Em uma frase
`EXPECT_CALL` descreve chamada esperada a mock, incluindo método, argumentos, frequência e resposta opcional.

## Por que importa
Interação é evidência útil quando contrato exige publicar evento ou consultar colaborador, sem substituir assertion de resultado principal.

## Como funciona
Declare expectativa antes de exercitar código, use matcher que revela regra e configure ação quando o retorno influencia caminho sob teste.

## Exemplo
Um mock de fila pode esperar uma publicação com identificador do pedido e devolver confirmação controlada ao serviço.

## Limites e trade-offs
Expectativas excessivamente exatas sobre chamadas internas deixam teste frágil; mock não comprova efeito no sistema externo real.

## Como verificar
Remova a chamada prevista e depois altere o argumento para confirmar que diagnostics distinguem ausência de interação e valor incorreto.

## Conexões
- [[googletest-global-environment-boundary]] — Veja também: GoogleTest: reservar environment global para recurso de programa.

## Fontes
- [gMock — For Dummies](https://google.github.io/googletest/gmock_for_dummies.html) — mock declarations, EXPECT_CALL and behavior; consultado em 2026-10-02.
- [gMock — Cookbook](https://google.github.io/googletest/gmock_cook_book.html) — advanced mock patterns, actions, matchers and lifetime; consultado em 2026-10-02.
