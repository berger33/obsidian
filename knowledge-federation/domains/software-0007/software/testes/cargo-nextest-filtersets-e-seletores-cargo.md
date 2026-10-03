---
id: software.testes.tranche15.000863
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
fontes: ["https://nexte.st/docs/filtersets/", "https://nexte.st/docs/ci-features/partitioning/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# cargo-nextest: combinar filtersets e filtros de substring conscientemente

## Em uma frase
O DSL de filtersets seleciona testes com predicados como package, test e dependências; quando também se fornece um filtro de substring tradicional, os dois conjuntos precisam ser satisfeitos.

## Por que importa
Vários filtersets na CLI formam uma união entre si, mas essa união é intersectada com a união dos filtros de substring.

## Como funciona
Uma expressão aparentemente ampla pode portanto produzir zero casos se um seletor cargo e um nome de teste não coincidirem simultaneamente.

## Exemplo
Para selecionar testes de um pacote e nomes que contenham uma de duas expressões, escreva a interseção deliberadamente, por exemplo `cargo nextest run -E 'package(api)' -- parse encode`.

## Limites e trade-offs
Espaços, operadores e regex do DSL têm sintaxe própria; filtros padrões configurados no projeto também podem restringir a seleção, a menos que sejam ignorados ou referenciados expressamente.

## Como verificar
Use `cargo nextest list` com a mesma expressão antes do job oneroso, leia os números de incluídos/excluídos e mantenha um teste sentinela para detectar seleção vazia.

## Conexões
- [[cargo-nextest-count-partition-depreciada]] — Veja também: cargo-nextest: substituir count por um particionamento documentado.
- [[cargo-nextest-deps-e-selecao-de-subgrafo]] — Veja também: cargo-nextest: usar deps e rdeps para delimitar um subgrafo de crates.

## Fontes
- [cargo-nextest — Filterset DSL](https://nexte.st/docs/filtersets/) — predicados, união e interseção de filtros de testes e pacotes; consultado em 2026-10-02.
- [cargo-nextest — Partitioning test runs in CI](https://nexte.st/docs/ci-features/partitioning/) — partições slice/hash/count, distribuição por shard e combinação de resultados; consultado em 2026-10-02.
