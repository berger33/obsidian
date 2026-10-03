---
id: software.testes.tranche15.000897
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
fontes: ["https://docs.deno.com/runtime/test/coverage/", "https://docs.deno.com/runtime/reference/cli/test/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Deno test: limpar perfis de cobertura antes de medir uma nova suíte

## Em uma frase
`deno test --coverage` coleta dados brutos em diretório configurável e o comando `deno coverage` produz o relatório; a coleta pode acumular arquivos de execuções anteriores.

## Por que importa
Perfis obsoletos de módulos renomeados ou removidos podem distorcer uma medição nova.

## Como funciona
A opção de limpeza deve ser usada no ponto que inicia a coleta quando o relatório precisa representar apenas o commit atual.

## Exemplo
Rode `deno test --clean --coverage` no job que gera cobertura do zero e, em seguida, `deno coverage coverage/` para produzir o resumo e examinar os arquivos incluídos.

## Limites e trade-offs
Remover o diretório errado destrói perfis de outro job ou etapa; escolha diretório separado por revisão e conserve o artifact bruto se a auditoria precisar reproduzir o relatório.

## Como verificar
Faça uma execução com um arquivo de teste que coleta cobertura, apague ou renomeie esse módulo e repita com `--clean`; confira que o perfil antigo não aparece no resultado.

## Conexões
- [[deno-test-filter-e-sharding-com-inventario]] — Veja também: Deno test: auditar filtro e shard como duas dimensões da seleção.
- [[deno-coverage-limites-por-metrica-e-exportacao]] — Veja também: Deno coverage: separar limiares de linhas, branches e funções.

## Fontes
- [Deno Runtime — Test coverage](https://docs.deno.com/runtime/test/coverage/) — coleta, limpeza, métricas, thresholds e exportação de cobertura; consultado em 2026-10-02.
- [Deno Runtime — deno test](https://docs.deno.com/runtime/reference/cli/test/) — flags de filtro, shard, cobertura, snapshots e execução do runner; consultado em 2026-10-02.
