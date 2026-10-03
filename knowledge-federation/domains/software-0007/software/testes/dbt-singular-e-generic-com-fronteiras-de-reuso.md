---
id: software.testes.tranche15.000911
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
fontes: ["https://docs.getdbt.com/docs/build/data-tests?version=2", "https://docs.getdbt.com/reference/resource-properties/data-tests?version=2"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# dbt data tests: decidir quando um teste singular deve virar genérico

## Em uma frase
Teste singular é uma query SQL de uma regra específica; teste genérico recebe argumentos e reutiliza uma mesma definição em modelos, colunas e recursos diferentes.

## Por que importa
Repetir a mesma estrutura trocando apenas nome de coluna ou modelo sinaliza oportunidade de abstração.

## Como funciona
Manter uma regra verdadeiramente única como arquivo singular, porém, deixa a intenção direta e evita criar macro com parâmetros desnecessários.

## Exemplo
Escreva uma consulta em `tests/assert_total_positive.sql` para regra única; transforme a lógica em bloco `{% test ... %}` quando a mesma condição precisar ser aplicada a várias colunas com argumentos.

## Limites e trade-offs
Testes singulares não são referenciados como testes genéricos nas propriedades YAML, e a estrutura de pastas pode ter configurações diferentes para definições e instâncias.

## Como verificar
Localize casos duplicados no projeto, compare as queries compiladas e confirme que a versão genérica preserva os mesmos registros violadores que cada consulta singular anterior.

## Conexões
- [[dbt-data-test-consulta-retorna-registros-que-falham]] — Veja também: dbt data tests: escrever a consulta a partir da linha que viola o contrato.
- [[dbt-arguments-obrigatorios-em-data-tests-v2]] — Veja também: dbt v2: colocar argumentos de testes genéricos no bloco arguments.

## Fontes
- [dbt v2 — Add data tests to your DAG](https://docs.getdbt.com/docs/build/data-tests?version=2) — testes singulares/genéricos, registros violadores e argumentos; consultado em 2026-10-02.
- [dbt v2 — Data test properties](https://docs.getdbt.com/reference/resource-properties/data-tests?version=2) — sintaxe YAML e propriedades de testes genéricos; consultado em 2026-10-02.
