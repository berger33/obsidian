---
id: software.testes.tranche15.000919
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
data_revisao_ia: "2026-10-02"
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://docs.getdbt.com/reference/data-test-configs?version=2", "https://docs.getdbt.com/reference/commands/test?version=2"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# dbt data tests: definir prazo de revisão para alertas de qualidade

## Em uma frase
Configurar severity de warning pode manter uma migração em andamento sem bloquear toda a build, mas transforma uma violação em sinal não bloqueante até a política mudar.

## Por que importa
Um aviso recorrente perde valor se não tiver owner, prazo e critério de promoção.

## Como funciona
Em vez de usar a configuração como exceção eterna, capture o número de falhas e determine quando o teste volta a ser erro.

## Exemplo
Associe uma severity warning temporária a um ticket ou marco de migração e registre no projeto o limite em que o job deve falhar; remova a tolerância quando o dado for corrigido.

## Limites e trade-offs
`warn_if` e `error_if` precisam refletir contagem interpretável; aumentar thresholds pode mascarar crescimento gradual de falhas.

## Como verificar
Rode um cenário abaixo e acima do limite, monitore o relatório ao longo de commits e verifique que o job ainda sinaliza warnings e errors de forma distinta.

## Conexões
- [[dbt-unit-tests-antes-de-materializar-modelo]] — Veja também: dbt unit tests: testar lógica de modelo com inputs controlados.

## Fontes
- [dbt v2 — Data test configurations](https://docs.getdbt.com/reference/data-test-configs?version=2) — severity, error_if, warn_if, store_failures, limit, where e fail_calc; consultado em 2026-10-02.
- [dbt v2 — About dbt test command](https://docs.getdbt.com/reference/commands/test?version=2) — seleção de data/unit tests e pré-requisitos de materialização; consultado em 2026-10-02.
