---
id: software.testes.tranche15.000895
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
fontes: ["https://docs.deno.com/runtime/test/", "https://docs.deno.com/runtime/reference/cli/test/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Deno test: usar affected tests como feedback incremental, não como cobertura final

## Em uma frase
`--changed` e `--related` ajudam a selecionar módulos afetados por alterações do git ou dependências declaradas, acelerando o ciclo local.

## Por que importa
Seleção incremental depende da análise de relações entre arquivos e do estado do checkout; um workflow que precisa certificar um commit deve manter uma execução completa, opcionalmente repartida por shard.

## Como funciona
A documentação do Deno recomenda a suíte completa em CI.

## Exemplo
Use `deno test --changed=origin/main` num feedback por pull request e execute `deno test` completo num job de integração ou release; registre qual seleção foi usada no log.

## Limites e trade-offs
Alterações de configuração, geradores ou dependências dinâmicas podem não produzir um recorte intuitivo; affected tests é uma conveniência do runner, não uma prova de ausência de impacto.

## Como verificar
Modifique uma dependência importada e compare os módulos selecionados com uma execução total de referência; valide separadamente o comportamento do job que não usa filtro incremental.

## Conexões
- [[deno-test-timeout-cobre-loop-sincrono-e-promise]] — Veja também: Deno test: colocar deadline em testes que podem pendurar.
- [[deno-test-filter-e-sharding-com-inventario]] — Veja também: Deno test: auditar filtro e shard como duas dimensões da seleção.

## Fontes
- [Deno Runtime — Testing](https://docs.deno.com/runtime/test/) — steps, timeouts, affected tests, permissões, snapshots, sanitizers e reporters; consultado em 2026-10-02.
- [Deno Runtime — deno test](https://docs.deno.com/runtime/reference/cli/test/) — flags de filtro, shard, cobertura, snapshots e execução do runner; consultado em 2026-10-02.
