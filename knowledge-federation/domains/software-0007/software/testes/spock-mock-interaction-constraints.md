---
id: software.testes.tranche13.000725
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

# Spock: especificar cardinalidade e alvo de interação

## Em uma frase
Interação em bloco `then:` descreve chamadas esperadas por cardinalidade, alvo, método e argumentos.

## Por que importa
Assertion de interação confirma colaboração relevante sem inferir chamada apenas a partir de estado final.

## Como funciona
Declare expectativa junto da ação em `when`, use matcher de argumento que expressa contrato e mantenha cardinalidade estrita somente quando número de chamadas importa.

## Exemplo
`1 * notifier.send(orderId)` afirma que confirmação publicou um evento para o pedido sob teste.

## Limites e trade-offs
Uma expectation excessivamente específica acopla teste à implementação e pode falhar quando colaboração equivalente muda de estratégia.

## Como verificar
Remova a chamada e depois duplique-a; confirme que cada variação falha na dimensão que o contrato decidiu observar.

## Conexões
- [[spock-where-iteration-isolation]] — Veja também: Spock: preservar isolamento entre linhas de dados.
- [[spock-stub-response-generator]] — Veja também: Spock: separar stubbing da verificação de interação.

## Fontes
- [Spock 2.4 — Interaction-Based Testing](https://spockframework.org/spock/docs/2.4/interaction_based_testing.html) — mock interaction constraints, stubbing and responses; consultado em 2026-10-02.
- [Spock 2.4 — Reference Documentation](https://spockframework.org/spock/docs/2.4/all_in_one.html) — specifications, feature blocks, fixtures and runner; consultado em 2026-10-02.
