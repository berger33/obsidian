---
id: software.testes.tranche15.000917
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
fontes: ["https://docs.getdbt.com/reference/commands/test?version=2", "https://docs.getdbt.com/docs/build/data-tests?version=2"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# dbt test: filtrar deliberadamente data, unit, singular ou generic tests

## Em uma frase
O comando `dbt test` executa data tests e unit tests existentes, e os seletor `test_type` distingue tipos de teste durante uma execução parcial.

## Por que importa
Seleção por modelo, pacote, origem ou tipo ajuda a dividir trabalhos.

## Como funciona
Escrever filtro diferente entre jobs pode deixar um grupo sem execução sem que o restante do pipeline indique a lacuna.

## Exemplo
Use `dbt test --select test_type:data` para somente data tests ou `test_type:unit` para unit tests e combine o predicado com o modelo alvo quando necessário.

## Limites e trade-offs
A seleção não constrói necessariamente o modelo de que o teste depende; o comando espera que os recursos apropriados tenham sido materializados ou preparados antes.

## Como verificar
Compare o inventário de testes descobertos com o plano selecionado e mantenha um job que cubra todos os tipos exigidos no mesmo commit.

## Conexões
- [[dbt-fail-calc-e-limite-de-registros-armazenados]] — Veja também: dbt data tests: distinguir métrica de falhas do limite de registros retornados.
- [[dbt-unit-tests-antes-de-materializar-modelo]] — Veja também: dbt unit tests: testar lógica de modelo com inputs controlados.

## Fontes
- [dbt v2 — About dbt test command](https://docs.getdbt.com/reference/commands/test?version=2) — seleção de data/unit tests e pré-requisitos de materialização; consultado em 2026-10-02.
- [dbt v2 — Add data tests to your DAG](https://docs.getdbt.com/docs/build/data-tests?version=2) — testes singulares/genéricos, registros violadores e argumentos; consultado em 2026-10-02.
