---
id: software.testes.tranche13.000721
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
fontes: ["https://spockframework.org/spock/docs/2.4/all_in_one.html#_fixture_methods", "https://spockframework.org/spock/docs/2.4/all_in_one.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Spock: dimensionar métodos de fixture por feature

## Em uma frase
`setupSpec`, `setup`, `cleanup` e `cleanupSpec` cobrem preparação e liberação em escopos diferentes.

## Por que importa
Fixture fresca por feature melhora isolamento; recurso caro compartilhado requer ciclo mais amplo deliberado.

## Como funciona
Use `setup/cleanup` para estado por método, `setupSpec/cleanupSpec` para recurso compartilhado e respeite ordem de herança: setup de superclasse antes da subclasse e cleanup no sentido inverso.

## Exemplo
Uma configuração de suite inicia banco uma vez, enquanto cada feature cria transação própria e a encerra após suas assertions.

## Limites e trade-offs
Métodos de fixture não devem depender de campos de instância no escopo Spec quando não são `@Shared`; não mova mutable state para static sem motivo.

## Como verificar
Registre chamadas em superclasse e subclasse e confira ordem nos dois sentidos com uma falha no corpo da feature.

## Conexões
- [[spock-given-when-then-contract]] — Veja também: Spock: estruturar feature com given when then.
- [[spock-shared-field-scope]] — Veja também: Spock: limitar uso de Shared para recurso realmente comum.

## Fontes
- [Spock 2.4 — Fixture Methods](https://spockframework.org/spock/docs/2.4/all_in_one.html#_fixture_methods) — fixture lifecycle and inheritance order; consultado em 2026-10-02.
- [Spock 2.4 — Reference Documentation](https://spockframework.org/spock/docs/2.4/all_in_one.html) — specifications, feature blocks, fixtures and runner; consultado em 2026-10-02.
