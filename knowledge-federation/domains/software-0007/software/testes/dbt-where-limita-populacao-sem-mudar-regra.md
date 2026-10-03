---
id: software.testes.tranche15.000915
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
fontes: ["https://docs.getdbt.com/reference/data-test-configs?version=2", "https://docs.getdbt.com/docs/build/data-tests?version=2"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# dbt data tests: usar where para limitar a população avaliada

## Em uma frase
O config `where` permite aplicar a regra a um subconjunto das linhas do recurso, útil quando dados históricos ou partições antigas não pertencem ao contrato operacional atual.

## Por que importa
Mudar a população testada altera o que significa passar, mesmo que a expressão genérica continue igual.

## Como funciona
O filtro precisa refletir uma fronteira de negócio explícita e deve ser revisado quando os dados ou a política de retenção mudarem.

## Exemplo
Configure `where` para selecionar apenas registros cuja data seja posterior à política ativa e mantenha uma asserção separada se o histórico também precisa de validação eventual.

## Limites e trade-offs
Condição de data pode excluir precisamente as linhas defeituosas e mascarar regressão; nulls, timezone e limites inclusivos precisam de tratamento deliberado.

## Como verificar
Crie exemplos no limite temporal, antes e depois, compare consulta compilada e contagem de linhas afetadas, e valide o contrato com proprietário dos dados.

## Conexões
- [[dbt-store-failures-e-ciclo-de-vida]] — Veja também: dbt data tests: armazenar linhas que falharam para análise controlada.
- [[dbt-fail-calc-e-limite-de-registros-armazenados]] — Veja também: dbt data tests: distinguir métrica de falhas do limite de registros retornados.

## Fontes
- [dbt v2 — Data test configurations](https://docs.getdbt.com/reference/data-test-configs?version=2) — severity, error_if, warn_if, store_failures, limit, where e fail_calc; consultado em 2026-10-02.
- [dbt v2 — Add data tests to your DAG](https://docs.getdbt.com/docs/build/data-tests?version=2) — testes singulares/genéricos, registros violadores e argumentos; consultado em 2026-10-02.
