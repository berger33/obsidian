---
id: software.testes.tranche13.000722
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
fontes: ["https://spockframework.org/spock/docs/2.4/all_in_one.html", "https://spockframework.org/spock/docs/2.4/all_in_one.html#_fixture_methods"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Spock: limitar uso de Shared para recurso realmente comum

## Em uma frase
Campos de instância recebem objeto independente para cada feature; `@Shared` amplia vida útil e partilha objeto entre métodos.

## Por que importa
A escolha afeta isolamento e pode transformar alteração de um feature em premissa do próximo.

## Como funciona
Mantenha dados mutáveis em campo de instância; reserve `@Shared` para recurso caro e gerencie setupSpec/cleanupSpec em torno dele.

## Exemplo
Um mapa de resultados novo pode ser campo de instância, enquanto um servidor imutável de apoio é recurso candidato a `@Shared`.

## Limites e trade-offs
Campos estáticos têm semântica global mais ampla; a documentação prefere compartilhamento explicitamente marcado quando necessário.

## Como verificar
Mude objeto compartilhado num feature e rode outro isoladamente e em conjunto para revelar se o contrato depende de ordem.

## Conexões
- [[spock-fixture-lifecycle-order]] — Veja também: Spock: dimensionar métodos de fixture por feature.
- [[spock-data-table-iterations]] — Veja também: Spock: parametrizar feature com where table.

## Fontes
- [Spock 2.4 — Reference Documentation](https://spockframework.org/spock/docs/2.4/all_in_one.html) — specifications, feature blocks, fixtures and runner; consultado em 2026-10-02.
- [Spock 2.4 — Fixture Methods](https://spockframework.org/spock/docs/2.4/all_in_one.html#_fixture_methods) — fixture lifecycle and inheritance order; consultado em 2026-10-02.
