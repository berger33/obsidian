---
id: software.testes.tranche15.000896
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
fontes: ["https://docs.deno.com/runtime/reference/cli/test/", "https://docs.deno.com/runtime/test/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Deno test: auditar filtro e shard como duas dimensões da seleção

## Em uma frase
Filtros por nome restringem casos dentro dos módulos descobertos, enquanto sharding separa o conjunto selecionado em partes para jobs diferentes.

## Por que importa
Um filtro aplicado junto a uma divisão pode deixar cada job sem casos ou excluir uma família necessária.

## Como funciona
O teste precisa distinguir módulo não descoberto, caso não correspondente e shard pertencente a outro job.

## Exemplo
Rode `deno test --filter 'database'` para depurar nomes e configure `--shard=1/4` até `--shard=4/4` nos jobs paralelos, sempre com os mesmos argumentos de seleção.

## Limites e trade-offs
Executar somente um shard localmente não verifica os três restantes, e alterações na seleção podem causar lacunas se workflows usam expressões divergentes.

## Como verificar
Colete a lista de testes ou a saída de cada job, una os nomes executados e compare com uma execução integral do mesmo commit para descobrir ausências e duplicações.

## Conexões
- [[deno-test-affected-tests-nao-substituem-ci-completa]] — Veja também: Deno test: usar affected tests como feedback incremental, não como cobertura final.
- [[deno-test-coverage-raw-data-e-relatorio-limpo]] — Veja também: Deno test: limpar perfis de cobertura antes de medir uma nova suíte.

## Fontes
- [Deno Runtime — deno test](https://docs.deno.com/runtime/reference/cli/test/) — flags de filtro, shard, cobertura, snapshots e execução do runner; consultado em 2026-10-02.
- [Deno Runtime — Testing](https://docs.deno.com/runtime/test/) — steps, timeouts, affected tests, permissões, snapshots, sanitizers e reporters; consultado em 2026-10-02.
