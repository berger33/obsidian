---
id: software.testes.tranche15.000943
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
fontes: ["https://pgtap.org/documentation.html#results_eq", "https://www.postgresql.org/docs/current/queries-order.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# pgTAP: escolher comparação de resultados que corresponda ao contrato

## Em uma frase
pgTAP oferece comparadores de resultados ordenados e não ordenados; selecione o contrato que trata corretamente ordem e multiplicidade das linhas.

## Por que importa
`results_eq()` compara resultados na mesma ordem e com tipos compatíveis.

## Como funciona
`set_eq()` ignora ordem e duplicatas, enquanto `bag_eq()` ignora ordem mas preserva multiplicidade.

## Exemplo
Use `set_eq()` quando ordem e duplicatas forem irrelevantes; use `bag_eq()` quando a ordem não importar mas cada ocorrência importar; use `results_eq()` quando a ordem contratual for explícita e as queries puderem ser ordenadas com `ORDER BY`.

## Limites e trade-offs
PostgreSQL não promete ordem sem ORDER BY; não infira estabilidade de uma execução observada. Escolha entre conjunto, multiconjunto e comparação ordenada de acordo com as duplicatas e a sequência observável.

## Como verificar
Varie inserção ou plano: confirme que set_eq aceita permutações e ignora duplicatas, bag_eq aceita permutações mas detecta multiplicidade, e results_eq exige a sequência contratada com ORDER BY.

## Conexões
- [[pgtap-assertions-de-esquema-antes-do-conteudo]] — Veja também: pgTAP: verificar contrato de schema com assertions específicas.
- [[pgtap-throws-ok-contrato-de-excecao]] — Veja também: pgTAP: validar SQLSTATE e mensagem de operações que devem falhar.

## Fontes
- [pgTAP — Result set comparison assertions](https://pgtap.org/documentation.html#results_eq) — comparadores de resultados ordenados e não ordenados, conjuntos e multiplicidade; consultado em 2026-10-02.
- [PostgreSQL — Sorting Rows](https://www.postgresql.org/docs/current/queries-order.html) — semântica de ORDER BY e ausência de garantia de ordenação sem cláusula explícita; consultado em 2026-10-02.
