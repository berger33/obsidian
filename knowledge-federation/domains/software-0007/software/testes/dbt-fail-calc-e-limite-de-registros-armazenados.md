---
id: software.testes.tranche15.000916
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
fontes: ["https://docs.getdbt.com/reference/resource-configs/fail_calc.md", "https://docs.getdbt.com/reference/resource-configs/limit.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# dbt data tests: distinguir métrica de falhas do limite de registros retornados

## Em uma frase
`fail_calc` define a expressão usada para calcular falhas; `limit` limita a quantidade de linhas de falha retornadas pela query do teste e também pode limitar o que fica armazenado.

## Por que importa
As opções têm papéis diferentes: fail_calc define a métrica de falhas, enquanto limit restringe os registros retornados, não apenas o volume de material guardado.

## Como funciona
Ao combiná-los, confira o SQL compilado e a semântica do adapter para não tratar uma amostra limitada como total de violações.

## Exemplo
Defina um fail_calc adequado ao contrato de severidade; use `limit: 100` para limitar linhas de falha retornadas/armazenadas em um teste volumoso e inspecione o SQL compilado antes de interpretar o número como contagem total.

## Limites e trade-offs
Um limite pode reduzir a evidência disponível para depuração e não deve ser descrito como simples teto de armazenamento. Agregações customizadas, sobretudo em resultados sem linhas, exigem um caso que retorne zero válido.

## Como verificar
Crie zero, poucas e muitas violações, execute com e sem limit, compare linhas retornadas e armazenadas e confira separadamente o valor usado por fail_calc e o SQL gerado.

## Conexões
- [[dbt-where-limita-populacao-sem-mudar-regra]] — Veja também: dbt data tests: usar where para limitar a população avaliada.
- [[dbt-test-select-data-unit-e-singular]] — Veja também: dbt test: filtrar deliberadamente data, unit, singular ou generic tests.

## Fontes
- [dbt — fail_calc](https://docs.getdbt.com/reference/resource-configs/fail_calc.md) — contagem padrão, expressão customizada e tratamento de resultado sem linhas; consultado em 2026-10-02.
- [dbt — limit](https://docs.getdbt.com/reference/resource-configs/limit.md) — limite de registros de falha retornados pela query e relação com armazenamento; consultado em 2026-10-02.
