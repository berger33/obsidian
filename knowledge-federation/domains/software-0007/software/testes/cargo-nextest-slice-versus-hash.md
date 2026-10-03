---
id: software.testes.tranche15.000860
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
fontes: ["https://nexte.st/docs/ci-features/partitioning/", "https://nexte.st/docs/filtersets/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# cargo-nextest: escolher partição slice ou hash conforme a estabilidade

## Em uma frase
Particionamento divide uma execução em buckets para vários jobs de CI; `slice` e `hash` distribuem os testes por critérios diferentes, portanto não são intercambiáveis.

## Por que importa
`slice` distribui em round-robin depois que filtros são aplicados e pode equilibrar contagens sem considerar duração; `hash` atribui teste por uma função estável sobre identidade de binário e nome.

## Como funciona
A segunda estratégia tende a manter um teste no mesmo bucket quando a lista cresce, mas não corrige custos desequilibrados por duração.

## Exemplo
Use `cargo nextest run --partition slice:1/4` quando os jobs devam receber fatias de uma lista selecionada, ou `--partition hash:1/4` quando quiser alocação estável baseada na identidade do teste.

## Limites e trade-offs
Adicionar filtro, renomear teste ou mudar binary ID pode alterar a composição; confirme que todos os shards usam a mesma seleção e não trate a hash como balanceador de wall-clock.

## Como verificar
Execute todos os índices da partição para o mesmo commit, junte os conjuntos de nomes esperados e verifique que cada teste selecionado aparece uma única vez.

## Conexões
- [[cargo-nextest-hash-bin-id-e-identidade-do-teste]] — Veja também: cargo-nextest: entender a chave estável da partição hash.

## Fontes
- [cargo-nextest — Partitioning test runs in CI](https://nexte.st/docs/ci-features/partitioning/) — partições slice/hash/count, distribuição por shard e combinação de resultados; consultado em 2026-10-02.
- [cargo-nextest — Filterset DSL](https://nexte.st/docs/filtersets/) — predicados, união e interseção de filtros de testes e pacotes; consultado em 2026-10-02.
