---
id: software.testes.tranche13.000726
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
fontes: ["https://spockframework.org/spock/docs/2.4/interaction_based_testing.html", "https://spockframework.org/spock/docs/2.4/data_driven_testing.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Spock: separar stubbing da verificação de interação

## Em uma frase
Operador `>>` define resposta que mock ou stub fornece quando recebe chamada correspondente.

## Por que importa
Controlar resposta permite explorar ramos sem acesso a serviço real, enquanto verification permanece focada apenas nas chamadas relevantes.

## Como funciona
Declare retorno fixo para caso simples e resposta calculada para chamada parametrizada; não adicione cardinalidade de verificação se o teste só precisa de estado.

## Exemplo
Um catálogo stub pode devolver taxa conhecida para subtotal e deixar feature verificar total final sem consultar serviço externo.

## Limites e trade-offs
Resposta configurada não garante que a unidade chamou a colaboração correta; use expectation separada quando a chamada for parte do contrato.

## Como verificar
Troque resposta por valor sentinela e confira que cálculo consome stub; acrescente interaction assertion somente se necessário para requisito.

## Conexões
- [[spock-mock-interaction-constraints]] — Veja também: Spock: especificar cardinalidade e alvo de interação.
- [[spock-lenient-mock-scope]] — Veja também: Spock: evitar over-specification em mocks lenientes.

## Fontes
- [Spock 2.4 — Interaction-Based Testing](https://spockframework.org/spock/docs/2.4/interaction_based_testing.html) — mock interaction constraints, stubbing and responses; consultado em 2026-10-02.
- [Spock 2.4 — Data-Driven Testing](https://spockframework.org/spock/docs/2.4/data_driven_testing.html) — where blocks, data tables, iteration isolation and failures; consultado em 2026-10-02.
