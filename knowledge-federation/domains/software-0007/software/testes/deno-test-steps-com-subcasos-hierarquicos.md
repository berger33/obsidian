---
id: software.testes.tranche15.000892
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

# Deno test: usar steps para estruturar uma operação com fases

## Em uma frase
`t.step` permite decompor um teste em etapas nomeadas, fazendo com que preparação e ações relacionadas apareçam como unidades subordinadas no resultado do runner.

## Por que importa
A hierarquia melhora diagnóstico quando um fluxo executa várias operações sob o mesmo setup; ela não transforma automaticamente cada step em fixture independente.

## Como funciona
O estado adquirido pelo teste continua pertencendo ao caso e precisa ser liberado mesmo quando uma etapa falha.

## Exemplo
Dentro de `Deno.test("database operations", async t => ...)`, crie steps como `insert user` e `read user`, aguardando cada chamada antes de avançar.

## Limites e trade-offs
Steps que dependem de execução sequencial não devem ser lançados em paralelo sem contrato; erro numa etapa pode impedir as seguintes e precisa deixar o sistema em estado limpável.

## Como verificar
Faça a segunda etapa falhar deliberadamente e leia a saída hierárquica, depois verifique se a limpeza do banco ocorre em bloco `finally` ou por recurso descartável.

## Conexões
- [[deno-test-permissoes-minimas-por-teste]] — Veja também: Deno test: restringir permissões por teste sem ampliar a concessão da CLI.
- [[deno-test-sanitizers-recursos-e-operacoes]] — Veja também: Deno test: reativar sanitizers para detectar recursos e operações vazados.

## Fontes
- [Deno Runtime — Testing](https://docs.deno.com/runtime/test/) — steps, timeouts, affected tests, permissões, snapshots, sanitizers e reporters; consultado em 2026-10-02.
- [Deno Runtime — deno test](https://docs.deno.com/runtime/reference/cli/test/) — flags de filtro, shard, cobertura, snapshots e execução do runner; consultado em 2026-10-02.
