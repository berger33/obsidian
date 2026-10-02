---
id: software.testes.tranche13.000724
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
fontes: ["https://spockframework.org/spock/docs/2.4/data_driven_testing.html", "https://spockframework.org/spock/docs/2.4/all_in_one.html#_fixture_methods"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Spock: preservar isolamento entre linhas de dados

## Em uma frase
Cada iteração de feature data-driven ganha instância própria da specification e passa por setup e cleanup.

## Por que importa
Separar linhas reduz contaminação de state e permite interpretar falhas individualmente, mesmo dentro do mesmo método.

## Como funciona
Crie fixture por iteração, não guarde resultado mutável em campo `@Shared` sem necessidade e use ordem de dados apenas para organizar leitura.

## Exemplo
Uma tabela de três payloads cria client limpo para cada valor e verifica status correspondente sem reusar cache entre linhas.

## Limites e trade-offs
Compartilhar objeto via static ou `@Shared` altera esse isolamento e pode afetar outras methods da specification.

## Como verificar
Execute iterações em ordem diferente e verifique que valores de linha não aparecem no estado observado pela seguinte.

## Conexões
- [[spock-data-table-iterations]] — Veja também: Spock: parametrizar feature com where table.
- [[spock-mock-interaction-constraints]] — Veja também: Spock: especificar cardinalidade e alvo de interação.

## Fontes
- [Spock 2.4 — Data-Driven Testing](https://spockframework.org/spock/docs/2.4/data_driven_testing.html) — where blocks, data tables, iteration isolation and failures; consultado em 2026-10-02.
- [Spock 2.4 — Fixture Methods](https://spockframework.org/spock/docs/2.4/all_in_one.html#_fixture_methods) — fixture lifecycle and inheritance order; consultado em 2026-10-02.
