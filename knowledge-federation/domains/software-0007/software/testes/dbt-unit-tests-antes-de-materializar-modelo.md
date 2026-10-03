---
id: software.testes.tranche15.000918
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
fontes: ["https://docs.getdbt.com/docs/build/unit-tests?version=2", "https://docs.getdbt.com/docs/build/data-tests?version=2"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# dbt unit tests: testar lógica de modelo com inputs controlados

## Em uma frase
Unit tests de dbt verificam transformações do modelo usando entradas simuladas antes que a tabela final precise ser materializada, em contraste com data tests que inspecionam dados construídos.

## Por que importa
O resultado esperado pode capturar regras de negócio e casos de borda sem carregar um conjunto inteiro de produção; definir casos explícitos também torna mudanças de SQL revisáveis.

## Como funciona
Os YAMLs de unit test vivem junto aos model paths, e não na pasta reservada a data tests.

## Exemplo
Escreva casos de input/output em `models/.../unit_tests.yml` e use o comando apropriado ou `dbt build` para executar unit tests antes da materialização e data tests depois.

## Limites e trade-offs
Unit tests não substituem validação de qualidade sobre o dataset real e algumas features do warehouse, macros ou incremental models podem exigir condições especiais.

## Como verificar
Faça um caso de cada branch da transformação, compare saída real com tabela esperada e depois execute data tests no modelo materializado para validar integração.

## Conexões
- [[dbt-test-select-data-unit-e-singular]] — Veja também: dbt test: filtrar deliberadamente data, unit, singular ou generic tests.
- [[dbt-warnings-nao-devem-virar-politica-permanente]] — Veja também: dbt data tests: definir prazo de revisão para alertas de qualidade.

## Fontes
- [dbt v2 — Unit tests](https://docs.getdbt.com/docs/build/unit-tests?version=2) — inputs e expected output de models antes da materialização; consultado em 2026-10-02.
- [dbt v2 — Add data tests to your DAG](https://docs.getdbt.com/docs/build/data-tests?version=2) — testes singulares/genéricos, registros violadores e argumentos; consultado em 2026-10-02.
