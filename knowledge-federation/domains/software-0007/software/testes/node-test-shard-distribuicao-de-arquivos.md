---
id: software.testes.tranche15.000937
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
fontes: ["https://nodejs.org/api/cli.html", "https://nodejs.org/api/test.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# node:test: coordenar shards sem sobrepor arquivos entre jobs

## Em uma frase
A flag `--test-shard` divide os arquivos de teste descobertos em partes, permitindo executar uma fração da suíte em cada job de uma matriz de CI.

## Por que importa
Cada worker precisa receber o mesmo inventário, versão de Node e padrão de descoberta.

## Como funciona
Se um shard não rodar ou um job aplicar filtro extra, a união deixa de representar a suíte.

## Exemplo
Configure `--test-shard=1/4` até `4/4` nos jobs e publique resultado de cada parte com identificador do commit e configuração de discovery.

## Limites e trade-offs
Distribuir arquivos não necessariamente equilibra tempo, pois um único arquivo pode conter uma porção desproporcional do custo; shard isolado local não valida as outras partições.

## Como verificar
Colete nomes de arquivos ou casos reportados por cada shard e compare a união com uma execução não particionada no mesmo commit.

## Conexões
- [[node-test-randomize-seed-para-diagnosticar-ordem]] — Veja também: node:test: repetir uma ordem aleatória com seed registrada.
- [[node-test-reporters-e-saidas-de-ci]] — Veja também: node:test: escolher reporter e destino sem perder diagnósticos.

## Fontes
- [Node.js v26.10 — Command-line API](https://nodejs.org/api/cli.html) — flags de execução, seleção, reporters, cobertura e sharding; consultado em 2026-10-02.
- [Node.js v26.10 — Test runner](https://nodejs.org/api/test.html) — TestContext, isolamento, hooks, mocks, concorrência e reporters; consultado em 2026-10-02.
