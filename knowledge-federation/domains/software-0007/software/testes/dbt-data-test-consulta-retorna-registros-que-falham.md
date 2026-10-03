---
id: software.testes.tranche15.000910
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
fontes: ["https://docs.getdbt.com/docs/build/data-tests?version=2", "https://docs.getdbt.com/reference/commands/test?version=2"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# dbt data tests: escrever a consulta a partir da linha que viola o contrato

## Em uma frase
Um data test passa quando sua query não retorna registros que violem a regra; cada linha devolvida funciona como evidência concreta de falha que pode ser investigada.

## Por que importa
Esse modelo inverte a intuição de uma assertion booleana: o SQL precisa selecionar as exceções, e resultado vazio representa que nenhum caso foi encontrado.

## Como funciona
Escolher colunas úteis no SELECT melhora o diagnóstico sem alterar o critério de falha.

## Exemplo
Para verificar valores não negativos, selecione as linhas do modelo em que `amount < 0`; valide localmente inserindo um registro inválido e confirmando que o teste o retorna.

## Limites e trade-offs
Um query vazia por erro de filtro também passa, então a regra deve ser testada com dados válidos e inválidos conhecidos; limite de linhas pode truncar detalhes de depuração.

## Como verificar
Compile o teste e inspecione o SQL final, rode sobre uma fixture que contém uma violação deliberada e confirme que ela desaparece quando o dado é corrigido.

## Conexões
- [[dbt-singular-e-generic-com-fronteiras-de-reuso]] — Veja também: dbt data tests: decidir quando um teste singular deve virar genérico.

## Fontes
- [dbt v2 — Add data tests to your DAG](https://docs.getdbt.com/docs/build/data-tests?version=2) — testes singulares/genéricos, registros violadores e argumentos; consultado em 2026-10-02.
- [dbt v2 — About dbt test command](https://docs.getdbt.com/reference/commands/test?version=2) — seleção de data/unit tests e pré-requisitos de materialização; consultado em 2026-10-02.
