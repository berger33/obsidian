---
id: software.testes.tranche15.000936
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

# node:test: repetir uma ordem aleatória com seed registrada

## Em uma frase
A randomização de testes pode revelar dependência de ordem; uma seed informada permite repetir a execução diagnóstica, mas a opção ainda é early development na CLI Node.js v26.10.

## Por que importa
Testes que passam isolados podem compartilhar cache, ambiente ou mocks com casos anteriores.

## Como funciona
A randomização é ferramenta de diagnóstico e não substitui independência entre casos; por estar em early development, valide a flag na versão de Node fixada.

## Exemplo
Na versão Node fixada, use `node --test --test-randomize --test-random-seed=42` (confirme os nomes na CLI daquela release); preserve a seed indicada no log da falha e repita com o mesmo inventário de testes.

## Limites e trade-offs
Mesmo seed depende do mesmo inventário e versão do Node; alteração na lista de arquivos pode mudar a ordem efetiva, e uma opção em early development pode evoluir entre releases.

## Como verificar
Confirme primeiro que a versão instalada reconhece ambas as flags, rode com seeds diferentes e então repita a seed que falhou em checkout idêntico; registre a versão junto ao log.

## Conexões
- [[node-test-fake-timers-com-avanco-explicito]] — Veja também: node:test: avançar fake timers em vez de esperar tempo real.
- [[node-test-shard-distribuicao-de-arquivos]] — Veja também: node:test: coordenar shards sem sobrepor arquivos entre jobs.

## Fontes
- [Node.js v26.10 — Command-line API](https://nodejs.org/api/cli.html) — flags de execução, seleção, reporters, cobertura e sharding; consultado em 2026-10-02.
- [Node.js v26.10 — Test runner](https://nodejs.org/api/test.html) — TestContext, isolamento, hooks, mocks, concorrência e reporters; consultado em 2026-10-02.
