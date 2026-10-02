---
id: software.testes.tranche13.000727
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
fontes: ["https://spockframework.org/spock/docs/2.4/interaction_based_testing.html", "https://spockframework.org/spock/docs/2.4/all_in_one.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Spock: evitar over-specification em mocks lenientes

## Em uma frase
Mocks Spock são lenientes por padrão para chamadas inesperadas que não foram descritas, respondendo com valor default.

## Por que importa
A tolerância a interações irrelevantes evita brittle tests que quebram a cada chamada interna adicional.

## Como funciona
Descreva somente interações que representam efeito requerido e adicione verificação negativa ou cardinalidade quando ausência ou frequência forem requisito explícito.

## Exemplo
Uma chamada interna de telemetria pode não importar ao teste que verifica publicação de recibo, portanto não precisa entrar na lista de expectations.

## Limites e trade-offs
Lenient não significa que chamada relevante possa faltar; interações descritas continuam sendo verificadas e chamadas podem retornar default sem produzir efeito esperado.

## Como verificar
Remova uma expectation relevante para demonstrar que teste depende também da saída, depois adicione expectation crítica e confirme diagnóstico.

## Conexões
- [[spock-stub-response-generator]] — Veja também: Spock: separar stubbing da verificação de interação.
- [[spock-exception-condition]] — Veja também: Spock: capturar exceção como parte da condição esperada.

## Fontes
- [Spock 2.4 — Interaction-Based Testing](https://spockframework.org/spock/docs/2.4/interaction_based_testing.html) — mock interaction constraints, stubbing and responses; consultado em 2026-10-02.
- [Spock 2.4 — Reference Documentation](https://spockframework.org/spock/docs/2.4/all_in_one.html) — specifications, feature blocks, fixtures and runner; consultado em 2026-10-02.
